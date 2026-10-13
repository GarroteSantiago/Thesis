# Skills

Three levels of facades. They are user-level skills, the same for every thesis, so they are not in this repository: they read the rules in `ai/` and the files in `research/` of the project they run in. Every skill can be called on its own, by typing `/<name>`.

```
thesis                      setup, entry point → route through sls and dsrm; status, profile, upgrade
├── sls                     runs SLS 1 → 5, with the snowballing loop
│   ├── sls-1-protocol
│   ├── sls-2-search
│   ├── sls-3-reading
│   ├── sls-4-synthesis
│   └── sls-5-gap
└── dsrm                    runs DSRM 1 → 6, with the design loop
    ├── dsrm-1-problem
    ├── dsrm-2-objectives
    ├── dsrm-3-design
    ├── dsrm-4-demonstration
    ├── dsrm-5-evaluation
    └── dsrm-6-communicate
```

- **`thesis`** sets up a new project (profile, git, AI policy), reads the entry point from step 0 or helps me choose it (`entry-points.md`), and calls `sls` and `dsrm` in the order that entry point needs. `/thesis status` reports where the thesis stands (`status.md`); `/thesis profile` builds a field profile (`profiles/README.md`); `/thesis upgrade` brings the workflow files up to the skill's version.
- **`sls`** and **`dsrm`** run their steps in order, handle their loops, and stop at every gate.
- **Step skills** run the rows of their step (`flow-sls.md`, `flow-dsrm.md`): they call the agents, then stop at the gate. Called directly, they work on the files that exist (e.g. `sls-3-reading P12` reads one paper).
- **Skills are procedures, agents are workers.** Step skills dispatch agents (`agents.md`); agents only write their outputs.
- **All skills are user-invoked** (`disable-model-invocation: true`), so they cost no context until I call one. A facade reaches a lower skill by reading its `SKILL.md` (a sibling folder of its own) and following it.
- **Shared procedure** lives in `ai/`, not in the skills: `running.md` (how a row runs), `gate.md` (how a gate runs), `agent-contract.md` (what every agent does).
