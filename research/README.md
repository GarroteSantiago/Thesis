# Research

Step 0 and two methods, each method followed as its source defines it.

| Folder | What | Role |
|---|---|---|
| `0-start/` | Step 0: the observation, my seeds and notes | Where the work starts. Frozen before the review. |
| `papers/` | PDFs of the included papers, `P{n}.pdf`. Not in git: published to the `papers` release of the GitHub repo (`papers/README.md`) | What `reader` reads first |
| `sls/` | Systematic Literature Study: protocol from Kitchenham and Charters [1], snowballing search from Wohlin [2] | Learn what exists, find the gap |
| `dsrm/` | Design Science Research Methodology from Peffers et al. [3] | Build and evaluate the artifact |

`sls/` and `dsrm/` share one layout: a `README.md` stating the method and its sources, then numbered step folders, each with a `step.md` (the method of that step and the files it produces), a `faq.md` (how and why), and the produced files. Every produced file is a copy of its template in `../ai/template/`; how AI produces them is in `../ai/`.

## How they connect
```
0-start → sls/1 protocol → … → sls/5 gap → dsrm/1 problem → dsrm/2 objectives → …
                               sls/4 synthesis ─────────────────────→ dsrm/3 design
```

| DSRM activity | Needs [3] | Comes from |
|---|---|---|
| — | (the study's starting point) | `0-start/` feeds `sls/1-protocol/` |
| 1 Problem | Knowledge of the state of the problem and why solving it matters | `sls/5-gap/` |
| 2 Objectives | Knowledge of current solutions and what is feasible | `sls/5-gap/solutions.md` |
| 3 Design | Knowledge of theory that can be brought to bear | `sls/4-synthesis/` |

## Thesis chapters
The thesis is built from both methods. Outline from `dsrm/6-communicate/step.md`. Chapter status is generated into `views/` (`../ai/checks.md`).

| Chapter | Built from |
|---|---|
| 1 Introduction | `dsrm/1-problem/`, `dsrm/2-objectives/` |
| 2 Literature review | `sls/4-synthesis/`, `sls/5-gap/` |
| 3 Method | `dsrm/README.md`, `sls/README.md` |
| 4 Artifact description | `dsrm/3-design/` |
| 5 Evaluation | `dsrm/4-demonstration/`, `dsrm/5-evaluation/` |
| 6 Discussion | `dsrm/5-evaluation/T*.md`, `dsrm/6-communicate/contribution.md` |
| 7 Conclusion | all of the above |

---

## References
1. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
2. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
3. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
