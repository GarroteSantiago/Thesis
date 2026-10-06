---
name: sls-5-gap
description: SLS step 5. Answer the review questions, state the gap, and challenge it, once snowballing has stopped.
disable-model-invocation: true
---
# SLS 5 — Gap

Runs rows 5a–5c of `ai/flow-sls.md`, following `ai/running.md`. Requires the stop rule met: the last round file's *Newly included* is "none". Otherwise, tell me and stop.

## Rows
1. **5a** — dispatch `synthesizer`. Inputs: the accepted `sls/4-synthesis/C*.md`, `sls/1-protocol/SQ*.md`. Outputs: `SQ{n}.answer.md` per SQ, `gap.md`, `solutions.md`, `history.md`, `limitations.md`.
2. **5b** — dispatch `skeptic`. Inputs: the 5a files. Output: `sls/5-gap/gap.skeptic.md`.
3. **5c** — gate. The gap is stated in my words: if I change it, the change is mine verbatim.

Done when 5c is done.
