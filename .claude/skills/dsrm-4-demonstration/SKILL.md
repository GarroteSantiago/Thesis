---
name: dsrm-4-demonstration
description: DSRM activity 4. Plan demonstrations for the latest accepted layer, run them, and confirm which instances were solved.
disable-model-invocation: true
---
# DSRM 4 — Demonstration

Runs rows 9a–9d of `ai/flow-dsrm.md`, following `ai/running.md`. Requires an accepted layer (8d).

## Rows
1. **9a** — dispatch `demonstrator`. Inputs: the latest accepted `dsrm/3-design/L{n}.md`, the accepted `O*.md`. Outputs: `D{n}.md` per instance.
2. **9b** — gate on the plan.
3. **9c** — dispatch `demonstrator`, one per accepted `D{n}.md`, in parallel. Inputs: `D{n}.md`, `artifact/L{n}/`. Output: `D{n}-run{k}.md`.
4. **9d** — gate on each run's *Solved*.

Done when 9d is done.
