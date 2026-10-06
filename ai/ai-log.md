# AI log

Everything the AI does is recorded, not only the decisions. Two parts in `research/ai-log/`.

## 1. Raw log
`raw/<session>.jsonl`: every action, written automatically.
- Written by Claude Code hooks, not by the agents, so no agent can forget or leave out an entry.
- One entry per event: my prompts, skill calls, agent starts and stops, and every tool call with its full input and full output.
- Each entry records: timestamp, session, skill, agent, flow row (e.g. `3a`), event type, input, output.
- At session end, the session transcript is copied in as well. It also holds the model's own messages, which tool hooks do not see.
- Append only. Never edited by hand.

## 2. Decisions
`decisions/{date}-{row}-{id}.md`: one file per gate.
```
---
row: 3c
target: sls/3-reading/P12.md
decision: accepted          # accepted | changed | rejected
---
Proposed by: reader, citation-checker
What I changed and why:
Raw log entries: <session> <first>–<last>
```

The raw log shows what the AI did. The decisions show what I did with it. Each decision points to the raw entries behind it.
