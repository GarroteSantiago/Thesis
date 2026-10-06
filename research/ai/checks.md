# Checks

Two `just` recipes. Neither is an agent: both are scripts, so they give the same answer every time.

## `just check`
Runs after every gate. Fails if any of these is broken:
- **Traceability:** every file names IDs that exist (O → RQ, D → O, E → O and D).
- **ID rule:** no ID was renamed or removed; it was retired instead (`dsrm/README.md`).
- **Stale chapters:** a chapter section whose sources changed after it was accepted.
- **Complete files:** no `{placeholder}` or `[ ]` left, and every section of the template present (`files.md`).
- **Decisions:** every gate has a decision file (`ai-log.md`).
- **Stop rule:** reports whether the last snowballing round added new papers (`flow-sls.md`).

## `just views`
Regenerates `views/` from frontmatter (`files.md`). Never edited by hand.
- Paper list
- Concept matrix
- Traceability: RQ → O → D → E
- Chapter status
