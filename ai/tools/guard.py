#!/usr/bin/env python3
"""Guard: refuse tool calls that break the workflow rules, before they run. Spec: ai/spec/README.md.

Wired as a PreToolUse hook in .claude/settings.json. Reads the hook event on stdin; to refuse, exits 2 with
the reason on stderr, which Claude Code hands back to the model. Fails open: if the guard itself breaks,
the call goes through (the AI log and `just check` still see it).

    python3 ai/tools/guard.py --test   # runs the built-in cases
"""
import json
import os
import re
import sys
import tomllib
from datetime import date
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2]).resolve()
RESEARCH = ROOT / "research"
SPEC = ROOT / "ai" / "spec" / "flow.toml"
DECIDED = {"accepted", "changed", "rejected", "retired"}
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}


class Refuse(Exception):
    pass


# ---------- spec ----------

def pattern_regex(pattern: str) -> str:
    """A spec path pattern as a regex: {n} {k} numbers, other {names} one path part, * and ** globs."""
    out, i = "", 0
    for token in re.findall(r"\*\*|\*|\{today\}|\{[a-z]+\}|[^*{]+|\{", pattern):
        if token == "**":
            out += ".*"
        elif token == "*":
            out += "[^/]*"
        elif token == "{today}":
            out += re.escape(date.today().isoformat())
        elif token in ("{n}", "{k}"):
            out += r"\d+"
        elif token.startswith("{") and token.endswith("}"):
            out += "[^/]+"
        else:
            out += re.escape(token)
    return out


def matches(path: str, patterns) -> bool:
    return any(re.fullmatch(pattern_regex(p), path) for p in patterns)


def prefix_of(path: str, patterns) -> bool:
    """A folder (or glob) that leads to some allowed pattern: listing it is allowed."""
    stem = re.split(r"[*?\[{]", path, maxsplit=1)[0].rstrip("/")
    if not stem:
        return True
    for p in patterns:
        parts = p.split("/")
        folders = ["/".join(parts[:d]) for d in range(1, len(parts)) if "**" not in parts[:d]]
        if any(re.fullmatch(pattern_regex(f), stem) for f in folders) or matches(stem, [p]):
            return True
    return False


def load_spec():
    with open(SPEC, "rb") as f:
        return tomllib.load(f)


def agent_paths(spec, agent: str):
    rows = [r for r in spec.get("row", []) if r.get("who") == agent]
    writes = [p for r in rows for p in r.get("outputs", [])]
    reads = writes + [p for r in rows for p in r.get("inputs", [])]
    return rows, writes, reads


# ---------- files ----------

def governed(raw: str):
    """(area, rel) for a path inside the project: area 'research', 'artifact', 'other'; None outside it."""
    if not raw:
        return None
    p = Path(raw)
    p = (Path(os.environ.get("GUARD_CWD", ROOT)) / p) if not p.is_absolute() else p
    try:
        rel = p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return None
    if rel == "research" or rel.startswith("research/"):
        return "research", rel[len("research/"):] if rel != "research" else ""
    if rel == "artifact" or rel.startswith("artifact/"):
        return "artifact", rel
    return "other", rel


def frontmatter_status(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    m = re.search(r"^status:\s*([\w-]+)", text[4:end if end > 0 else len(text)], re.M)
    return m.group(1) if m else ""


def current_status(rel: str) -> str:
    path = RESEARCH / rel
    return frontmatter_status(path.read_text(encoding="utf-8")) if path.is_file() else ""


def new_statuses(tool: str, inp: dict):
    """Every status value the call would write into frontmatter."""
    if tool == "Write":
        s = frontmatter_status(inp.get("content", ""))
        return [s] if s else []
    texts = [inp.get("new_string", "")] + [e.get("new_string", "") for e in inp.get("edits", []) or []]
    return [m for t in texts for m in re.findall(r"^status:\s*([\w-]+)", t, re.M)]


def has_decision(rel: str) -> bool:
    folder = RESEARCH / "ai-log" / "decisions"
    for f in folder.glob("*.md") if folder.is_dir() else []:
        m = re.search(r"^target:\s*(\S+)", f.read_text(encoding="utf-8"), re.M)
        if m and m.group(1).removeprefix("research/") == rel:
            return True
    return False


def exists_any(globs) -> bool:
    return any(re.fullmatch(pattern_regex(g), f.relative_to(RESEARCH).as_posix())
               for g in globs for f in RESEARCH.rglob("*") if f.is_file())


# ---------- rules ----------

def check_write(spec, agent, tool, inp, path_key="file_path"):
    where = governed(inp.get(path_key) or inp.get("notebook_path", ""))
    if where is None:
        return
    area, rel = where
    if agent:
        _, writes, _ = agent_paths(spec, agent)
        target = rel if area != "other" else None
        if area == "other" or not matches(target, writes):
            raise Refuse(f"the {agent} agent may write only the outputs of its rows ({', '.join(writes) or 'none'}), "
                         f"not {('research/' + rel) if area == 'research' else rel}. Report anything else as an open issue.")
    if area != "research":
        return
    if rel.startswith("ai-log/raw/"):
        raise Refuse("the raw AI log is append-only and written only by the log hook (ai/ai-log.md).")
    if rel.startswith("ai-log/decisions/") and (RESEARCH / rel).exists():
        raise Refuse("a decision file is a record and is never edited. Write a new decision for a new decision (ai/gate.md).")
    if not rel.endswith(".md") or rel.startswith(("ai-log/", "views/")):
        return
    statuses = new_statuses(tool, inp)
    if agent and any(s != "proposed" for s in statuses):
        raise Refuse("agents write `status: proposed` only; every other status is mine, set at a gate (ai/agent-contract.md).")
    before = current_status(rel)
    for s in statuses:
        if s in DECIDED and s != before and not has_decision(rel):
            raise Refuse(f"research/{rel} can be marked {s} only once its decision file exists. "
                         "Record the decision first (ai/gate.md, step 4), then set the status.")
    if before in ("accepted", "changed"):
        for rule in spec.get("frozen", []):
            if matches(rel, rule.get("paths", [])) and not exists_any(rule.get("unless", [])):
                raise Refuse(f"research/{rel} is frozen: {rule.get('reason', '')}")


METHOD_DOCS = ["**/README.md", "**/step.md", "**/faq.md", "README.md", "views/*.md"]
INTERPRETERS = {"python", "python3", "perl", "node", "ruby"}
SHELLS = {"bash", "sh", "zsh"}
CODE_WRITE = re.compile(r"""open\(\s*(?P<a>[^,()]+?)\s*,\s*['"](?:[wax]|r\+)""" r"""|(?P<b>[\w.\[\]'"/-]+?)\)?\.write_(?:text|bytes)\("""
                        r"""|shutil\.(?:copy\w*|move)\([^,]+,\s*(?P<c>[^,)]+)|os\.(?:remove|unlink|rename|replace)\(\s*(?P<d>[^,)]+)""")


def heredocs(command: str):
    """Split a command into its shell text and its heredoc bodies: (text, [(owner words, body)])."""
    bodies, out, lines, i = [], [], command.split("\n"), 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        tags = re.findall(r"<<-?\s*['\"]?(\w+)['\"]?", line)
        for tag in tags:
            out[-1] = re.sub(r"<<-?\s*['\"]?" + tag + r"['\"]?", f" __HEREDOC_{len(bodies)}__ ", out[-1], count=1)
            bodies.append(None)
        i += 1
        for n, tag in enumerate(tags):
            body = []
            while i < len(lines) and lines[i].strip() != tag:
                body.append(lines[i])
                i += 1
            i += 1
            bodies[len(bodies) - len(tags) + n] = "\n".join(body)
    return "\n".join(out), bodies


def simple_commands(text: str):
    """Words of each simple command, in order; None if the text cannot be parsed."""
    import shlex
    try:
        lexer = shlex.shlex(text, posix=True, punctuation_chars=";&|()<>")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        return None
    cmds, cur = [], []
    for t in tokens:
        if t and set(t) <= set(";&|()") and t not in ("&",) or t in ("&&", "||", ";", "|", "(", ")", ";;"):
            if cur:
                cmds.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        cmds.append(cur)
    return cmds


def code_paths(code: str):
    """(read, written) path literals in a script: written when opened for writing, written to, copied or moved onto."""
    literals = {m.group(2) for m in re.finditer(r"""(['"])([^'"\n]*(?:research|artifact)[^'"\n]*)\1""", code)}
    names = {m.group(1): m.group(3) for m in re.finditer(r"""^\s*(\w+)\s*=\s*(?:Path\()?(['"])([^'"\n]+)\2""", code, re.M)}
    written = set()
    for m in CODE_WRITE.finditer(code):
        arg = next(g for g in m.groups() if g).strip()
        arg = re.sub(r"^(?:Path|str)\(|\)$", "", arg).strip()
        lit = re.fullmatch(r"""['"]([^'"]+)['"]""", arg)
        target = lit.group(1) if lit else names.get(arg)
        if target:
            written.add(target)
    return literals | {v for v in names.values() if "research" in v or "artifact" in v}, written


def shell_paths(command: str, cwd: Path):
    """(read, written) project paths a shell command names, following cd. Raises ValueError if unparsable."""
    text, bodies = heredocs(command)
    cmds = simple_commands(text)
    if cmds is None:
        raise ValueError("unparsable")
    reads, writes = [], []

    env = {}

    def expand(word):
        word = re.sub(r"\$\{?(\w+)\}?", lambda m: env.get(m.group(1), m.group(0)), word)
        return os.path.expanduser(word)

    def is_path(word):
        return ("/" in word or re.search(r"\.\w{1,5}$", word) or word.rstrip("/") in ("research", "artifact", ".")) \
            and not re.search(r"\s|://|[\\|^$<>(){}]", word) and not word.startswith("-")

    def at(word, base):
        p = Path(word)
        return (p if p.is_absolute() else base / p)

    for words in cmds:
        assigns = [w for w in words if re.fullmatch(r"\w+=.*", w)]
        if words and words[0] == "export":
            assigns, words = words[1:], []
        for a in assigns:
            k, v = a.split("=", 1)
            env[k] = expand(v)
        while words and re.fullmatch(r"\w+=.*", words[0]):
            words = words[1:]
        if words and words[0] in ("sudo", "env", "command", "time", "xargs", "nohup"):
            words = words[1:]
        if not words:
            continue
        words = [expand(w) for w in words]
        name = os.path.basename(words[0])
        docs = [bodies[int(m.group(1))] for w in words if (m := re.fullmatch(r"__HEREDOC_(\d+)__", w))]
        words = [w for w in words if not re.fullmatch(r"__HEREDOC_\d+__", w)]
        args = words[1:]
        for body in docs:
            if name in INTERPRETERS:
                r, w = code_paths(body)
                reads += [at(x, cwd) for x in r]
                writes += [at(x, cwd) for x in w]
            elif name in SHELLS:
                r, w = shell_paths(body, cwd)
                reads += r
                writes += w
        if name == "cd" and args:
            cwd = at(args[0], cwd)
            continue
        plain = []
        k = 0
        while k < len(args):
            a = args[k]
            if a in (">", ">>", ">|") and k + 1 < len(args):
                if is_path(args[k + 1]) or "/" not in args[k + 1]:
                    writes.append(at(args[k + 1], cwd))
                k += 2; continue
            if a == "<" and k + 1 < len(args):
                reads.append(at(args[k + 1], cwd)); k += 2; continue
            if a.startswith(("&", ">&")) or re.fullmatch(r"\d", a):
                k += 1; continue
            plain.append(a); k += 1
        operands = [a for a in plain if not a.startswith("-")]
        if name in ("sed", "grep", "egrep", "fgrep", "rg", "awk", "gawk", "perl") and not any(a in ("-e", "-f") for a in plain):
            operands = operands[1:]  # the script or pattern
        if name in ("curl", "wget"):
            operands = []  # URLs and option values, not local files
        paths = [a for a in operands if is_path(a)]
        reads += [at(a, cwd) for a in paths]
        if name == "tee":
            writes += [at(a, cwd) for a in paths]
        elif name in ("sed", "perl") and any(re.fullmatch(r"-[a-zA-Z]*i\S*", a) for a in plain):
            writes += [at(a, cwd) for a in paths]
        elif name in ("mv", "rm", "touch", "truncate", "ln", "unlink", "shred", "rmdir"):
            writes += [at(a, cwd) for a in paths]
        elif name in ("cp", "install", "rsync") and paths:
            writes.append(at(paths[-1], cwd))
        elif name in ("curl", "wget"):
            for j, a in enumerate(plain):
                if a in ("-o", "--output", "-O") and j + 1 < len(plain) and not (name == "curl" and a == "-O"):
                    writes.append(at(plain[j + 1], cwd))
                elif name == "curl" and a in ("-O", "--remote-name"):
                    writes.append(cwd)
        elif name == "git" and plain[:1] and plain[0] in ("checkout", "restore", "rm", "mv", "reset", "clean"):
            targets = [at(a, cwd) for a in plain[1:] if not a.startswith("-") and a != "--" and is_path(a)]
            writes += targets or [cwd]
        elif name in INTERPRETERS and "-c" in plain:
            code = plain[plain.index("-c") + 1] if plain.index("-c") + 1 < len(plain) else ""
            r, w = code_paths(code)
            reads += [at(x, cwd) for x in r]
            writes += [at(x, cwd) for x in w]
    reads = [p for p in reads if "$" not in str(p)]
    writes = [p for p in writes if "$" not in str(p)]
    return reads, writes


def dispatch_state(event):
    import tempfile
    folder = Path(event.get("scratchpad_dir") or tempfile.gettempdir())
    return folder / f"thesis-guard-{event.get('session_id', 'session')}.json"


def dispatched_inputs(event, agent):
    path = dispatch_state(event)
    try:
        return json.loads(path.read_text(encoding="utf-8")).get(agent, [])
    except Exception:
        return []


def record_dispatch(event, inp):
    """When the main session dispatches an agent, remember the research files its prompt names: it may read them."""
    agent = inp.get("subagent_type") or ""
    prompt = inp.get("prompt") or ""
    if not agent:
        return
    found = set(re.findall(r"(?:research/)?((?:0-start|sls|dsrm|papers|views)/[^\s`'\"),;]+)", prompt))
    found |= {"artifact/" + m for m in re.findall(r"artifact/([^\s`'\"),;]+)", prompt)}
    path = dispatch_state(event)
    try:
        state = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    except Exception:
        state = {}
    state[agent] = sorted(set(state.get(agent, [])) | {f.rstrip(".") for f in found})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state), encoding="utf-8")


def allowed_reads(spec, agent, event):
    return agent_paths(spec, agent)[2] + METHOD_DOCS + dispatched_inputs(event, agent)


def check_shell(spec, agent, inp, event):
    command = inp.get("command", "")
    if re.fullmatch(r"\s*(cd\s+\S+\s*(&&|;)\s*)?python3\s+ai/tools/log_hook\.py\s+--compact\s+[^;&|<>]+", command):
        return  # the one scripted edit of the raw log (ai/ai-log.md)
    if not re.search(r"research|artifact", command) and not re.search(r"\bcd\b", command):
        return
    cwd = Path(event.get("cwd") or ROOT)
    try:
        reads, writes = shell_paths(command, cwd)
    except ValueError:
        reads, writes = [], []
        if agent and re.search(r"research/\S+\.md", command) and re.search(r">|sed\s+-i|write|open\(", command):
            raise Refuse("this command could not be read safely and seems to change research files: use the Write and Edit tools.")
    readable = allowed_reads(spec, agent, event) if agent and not agent.startswith("~") else None
    writable = agent_paths(spec, agent)[1] if agent else None
    for p in reads:
        where = governed(str(p))
        if readable is not None and where and where[0] == "research" and where[1]:
            if not (matches(where[1], readable) or prefix_of(where[1], readable)):
                raise Refuse(f"the {agent.lstrip('~')} agent may read in research/ only its inputs and outputs, not research/{where[1]}. "
                             "Ask for the file as an input if it is needed.")
    for p in writes:
        where = governed(str(p))
        if not where or where[0] == "other":
            if agent and where:
                raise Refuse(f"the {agent.lstrip('~')} agent may not write {where[1]}: only the outputs of its rows.")
            continue
        area, rel = where
        shown = ("research/" + rel) if area == "research" else rel
        if area == "research" and rel.startswith("ai-log/raw"):
            raise Refuse("the raw AI log is append-only and written only by the log hook (ai/ai-log.md).")
        if area == "research" and rel.startswith("ai-log/decisions/") and (RESEARCH / rel).exists():
            raise Refuse("a decision file is a record and is never edited (ai/gate.md).")
        if area == "research" and (not rel or rel.rstrip("/").count("/") == 0 and not re.search(r"\.\w+$", rel)):
            raise Refuse(f"this command would change the whole of {shown}; change research files one by one.")
        if agent and not (matches(rel, writable) or (not re.search(r"\.\w+$", rel) and prefix_of(rel, writable))):
            raise Refuse(f"the {agent.lstrip('~')} agent may write only the outputs of its rows, not {shown}.")
        if area == "research" and rel.endswith(".md"):
            snapshot(event, rel)


def check_read(spec, agent, tool, inp, event):
    if not agent:
        return
    reads = allowed_reads(spec, agent, event)
    raw = inp.get("file_path") or inp.get("path") or ""
    where = governed(raw) if raw else None
    if tool in ("Glob", "Grep") and not raw:
        pat = inp.get("pattern", "") if tool == "Glob" else inp.get("glob", "")
        where = governed(pat) if pat and ("research" in pat) else None
    if not where or where[0] != "research" or not where[1]:
        return
    rel = where[1]
    if not (matches(rel, reads) or prefix_of(rel, reads)):
        raise Refuse(f"the {agent} agent may read in research/ only its inputs and outputs, not research/{rel}. "
                     "Ask for the file as an input if it is needed.")


def snapshot(event, rel):
    """Keep a file's content before a shell command that writes it, so a broken rule can be undone after."""
    path = dispatch_state(event).with_suffix(".snap.json")
    try:
        state = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    except Exception:
        state = {}
    target = RESEARCH / rel
    entry = state.setdefault(event.get("tool_use_id", "?"), {"agent": event.get("agent_type") or "", "files": {}})
    entry["files"].setdefault(rel, target.read_text(encoding="utf-8") if target.is_file() else None)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state), encoding="utf-8")


def violation(spec, agent, rel, before_text, after_text):
    """The rule a change breaks, judged from the file before and after; None if it keeps them all."""
    if after_text is None or after_text == before_text:
        return None
    before, after = frontmatter_status(before_text or ""), frontmatter_status(after_text)
    if agent and after and after != "proposed":
        return "agents write `status: proposed` only; every other status is mine, set at a gate (ai/agent-contract.md)."
    if after in DECIDED and after != before and not has_decision(rel):
        return f"research/{rel} was marked {after} with no decision file. Record the decision first (ai/gate.md, step 4)."
    if before in ("accepted", "changed"):
        for rule in spec.get("frozen", []):
            if matches(rel, rule.get("paths", [])) and not exists_any(rule.get("unless", [])):
                return f"research/{rel} is frozen: {rule.get('reason', '')}"
    return None


def after_shell(event):
    """PostToolUse for Bash: check every research file the command wrote; undo the ones that break a rule."""
    path = dispatch_state(event).with_suffix(".snap.json")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    entry = state.pop(event.get("tool_use_id", "?"), None)
    path.write_text(json.dumps(state), encoding="utf-8")
    if not entry:
        return
    spec = load_spec()
    agent = entry.get("agent", "")
    if agent and agent not in {r.get("who") for r in spec.get("row", [])}:
        agent = "~" + agent
    undone = []
    for rel, before in entry["files"].items():
        target = RESEARCH / rel
        after = target.read_text(encoding="utf-8") if target.is_file() else None
        why = violation(spec, agent, rel, before, after)
        if why:
            if before is None:
                target.unlink(missing_ok=True)
            else:
                target.write_text(before, encoding="utf-8")
            undone.append(why)
    if undone:
        raise Refuse("the command's change was undone. " + " ".join(undone))


def decide(event: dict):
    tool, inp = event.get("tool_name", ""), event.get("tool_input", {}) or {}
    if event.get("hook_event_name") == "PostToolUse":
        if tool == "Bash":
            after_shell(event)
        return
    agent = event.get("agent_type") or ""
    os.environ["GUARD_CWD"] = event.get("cwd") or str(ROOT)
    spec = load_spec()
    if agent and agent not in {r.get("who") for r in spec.get("row", [])}:
        agent = "~" + agent  # an agent outside the workflow: may read, may not write the research
    if tool in ("Agent", "Task") and not agent:
        record_dispatch(event, inp)
    elif tool in WRITE_TOOLS:
        check_write(spec, agent, tool, inp, "notebook_path" if tool == "NotebookEdit" else "file_path")
    elif tool == "Bash":
        check_shell(spec, agent if not agent.startswith("~") else agent, inp, event)
    elif tool in ("Read", "Glob", "Grep") and not agent.startswith("~"):
        check_read(spec, agent, tool, inp, event)


def main():
    event = json.loads(sys.stdin.read())
    try:
        decide(event)
    except Refuse as r:
        print(f"Blocked by the thesis guard: {r}", file=sys.stderr)
        sys.exit(2)


# ---------- tests ----------

def _test():
    import tempfile
    global ROOT, RESEARCH, SPEC
    spec_src = SPEC
    with tempfile.TemporaryDirectory() as tmp:
        ROOT = Path(tmp).resolve()
        RESEARCH, SPEC = ROOT / "research", ROOT / "ai" / "spec" / "flow.toml"
        SPEC.parent.mkdir(parents=True)
        SPEC.write_text(spec_src.read_text(encoding="utf-8"), encoding="utf-8")
        (RESEARCH / "0-start").mkdir(parents=True)
        (RESEARCH / "sls" / "3-reading").mkdir(parents=True)
        (RESEARCH / "ai-log" / "decisions").mkdir(parents=True)
        (RESEARCH / "ai-log" / "raw").mkdir(parents=True)
        (RESEARCH / "0-start" / "observation.md").write_text("---\nid: observation\nstatus: accepted\n---\n# O\n")
        (RESEARCH / "sls" / "3-reading" / "P1.md").write_text("---\nid: P1\nstatus: proposed\n---\n# P1\n")
        (RESEARCH / "ai-log" / "decisions" / "2026-01-01-3c-P2.md").write_text("---\nrow: 3c\ntarget: sls/3-reading/P2.md\n---\n")
        (RESEARCH / "sls" / "3-reading" / "P2.md").write_text("---\nid: P2\nstatus: proposed\n---\n# P2\n")
        r = lambda rel: str(RESEARCH / rel)
        md = lambda s: f"---\nid: X\nstatus: {s}\n---\n# X\n"
        cases = [
            ("reader writes its record", "reader", "Write", {"file_path": r("sls/3-reading/P3.md"), "content": md("proposed")}, True),
            ("reader writes a concept", "reader", "Write", {"file_path": r("sls/4-synthesis/C1.md"), "content": md("proposed")}, False),
            ("reader accepts its own record", "reader", "Edit", {"file_path": r("sls/3-reading/P1.md"), "old_string": "status: proposed", "new_string": "status: accepted"}, False),
            ("reader edits rules", "reader", "Edit", {"file_path": str(ROOT / "ai" / "gate.md"), "old_string": "a", "new_string": "b"}, False),
            ("reader writes scratch", "reader", "Write", {"file_path": "/tmp/x.txt", "content": "x"}, True),
            ("reader reads the criteria", "reader", "Read", {"file_path": r("sls/1-protocol/criteria.md")}, True),
            ("reader reads the gap", "reader", "Read", {"file_path": r("sls/5-gap/gap.md")}, False),
            ("reader downloads its PDF", "reader", "Bash", {"command": f"curl -L -o {r('papers/P3.pdf')} https://x"}, True),
            ("reader edits its record by script", "reader", "Bash", {"command": "python3 - <<'EOF'\np='research/sls/3-reading/P1.md'\nopen(p,'w').write('x')\nEOF"}, True),
            ("reader edits a concept by script", "reader", "Bash", {"command": "python3 - <<'EOF'\np='research/sls/4-synthesis/C1.md'\nopen(p,'w').write('x')\nEOF"}, False),
            ("reader greps its record", "reader", "Bash", {"command": f"grep -n Notes {r('sls/3-reading/P1.md')}"}, True),
            ("checker reads a record", "citation-checker", "Bash", {"command": "head -30 research/sls/3-reading/P1.md"}, True),
            ("main accepts with no decision", "", "Edit", {"file_path": r("sls/3-reading/P1.md"), "old_string": "status: proposed", "new_string": "status: accepted"}, False),
            ("main accepts after the decision", "", "Edit", {"file_path": r("sls/3-reading/P2.md"), "old_string": "status: proposed", "new_string": "status: accepted"}, True),
            ("main edits frozen step 0", "", "Edit", {"file_path": r("0-start/observation.md"), "old_string": "# O", "new_string": "# O2"}, False),
            ("main edits the raw log", "", "Write", {"file_path": r("ai-log/raw/s.jsonl"), "content": "{}"}, False),
            ("main rewrites a decision", "", "Write", {"file_path": r("ai-log/decisions/2026-01-01-3c-P2.md"), "content": "x"}, False),
            ("main writes a new decision", "", "Write", {"file_path": r("ai-log/decisions/2026-01-02-3c-P1.md"), "content": "x"}, True),
            ("main seds a record (checked after)", "", "Bash", {"command": "sed -i 's/proposed/accepted/' research/sls/3-reading/P1.md"}, True),
            ("main wipes the research folder", "", "Bash", {"command": "rm -rf research"}, False),
            ("main writes the raw log by shell", "", "Bash", {"command": "echo x >> research/ai-log/raw/s.jsonl"}, False),
            ("main commits", "", "Bash", {"command": "git add -A && git commit -m 'gate 3c: P1 accepted'"}, True),
            ("main runs check", "", "Bash", {"command": "just check 2>&1 | tail -5"}, True),
            ("main compacts a log", "", "Bash", {"command": "python3 ai/tools/log_hook.py --compact research/ai-log/raw/s.jsonl"}, True),
            ("builder writes code", "builder", "Write", {"file_path": str(ROOT / "artifact" / "L1" / "main.py"), "content": "x"}, True),
            ("builder runs tests", "builder", "Bash", {"command": "cd artifact/L1 && python3 -m pytest > artifact/L1/test.log"}, True),
            ("outside agent writes research", "general-purpose", "Write", {"file_path": r("sls/3-reading/P9.md"), "content": md("proposed")}, False),
            ("checker counts verdicts with awk", "citation-checker", "Bash", {"command": f"cd {r('sls/3-reading')}; awk -F'|' 'NR>0 && /^\\| /{{print $5}}' P1.citations.md | sort | uniq -c"}, True),
            ("main writes a table to scratch", "", "Bash", {"command": "python3 - <<'EOF' > /tmp/batch1.tsv\nprint(open('research/sls/3-reading/P1.md').read())\nEOF"}, True),
            ("snowballer saves a script to scratch", "snowballer", "Bash", {"command": "cd /tmp && cat > verdicts.py <<'EOF'\nopen('research/sls/2-search/R0.md','w')\nEOF"}, True),
            ("snowballer runs a script writing its round", "snowballer", "Bash", {"command": "cd /tmp && python3 - <<'EOF'\nopen('" + r("sls/2-search/R1-backward.md") + "','w').write('x')\nEOF"}, True),
            ("reader reads a method doc", "reader", "Read", {"file_path": r("sls/3-reading/step.md")}, True),
            ("reader downloads into papers after cd", "reader", "Bash", {"command": f"cd {r('papers')}; curl -sL -o P4.pdf https://x"}, True),
            ("snowballer writes a second batch", "snowballer", "Write", {"file_path": r("sls/2-search/R1-backward-2.md"), "content": md("proposed")}, True),
            ("reader downloads into a concept", "reader", "Bash", {"command": f"curl -sL -o {r('sls/4-synthesis/C1.md')} https://x"}, False),
            ("reader fetches with a user agent", "reader", "Bash", {"command": "S=/tmp/x; mkdir -p $S/img; cd $S; curl -sL -A \"Mozilla/5.0\" -o rg.pdf https://a.b/c.pdf"}, True),
            ("reader seds its record with slashes", "reader", "Bash", {"command": f"sed -i 's/(title page, p. i)/(p. 3)/' {r('sls/3-reading/P1.md')}"}, True),
            ("snowballer greps excluding a path", "snowballer", "Bash", {"command": "grep -rn R0 . | grep -v research/ai-log | head"}, True),
        ]
        dispatch = {"tool_name": "Agent", "tool_input": {"subagent_type": "reader", "prompt": "Inputs: sls/1-protocol/changes/2026-10-06-pilot.md"}, "cwd": str(ROOT), "session_id": "t"}
        decide(dispatch)
        cases.append(("reader reads an input its dispatch named", "reader", "Read", {"file_path": r("sls/1-protocol/changes/2026-10-06-pilot.md")}, True))
        cases.append(("reader reads a file no dispatch named", "reader", "Read", {"file_path": r("sls/1-protocol/changes/2026-11-01-other.md")}, False))
        failed = 0
        for name, agent, tool, inp, allowed in cases:
            try:
                decide({"tool_name": tool, "tool_input": inp, "agent_type": agent, "cwd": str(ROOT), "session_id": "t"})
                got, why = True, ""
            except Refuse as e:
                got, why = False, str(e)
            ok = got == allowed
            failed += not ok
            print(f"{'ok  ' if ok else 'FAIL'} {name}: {'allowed' if got else 'refused'}" + (f" ({why})" if not ok and why else ""))
        # after a shell command: a broken rule is undone
        def run(name, agent, command, change, expect_undone):
            nonlocal failed
            ev = {"tool_name": "Bash", "tool_input": {"command": command}, "agent_type": agent, "cwd": str(ROOT),
                  "session_id": "t", "tool_use_id": name}
            decide(dict(ev, hook_event_name="PreToolUse"))
            target, before = RESEARCH / "sls/3-reading/P1.md", (RESEARCH / "sls/3-reading/P1.md").read_text()
            target.write_text(change)
            try:
                decide(dict(ev, hook_event_name="PostToolUse")); undone = False
            except Refuse:
                undone = True
            restored = target.read_text() == before
            ok = undone == expect_undone and restored == expect_undone
            failed += not ok
            print(f"{'ok  ' if ok else 'FAIL'} {name}: {'undone' if undone else 'kept'}")
            target.write_text(before)
            cases.append(name)
        cmd = "sed -i 's/x/y/' research/sls/3-reading/P1.md"
        run("reader script sets its record accepted", "reader", cmd, md("accepted"), True)
        run("reader script keeps its record proposed", "reader", cmd, md("proposed"), False)
        run("main script accepts with no decision", "", cmd, md("accepted"), True)
        print(f"{len(cases) - failed} of {len(cases)} passed")
        return 1 if failed else 0


if __name__ == "__main__":
    if sys.argv[1:2] == ["--test"]:
        sys.exit(_test())
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)  # fail open
