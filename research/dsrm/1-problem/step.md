# Activity 1 — Problem identification and motivation

> **Inputs:** `0-start/`, `sls/5-gap/` · **Next:** `2-objectives/`

> Peffers [1]: define the research problem and justify the value of a solution, from knowledge of the state of the problem.

## In plain words
From step 0 and the gap, we build the problem the thesis solves: why it matters, the design problem in one sentence, the research questions, what I expect the answers to be, what the thesis leaves out, and who is affected. If I wrote notes at step 0, each of my earlier beliefs is checked against the literature.

- **The AI:** drafts all of it; the skeptic attacks it.
- **I decide:** each file, the design problem and the research questions first. Usually 8–15 decisions.
- **Result:** the problem, accepted.

## Rules
- **Design problem, exactly one.** Template (Wieringa [2]): *Improve <a problem context> by <(re)designing an artifact> that satisfies <some requirements> in order to <help stakeholders achieve some goals>.*
- **Stakeholders:** anyone affected by the problem or the artifact [2].
- **Knowledge questions** use the question types of the project's profile (`ai/profiles/`; the computing profile uses Shaw's types [3]). Each one could be answered "no".


## Produces
Templates in `ai/template/dsrm/1-problem/`. Flow rows 6a–6d (`ai/flow-dsrm.md`).

| File | Holds |
|---|---|
| `motivation.md` | Why it matters and why earlier attempts failed, backed by the review |
| `revision.md` | Each claim in `0-start/notes.md` checked against the review |
| `design-problem.md` | The design problem |
| `RQ{n}.md` | One knowledge question each |
| `H{n}.md` | One hypothesis each, tested by an RQ |
| `stances.md` | What the thesis deliberately does not solve |
| `stakeholders.md` | Who is affected and their goals |

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
2. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
3. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
