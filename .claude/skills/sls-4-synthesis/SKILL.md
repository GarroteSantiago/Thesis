---
name: sls-4-synthesis
description: SLS step 4. Update the concepts from the accepted paper records and accept them.
disable-model-invocation: true
---
# SLS 4 — Synthesis

Runs rows 4a–4b of `ai/flow-sls.md`, following `ai/running.md`.

## Rows
1. **4a** — dispatch `synthesizer`. Inputs: every accepted `sls/3-reading/P*.md` and the existing `sls/4-synthesis/C*.md`. Outputs: new `C{n}.md` files, and existing ones it updates.
2. **4b** — gate, one decision per new or updated concept. Merges and splits I ask for are applied as changes.

Then run `just views` to regenerate the concept matrix.

Done when every new or updated concept is decided.
