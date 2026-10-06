# Step 2 — Search (snowballing)

> **Inputs:** `1-protocol/`, `0-start/seeds.md` · **Next:** `3-reading/` for each paper included

> Wohlin [1]: start from a set of papers, then follow references backward and citations forward, round by round.

## Rules
- **Start set:** seeds plus a database search, so it is varied [1].
- **Each round** examines only the papers included in the previous one.
  - **Backward:** the reference list of each paper.
  - **Forward:** the papers that cite it.
- **Screening** applies only the criteria in `1-protocol/criteria.md`.
- **Stop** when a round includes no new papers [1].
- Papers get P IDs in the order they are first included. Never renumber.

## Produces
Templates in `ai/template/sls/2-search/`. Flow rows 2a–2d (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `search-string.md` | The database search and where it was run |
| `R0.md` | The start set, screened |
| `R{k}-backward.md`, `R{k}-forward.md` | One round in one direction, screened |

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
