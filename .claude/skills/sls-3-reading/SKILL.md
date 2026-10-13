---
name: sls-3-reading
description: SLS step 3. Read the newly included papers (or one, by P ID), draft their records, check their citations, and accept them.
disable-model-invocation: true
argument-hint: "[P{n}]"
---
# SLS 3 — Reading

Runs rows 3a–3c of `ai/flow-sls.md`, following `ai/running.md`.

## Work set
Every P ID included in an `sls/2-search/R*.md` file with no `sls/3-reading/P{n}.md` yet. With an argument, only that paper.

## Rows
0. **PDFs** — run `just papers-pull`, so PDFs published from another machine are in `research/papers/`.
1. **3a** — dispatch one `reader` per paper, in parallel. Inputs: the paper (`papers/P{n}.pdf` if present, and its reference line from the round file), `sls/1-protocol/quality.md`, `extraction-form.md`, `criteria.md`, `SQ*.md` (to judge I4), and the accepted `sls/4-synthesis/C*.md` once any exist. For a paper whose round-file reason says "full text decides": read the abstract and introduction first and stop early, recording the X criterion, when one clearly applies. Outputs: `sls/3-reading/P{n}.md`, and `papers/P{n}.pdf` if the reader downloads it.
2. **3b** — dispatch one `citation-checker` per record, in parallel. Inputs: `P{n}.md`, the paper. Output: `P{n}.citations.md`.
3. **3c** — gate, one decision per record. At this gate, propose which papers are key (`sls/3-reading/step.md`, *Rules*), with the test each passes. The list is provisional; it is fixed at 4b.

4. **Publish** — run `just papers-push`, so every PDF in `research/papers/` is published to the `papers` release of the GitHub repo.

Done when every paper in the work set has a decided record and its PDF, if any, is published.
