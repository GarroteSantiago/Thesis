# Files

Small files, each produced whole in one transaction. No large file that fills up over months.

## Rules
- **One file per output.** Each flow row writes the exact files listed in its Output column, and reads only the files in its Input column (`flow-sls.md`, `flow-dsrm.md`).
- **One file per entity,** named by its ID: `SQ1.md`, `P12.md`, `C3.md`, `O1.md`, `D1.md`, `E1.md`. Anything that would grow (a log, a list of rounds) is a folder of entries instead.
- **Reviews of a file sit next to it,** named `<file>.<kind>.md`: `P12.citations.md`, `gap.skeptic.md`.
- **Complete when written.** A file has no `{placeholder}` or `[ ]` left. If a field cannot be filled, it says why.
- **A gate changes only `status`.** If I change content, the decision file says what and why (`ai-log.md`).
- **Tables are generated, not written.** The concept matrix, paper list, traceability (RQ → O → D → E) and chapter status are built by `just views` into `views/`, which is never edited by hand (`checks.md`).
- **The template is the spec.** Every file is a copy of its template in `template/`, which lists where each one is saved and which row writes it. `step.md` keeps only the method: what the step means, its sources, its rules. `faq.md` stays as it is.

## Frontmatter
On every file:
```
---
id: P12
row: 3a                    # the flow row that wrote it
by: reader                 # agent name, or me
status: proposed           # provisional | proposed | accepted | changed | rejected | retired
inputs: [sls/1-protocol/extraction-form.md, sls/1-protocol/quality.md]
---
```
