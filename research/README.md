# Research methods

Two methods, each followed as its source defines it.

| Folder | Method | Role |
|---|---|---|
| `sls/` | Systematic Literature Study: protocol from Kitchenham and Charters [1], snowballing search from Wohlin [2] | Learn what exists, find the gap |
| `dsrm/` | Design Science Research Methodology from Peffers et al. [3] | Build and evaluate the artifact |

Both folders share one layout: a `README.md` stating the method and its sources, then numbered step folders, each with a `step.md` (what to fill in) and a `faq.md` (how and why).

## How they connect
```
dsrm/1 §1.1 observation → sls/1 protocol → … → sls/5 gap → dsrm/1 problem → dsrm/2 objectives → …
                                                sls/4 synthesis ────────────────────────────→ dsrm/3 design
```

| DSRM activity | Needs [3] | Comes from |
|---|---|---|
| — | (the study's starting point) | `dsrm/1-problem/step.md` §1.1 feeds `sls/1-protocol/` |
| 1 Problem | Knowledge of the state of the problem and why solving it matters | `sls/5-gap/step.md` |
| 2 Objectives | Knowledge of current solutions and what is feasible | `sls/5-gap/step.md` |
| 3 Design | Knowledge of theory that can be brought to bear | `sls/4-synthesis/step.md` |

## Thesis chapters
The thesis is built from both methods. Outline from `dsrm/6-communicate/step.md`.

| Chapter | Built from | Draft status | Last synced with source |
|---|---|---|---|
| 1 Introduction | `dsrm/1-problem/`, `dsrm/2-objectives/` | `[todo/draft/stable]` | `[date or commit]` |
| 2 Literature review | `sls/4-synthesis/`, `sls/5-gap/` | `[ ]` | `[ ]` |
| 3 Method | `dsrm/README.md`, `sls/README.md` | `[ ]` | `[ ]` |
| 4 Artifact description | `dsrm/3-design/` | `[ ]` | `[ ]` |
| 5 Evaluation | `dsrm/4-demonstration/`, `dsrm/5-evaluation/` | `[ ]` | `[ ]` |
| 6 Discussion | `dsrm/5-evaluation/` §5.3, contribution type in `dsrm/6-communicate/step.md` | `[ ]` | `[ ]` |
| 7 Conclusion | all of the above | `[ ]` | `[ ]` |

If a source changed after the "last synced" date, the chapter is stale.

---

## References
1. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
2. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
3. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
