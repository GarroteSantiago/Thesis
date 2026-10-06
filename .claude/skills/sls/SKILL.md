---
name: sls
description: Run the systematic literature study, steps 1 to 5 with the snowballing loop.
disable-model-invocation: true
---
# SLS

Runs SLS steps 1–5 (`ai/flow-sls.md`), resuming where the files show the work stopped (`ai/running.md`).

1. **Protocol.** Read and follow `.claude/skills/sls-1-protocol/SKILL.md`.
2. **Snowballing loop.** Repeat until the stop rule is met:
   1. Read and follow `.claude/skills/sls-2-search/SKILL.md` (one round).
   2. Read and follow `.claude/skills/sls-3-reading/SKILL.md` (the papers that round included).
   3. Read and follow `.claude/skills/sls-4-synthesis/SKILL.md`.
   4. **Stop rule (↺):** the last round file's *Newly included* is "none" → step 3. Otherwise → next round.
3. **Gap.** Read and follow `.claude/skills/sls-5-gap/SKILL.md`.

Done when the gap gate (5c) is done. Next: the `dsrm` skill.
