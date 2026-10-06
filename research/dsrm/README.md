# Method: Design Science Research Methodology

The process of Peffers et al. [1]: six activities, nominally sequential, run here as written.

## Activities
| Folder | Activity [1] | Changes |
|---|---|---|
| `1-problem/` | Problem identification and motivation | Rarely |
| `2-objectives/` | Define the objectives for a solution | Rarely |
| `3-design/` | Design and development | Every iteration |
| `4-demonstration/` | Demonstration | Every iteration |
| `5-evaluation/` | Evaluation | Every iteration |
| `6-communicate/` | Communication | When chapters move |

## Sequence, entry point, iteration
- **Sequence:** 1 → 2 → 3 → 4 → 5 → 6 [1].
- **Entry point:** problem-centred. The work starts from an observation (`../0-start/observation.md`) [1].
- **Iteration:** Peffers allows going back from Evaluation (5) and Communication (6) to Objectives (2) or Design (3) [1]. Each pass through 3 → 5 is Simon's generate–test cycle [2] and Hevner's design cycle [3]. Every evaluation entry states where the next pass goes.

## My operational rules (not part of Peffers)
These are working rules for keeping the repository consistent. They do not change the method.
- **Traceability [4]:** Observation → Design problem → Questions (RQ) → Objectives (O) → Demonstrations (D) and Evaluations (E). Every piece names the ID it serves.
- **ID rule:** never rename an ID. Retire it and create a new one.
- **Re-check after iterating:** when an iteration arc changes step 2 or 3, re-check the later steps that used the old version.
- **Sorting rule for any demo or result:**
  1. Someone else built it → not logged here.
  2. I built it and it shows the artifact solving an instance → a demonstration run (`4-demonstration/D{n}-run{k}.md`).
  3. I built it and it measures an objective → an evaluation (`5-evaluation/E{n}.md`).
  4. I built it and it serves no question → exploration notes. If it reveals a new question, go back to `1-problem/`.
- **One folder per activity,** because each changes at a different speed [5]. Create a folder only when a real file needs it [6][7].

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
2. Simon (1996). *The Sciences of the Artificial* (3rd edition). Massachusetts Institute of Technology Press.
3. Hevner (2007). *A Three Cycle View of Design Science Research*. Scandinavian Journal of Information Systems 19(2).
4. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
5. Parnas (1972). *On the Criteria to Be Used in Decomposing Systems into Modules*. Communications of the Association for Computing Machinery 15(12).
6. Beck (2000). *Extreme Programming Explained: Embrace Change*. Addison-Wesley.
7. Wilson et al. (2017). *Good Enough Practices in Scientific Computing*. Public Library of Science Computational Biology 13(6).
