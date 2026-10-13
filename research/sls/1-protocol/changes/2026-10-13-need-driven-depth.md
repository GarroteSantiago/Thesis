---
id: change-2026-10-13-need-driven-depth
row: 1c
by: me
status: accepted
inputs: [sls/1-protocol/step.md, sls/1-protocol/SQ*.md, sls/3-reading/step.md]
---
# Protocol change: need-driven-depth

Saved as `sls/1-protocol/changes/2026-10-13-need-driven-depth.md`.

## What changed
- `sls/1-protocol/SQ1.md` to `SQ19.md`:
  - Before: each SQ held *Question*, *Why it matters* and *Origin*. Nothing said how many papers a question needs, so every included paper was to be read in full.
  - After: each SQ also states its *Kind* (census, kinds or evidence), its *Unit* (what counts as new), *Enough when* (its stop rule) and *Reading order*, as `sls/1-protocol/step.md`, *How much each question needs*, defines them. They are decided at gate 1c.
- `sls/3-reading/P*.md` (every record not rejected): a *Serves* section is added, naming each SQ the paper serves and what it adds to it, in that SQ's unit, with page. Decided at gate 3c.
- `sls/4-synthesis/SQ{n}.coverage.md`: written from the records, saying per SQ what is covered, what to read next and what is deferred.
- Depth follows need (`sls/3-reading/step.md`, *Rules*): the papers read are those serving an open SQ, in its reading order, the key papers, and the audit draws. An included paper whose SQs are all saturated or complete is deferred: it stays in the review and is read if one of them reopens.
- Departure stated: Kitchenham and Charters (2007) assess every included study. This review does not read every included paper; the limitations report, per SQ, the papers found, read, deferred and audited.

## Why
Too many papers to read: search round 0 included 280 papers (P1–P280), more than can be read in full.

## Papers affected
None re-screened: the criteria do not change, and every included paper stays included. None re-read: the records already decided keep their content and gain only *Serves*. Included papers not yet read are read or deferred according to each SQ's coverage.
