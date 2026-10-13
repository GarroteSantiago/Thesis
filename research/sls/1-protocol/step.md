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

## How much each question needs
A review reads what its questions need: no paper that changes an answer is left out, and no paper is read in full that cannot change one. Every SQ states it, before any search, so the limit cannot bend to the results:

| Kind | The question asks | Unit (what counts as new) | Enough when |
|---|---|---|---|
| **census** | which instances exist, every one | one instance, e.g. a system | every distinct instance is covered by one read paper, and a search round finds no new instance (Wohlin's stop rule, per question [2]) |
| **kinds** | which kinds of instance exist | one kind, e.g. a kind of system | saturation, as for evidence |
| **evidence** | what the evidence says | one finding: a claim, cause, measurement or counter-argument | at least 10 papers serving it read, in its reading order, then 3 in a row add nothing new: the 10 + 3 rule of Francis et al. [3], adapted from interviews to papers; the review is complete when new papers stop adding new concepts (Webster and Watson [4]) |

- **Census or kinds** is the choice that decides most of a review's size: a question about every instance can need a hundred papers where its kinds need thirty. It is mine, at the protocol gate, with its reason.
- **The numbers are mine too:** 10 and 3 are the default; papers vary more than interviews, so a larger stopping criterion (e.g. 10 + 5) is safer where the field is heterogeneous.
- **Reading order:** each SQ states how its papers are ordered (both sides alternating, different groups and decades, strongest first), so saturation is not reached on ten similar papers (Francis et al.'s purposive diversity [3]).

## Produces
Templates in `ai/template/sls/1-protocol/`. Flow rows 1a–1c (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `need.md` | What the review is about; existing reviews and why they are not enough |
| `SQ{n}.md` | One review question each, with its kind, unit, enough-when rule and reading order |
| `criteria.md` | Inclusion (I) and exclusion (X) criteria |
| `quality.md` | Quality checklist (Q) |
| `extraction-form.md` | Fields extracted from every paper |
| `changes/{date}-{slug}.md` | One per change after freezing |

---

## References
1. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
2. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
3. Francis et al. (2010). *What Is an Adequate Sample Size? Operationalising Data Saturation for Theory-Based Interview Studies*. Psychology & Health 25(10), 1229–1245.
4. Webster, Watson (2002). *Analyzing the Past to Prepare for the Future: Writing a Literature Review*. Management Information Systems Quarterly 26(2).
