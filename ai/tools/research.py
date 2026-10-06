#!/usr/bin/env python3
"""`just check` and `just views` for the research folder. Spec: ai/checks.md.

    python3 ai/tools/research.py check   # exits 1 if any rule is broken
    python3 ai/tools/research.py views   # regenerates research/views/
"""
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"
TEMPLATE = ROOT / "ai" / "template"
VIEWS = RESEARCH / "views"
DECISIONS = RESEARCH / "ai-log" / "decisions"
STATUSES = {"provisional", "proposed", "accepted", "changed", "rejected", "retired"}
DECIDED = {"accepted", "changed", "rejected", "retired"}
LIVE = {"accepted", "changed"}


# ---------- reading files ----------

class Doc:
    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(RESEARCH).as_posix()
        self.text = path.read_text(encoding="utf-8")
        self.meta, self.body = parse_frontmatter(self.text)

    @property
    def id(self):
        return self.meta.get("id", "")

    @property
    def status(self):
        return self.meta.get("status", "")

    def section(self, heading: str) -> str:
        return section(self.body, heading)


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = re.sub(r"\s+#.*$", "", value).strip()
        if value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        meta[key.strip()] = value
    return meta, text[end + 5:]


def section(body: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    return m.group(1) if m else ""


def headings(body: str):
    return re.findall(r"^## (.+?)\s*$", body, re.M)


def tables(text: str):
    """Rows of every markdown table in text, as dicts keyed by header."""
    rows, header = [], None
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            header = cells
        elif not all(re.fullmatch(r":?-+:?", c) for c in cells):
            rows.append(dict(zip(header, cells)))
    return rows


def produced_docs():
    """Every research file with frontmatter: the outputs of the flow."""
    docs = []
    for path in sorted(RESEARCH.rglob("*.md")):
        rel = path.relative_to(RESEARCH).as_posix()
        if rel.startswith(("views/", "ai-log/raw/")):
            continue
        doc = Doc(path)
        if doc.meta:
            docs.append(doc)
    return docs


def decision_docs(docs):
    return [d for d in docs if d.rel.startswith("ai-log/decisions/")]


def flow_docs(docs):
    return [d for d in docs if not d.rel.startswith("ai-log/")]


def num(id_: str) -> int:
    m = re.search(r"\d+", id_)
    return int(m.group()) if m else 0


# ---------- templates ----------

def template_for(rel: str):
    parts = rel.split("/")
    name, folder = parts[-1], "/".join(parts[:-1])
    if rel.startswith("ai-log/decisions/"):
        return TEMPLATE / "ai-log" / "decision.md"
    for kind in ("skeptic", "citations", "examiner"):
        if name.endswith(f".{kind}.md"):
            return TEMPLATE / "reviews" / f"{kind}.md"
    if folder == "sls/1-protocol/changes":
        return TEMPLATE / "sls" / "1-protocol" / "change.md"
    if folder == "sls/2-search" and re.fullmatch(r"R\d+(-backward|-forward)?\.md", name):
        return TEMPLATE / folder / "R.md"
    if folder == "dsrm/4-demonstration" and re.fullmatch(r"D\d+-run\d+\.md", name):
        return TEMPLATE / folder / "D-run.md"
    if folder == "dsrm/6-communicate":
        for kind in ("outline", "draft"):
            if name.endswith(f".{kind}.md"):
                return TEMPLATE / folder / f"section.{kind}.md"
        if re.fullmatch(r"ch\d+-[^.]+\.md", name):
            return TEMPLATE / folder / "section.md"
    candidate = TEMPLATE / folder / re.sub(r"\d+", "", name)
    return candidate if candidate.is_file() else None


def without_code(text: str) -> str:
    return re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)


# ---------- git ----------

def git(*args) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def changed_at(path: Path) -> float:
    """Last commit time of a file, or now if it has uncommitted changes."""
    rel = path.relative_to(ROOT).as_posix()
    if git("status", "--porcelain", "--", rel).strip():
        return time.time()
    out = git("log", "-1", "--format=%ct", "--", rel).strip()
    return float(out) if out else time.time()


# ---------- checks ----------

def check_complete(docs, errors):
    for d in docs:
        if d.status == "retired":
            continue
        tpl = template_for(d.rel)
        if tpl is None:
            errors.append(f"{d.rel}: no template matches this file name (ai/template/README.md)")
            continue
        for ph in re.findall(r"\{[^{}\n]*\}|\[ \]", without_code(d.text)):
            errors.append(f"{d.rel}: placeholder left: {ph}")
        _, tpl_body = parse_frontmatter(tpl.read_text(encoding="utf-8"))
        have = set(headings(d.body))
        for h in headings(tpl_body):
            if "{" not in h and h not in have:
                errors.append(f"{d.rel}: missing section '## {h}' from {tpl.relative_to(ROOT)}")


def check_status(docs, errors):
    for d in flow_docs(docs):
        if d.status not in STATUSES:
            errors.append(f"{d.rel}: status '{d.status}' is not one of {sorted(STATUSES)}")


def check_decisions(docs, errors):
    targets = {d.meta.get("target", "").removeprefix("research/") for d in decision_docs(docs)}
    for d in flow_docs(docs):
        if d.status in DECIDED and d.rel not in targets:
            errors.append(f"{d.rel}: status '{d.status}' but no decision file targets it (ai/gate.md)")
    for d in decision_docs(docs):
        t = d.meta.get("target", "").removeprefix("research/")
        if t and not (RESEARCH / t).is_file():
            errors.append(f"{d.rel}: target '{t}' does not exist")


def check_id_rule(errors):
    for rel in git("ls-tree", "-r", "--name-only", "HEAD", "research").split():
        if not rel.endswith(".md") or rel.startswith(("research/views/", "research/ai-log/")):
            continue
        old, _ = parse_frontmatter(git("show", f"HEAD:{rel}"))
        old_id = old.get("id")
        if not old_id:
            continue
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"{rel}: ID {old_id} was removed. Retire it instead (status: retired)")
            continue
        new_id = parse_frontmatter(path.read_text(encoding="utf-8"))[0].get("id")
        if new_id != old_id:
            errors.append(f"{rel}: ID renamed {old_id} -> {new_id}. Retire it and create a new ID instead")


def assigned_papers(docs):
    """P IDs assigned at the include/exclude gates, from the round files."""
    papers = {}
    for d in docs:
        if not d.rel.startswith("sls/2-search/R"):
            continue
        for row in tables(d.section("Candidates")):
            pid = row.get("P ID", "")
            if re.fullmatch(r"P\d+", pid):
                papers[pid] = {"reference": row.get("Reference", ""), "round": d.id}
    return papers


TRACE = {
    # file kind: [(section, ID pattern), ...]
    "O": [("Traces to", r"RQ\d+")],
    "H": [("Tested by", r"RQ\d+")],
    "D": [("Feeds", r"O\d+"), ("Artifact layer", r"L\d+")],
    "E": [("Question", r"RQ\d+"), ("Objective", r"O\d+"), ("Demonstrations used", r"D\d+-run\d+")],
    "L": [("Decisions implemented", r"DEC\d+")],
}


def kind_of(d: Doc) -> str:
    m = re.fullmatch(r"(RQ|DEC|[A-Z])\d+(-run\d+)?", d.id)
    if not m:
        return ""
    return "D-run" if m.group(2) else m.group(1)


def check_traceability(docs, errors):
    ids = {d.id: d for d in flow_docs(docs)}
    for d in flow_docs(docs):
        if d.status in ("retired", "rejected"):
            continue
        for heading, pattern in TRACE.get(kind_of(d), []):
            for ref in re.findall(rf"\b{pattern}\b", d.section(heading)):
                target = ids.get(ref)
                if target is None:
                    errors.append(f"{d.rel}: '{heading}' names {ref}, which does not exist")
                elif target.status in ("retired", "rejected"):
                    errors.append(f"{d.rel}: '{heading}' names {ref}, which is {target.status}")


def chapter_sections(docs):
    out = {}
    for d in docs:
        m = re.fullmatch(r"dsrm/6-communicate/(ch\d+-[^.]+)(?:\.(outline|draft))?\.md", d.rel)
        if m:
            out.setdefault(m.group(1), {})[m.group(2) or "final"] = d
    return out


def stale_sections(docs):
    decided_at = {}
    for d in decision_docs(docs):
        decided_at[d.meta.get("target", "").removeprefix("research/")] = changed_at(d.path)
    stale = {}
    for name, parts in chapter_sections(docs).items():
        final, outline = parts.get("final"), parts.get("outline")
        if not final or final.status not in LIVE or final.rel not in decided_at:
            continue
        sources = [outline.path] if outline else []
        for pattern in (outline.meta.get("inputs", []) if outline else []):
            sources += [p for p in RESEARCH.glob(pattern) if p.is_file()]
        newer = [p.relative_to(RESEARCH).as_posix() for p in sources if changed_at(p) > decided_at[final.rel]]
        if newer:
            stale[name] = newer
    return stale


def stop_rule(docs) -> str:
    rounds = [d for d in docs if re.fullmatch(r"sls/2-search/R\d+(-backward|-forward)?\.md", d.rel)]
    if not rounds:
        return "no rounds yet"
    k = max(num(d.rel.split("/")[-1]) for d in rounds)
    last = [d for d in rounds if num(d.rel.split("/")[-1]) == k]
    new = [p for d in last for p in re.findall(r"\bP\d+\b", d.section("Newly included"))]
    if new:
        return f"round {k} included {', '.join(sorted(set(new), key=num))}: run another round"
    return f"round {k} included no new papers: stop rule met"


def check(_args):
    docs = produced_docs()
    errors = []
    check_status(docs, errors)
    check_complete(docs, errors)
    check_decisions(docs, errors)
    check_id_rule(errors)
    check_traceability(docs, errors)
    for name, newer in stale_sections(docs).items():
        errors.append(f"chapter section {name} is stale: changed since accepted: {', '.join(newer)}")

    print(f"Checked {len(docs)} files.")
    print(f"Stop rule: {stop_rule(docs)}.")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("All checks pass.")
    return 0


# ---------- views ----------

HEADER = "Generated by `just views` from the research files. Do not edit.\n"


def table(header, rows):
    if not rows:
        return "_None yet._\n"
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines) + "\n"


def view_papers(docs):
    records = {d.id: d for d in docs if d.rel.startswith("sls/3-reading/") and kind_of(d) == "P"}
    rows = []
    for pid, info in sorted(assigned_papers(docs).items(), key=lambda kv: num(kv[0])):
        rec = records.get(pid)
        rows.append([pid, info["reference"], info["round"],
                     rec.status if rec else "not read",
                     rec.section("Deepest pass").strip() if rec else ""])
    return "# Papers\n\n" + HEADER + "\n" + table(["P", "Reference", "Round", "Record", "Deepest pass"], rows)


def view_concepts(docs):
    concepts = sorted((d for d in docs if d.rel.startswith("sls/4-synthesis/") and kind_of(d) == "C"
                       and d.status in LIVE | {"proposed"}), key=lambda d: num(d.id))
    records = sorted((d for d in docs if d.rel.startswith("sls/3-reading/") and kind_of(d) == "P"
                      and d.status in LIVE), key=lambda d: num(d.id))
    names = {}
    for c in concepts:
        m = re.search(r"^# C\d+: (.+)$", c.body, re.M)
        names[c.id] = m.group(1).strip() if m else ""
    rows = []
    for p in records:
        cells = {}
        for row in tables(p.section("Concepts")):
            for cid in re.findall(r"\bC\d+\b", row.get("Concept", "")):
                cells[cid] = f"x, {row.get('Page', '')}".rstrip(", ")
        rows.append([p.id] + [cells.get(c.id, "") for c in concepts])
    legend = "\n".join(f"- **{c.id}**: {names[c.id]}" for c in concepts)
    return ("# Concept matrix\n\n" + HEADER + "\nRows: accepted paper records. Columns: concepts. "
            "Webster and Watson.\n\n" + table(["Paper"] + [c.id for c in concepts], rows)
            + ("\n" + legend + "\n" if legend else ""))


def view_traceability(docs):
    by_kind = {}
    for d in flow_docs(docs):
        by_kind.setdefault(kind_of(d), []).append(d)

    def refs(d, heading, pattern):
        return set(re.findall(rf"\b{pattern}\b", d.section(heading)))

    def label(d):
        return f"{d.id} ({d.status})"

    rows = []
    for rq in sorted(by_kind.get("RQ", []), key=lambda d: num(d.id)):
        objectives = [o for o in by_kind.get("O", []) if rq.id in refs(o, "Traces to", r"RQ\d+")]
        if not objectives:
            rows.append([label(rq), "", "", "", ""])
        for o in sorted(objectives, key=lambda d: num(d.id)):
            demos = [d for d in by_kind.get("D", []) if o.id in refs(d, "Feeds", r"O\d+")]
            runs = [r for r in by_kind.get("D-run", []) if r.id.split("-")[0] in {d.id for d in demos}]
            evals = [e for e in by_kind.get("E", []) if o.id in refs(e, "Objective", r"O\d+")]
            rows.append([label(rq), label(o),
                         ", ".join(label(d) for d in demos),
                         ", ".join(label(r) for r in runs),
                         ", ".join(label(e) for e in evals)])
    return "# Traceability\n\n" + HEADER + "\nRQ → O → D → runs → E.\n\n" + table(
        ["RQ", "Objective", "Demonstrations", "Runs", "Evaluations"], rows)


def view_chapters(docs):
    stale = stale_sections(docs)
    rows = []
    for name, parts in sorted(chapter_sections(docs).items(), key=lambda kv: (num(kv[0]), kv[0])):
        rows.append([name] + [parts[k].status if k in parts else "—" for k in ("outline", "draft", "final")]
                    + ["stale" if name in stale else ""])
    return "# Chapters\n\n" + HEADER + "\n" + table(["Section", "Outline", "Draft", "Final", "Stale"], rows)


def views(_args):
    docs = produced_docs()
    VIEWS.mkdir(exist_ok=True)
    for name, build in (("papers", view_papers), ("concept-matrix", view_concepts),
                        ("traceability", view_traceability), ("chapters", view_chapters)):
        (VIEWS / f"{name}.md").write_text(build(docs), encoding="utf-8")
        print(f"research/views/{name}.md")
    return 0


if __name__ == "__main__":
    commands = {"check": check, "views": views}
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print(__doc__)
        sys.exit(2)
    sys.exit(commands[sys.argv[1]](sys.argv[2:]))
