# Activity 3 — Design and development

> **Inputs:** accepted `2-objectives/O*.md`, `sls/4-synthesis/C*.md` · **Next:** `4-demonstration/`

> Peffers [1]: create the artifact, deciding its functionality and architecture.

## Rules
- Build the cheapest layer first. Each layer is demonstrated and evaluated before the next.

| Layer | |
|---|---|
| 1 | Paper design |
| 2 | Executable model / simulator |
| 3 | Formal specification (optional) |
| 4 | Hardware prototype (optional) |

- The layer itself lives in `artifact/L{n}/`; its form for each layer is in `ai/agents.md`.

## Produces
Templates in `ai/template/dsrm/3-design/`. Flow rows 8a–8d (`ai/flow-dsrm.md`).

| File | Holds |
|---|---|
| `DEC{n}.options.md` | The options for one design decision |
| `DEC{n}.md` | The option chosen and why |
| `L{n}.md` | What was built in one layer, and its checks |

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
