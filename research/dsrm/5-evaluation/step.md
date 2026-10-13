# Activity 5 — Evaluation

> **Inputs:** accepted `2-objectives/`, `4-demonstration/D*-run*.md` · **Next:** `6-communicate/`, or iterate back to `2-objectives/` or `3-design/` [1]

> Peffers [1]: observe and measure how well the artifact supports a solution, by comparing the objectives with the results observed in the demonstration.

## In plain words
We measure how well the artifact meets each objective, against the baseline, and list honest reasons the results might be wrong. Then I decide where to go next: build the next layer or fix this one, rethink an objective, or move on to writing.

- **The AI:** measures and drafts the evaluations and threats; the skeptic attacks them.
- **I decide:** each result, then where the next iteration goes.
- **Result:** evaluated results, and the next step.

## Rules
- Each objective's validation type is set in its `O{n}.md`, from the types of the project's profile (`ai/profiles/`; the computing profile uses Shaw's [2]).
- Every evaluation states where the next iteration goes.
- Threats to validity use the categories of the project's profile (the computing profile uses the four of Wohlin et al. [3]: conclusion, internal, construct, external).

## Produces
Templates in `ai/template/dsrm/5-evaluation/`. Flow rows 10a–10c (`ai/flow-dsrm.md`).

| File | Holds |
|---|---|
| `E{n}.md` | One evaluation: measurements, met or not, what comes next |
| `T{n}.md` | One threat to validity and what I did about it |

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
2. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
3. Wohlin et al. (2012). *Experimentation in Software Engineering*. Springer.
