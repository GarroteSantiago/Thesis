# Flow: SLS

Rows run by the `sls` skill (`skills.md`), after step 0 (`kickstart.md`). Paths are relative to `research/`. `{n}` is an ID number, `{k}` a round number. Every gate also writes one decision file (`ai-log.md`). `↺` rows are loop decisions.

| # | Who | Input | Output | Gate |
|---|---|---|---|---|
| **SLS 1 Protocol** · `sls-1-protocol` | | | | |
| 1a | `protocol-critic` | `0-start/*.md` | `sls/1-protocol/`: `need.md`, `SQ{n}.md`, `criteria.md`, `quality.md`, `extraction-form.md` | — |
| 1b | `skeptic` | `0-start/*.md`, `sls/1-protocol/SQ*.md` | `sls/1-protocol/SQ{n}.md` (counter-evidence SQs), `protocol.skeptic.md` | — |
| 1c | Me | 1a + 1b files | Status of each set | **Protocol frozen.** Later changes: `sls/1-protocol/changes/{date}-{slug}.md` |
| **SLS 2 Search** · `sls-2-search` | | | | |
| 2a | `snowballer` | `sls/1-protocol/criteria.md`, `0-start/seeds.md` | `sls/2-search/search-string.md`, `R0.md` (candidates, each with its I/X criterion) | — |
| 2b | Me | `sls/2-search/R0.md` | P IDs assigned in `R0.md` | **Include/exclude** |
| 2c | `snowballer` | `sls/2-search/R{k-1}*.md`, `sls/1-protocol/criteria.md` | `sls/2-search/R{k}-backward.md`, `R{k}-forward.md` | — |
| 2d | Me | 2c files | P IDs assigned | **Include/exclude** |
| **SLS 3 Reading** · `sls-3-reading` (for each new P) | | | | |
| 3a | `reader` | The paper, `sls/1-protocol/quality.md`, `extraction-form.md` | `sls/3-reading/P{n}.md` | — |
| 3b | `citation-checker` | `sls/3-reading/P{n}.md`, the paper | `sls/3-reading/P{n}.citations.md` | — |
| 3c | Me | 3a + 3b files | Status set; key papers read in full | **Record accepted** |
| **SLS 4 Synthesis** · `sls-4-synthesis` | | | | |
| 4a | `synthesizer` | Accepted `sls/3-reading/P*.md`, `sls/4-synthesis/C*.md` | `sls/4-synthesis/C{n}.md` (definition, papers, comparison), new or updated | — |
| 4b | Me | 4a files | Status set; merges and splits | **Concepts accepted** |
| ↺ | `just check` | Last `sls/2-search/R{k}*.md` | New papers? Yes → 2c. No → 5a | Stop rule [1] |
| **SLS 5 Gap** · `sls-5-gap` | | | | |
| 5a | `synthesizer` | Accepted `sls/4-synthesis/C*.md`, `sls/1-protocol/SQ*.md` | `sls/5-gap/`: `SQ{n}.answer.md`, `gap.md`, `solutions.md`, `history.md`, `limitations.md` | — |
| 5b | `skeptic` | 5a files | `sls/5-gap/gap.skeptic.md` | — |
| 5c | Me | 5a + 5b files | Status set | **Gap** |

Next: row 6a (`flow-dsrm.md`).

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
