# Flow: DSRM

Rows run by the `dsrm` skill (`skills.md`), after the SLS (`flow-sls.md`). Paths are relative to `research/`. `{n}` is an ID number, `{k}` a run number. Every gate also writes one decision file (`ai-log.md`). `↺` rows are loop decisions.

| # | Who | Input | Output | Gate |
|---|---|---|---|---|
| **DSRM 1 Problem** · `dsrm-1-problem` | | | | |
| 6a | `synthesizer` | `0-start/*.md`, `sls/5-gap/*.md` | `dsrm/1-problem/`: `motivation.md` (why it matters and why earlier attempts failed, backed by P IDs), `revision.md` (only if `0-start/notes.md` exists: each claim confirmed / to revise / contradicted) | — |
| 6b | `synthesizer` | `0-start/*.md`, 6a files | `dsrm/1-problem/`: `design-problem.md`, `RQ{n}.md`, `H{n}.md`, `stances.md`, `stakeholders.md` | — |
| 6c | `skeptic` | 6a + 6b files | `dsrm/1-problem/problem.skeptic.md` | — |
| 6d | Me | 6a–6c files | Status set; what I change is recorded in the decision file | **Problem and RQs** |
| **DSRM 2 Objectives** · `dsrm-2-objectives` | | | | |
| 7a | Me | Accepted `dsrm/1-problem/RQ*.md`, `sls/5-gap/solutions.md` | `dsrm/2-objectives/`: `O{n}.md` (traces to, kind, check, validation type), `metrics.md`, `baselines.md` | — |
| 7b | `skeptic` | 7a files | `dsrm/2-objectives/objectives.skeptic.md` | — |
| 7c | Me | 7a + 7b files | Status set | **Objectives frozen** before any results |
| **DSRM 3 Design** · `dsrm-3-design` | | | | |
| 8a | `designer` | Accepted `O*.md`, `C*.md`, `dsrm/3-design/DEC*.md` | `dsrm/3-design/DEC{n}.options.md` | — |
| 8b | Me | `DEC{n}.options.md` | `dsrm/3-design/DEC{n}.md` (choice and why) | **Design choice** |
| 8c | `builder` | Accepted `DEC*.md`, current layer | `artifact/L{n}/…`, `dsrm/3-design/L{n}.md` (what was built, version, check results) | — |
| 8d | Me | 8c files | Status set; I can explain the layer | **Layer accepted** |
| **DSRM 4 Demonstration** · `dsrm-4-demonstration` | | | | |
| 9a | `demonstrator` | `dsrm/3-design/L{n}.md`, accepted `O*.md` | `dsrm/4-demonstration/D{n}.md` (instance, layer, activity, objectives fed) | — |
| 9b | Me | `D{n}.md` | Status set | **Plan** |
| 9c | `demonstrator` | Accepted `D{n}.md`, `artifact/L{n}/` | `dsrm/4-demonstration/D{n}-run{k}.md` | — |
| 9d | Me | `D{n}-run{k}.md` | Status set | **Solved?** |
| **DSRM 5 Evaluation** · `dsrm-5-evaluation` | | | | |
| 10a | `evaluator` | Accepted `O*.md`, `metrics.md`, `baselines.md`, `D*-run*.md` | `dsrm/5-evaluation/E{n}.md`, `T{n}.md` (threats) | — |
| 10b | `skeptic` | 10a files | `dsrm/5-evaluation/E{n}.skeptic.md` | — |
| 10c | Me | 10a + 10b files | Status set | **Results** |
| ↺ | Me | Accepted `E*.md` | Next layer or fix → 8a. Objective wrong → 7a. All met → 11a | **Iteration** [1] |
| **DSRM 6 Communicate** · `dsrm-6-communicate` | | | | |
| 11a | Me | Accepted files of 1–5 | `dsrm/6-communicate/ch{n}-{section}.outline.md` (claims, sources) | **Argument** |
| 11b | `drafter` | One outline + its sources | `dsrm/6-communicate/ch{n}-{section}.draft.md` | — |
| 11c | `citation-checker` | The draft + its sources | `ch{n}-{section}.citations.md` | — |
| 11d | `examiner` | The draft | `ch{n}-{section}.examiner.md` | — |
| 11e | Me | 11b–11d files | `ch{n}-{section}.md` (final), `contribution.md` | **Text** |
| ↺ | Me | 11d–11e files | Writing exposes a hole → 7a or 8a | **Iteration** [1] |

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
