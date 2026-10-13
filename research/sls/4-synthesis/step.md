# Step 4 — Synthesis (concept matrix)

> **Inputs:** accepted `3-reading/P*.md` · **Next:** `5-gap/`

> Webster and Watson [1]: organize the review by concept, not by author.
> - Rows = papers. Columns = concepts found in the papers.
> - Mark a cell when the paper discusses that concept, with the page.

## In plain words
Instead of summarising paper by paper, we organise what was read by idea (concept): what each paper says about it, where they agree, where they disagree, what nobody covers.

- **The AI:** proposes new concepts and updates existing ones from the accepted records.
- **I decide:** each new or changed concept, and any merge or split. A handful per round. Then the list of key papers is updated from the papers each accepted concept rests on (`3-reading/step.md`, *Rules*).
- **Result:** the concepts and the concept matrix. Then the next snowballing round, until a round adds no new paper.

## Rules
- The matrix is generated from the concepts in each `P{n}.md` (`just views`), never written by hand.
- **Coverage, per question:** `SQ{n}.coverage.md` lists the papers read for that question in reading order, marks each contribution *new* or *covered by* an earlier paper, applies the question's enough-when rule (`1-protocol/step.md`), and lists what to read next, what is deferred, and the audit. A review is nearing completion when new papers stop adding new concepts [1]; the coverage files apply that test question by question.
- `just views` builds the paper × question matrix (`views/paper-questions.md`) and the coverage summary (`views/coverage.md`) from these files.

## Produces
Template in `ai/template/sls/4-synthesis/`. Flow rows 4a–4b (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `C{n}.md` | One concept: definition, and what the papers say, compared |
| `SQ{n}.coverage.md` | One question: the papers read for it and what each added, its status, what to read next, what is deferred |

---

## References
1. Webster, Watson (2002). *Analyzing the Past to Prepare for the Future: Writing a Literature Review*. Management Information Systems Quarterly 26(2).
