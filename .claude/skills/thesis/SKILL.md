---
name: thesis
description: Run the whole thesis workflow from its entry point, through the SLS and DSRM skills.
disable-model-invocation: true
---
# Thesis

The top facade (`ai/skills.md`). Runs the SLS and the DSRM in the order the entry point needs.

1. **Entry point.** Ask me which of the four entry points applies (`ai/entry-points.md`), with the AskUserQuestion tool. Problem-centred initiation is this thesis.
2. **Route.** Problem-centred initiation has its rows defined (`ai/kickstart.md`, `ai/flow-sls.md`, `ai/flow-dsrm.md`): go to step 3. The other three entry points have a route in `ai/entry-points.md` but no rows yet: tell me so and stop.
3. **SLS.** Read and follow `.claude/skills/sls/SKILL.md`.
4. **DSRM.** Read and follow `.claude/skills/dsrm/SKILL.md`.

Each facade resumes from where the files show the work stopped (`ai/running.md`, *Where to start*), so this skill can be run again at any time.
