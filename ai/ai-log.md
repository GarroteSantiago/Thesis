# AI log

Everything the AI does is recorded, not only the decisions. Two parts in `research/ai-log/`.

## 1. Raw log
`raw/<session>.jsonl`: every action, written automatically.
- Written by the hooks in `.claude/settings.json`, which call `ai/tools/log_hook.py`, not by the agents, so no agent can forget or leave out an entry.
- One entry per hook event, as Claude Code sends it, plus a timestamp: session start and end, my prompts, every tool call before it runs and after (full input and full output), every agent stop, every compaction.
- Binary payloads are not stored: every `base64` field (e.g. a rendered page image an agent read) is replaced by `{"omitted": "binary", "sha256", "bytes"}`. The hash proves which bytes were seen; the image itself can be rendered again from the published PDF named in the tool input. All text stays in full.
- A part over 40 MB continues in `raw/<session>.2.jsonl`, `.3.jsonl`, ..., so no file reaches GitHub's size limits.
- Skill calls and agent dispatches are tool calls (`Skill`, `Agent`), so the skill, the agent and the row it was given are in their logged input. Subagents' own tool calls are logged too.
- `raw/<session>.transcript.jsonl` is a copy of the session transcript, refreshed at every stop and at session end. It also holds the model's own messages, which tool hooks do not see.
- At session start the hook gives the model the session ID, so gates can write it into decision files.
- Append only. Never edited by hand. The one exception is scripted: `python3 ai/tools/log_hook.py --compact <file>` strips binary payloads from logs written before 2026-10-12 the same way; nothing else in the line changes. Applied on 2026-10-12 to `3b06c4e5-...jsonl` and `e8075297-...jsonl`.

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
