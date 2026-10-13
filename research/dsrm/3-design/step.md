# Activity 3 — Design and development

> **Inputs:** accepted `2-objectives/O*.md`, `sls/4-synthesis/C*.md` · **Next:** `4-demonstration/`

> Peffers [1]: create the artifact, deciding its functionality and architecture.

## In plain words
We design and build the artifact, cheapest version first. Two kinds of work alternate: deciding (one design choice at a time, with its options laid out) and building (the next layer, from the choices made).

- **The AI:** lays out options for each design choice; builds each layer and runs its checks.
- **I decide:** each design choice, with my reason; and whether I accept each layer, which I only do once I can explain it.
- **Result:** a layer of the artifact, ready to be demonstrated.

## Rules
- Build the cheapest layer first. Each layer is demonstrated and evaluated before the next.
- The layers, their order, their form and their check are in the project's profile (`ai/profiles/`, *Build layers*). The usual shape: a paper design first, then a version that can be run or tried, then the real thing.
- The layer itself lives in `artifact/L{n}/`.

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
