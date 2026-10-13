# AI workflow

How AI skills and agents run the steps of `research/sls/` and `research/dsrm/`. These are working rules. They do not change either method.

## The line
- **AI does the labour:** searching, drafting, building, measuring, writing prose.
- **I make the decisions:** every gate in the flow. Each one is a decision, not a piece of work.
- **Test:** I can defend every output at the defense with no AI in the room.
- **The rules are enforced:** a hook refuses, before it runs, any tool call that breaks them, and undoes any shell command that broke one (`spec/README.md`).
- **Everything is logged:** every action the AI takes, not only the decisions (`ai-log.md`). The thesis Method chapter states how AI was used.

## Files
| File | Answers |
|---|---|
| `glossary.md` | What the method's terms mean, in plain words |
| `project.md` | This project's settings: its profile and the university's AI policy |
| `profiles/` | What changes from one field of study to another |
| `skills.md` | Which skills exist and how they call each other |
| `agents.md` | Which agents exist and what each one does |
| `running.md` | How a skill runs a row: where to start, agent rows, rows by me, loops |
| `gate.md` | How a gate runs: present, wait, apply, record, check |
| `agent-contract.md` | What every agent receives, does, and returns |
| `entry-points.md` | Where the work can start, and the route from each start |
| `kickstart.md` | Step 0 (`0-start/`): the observation, and the safeguards against my own bias |
| `files.md` | How every output is stored: small files, one per output |
| `flow-sls.md` | Rows 1a–5c: who reads and writes what, and where I decide |
| `flow-dsrm.md` | Rows 6a–11e: same, for DSRM |
| `ai-log.md` | How everything the AI does is recorded |
| `checks.md` | What `just check` and `just views` do |
| `status.md` | What `/thesis status` reports |
| `export.md` | How the thesis becomes one document, and why the research files stay the source |
| `template/` | The template of every file the flow produces |
| `spec/` | The workflow as data, and the rules the guard hook enforces (`spec/README.md`) |

## Order
Step 0 (`kickstart.md`) → `flow-sls.md` → `flow-dsrm.md`, in the order of the entry point's route (`entry-points.md`).
