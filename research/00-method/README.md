# Method: Design Science Research

One design problem, filled in passes. Each step lives in its own file because each changes at a different speed [1].

## Files
| File | Step | Changes |
|---|---|---|
| `1-problem.md` | Identify the problem | Rarely |
| `2-objectives.md` | Define objectives | Rarely |
| `3-literature.md` | Literature review + concept matrix | Every reading session |
| `4-design.md` | Design and develop | Every experiment |
| `5-evaluation.md` | Evidence, results log, threats | Every experiment |
| `6-communicate.md` | Chapter outline and drafting | When chapters move |

## Chain
**Observation → Questions → Objectives → Evidence → Matrix columns → Experiments**

Every piece points back to the question it serves (*traceability*) [2].

## Dependency rule (not a sequence)
A step can run any time its inputs exist, even rough ones [3][4].

| Step | Needs some content in… |
|---|---|
| 1 | nothing |
| 2 | 1 |
| 3 | 2 (matrix columns = objectives) |
| 4 | 2, and 3 for the gap |
| 5 | 2 and 4 |
| 6 | whatever is stable |

- **Stale marking:** when a step changes, re-check the steps that depend on it, the way Nix or Make rebuild only what depends on a changed input.
- **ID rule:** IDs (RQ1, O1, …) link the files. Never rename one; retire it and create a new one.

## Sorting rule for any demo or result
1. Someone else built it → row in the matrix (`3-literature.md`).
2. I built it and it answers a question → results log (`5-evaluation.md`).
3. I built it and it answers no question → exploration notes. If it reveals a new question, go back to `1-problem.md`.

---

## References
1. Parnas (1972). *On the Criteria to Be Used in Decomposing Systems into Modules*. Communications of the Association for Computing Machinery 15(12).
2. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
3. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
4. Hevner (2007). *A Three Cycle View of Design Science Research*. Scandinavian Journal of Information Systems 19(2).
5. Hevner, March, Park, Ram (2004). *Design Science in Information Systems Research*. Management Information Systems Quarterly 28(1).
6. Simon (1996). *The Sciences of the Artificial* (3rd edition). Massachusetts Institute of Technology Press.
7. Ries (2011). *The Lean Startup*. Crown Business.
8. Beck (2000). *Extreme Programming Explained: Embrace Change*. Addison-Wesley.
9. Wilson et al. (2017). *Good Enough Practices in Scientific Computing*. Public Library of Science Computational Biology 13(6).
