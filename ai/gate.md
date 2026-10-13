# Gate

How a skill runs a gate row. The decision is mine; the skill prepares it, records it, and checks it.

1. **Present.** For each file waiting at this gate: its path, one line on what it holds, and every flag raised by its reviews (`.skeptic.md`, `.citations.md`, `.examiner.md` next to it). Give the paths so I can open the files myself. Show a file's content when I ask; never make me judge from a bare list.
2. **Ask** with the AskUserQuestion tool, not in prose, so every decision is a choice:
   - **Order.** Files that others depend on first (e.g. SQs before `criteria.md` and `extraction-form.md`, which must serve the kept SQs). Open decisions the agents named as mine come before the files they affect.
   - **One question per file**, up to four per call. Options: *Accept*; one option per concrete fix a review or the agent suggested, with the exact edit in its description (*multiSelect* when the fixes are independent); *Reject*. *Other* takes my own edits.
   - **Unflagged files** may be offered together in one *multiSelect* question ("accept these"); any I leave unselected get their own question.
   - **Recommend** one option when the reviews support it, marked "(Recommended)" and listed first.
3. **Wait** for my decision on each file: accept, change, or reject. My decision is the only input to the next step; a file I have not decided on stays `proposed`.
4. **Apply.**
   - Accept: `status: accepted`.
   - Change: apply exactly the edits I give, then `status: changed`.
   - Reject: `status: rejected`.
   - Gates that assign values in a table (P IDs in 2b and 2d) write those values too.
5. **Record.** One decision file per decided file, from `ai/template/ai-log/decision.md`, saved as `research/ai-log/decisions/{date}-{row}-{id}.md`. *What I changed and why* holds my words. *Raw log entries* holds the session ID given at session start and the time span from the row's first dispatch to this gate (`ai/ai-log.md`).
6. **Check.** Run `just check`.

The gate is done when every file waiting at it has a status other than `proposed` and a decision file.
