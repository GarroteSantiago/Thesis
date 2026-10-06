---
name: sls-2-search
description: SLS step 2. Run one snowballing round, the start set first and then backward and forward rounds, with my include/exclude gate.
disable-model-invocation: true
---
# SLS 2 — Search

Runs one round of rows 2a–2d of `ai/flow-sls.md`, following `ai/running.md`. Requires the protocol frozen (1c done).

## Which round
- No `sls/2-search/R0.md` yet → the start set: rows 2a, 2b.
- Otherwise → round `k` = last round + 1: rows 2c, 2d, built from the papers included in round `k-1`.
- Round `k-1` included no new papers → the stop rule is already met: tell me and stop.

## Rows
1. **2a** — dispatch `snowballer`. Inputs: `sls/1-protocol/criteria.md`, the SQ files, `0-start/seeds.md` if present. Outputs: `search-string.md`, `R0.md`.
   **2c** — dispatch `snowballer`, one per direction in parallel. Inputs: the last round files, `criteria.md`. Outputs: `R{k}-backward.md`, `R{k}-forward.md`.
2. **2b / 2d** — gate. I decide each candidate; included papers get the next free P IDs, in order, written in the round file's *P ID* column and *Newly included* section.

Done when the round's gate is done.
