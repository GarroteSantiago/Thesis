# Spec

The workflow as data, for the tools that enforce it: the guard hook now (`ai/tools/guard.py`), and the app runtime later. The markdown rules in `ai/` stay the explanation, for people and for Claude; the spec holds the facts that are checked by code.

| File | Holds | Twin in prose |
|---|---|---|
| `flow.toml` | Every row: who runs it, what it reads and writes, which rows are gates; the frozen files | `ai/kickstart.md`, `ai/flow-sls.md`, `ai/flow-dsrm.md` |
| `decision-card.schema.json` | The shape of a decision: plain part for me, exact edits for the tools | `ai/gate.md`, *Decision card* |

## Keeping the twins in step
`just check` compares `flow.toml` with the flow tables: every row in one is in the other, with the same *Who*, and every output path in the spec appears in its row of the table. Change both together.

## What the guard enforces
`ai/tools/guard.py` runs before every tool call (`.claude/settings.json`) and refuses, with the reason, any call that breaks these rules. The refusal goes back to the model, which then does it the right way.

| Rule | From |
|---|---|
| An agent writes only the outputs of its rows in `flow.toml`, and only with the file tools | `ai/agent-contract.md`, *You do* 4 |
| An agent reads in `research/` only the inputs and outputs of its rows | `ai/agent-contract.md`, *You do* 1 |
| An agent writes `status: proposed`, nothing else | `ai/agent-contract.md`, *You do* 3 |
| A file gets a decided status only once its decision file exists | `ai/gate.md`, steps 4–5 |
| Frozen files (`[[frozen]]`) are not edited once decided, unless their condition holds | `ai/kickstart.md`, `ai/flow-sls.md`, `ai/flow-dsrm.md` |
| The raw AI log and existing decision files are never edited | `ai/ai-log.md` |
| Research files are changed only with the file tools, never by shell commands, so every change passes these checks | this file |

## Limits
- The guard sees each tool call, not its effects: a program run from the shell could still write a file it does not name on its command line. The guard refuses the shell commands that visibly write research files; `just check` catches what remains (a decided status with no decision file, a removed ID) after every gate. The app runtime closes this fully: there, agents get no shell access to the research files at all.
- Read limits apply per agent, not per row: an agent may read the inputs of any row it runs. The skill's dispatch narrows it to one row's inputs.
