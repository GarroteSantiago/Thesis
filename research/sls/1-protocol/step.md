# Step 1 — Protocol

> **Inputs:** `0-start/` · **Next:** `2-search/`

> Kitchenham and Charters [1]: define the review before running it.

## In plain words
Before looking for any paper, we write down the rules of the review: the questions the literature should answer, which papers count and which do not, how each paper is judged, and which facts are taken from every paper. Fixing the rules first stops the review from bending toward what I hope to find.

- **The AI:** drafts the rules from step 0; the skeptic adds questions that look for evidence against my idea.
- **I decide:** each question, the inclusion and exclusion rules, the quality checklist and the extraction form. Usually 10–20 decisions.
- **Result:** the protocol, frozen. Changing it later is allowed, but each change is written down with its reason.

## Rules
- The protocol is written and frozen before any search, so selection does not bend to what I hoped to find [1].
- Every SQ is served by at least one field of the extraction form.
- Any change after freezing is a change file with its reason.

## Produces
Templates in `ai/template/sls/1-protocol/`. Flow rows 1a–1c (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `need.md` | What the review is about; existing reviews and why they are not enough |
| `SQ{n}.md` | One review question each |
| `criteria.md` | Inclusion (I) and exclusion (X) criteria |
| `quality.md` | Quality checklist (Q) |
| `extraction-form.md` | Fields extracted from every paper |
| `changes/{date}-{slug}.md` | One per change after freezing |

---

## References
1. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
