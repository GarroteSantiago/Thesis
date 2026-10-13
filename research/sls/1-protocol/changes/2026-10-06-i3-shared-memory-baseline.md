---
id: change-2026-10-06-i3-shared-memory-baseline
row: 1c
by: me
status: accepted
inputs: [sls/1-protocol/criteria.md]
---
# Protocol change: i3-shared-memory-baseline

Saved as `sls/1-protocol/changes/2026-10-06-i3-shared-memory-baseline.md`.

## What changed
`criteria.md`, I3. Before: "…either split by communication mechanism (shared memory versus message passing) or for programs or systems built on message passing only. (SQ7)". After: "…either split by communication mechanism (shared memory versus message passing) or for programs or systems built on message passing only, or for programs or systems built on shared memory only, as the comparison baseline for SQ7. (SQ7)".

## Why
SQ7 asks for the comparison with programs or systems that share memory, but I3 as written let in no shared-memory-only defect study, so SQ7 had no shared-memory side. Found at gate 2b: the seed Lu et al. (2008), R0-005, failed I3 as written.

## Papers affected
None have P IDs yet (gate 2b not done). In `sls/2-search/R0.md`, R0-005 and the bug-study candidates (search block B3) are re-screened against the new I3 in the 2a rerun.
