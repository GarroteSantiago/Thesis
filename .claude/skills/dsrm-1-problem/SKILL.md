---
name: dsrm-1-problem
description: DSRM activity 1. Build the problem (motivation, design problem, RQs, hypotheses, stances, stakeholders) from step 0 and the gap, challenge it, and decide it.
disable-model-invocation: true
---
# DSRM 1 — Problem

Runs rows 6a–6d of `ai/flow-dsrm.md`, following `ai/running.md`. Requires the SLS gap gate (5c) done.

## Rows
1. **6a** — dispatch `synthesizer`. Inputs: `0-start/*.md`, the accepted `sls/5-gap/*.md`. Outputs: `dsrm/1-problem/motivation.md`, and `revision.md` if `0-start/notes.md` exists.
2. **6b** — dispatch `synthesizer`. Inputs: `0-start/*.md`, the 6a files. Outputs: `design-problem.md`, `RQ{n}.md`, `H{n}.md`, `stances.md`, `stakeholders.md`.
3. **6c** — dispatch `skeptic`. Inputs: the 6a and 6b files. Output: `dsrm/1-problem/problem.skeptic.md`.
4. **6d** — gate. The design problem and the RQs are where my judgement matters most: present them first, with every skeptic attack on them.

Done when 6d is done.
