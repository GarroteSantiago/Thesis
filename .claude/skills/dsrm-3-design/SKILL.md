---
name: dsrm-3-design
description: DSRM activity 3. Prepare and record a design decision, or build and accept the next artifact layer.
disable-model-invocation: true
argument-hint: "[decide <topic> | build]"
---
# DSRM 3 — Design

Runs rows 8a–8d of `ai/flow-dsrm.md`, following `ai/running.md`. Requires 7c done.

## Which path
- `decide <topic>` → rows 8a, 8b for that decision.
- `build` → rows 8c, 8d for the cheapest layer not yet accepted (layer order in `research/dsrm/3-design/step.md`).
- No argument → list the open decisions (from earlier builder reports and my requests) and the next layer, and ask me which.

## Decide
1. **8a** — dispatch `designer`. Inputs: the accepted `O*.md`, `sls/4-synthesis/C*.md`, `dsrm/3-design/DEC*.md`. Output: `DEC{n}.options.md`.
2. **8b** — mine, and a gate. Present the options file; write `DEC{n}.md` from my choice and reason (*Rows by me*), then record the decision (`ai/gate.md`).

## Build
1. **8c** — dispatch `builder`. Inputs: the accepted `DEC*.md` and the current layer. Outputs: `artifact/L{n}/` and `dsrm/3-design/L{n}.md`. Decisions the builder reports as open go to *Decide* before the layer is accepted.
2. **8d** — gate. I accept the layer only once I can explain it.

Done when the chosen path's gate is done.
