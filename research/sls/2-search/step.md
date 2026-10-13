# Step 2 — Search (snowballing)

> **Inputs:** `1-protocol/` (criteria and SQs), `0-start/seeds.md` · **Next:** `3-reading/` for each paper included

> Wohlin [1]: start from a set of papers, then follow references backward and citations forward, round by round.

## In plain words
We find the papers. First a start set: my seed papers plus a database search. Then rounds of snowballing: for each paper let in, the papers it cites and the papers that cite it. Each candidate is checked against the protocol's rules.

- **The AI:** searches, collects candidates and suggests in or out for each, naming the rule that decides it.
- **I decide:** in or out, for every candidate. The first round can bring dozens to hundreds of candidates; later rounds usually fewer.
- **Result:** the list of papers in the review, each with its ID.

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
