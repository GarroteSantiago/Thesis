# Step 3 — Reading and extraction

> **Inputs:** a paper included in `2-search/`, `1-protocol/quality.md`, `1-protocol/extraction-form.md`, `1-protocol/criteria.md`, `1-protocol/SQ*.md` · **Next:** `4-synthesis/`

> Keshav [1]: read in up to three passes, stopping when the paper has given what you need.
> Kitchenham and Charters [2]: assess quality and extract the same fields from every paper.

## In plain words
Each paper let in is read and summarised the same way: what kind of paper it is, how solid it is, the facts the extraction form asks for, and the ideas it covers, all with page numbers. A second helper checks every claim against the page cited.

- **The AI:** reads each paper and writes its reading record; checks its citations.
- **I decide:** whether each record is faithful to its paper. One decision per paper. The papers my argument rests on I read myself, in full.
- **Result:** one accepted record per paper.

## Rules
- Every extracted value and concept has a page.
- Papers my argument depends on are read in full by me.

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
