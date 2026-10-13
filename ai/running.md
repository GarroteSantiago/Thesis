# Running rows

How a thesis skill (`skills.md`) runs the rows of a step (`ai/flow-sls.md`, `ai/flow-dsrm.md`). Every step skill follows this.

## Talking to me
Everything meant for me follows *Talking to me* in `ai/gate.md`: plain words first, IDs after them in parentheses, no internal codes, method terms explained the first time (`ai/glossary.md`).

## Before anything: the AI log
Every session must be logged (`ai/ai-log.md`). The session start hook adds a line `Raw AI log session: <id>` to your context. If that line is missing, the log is off: stop before running any row and tell me, in these words or close to them:

> The AI log is not running, so nothing done in this session would be recorded. Usually this means Claude Code was started outside the thesis environment. To fix it: close Claude Code, open a terminal in the thesis folder, run `direnv allow` (only needed once), check that `python3 --version` prints a version, then start Claude Code again from that same terminal.

## This thesis's own rules
Before running a step, read `ai/project.md`. Its *Rules for this thesis* refine the workflow for this thesis: where one differs from a step's instructions, the rule wins. When you apply one, say so in plain words ("this thesis also searches the IEEE library, as its project settings say"). Its *Notes for this thesis* are leads to pass to agents where they help, not evidence.

## The guard
A hook refuses tool calls that break the workflow rules, before they run, and undoes shell commands that broke one after they ran (`ai/spec/README.md`). A refusal is a rule, not an obstacle: follow its reason (record the decision first, use the Write tool, ask me for the file as an input), or tell me why the rule seems wrong here. Never work around it.

## Where to start
Before running anything, read the step's existing files in `research/` and find the first row not done:
- An agent row is done when all its output files exist.
- A gate row is done when none of its files is `proposed` and each has a decision file in `research/ai-log/decisions/`.

Resume from there. A step already done is reported and skipped.

## Starting a step
When a step starts, or resumes after a break, introduce it before the first row, from the step's `step.md`, section *In plain words*:
- what the step is for, in two or three sentences;
- what the AI will do, and what I will decide, with roughly how many decisions are coming;
- where we are: rows done, rows left.

Keep it short; I can ask for more.

## Agent rows
Dispatch the row's agent with the Agent tool (`subagent_type` = the agent's name). The prompt states:
- **Row:** the row ID.
- **Inputs:** the exact input files, expanded from the row's globs to real paths, and only files whose status allows it (rows that say "accepted" read only `accepted` or `changed` files).
- **Outputs:** the exact output paths, with `{n}` and `{k}` replaced by the next free number.

Independent dispatches run in parallel (e.g. one `reader` per paper in row 3a). When the agent returns, check its outputs against the agent contract (`ai/agent-contract.md`, *Your output is done when*). A missing file or a leftover placeholder goes back to the agent once, then to me as an open issue.

### Large batches
Before dispatching more than 10 agents in one row (e.g. one `reader` per paper), ask me first, with a decision card (`ai/gate.md`):
- how many agents, and roughly how much usage it costs, in the plain terms of my plan (a large batch can use up a usage limit or a budget);
- how many decisions it will bring me at the gate;
- options: all at once; a first batch of about 10, the most central first, so the result can be checked before the rest; or a number I choose.

## Rows by me
Rows whose *Who* is me and that write files (0, 7a, 8b, 11a, 11e). Show me the row's input files, ask for the content, and write each output from its template using my words only, with `by: me`. Where my words leave a template field empty, ask; the field stays mine. Rows by me that are not gates (row 0) end with a commit, as a gate does (`ai/gate.md`, step 7).

## Gate rows
Follow `ai/gate.md`.

## Loop rows (`↺`)
Evaluate the condition from the files, tell me the result, and go to the row it names. A loop row decided by me is a gate: follow `ai/gate.md`, with the next row as the decision.

## Step done
The step is done when its last row is done. Report: files accepted, changed, rejected, and open issues. Then say what comes next, in plain words.
