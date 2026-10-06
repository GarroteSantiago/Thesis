---
name: dsrm
description: Run design science activities 1 to 6, with the design–demonstration–evaluation loop.
disable-model-invocation: true
---
# DSRM

Runs DSRM activities 1–6 (`ai/flow-dsrm.md`), resuming where the files show the work stopped (`ai/running.md`). Requires the SLS gap gate (5c) done.

1. **Problem.** Read and follow `.claude/skills/dsrm-1-problem/SKILL.md`.
2. **Objectives.** Read and follow `.claude/skills/dsrm-2-objectives/SKILL.md`.
3. **Design loop.** Repeat until the iteration gate sends us to 6:
   1. Read and follow `.claude/skills/dsrm-3-design/SKILL.md`.
   2. Read and follow `.claude/skills/dsrm-4-demonstration/SKILL.md`.
   3. Read and follow `.claude/skills/dsrm-5-evaluation/SKILL.md`. Its iteration gate decides: next layer or fix → 3.1; objective wrong → step 2; all met → step 4.
4. **Communicate.** Read and follow `.claude/skills/dsrm-6-communicate/SKILL.md`, section by section. If writing exposes a hole, its gate sends us to step 2 or 3.

Done when every chapter section is final and `contribution.md` is decided.
