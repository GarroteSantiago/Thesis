# Running rows

How a skill in `.claude/skills/` runs the rows of a step (`ai/flow-sls.md`, `ai/flow-dsrm.md`). Every step skill follows this.

## Where to start
Before running anything, read the step's existing files in `research/` and find the first row not done:
- An agent row is done when all its output files exist.
- A gate row is done when none of its files is `proposed` and each has a decision file in `research/ai-log/decisions/`.

Resume from there. A step already done is reported and skipped.

## Agent rows
Dispatch the row's agent with the Agent tool (`subagent_type` = the agent's name). The prompt states:
- **Row:** the row ID.
- **Inputs:** the exact input files, expanded from the row's globs to real paths, and only files whose status allows it (rows that say "accepted" read only `accepted` or `changed` files).
- **Outputs:** the exact output paths, with `{n}` and `{k}` replaced by the next free number.

Independent dispatches run in parallel (e.g. one `reader` per paper in row 3a). When the agent returns, check its outputs against the agent contract (`ai/agent-contract.md`, *Your output is done when*). A missing file or a leftover placeholder goes back to the agent once, then to me as an open issue.

## Rows by me
Rows whose *Who* is me and that write files (7a, 8b, 11a, 11e). Show me the row's input files, ask for the content, and write each output from its template using my words only, with `by: me`. Where my words leave a template field empty, ask; the field stays mine.

## Gate rows
Follow `ai/gate.md`.

## Loop rows (`↺`)
Evaluate the condition from the files, tell me the result, and go to the row it names. A loop row decided by me is a gate: follow `ai/gate.md`, with the next row as the decision.

## Step done
The step is done when its last row is done. Report: files accepted, changed, rejected, and open issues.
