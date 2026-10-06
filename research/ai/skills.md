# Skills

Three levels of facades. Every skill can be called on its own.

```
thesis                      entry point → route through sls and dsrm
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

- **`thesis`** asks for the entry point (`entry-points.md`) and calls `sls` and `dsrm` in the order that entry point needs.
- **`sls`** and **`dsrm`** run their steps in order, handle their loops, and stop at every gate.
- **Step skills** run the rows of their step (`flow-sls.md`, `flow-dsrm.md`): they call the agents, then stop at the gate. Called directly, they work on the files that exist (e.g. `sls-3-reading P12` reads one paper).
- **Skills are procedures, agents are workers.** Step skills call agents (`agents.md`); agents never call skills.
