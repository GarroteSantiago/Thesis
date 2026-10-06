# Gate

How a skill runs a gate row. The decision is mine; the skill prepares it, records it, and checks it.

1. **Present.** For each file waiting at this gate: its path, one line on what it holds, and every flag raised by its reviews (`.skeptic.md`, `.citations.md`, `.examiner.md` next to it). Give the paths so I can open the files myself.
2. **Wait** for my decision on each file: accept, change, or reject. My decision is the only input to the next step; a file I have not decided on stays `proposed`.
3. **Apply.**
   - Accept: `status: accepted`.
   - Change: apply exactly the edits I give, then `status: changed`.
   - Reject: `status: rejected`.
   - Gates that assign values in a table (P IDs in 2b and 2d) write those values too.
4. **Record.** One decision file per decided file, from `ai/template/ai-log/decision.md`, saved as `research/ai-log/decisions/{date}-{row}-{id}.md`. *What I changed and why* holds my words. *Raw log entries* holds the session ID given at session start and the time span from the row's first dispatch to this gate (`ai/ai-log.md`).
5. **Check.** Run `just check`.

The gate is done when every file waiting at it has a status other than `proposed` and a decision file.
