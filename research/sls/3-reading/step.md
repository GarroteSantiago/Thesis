# Step 3 — Reading and extraction

> **Inputs:** a paper included in `2-search/`, `1-protocol/quality.md`, `1-protocol/extraction-form.md`, `1-protocol/criteria.md`, `1-protocol/SQ*.md` · **Next:** `4-synthesis/`

> Keshav [1]: read in up to three passes, stopping when the paper has given what you need.
> Kitchenham and Charters [2]: assess quality and extract the same fields from every paper.

## In plain words
Each paper let in is read and summarised the same way: what kind of paper it is, how solid it is, the facts the extraction form asks for, and the ideas it covers, all with page numbers. A second helper checks every claim against the page cited.

- **The AI:** reads each paper and writes its reading record; checks its citations.
- **I decide:** whether each record is faithful to its paper. One decision per paper. The AI also proposes which papers look *key*, the ones my argument will rest on; I read those in full later, once the argument exists, before the gap is decided.
- **Result:** one accepted record per paper.

## Rules
- Every extracted value and concept has a page.
- **Serves:** every record states each SQ the paper serves and what it contributes, in that SQ's unit, with page. This is the link from each paper to each question.
- **Depth follows need:** the papers read are those serving an open question, in its reading order (`4-synthesis/SQ{n}.coverage.md`, *To read next*), the key papers, and the audit draws. An included paper whose questions are all saturated or complete is **deferred**: it stays in the review, listed with its questions, and is read if one of them reopens. This departs from assessing every included study [2]; the limitations report, per question, papers found, read, deferred and audited.
- **Nothing that could change an answer is deferred:** a paper whose screening suggests a contribution not yet in its question's coverage is read (contradiction trigger), and for each saturated question a few deferred papers are drawn at random and read; if one adds something new, the question reopens.
- Papers my argument depends on (key papers) are read in full by me. A paper is key if it passes at least one test:
  1. **Sole or main evidence:** it is the only paper, or one of very few, answering an SQ.
  2. **Load-bearing claim:** the problem or the gap rests on a claim it makes.
  3. **Strongest counter-evidence:** it argues most strongly against step 0.
  4. **Seed:** it is in `0-start/seeds.md`.
- Key papers are proposed, with the test each passes, at 3c (provisional); updated at each 4b from the papers each accepted concept rests on; extended at 5c with any paper `5-gap/gap.md` rests on; and read in full by me before the gap gate (5c) is decided. At 3c the argument does not exist yet: it is built at synthesis and at the gap, so which papers it rests on can only be known from the concepts and the gap.

## Produces
Template in `ai/template/sls/3-reading/`. Flow rows 3a–3c (`ai/flow-sls.md`).

| File | Holds |
|---|---|
| `P{n}.md` | The record of one paper: five Cs, quality, extracted fields, the questions it serves and what it adds to each, concepts |
| `P{n}.citations.md` | The citation check of that record |

---

## References
1. Keshav (2007). *How to Read a Paper*. Association for Computing Machinery Special Interest Group on Data Communication, Computer Communication Review 37(3).
2. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
