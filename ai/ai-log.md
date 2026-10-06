# AI log

Everything the AI does is recorded, not only the decisions. Two parts in `research/ai-log/`.

## 1. Raw log
`raw/<session>.jsonl`: every action, written automatically.
- Written by the hooks in `.claude/settings.json`, which call `ai/tools/log_hook.py`, not by the agents, so no agent can forget or leave out an entry.
- One entry per hook event, as Claude Code sends it, plus a timestamp: session start and end, my prompts, every tool call before it runs and after (full input and full output), every agent stop, every compaction.
- Skill calls and agent dispatches are tool calls (`Skill`, `Agent`), so the skill, the agent and the row it was given are in their logged input. Subagents' own tool calls are logged too.
- `raw/<session>.transcript.jsonl` is a copy of the session transcript, refreshed at every stop and at session end. It also holds the model's own messages, which tool hooks do not see.
- At session start the hook gives the model the session ID, so gates can write it into decision files.
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
