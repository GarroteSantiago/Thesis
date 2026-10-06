# Checks

Two `just` recipes, both running `ai/tools/research.py`. Neither is an agent: both are scripts, so they give the same answer every time.

## `just check`
Runs after every gate. Fails if any of these is broken:
- **Status:** every file's `status` is one of the six in `files.md`.
- **Traceability:** the linking sections name IDs that exist and are not retired or rejected: O *Traces to* → RQ, H *Tested by* → RQ, D *Feeds* → O and *Artifact layer* → L, E *Question* → RQ, *Objective* → O and *Demonstrations used* → D runs, L *Decisions implemented* → DEC.
- **ID rule:** compared with the last commit, no file with an ID was removed and no ID changed; it was retired instead (`research/dsrm/README.md`).
- **Stale chapters:** an accepted chapter section whose outline or outline inputs changed after its decision file.
- **Complete files:** every file matches a template, has every `##` section of it, and has no `{placeholder}` or `[ ]` left outside code blocks (`files.md`).
- **Decisions:** every file with a decided status has a decision file targeting it, and every decision targets a file that exists (`ai-log.md`).
- **Stop rule:** reports whether the last snowballing round added new papers (`flow-sls.md`).

## `just views`
Regenerates `views/` from frontmatter (`files.md`). Never edited by hand.
- Paper list
- Concept matrix
- Traceability: RQ → O → D → E
- Chapter status
