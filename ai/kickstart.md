# Kickstart

The pipeline starts from step 0: the observation. It lives in `research/0-start/`, apart from the DSRM steps, because it is my input, not the output of any step.

## Step 0
For the problem-centred route (`entry-points.md`):

| File | Required | Holds |
|---|---|---|
| `observation.md` | yes | The observation as a gap: what is true in one domain and not in another |
| `seeds.md` | no | References I already know. Seeds for the start set (row 2a), not results. |
| `notes.md` | no | Anything I already think about the problem, as I wrote it. Input for DSRM 1, not a commitment. |

| # | Who | Input | Output | Gate |
|---|---|---|---|---|
| **0** | Me | — | `0-start/*.md` | **Start.** Frozen when row 1a runs. |

Everything else about the problem (motivation, design problem, RQs, hypotheses, stances, stakeholders) is built in DSRM 1, after the SLS, from the observation and the literature (rows 6a–6d, `flow-dsrm.md`). Peffers et al. build the problem from knowledge of the state of the problem [2]; step 0 comes before that knowledge.

## Rules
- **Step 0 is never edited after it is frozen.** It records where the work started.
- **`notes.md` is checked, not trusted.** DSRM 1 marks each of its claims confirmed, to revise or contradicted by the literature (row 6a).

## Safeguards
- **Protocol bias:** if `notes.md` argues for a conclusion, SQs drawn from it would only look for support. `skeptic` adds SQs that look for evidence against it (row 1b, `flow-sls.md`).
- **Start set bias:** snowballing only from `seeds.md` mostly finds more of the same. The start set also uses a database search string (row 2a), as Wohlin recommends a varied start set [1].

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
2. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
