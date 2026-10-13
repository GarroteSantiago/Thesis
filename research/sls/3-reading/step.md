# Step 3 — Reading and extraction

> **Inputs:** a paper included in `2-search/`, `1-protocol/quality.md`, `1-protocol/extraction-form.md` · **Next:** `4-synthesis/`

> Keshav [1]: read in up to three passes, stopping when the paper has given what you need.
> Kitchenham and Charters [2]: assess quality and extract the same fields from every paper.

## Rules
- Every extracted value and concept has a page.
- Papers my argument depends on (key papers) are read in full by me. A paper is key if it passes at least one test:
  1. **Sole or main evidence:** it is the only paper, or one of very few, answering an SQ.
  2. **Load-bearing claim:** the problem or the gap rests on a claim it makes.
  3. **Strongest counter-evidence:** it argues most strongly against the observation.
  4. **Seed:** it is in `0-start/seeds.md`.
- Key papers are proposed, with the test each passes, at 3c (provisional); updated at each 4b from the papers each accepted concept rests on; extended at 5c with any paper `5-gap/gap.md` rests on; and read in full before the gap gate (5c) is decided. Change: `1-protocol/changes/2026-10-12-key-papers.md`.

## Produces
Template in `ai/template/sls/3-reading/`. Flow rows 3a–3c (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `P{n}.md` | The record of one paper: five Cs, quality, extracted fields, concepts |
| `P{n}.citations.md` | The citation check of that record |

---

## References
1. Keshav (2007). *How to Read a Paper*. Association for Computing Machinery Special Interest Group on Data Communication, Computer Communication Review 37(3).
2. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
