#!/usr/bin/env python3
"""`just check`, `just views` and `just status` for the research folder. Spec: ai/checks.md, ai/status.md.

    python3 ai/tools/research.py check    # exits 1 if any rule is broken
    python3 ai/tools/research.py views    # regenerates research/views/
    python3 ai/tools/research.py status   # where the thesis stands
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
    if folder == "sls/2-search" and re.fullmatch(r"R\d+(-backward|-forward)?(-\d+)?\.md", name):
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
        # A source in parentheses is not part of the section's name: "Type (Shaw)" is the section "Type".
        bare = lambda h: re.sub(r"\s*\([^)]*\)$", "", h)
        have = {bare(h) for h in headings(d.body)}
        for h in headings(tpl_body):
            if "{" not in h and bare(h) not in have:
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
    "P": [("Serves", r"SQ\d+")],
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
    rounds = [d for d in docs if re.fullmatch(r"sls/2-search/R\d+(-backward|-forward)?(-\d+)?\.md", d.rel)]
    if not rounds:
        return "no rounds yet"
    k = max(num(d.rel.split("/")[-1]) for d in rounds)
    last = [d for d in rounds if num(d.rel.split("/")[-1]) == k]
    new = [p for d in last for p in re.findall(r"\bP\d+\b", d.section("Newly included"))]
    if new:
        new = sorted(set(new), key=num)
        listed = ", ".join(new) if len(new) <= 10 else f"{len(new)} papers ({new[0]}–{new[-1]})"
        return f"round {k} included {listed}: run another round"
    return f"round {k} included no new papers: stop rule met"


def check_spec(errors):
    """ai/spec/flow.toml and the flow tables state the same rows, run by the same agent, writing the same files."""
    import tomllib
    spec_path = ROOT / "ai" / "spec" / "flow.toml"
    if not spec_path.is_file():
        return
    with open(spec_path, "rb") as f:
        rows = {r["id"]: r for r in tomllib.load(f).get("row", [])}
    table = {}
    for name in ("kickstart.md", "flow-sls.md", "flow-dsrm.md"):
        path = ROOT / "ai" / name
        for line in path.read_text(encoding="utf-8").splitlines() if path.is_file() else []:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            m = re.fullmatch(r"\**(\d+[a-z]?)\**", cells[0]) if len(cells) >= 5 else None
            if m:
                table[m.group(1)] = (cells[1], line, name)
    for rid, (who, line, name) in table.items():
        row = rows.get(rid)
        if row is None:
            errors.append(f"ai/{name}: row {rid} is not in ai/spec/flow.toml")
            continue
        named = re.findall(r"`([\w-]+)`", who)
        stated = named[0] if named else ("me" if who.lower().startswith("me") else who)
        if stated != row["who"] and not (row["who"] == "check" and "check" in who):
            errors.append(f"row {rid}: ai/{name} says it is run by {who}, ai/spec/flow.toml by {row['who']}")
        for out in row.get("outputs", []):
            shown = out.rsplit("/**", 1)[0] + "/" if out.endswith("/**") else out.rsplit("/", 1)[-1]
            if shown not in line:
                errors.append(f"row {rid}: output {out} of ai/spec/flow.toml is not in its row of ai/{name}")
    for rid in rows:
        if re.fullmatch(r"\d+[a-z]?", rid) and rid not in table:
            errors.append(f"ai/spec/flow.toml: row {rid} is in no flow table")


# ---------- need: papers per question (research/sls/1-protocol/step.md, *How much each question needs*) ----------

COVERAGE_STATES = ("open", "saturated", "complete")


def questions(docs):
    """Live SQs: id -> (question, kind)."""
    out = {}
    for d in docs:
        if re.fullmatch(r"sls/1-protocol/SQ\d+\.md", d.rel) and d.status in LIVE | {"proposed"}:
            kind = (re.findall(r"\b(census|kinds|evidence)\b", d.section("Kind")) or [""])[0]
            out[d.id] = (d.section("Question").strip().splitlines()[0] if d.section("Question").strip() else "", kind)
    return dict(sorted(out.items(), key=lambda kv: num(kv[0])))


def coverage(docs):
    """SQ id -> what its coverage file says: status, papers read (new or not), to read next, deferred, audit."""
    out = {}
    for d in docs:
        m = re.fullmatch(r"sls/4-synthesis/(SQ\d+)\.coverage\.md", d.rel)
        if not m or d.status in ("rejected", "retired"):
            continue
        read = [(r.get("Paper", ""), r.get("New?", "").lower().startswith("new")) for r in tables(d.section("Read"))]
        state = (re.findall(r"\b(open|saturated|complete)\b", d.section("Status")) or [""])[0]
        out[m.group(1)] = {
            "doc": d, "state": state, "decided": d.status in LIVE,
            "read": [((re.findall(r"P\d+", p) or [""])[0], new) for p, new in read],
            "next": re.findall(r"\bP\d+\b", d.section("To read next")),
            "deferred": re.findall(r"\bP\d+\b", d.section("Deferred")),
            "audit": d.section("Audit").strip(),
        }
    return out


def serves_by_paper(docs):
    """P ID -> SQs it serves: from its reading record, else from its row in the round files."""
    out = {}
    for d in docs:
        if not re.fullmatch(r"sls/2-search/R\d+(-backward|-forward)?(-\d+)?\.md", d.rel):
            continue
        for row in tables(d.section("Candidates")):
            pid = row.get("P ID", "").strip()
            if re.fullmatch(r"P\d+", pid):
                out.setdefault(pid, set()).update(re.findall(r"SQ\d+", row.get("Serves", "")))
    for d in docs:
        if re.fullmatch(r"sls/3-reading/P\d+\.md", d.rel) and d.section("Serves").strip():
            out[d.id] = set(re.findall(r"SQ\d+", d.section("Serves")))
    return out


def need_summary(docs) -> str:
    cov, qs = coverage(docs), questions(docs)
    if not qs:
        return "no review questions yet"
    if not cov:
        return f"{len(qs)} questions, no coverage yet: every included paper waits to be read"
    done = [q for q in qs if cov.get(q, {}).get("state") in ("saturated", "complete") and cov[q]["decided"]]
    open_ = [q for q in qs if q not in done]
    waiting = sorted({p for q in open_ for p in cov.get(q, {}).get("next", [])}, key=num)
    deferred = sorted({p for c in cov.values() for p in c["deferred"]} - set(waiting), key=num)
    papers = lambda k: f"{k} paper" + ("" if k == 1 else "s")
    return (f"{len(done)} of {len(qs)} questions have what they need; {len(open_)} open; "
            f"{papers(len(waiting))} to read next, {len(deferred)} deferred")


def check_coverage(docs, errors):
    assigned = assigned_papers(docs)
    qs = questions(docs)
    for sq, c in coverage(docs).items():
        rel = c["doc"].rel
        if sq not in qs:
            errors.append(f"{rel}: there is no live {sq}")
        if c["state"] not in COVERAGE_STATES:
            errors.append(f"{rel}: *Status* must start with open, saturated or complete")
        for p in [p for p, _ in c["read"]] + c["next"] + c["deferred"]:
            if p and p not in assigned:
                errors.append(f"{rel}: names {p}, which no round file assigns")


def check_papers(docs, errors):
    """Every P ID cell of a round file holds an ID or nothing, and every reading record's paper was let in by a round."""
    for d in docs:
        if not re.fullmatch(r"sls/2-search/R\d+(-backward|-forward)?(-\d+)?\.md", d.rel):
            continue
        for row in tables(d.section("Candidates")):
            cell = row.get("P ID", "").strip()
            if cell and not re.fullmatch(r"P\d+|—|-|", cell):
                ref = row.get("#") or row.get("Reference", "")[:40]
                errors.append(f"{d.rel}: the P ID column of row {ref} holds text, not an ID: \"{cell[:60]}\". "
                              "Put the ID back and move the text to the Decision column.")
    assigned = assigned_papers(docs)
    for d in docs:
        if re.fullmatch(r"sls/3-reading/P\d+\.md", d.rel) and d.id not in assigned:
            errors.append(f"{d.rel}: {d.id} has a reading record but no round file assigns it (sls/2-search/R*.md, P ID column)")


def check(_args):
    docs = produced_docs()
    errors = []
    check_spec(errors)
    check_papers(docs, errors)
    check_coverage(docs, errors)
    check_status(docs, errors)
    check_complete(docs, errors)
    check_decisions(docs, errors)
    check_id_rule(errors)
    check_traceability(docs, errors)
    for name, newer in stale_sections(docs).items():
        errors.append(f"chapter section {name} is stale: changed since accepted: {', '.join(newer)}")

    print(f"Checked {len(docs)} files.")
    print(f"Stop rule: {stop_rule(docs)}.")
    print(f"Questions: {need_summary(docs)}.")
    need_gaps = [e for e in errors if re.search(r"sls/1-protocol/SQ\d+\.md: missing section '## (Kind|Unit|Enough when|Reading order)'"
                                                r"|sls/3-reading/P\d+\.md: missing section '## Serves'", e)]
    if need_gaps:
        errors = [e for e in errors if e not in need_gaps]
        errors.append(f"{len(need_gaps)} sections are missing because this review started before each question stated what it needs "
                      "and each record which questions it serves: adopt it with `/sls-1-protocol need` (research/sls/1-protocol/step.md)")
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


def view_ai_usage(docs):
    """What the AI proposed and what I did with it, per row: the basis of the Method chapter's AI statement."""
    counts = {}
    for d in decision_docs(docs):
        row = d.meta.get("row", "?")
        outcome = d.meta.get("decision", "?")
        counts.setdefault(row, {}).setdefault(outcome, 0)
        counts[row][outcome] += 1
    rows = []
    for row in sorted(counts, key=lambda r: (num(r), r)):
        c = counts[row]
        total = sum(c.values())
        rows.append([row, total, c.get("accepted", 0), c.get("changed", 0), c.get("rejected", 0)])
    totals = [sum(r[i] for r in rows) for i in range(1, 5)]
    sessions = len(list((RESEARCH / "ai-log" / "raw").glob("*.jsonl"))) - len(list((RESEARCH / "ai-log" / "raw").glob("*.transcript.jsonl"))) \
        if (RESEARCH / "ai-log" / "raw").is_dir() else 0
    return ("# AI usage\n\n" + HEADER + "\nDecisions I made at the gates, on files the AI proposed or I wrote "
            "(`ai/ai-log.md`). *Changed* means I accepted the file with my own edits.\n\n"
            + table(["Row", "Decisions", "Accepted as proposed", "Changed", "Rejected"], rows + ([["all", *totals]] if rows else []))
            + f"\nLogged sessions: {sessions}.\n")


def view_paper_questions(docs):
    """The link from each paper to each question: one row per included paper, one column per question."""
    qs, cov, serves = questions(docs), coverage(docs), serves_by_paper(docs)
    mark = {}
    for sq, c in cov.items():
        for p, new in c["read"]:
            mark[(p, sq)] = "+" if new else "="
        for p in c["next"]:
            mark.setdefault((p, sq), "→")
        for p in c["deferred"]:
            mark.setdefault((p, sq), "d")
    rows, none = [], []
    for pid, info in sorted(assigned_papers(docs).items(), key=lambda kv: num(kv[0])):
        sqs = serves.get(pid, set()) | {sq for (p, sq) in mark if p == pid}
        if not sqs:
            none.append(pid)
        cells = [mark.get((pid, sq), "·" if sq in sqs else "") for sq in qs]
        rows.append([f"{pid} {info['reference'][:50]}"] + cells)
    legend = ("`+` read, added something new · `=` read, nothing new for this question · `→` to read next · "
              "`d` deferred: the question has what it needs · `·` serves it, not yet in its coverage")
    tail = (f"\n**Serving no question ({len(none)}):** " + ", ".join(none) + "\n") if none else ""
    return ("# Papers and questions\n\n" + HEADER + "\n" + legend + "\n\n"
            + table(["Paper"] + list(qs), rows) + tail)


def view_coverage(docs):
    qs, cov = questions(docs), coverage(docs)
    rows = []
    for sq, (question, kind) in qs.items():
        c = cov.get(sq)
        if not c:
            rows.append([sq, question[:70], kind or "?", "no coverage yet", "", "", "", ""])
            continue
        state = c["state"] + ("" if c["decided"] else " (proposed)")
        rows.append([sq, question[:70], kind or "?", state, len(c["read"]), sum(1 for _, n in c["read"] if n),
                     len(c["next"]), len(c["deferred"])])
    return ("# Coverage\n\n" + HEADER + "\nWhether each review question has what it needs "
            "(`research/sls/1-protocol/step.md`, *How much each question needs*). " + need_summary(docs) + ".\n\n"
            + table(["SQ", "Question", "Kind", "Status", "Read", "Added something", "To read next", "Deferred"], rows))


def views(_args):
    docs = produced_docs()
    VIEWS.mkdir(exist_ok=True)
    for name, build in (("papers", view_papers), ("concept-matrix", view_concepts),
                        ("traceability", view_traceability), ("chapters", view_chapters),
                        ("ai-usage", view_ai_usage), ("paper-questions", view_paper_questions),
                        ("coverage", view_coverage)):
        (VIEWS / f"{name}.md").write_text(build(docs), encoding="utf-8")
        print(f"research/views/{name}.md")
    return 0


# ---------- status ----------

REVIEW = re.compile(r"\.(skeptic|citations|examiner)\.md$")
ENTRY_FILES = {  # the required step 0 file of each entry point (ai/entry-points.md)
    "observation.md": "problem-centred",
    "objectives.md": "objective-centred",
    "artifact.md": "design-centred",
    "context.md": "context-initiated, client engagement",
    "solution.md": "context-initiated, retroactive",
}


def entry_point():
    for name, entry in ENTRY_FILES.items():
        if (RESEARCH / "0-start" / name).is_file():
            return entry
    return ""


def project_settings():
    path = ROOT / "ai" / "project.md"
    return parse_frontmatter(path.read_text(encoding="utf-8"))[0] if path.is_file() else {}


def in_folder(docs, folder):
    return [d for d in flow_docs(docs) if d.rel.startswith(folder + "/") and not REVIEW.search(d.rel)]


def by_status(docs):
    counts = {}
    for d in docs:
        counts[d.status] = counts.get(d.status, 0) + 1
    order = ["accepted", "changed", "proposed", "provisional", "rejected", "retired"]
    return ", ".join(f"{counts[s]} {s}" for s in order if s in counts) or "nothing yet"


def step_state(docs, folder, done_when):
    """(state, detail) of one step folder: 'not started', 'in progress' or 'done'."""
    files = in_folder(docs, folder)
    if not files:
        return "not started", ""
    waiting = [d for d in files if d.status in ("proposed", "provisional")]
    done = not waiting and done_when(files)
    return ("done" if done else "in progress"), by_status(files)


def has(files, name, decided=True):
    return any(d.rel.endswith("/" + name) and (not decided or d.status in LIVE) for d in files)


def steps(docs):
    """Every step, in route order (ai/entry-points.md), as (name, state, detail)."""
    papers = assigned_papers(docs)
    records = {d.id: d for d in in_folder(docs, "sls/3-reading")}
    read = sum(1 for p in papers if p in records and records[p].status in DECIDED)
    objectives = [d for d in in_folder(docs, "dsrm/2-objectives") if kind_of(d) == "O" and d.status in LIVE]
    met = {o for e in in_folder(docs, "dsrm/5-evaluation") if kind_of(e) == "E" and e.status in LIVE
           and e.section("Result").strip().startswith("met") for o in re.findall(r"\bO\d+\b", e.section("Objective"))}
    finals = [n for n, p in chapter_sections(docs).items() if "final" in p and p["final"].status in LIVE]

    rows = {
        "0": ("Step 0, the starting point", *step_state(docs, "0-start", lambda f: True)),
        "S1": ("Literature 1, the review rules", *step_state(docs, "sls/1-protocol", lambda f: has(f, "criteria.md"))),
        "S2": ("Literature 2, finding papers", *step_state(docs, "sls/2-search", lambda f: "stop rule met" in stop_rule(docs))),
        "S3": ("Literature 3, reading papers", *step_state(docs, "sls/3-reading", lambda f: read == len(papers))),
        "S4": ("Literature 4, concepts", *step_state(docs, "sls/4-synthesis", lambda f: "stop rule met" in stop_rule(docs))),
        "S5": ("Literature 5, the gap", *step_state(docs, "sls/5-gap", lambda f: has(f, "gap.md"))),
        "D1": ("Design 1, the problem", *step_state(docs, "dsrm/1-problem", lambda f: has(f, "design-problem.md"))),
        "D2": ("Design 2, objectives", *step_state(docs, "dsrm/2-objectives", lambda f: bool(objectives))),
        "D3": ("Design 3, design and build", *step_state(docs, "dsrm/3-design", lambda f: bool(objectives) and met == {o.id for o in objectives})),
        "D4": ("Design 4, demonstration", *step_state(docs, "dsrm/4-demonstration", lambda f: bool(objectives) and met == {o.id for o in objectives})),
        "D5": ("Design 5, evaluation", *step_state(docs, "dsrm/5-evaluation", lambda f: bool(objectives) and met == {o.id for o in objectives})),
        "D6": ("Design 6, writing", *step_state(docs, "dsrm/6-communicate", lambda f: len(finals) >= 7 and has(f, "contribution.md"))),
    }
    extra = {
        "S2": stop_rule(docs),
        "S3": f"{read} of {len(papers)} papers in the review have a decided reading record; {need_summary(docs)}",
        "D5": f"{len(met)} of {len(objectives)} objectives met" if objectives else "",
        "D6": f"{len(finals)} final sections" if finals else "",
    }
    order = list(rows)  # every entry point runs the same order (ai/entry-points.md, *Routes*)
    out = []
    for key in order:
        name, state, detail = rows[key]
        detail = "; ".join(x for x in (detail, extra.get(key, "")) if x and state != "not started")
        out.append((name, state, detail))
    return out


def status(_args):
    docs = produced_docs()
    settings = project_settings()
    print(f"Entry point: {entry_point() or 'not chosen yet'}. Profile: {settings.get('profile', 'not chosen yet')}.")

    last = git("log", "-1", "--format=%h, %cr: %s").strip()
    print(f"\nLast commit: {last or 'none yet'}")
    if last:
        files = [f for f in git("show", "--name-only", "--format=", "HEAD").split() if not f.startswith("research/ai-log/raw/")]
        print(f"  {len(files)} file(s): " + ", ".join(files[:8]) + (", …" if len(files) > 8 else ""))

    pending = [l[3:] for l in git("status", "--porcelain", "--", "research", "artifact").splitlines()
               if "research/ai-log/raw/" not in l]
    print(f"\nIn progress (not committed): {len(pending)} file(s)")
    for f in pending[:15]:
        print(f"  {f}")
    if len(pending) > 15:
        print(f"  … and {len(pending) - 15} more")

    print("\nSteps:")
    current = None
    for name, state, detail in steps(docs):
        print(f"  [{ {'done': 'x', 'in progress': '~', 'not started': ' '}[state] }] {name}: {state}" + (f" ({detail})" if detail else ""))
        if current is None and state != "done":
            current = name
    done = sum(1 for _, s, _ in steps(docs) if s == "done")
    print(f"\nProgress: {done} of 12 steps done. Current step: {current or 'all done'}.")
    waiting = [d for d in flow_docs(docs) if d.status in ("proposed", "provisional") and not REVIEW.search(d.rel)]
    print(f"Waiting for my decision: {len(waiting)} file(s).")
    return 0


# ---------- export ----------

BUILD = ROOT / "build"
REFERENCES = VIEWS / "references.json"  # generated, committed, so an export works offline
DOI = re.compile(r"\b(10\.\d{4,9}/[^\s|)>\]]+)", re.I)
CITE = re.compile(r"@(P\d+)\b")
CHAPTERS = {1: "Introduction", 2: "Literature review", 3: "Method", 4: "Artifact description",
            5: "Evaluation", 6: "Discussion", 7: "Conclusion"}  # research/README.md, *Thesis chapters*


def natural(text: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", text)]


def paper_doi(pid, records, papers):
    """The paper's DOI: its record's frontmatter, its reference, or its row in the round file."""
    rec = records.get(pid)
    for text in ((rec.meta.get("doi", "") if rec else ""), (rec.section("Reference") if rec else ""),
                 papers.get(pid, {}).get("reference", "")):
        m = DOI.search(text or "")
        if m:
            return m.group(1).rstrip(".,;")
    return ""


def fetch_csl(doi: str):
    """CSL-JSON for a DOI, by content negotiation at doi.org. None when offline or unknown."""
    import json
    import urllib.request
    req = urllib.request.Request(f"https://doi.org/{doi}", headers={"Accept": "application/vnd.citationstyles.csl+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return clean_csl(json.loads(r.read().decode("utf-8")))
    except Exception:
        return None


CSL_NAMES = {"author", "editor"}
CSL_DATES = {"issued"}
CSL_TEXT = {"type", "title", "container-title", "collection-title", "volume", "issue", "page", "DOI", "URL",
            "publisher", "publisher-place", "edition", "ISBN", "ISSN", "event", "genre", "number"}


def clean_csl(item: dict) -> dict:
    """Keep only standard CSL fields: doi.org adds registry data (lists, nested records) pandoc rejects."""
    out = {}
    for key, value in item.items():
        if key in CSL_NAMES and isinstance(value, list):
            out[key] = [{k: v for k, v in n.items() if k in ("given", "family", "literal", "suffix", "non-dropping-particle")}
                        for n in value if isinstance(n, dict)]
        elif key in CSL_DATES and isinstance(value, dict) and "date-parts" in value:
            out[key] = {"date-parts": value["date-parts"]}
        elif key in CSL_TEXT:
            if isinstance(value, list):
                value = value[0] if value else None
            if isinstance(value, (str, int)) and value != "":
                out[key] = value
    return out


def parse_reference(pid: str, text: str):
    """A minimal CSL item from a reference written as 'Authors (year). *Title*. Venue.'"""
    m = re.match(r"\s*(?P<authors>.+?)\s*\((?P<year>\d{4})[a-z]?\)\.?\s*\*(?P<title>.+?)\*\.?\s*(?P<venue>.*?)\.?\s*$", text)
    if not m:
        return {"id": pid, "type": "article", "title": text.strip()}
    item = {"id": pid, "type": "article-journal", "title": m["title"], "issued": {"date-parts": [[int(m["year"])]]},
            "author": [{"literal": a.strip()} for a in re.split(r",\s*(?:and\s+)?|\s+and\s+", m["authors"]) if a.strip()]}
    if m["venue"]:
        item["container-title"] = m["venue"]
    return item


def build_references(docs, cited):
    """research/views/references.json: one CSL item per cited paper, keyed by its P ID."""
    import json
    old = {}
    if REFERENCES.is_file():
        old = {i["id"]: i for i in json.loads(REFERENCES.read_text(encoding="utf-8"))}
    papers = assigned_papers(docs)
    records = {d.id: d for d in docs if d.rel.startswith("sls/3-reading/") and kind_of(d) == "P"}
    items, notes = [], []
    for pid in sorted(cited, key=num):
        doi = paper_doi(pid, records, papers)
        item = old.get(pid)
        if item is None or (doi and item.get("DOI", "").lower() != doi.lower()):
            fetched = fetch_csl(doi) if doi else None
            if fetched:
                item = fetched
            else:
                ref = records[pid].section("Reference").strip() if pid in records else papers.get(pid, {}).get("reference", "")
                item = parse_reference(pid, ref)
                notes.append(f"{pid}: " + (f"DOI {doi} could not be looked up (offline?)" if doi else "no DOI") + "; built from its reference text")
        item["id"] = pid
        items.append(item)
    VIEWS.mkdir(exist_ok=True)
    REFERENCES.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return notes


def export(args):
    """Assemble the accepted final sections into build/thesis.md, then build .docx and .pdf with pandoc."""
    docs = produced_docs()
    settings = project_settings()
    sections = sorted(((n, p["final"]) for n, p in chapter_sections(docs).items()
                       if "final" in p and p["final"].status in LIVE),
                      key=lambda kv: (num(kv[0]), natural(kv[0])))
    if not sections:
        print("No accepted final section yet (dsrm/6-communicate/ch{n}-{section}.md): nothing to export.")
        return 1
    body, chapter, cited, bare = [], None, set(), set()
    for name, d in sections:
        n = num(name)
        if n != chapter:
            body.append(f"# {CHAPTERS.get(n, f'Chapter {n}')}\n")
            chapter = n
        text = re.sub(r"^# .*\n", "", d.body, count=1)              # the file's own title
        text = re.sub(r"^Saved as `.*\n", "", text, flags=re.M)      # template boilerplate
        title = re.sub(r"^\d+-", "", name.split("-", 1)[1]).replace("-", " ").capitalize()
        body.append(f"## {title}\n\n{text.strip()}\n")
        here = set(CITE.findall(text))
        cited |= here
        bare |= set(re.findall(r"(?<![@\w])P\d+\b", text)) - here
    notes = build_references(docs, cited)

    BUILD.mkdir(exist_ok=True)
    bibs = [REFERENCES] + ([RESEARCH / "references.bib"] if (RESEARCH / "references.bib").is_file() else [])
    meta = ["---", f"title: \"{settings.get('title', 'Thesis')}\"", f"author: \"{settings.get('author', '')}\"",
            "link-citations: true", "bibliography:"] + [f"  - {p.relative_to(ROOT).as_posix()}" for p in bibs]
    style = settings.get("citation_style", "default")
    if style not in ("", "default"):
        meta.append(f"csl: {style}")
    meta += ["---", ""]
    source = BUILD / "thesis.md"
    source.write_text("\n".join(meta) + "\n".join(body) + "\n# References\n", encoding="utf-8")
    print(f"{source.relative_to(ROOT)}: {len(sections)} section(s), {len(cited)} paper(s) cited.")
    for note in notes:
        print(f"  reference: {note}")
    if bare:
        print(f"  not cited with [@P..] syntax, so not in the bibliography: {', '.join(sorted(bare, key=num))}")

    failed = 0
    reference_doc = settings.get("reference_doc", "none")
    for target, extra in (("docx", [f"--reference-doc={reference_doc}"] if reference_doc not in ("", "none") else []),
                          ("pdf", ["--pdf-engine=typst", "-V", "mainfont=Libertinus Serif"])):
        out = BUILD / f"thesis.{target}"
        r = subprocess.run(["pandoc", source.relative_to(ROOT).as_posix(), "--citeproc",
                            "-o", out.relative_to(ROOT).as_posix(), *extra],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode == 0:
            print(f"{out.relative_to(ROOT)}")
        else:
            failed = 1
            print(f"{out.relative_to(ROOT)}: pandoc failed:\n{r.stderr.strip()}")
    return failed


if __name__ == "__main__":
    commands = {"check": check, "views": views, "status": status, "export": export}
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print(__doc__)
        sys.exit(2)
    sys.exit(commands[sys.argv[1]](sys.argv[2:]))
