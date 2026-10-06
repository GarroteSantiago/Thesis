---
name: dsrm-5-evaluation
description: DSRM activity 5. Measure the runs against the frozen objectives, challenge the results, decide them, and decide where the next iteration goes.
disable-model-invocation: true
---
# DSRM 5 — Evaluation

Runs rows 10a–10c and the iteration row of `ai/flow-dsrm.md`, following `ai/running.md`. Requires 9d done.

## Rows
1. **10a** — dispatch `evaluator`. Inputs: the accepted `O*.md`, `metrics.md`, `baselines.md`, the accepted `D*-run*.md`. Outputs: `E{n}.md`, `T{n}.md`.
2. **10b** — dispatch `skeptic`. Inputs: the 10a files. Output: `E{n}.skeptic.md` per evaluation.
3. **10c** — gate on each result.
4. **Iteration (↺)** — a gate. Present each `E{n}.md`'s *Next* and ask me: next layer or fix → DSRM 3; objective wrong → DSRM 2; all met → DSRM 6.

Done when the iteration decision is recorded.
