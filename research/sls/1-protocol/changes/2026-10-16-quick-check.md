---
id: change-2026-10-16-quick-check
row: 1c
by: me
status: accepted
inputs: [sls/2-search/R0.md, sls/2-search/step.md]
---
# Protocol change: quick-check

Saved as `sls/1-protocol/changes/2026-10-16-quick-check.md`.

## What changed
- How screening runs (recorded in *Rules for this thesis*, `ai/project.md`):
  - Before: a paper included in round 0 with "full text decides" stayed included until reading (row 3a) settled it.
  - After: papers included in round 0 with "full text decides" that have no reading record are re-screened against the criteria as changed on 2026-10-16, from their abstract, introduction and conclusion. Verdicts are decided at a screening gate. Papers already read keep their full-text verdict.
- Run in one pass with the re-screen of `2026-10-16-i4-premise.md`.

## Why
The quick check: many included papers probably do not belong.

## Papers affected
The 122 unread papers marked "full text decides" in `sls/2-search/R0.md`. P15, P33, P49, P53, P72, P73, P74 and P102, already read, keep their verdict.
