# Flow: SLS

Rows run by the `sls` skill (`skills.md`), after step 0 (`kickstart.md`). Paths are relative to `research/`. `{n}` is an ID number, `{k}` a round number. Every gate also writes one decision file (`ai-log.md`). `↺` rows are loop decisions.

| # | Who | Input | Output | Gate |
|---|---|---|---|---|
| **SLS 1 Protocol** · `sls-1-protocol` | | | | |
| 1a | `protocol-critic` | `0-start/*.md` | `sls/1-protocol/`: `need.md`, `SQ{n}.md` (each with its kind, unit and enough-when rule), `criteria.md`, `quality.md`, `extraction-form.md` | — |
| 1b | `skeptic` | `0-start/*.md`, `sls/1-protocol/SQ*.md` | `sls/1-protocol/SQ{n}.md` (counter-evidence SQs), `protocol.skeptic.md` | — |
| 1c | Me | 1a + 1b files | Status of each set | **Protocol frozen.** Later changes: `sls/1-protocol/changes/{date}-{slug}.md` |
| **SLS 2 Search** · `sls-2-search` | | | | |
| 2a | `snowballer` | `sls/1-protocol/criteria.md`, `sls/1-protocol/SQ*.md`, `0-start/seeds.md` | `sls/2-search/search-string.md`, `R0.md` (candidates, each with its I/X criterion and the SQs it would serve) | — |
| 2b | Me | `sls/2-search/R0.md` | P IDs assigned in `R0.md` | **Include/exclude** |
| 2c | `snowballer` | `sls/2-search/R{k-1}*.md`, `sls/1-protocol/criteria.md`, `sls/1-protocol/SQ*.md`, accepted `sls/4-synthesis/SQ*.coverage.md`: only the papers that added something new to a question still open | `sls/2-search/R{k}-backward*.md`, `R{k}-forward*.md` (one pair per batch: `R{k}-backward.md`, `R{k}-backward-2.md`…) | — |
| 2d | Me | 2c files | P IDs assigned | **Include/exclude** |
| **SLS 3 Reading** · `sls-3-reading` (for each new P) | | | | |
| 3a | `reader` | `papers/P{n}.pdf` (else the paper online), `sls/1-protocol/quality.md`, `extraction-form.md`, `criteria.md`, `SQ*.md`, accepted `sls/4-synthesis/C*.md` once any exist | `sls/3-reading/P{n}.md` (with the SQs it serves and what it adds to each), `papers/P{n}.pdf` if downloaded | — |
| 3b | `citation-checker` | `sls/3-reading/P{n}.md`, the paper | `sls/3-reading/P{n}.citations.md` | — |
| 3c | Me | 3a + 3b files | Status set; key papers proposed (`sls/3-reading/step.md`); PDFs published with `just papers-push` | **Record accepted** |
| **SLS 4 Synthesis** · `sls-4-synthesis` | | | | |
| 4a | `synthesizer` | Accepted `sls/3-reading/P*.md`, `sls/4-synthesis/C*.md`, `sls/4-synthesis/SQ*.coverage.md`, `sls/1-protocol/SQ*.md`, `sls/2-search/R*.md` | `sls/4-synthesis/C{n}.md` (definition, papers, comparison), new or updated; `SQ{n}.coverage.md` per SQ (papers read, what is new, status, what to read next, what is deferred) | — |
| 4b | Me | 4a files | Status set; merges and splits; key papers updated; each question's status (open, saturated, complete) confirmed | **Concepts and coverage accepted** |
| ↺ | `just check` | Accepted `sls/4-synthesis/SQ*.coverage.md`, last `sls/2-search/R{k}*.md` | Every SQ saturated or complete, or the last round found no new paper → 5a. An open SQ with papers to read next → 3a. An open SQ with none → 2c | Stop rule [1][2][3] |
| **SLS 5 Gap** · `sls-5-gap` | | | | |
| 5a | `synthesizer` | Accepted `sls/4-synthesis/C*.md`, `sls/4-synthesis/SQ*.coverage.md`, `sls/1-protocol/SQ*.md` | `sls/5-gap/`: `SQ{n}.answer.md`, `gap.md`, `solutions.md`, `history.md`, `limitations.md` | — |
| 5b | `skeptic` | 5a files | `sls/5-gap/gap.skeptic.md` | — |
| 5c | Me | 5a + 5b files | Status set; key papers extended from `gap.md` and read in full | **Gap** |

Next: row 6a (`flow-dsrm.md`).

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
2. Webster, Watson (2002). *Analyzing the Past to Prepare for the Future: Writing a Literature Review*. Management Information Systems Quarterly 26(2).
3. Francis et al. (2010). *What Is an Adequate Sample Size? Operationalising Data Saturation for Theory-Based Interview Studies*. Psychology & Health 25(10), 1229–1245.
