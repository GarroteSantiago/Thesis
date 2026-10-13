# Gate

How a skill runs a gate row. The decision is mine; the skill prepares it, records it, and checks it.

1. **Present.** For each file waiting at this gate: what it holds, in plain words (*Talking to me*, below), every flag raised by its reviews (`.skeptic.md`, `.citations.md`, `.examiner.md` next to it), and its path so I can open it myself. Show a file's content when I ask; never make me judge from a bare list.
2. **Ask** with the AskUserQuestion tool, one decision card per decision (below), so every decision is a choice.
   - **Order.** Files that others depend on first (e.g. SQs before `criteria.md` and `extraction-form.md`, which must serve the kept SQs). Open decisions the agents named as mine come before the files they affect.
   - **One question per decision**, up to four per call.
   - **Group** decisions that share the same situation, the same options and the same reason (e.g. ten papers the reader flagged for the same criterion, on the same grounds): one question, *multiSelect*, one option per file, with what sets each one apart in its description. Any I leave unselected get their own question.
   - **Unflagged files** may be offered together in one *multiSelect* question ("accept these"); any I leave unselected get their own question.
   - **Recommend** one option when the reviews support it, marked "(Recommended)" and listed first.
3. **Wait** for my decision on each file: accept, change, or reject. My decision is the only input to the next step; a file I have not decided on stays `proposed`.
4. **Record.** One decision file per decided file, from `ai/template/ai-log/decision.md`, saved as `research/ai-log/decisions/{date}-{row}-{id}.md`, with `decision:` set to what I chose. *What I changed and why* holds my words. *Raw log entries* holds the session ID given at session start and the time span from the row's first dispatch to this gate (`ai/ai-log.md`). The decision is recorded before it is applied: the guard refuses a decided status on a file with no decision file (`ai/spec/README.md`).
5. **Apply.**
   - Accept: `status: accepted`.
   - Change: apply exactly the edits of the option I chose, or the edits I gave, then `status: changed`.
   - Reject: `status: rejected`.
   - Gates that assign values in a table (P IDs in 2b and 2d) write those values too.
6. **Check.** Run `just check`.
7. **Commit.** `git add -A && git commit -m "gate {row}: {what was decided, in a few plain words}"`. The commit is the gate's undo point and the history `/thesis status` reads (`ai/status.md`). If `just check` failed, commit anyway and name the problems in the message: the decisions are mine and stand; the problems become open issues.

The gate is done when every file waiting at it has a status other than `proposed` and a decision file, and the gate is committed.

## Decision card
Every question must make sense to someone who has never opened the research files and does not know the method's vocabulary. Each card has:

- **Situation** (in the text before the question, or in the question itself): what is being decided and why it comes up now, in one to three sentences. Name who raised it (the reader, the skeptic…) and on what grounds.
- **Why it matters:** what changes in the thesis depending on the answer, in one sentence. "This paper will be used as evidence when answering *does X cost performance*", not "R0-023 → I4".
- **Question:** the choice itself, ending with a question mark.
- **Options:**
  - *label*: the action in plain words, one to five words ("Count it for both", "Re-check later", "Exclude it"). Never an ID or a code alone.
  - *description*: what choosing it means and what follows from it: what the thesis gains or loses, what work it triggers, what it costs.
  - *preview* (single-select questions only): the exact edits the option makes, file by file, for me to inspect if I want. In multiSelect questions, the skill keeps the edits itself and applies them on my choice.

### Talking to me
This applies to everything meant for me: cards, reports, progress notes, step introductions.
- **IDs:** give what the ID stands for first, as a short paraphrase of its file, and the ID after it in parentheses: "does building the hardware around the language cost performance (SQ9)", "included if it directly answers one of the later questions (I4)", "Smith 2019, *Title in short* (P46)". Never a bare list of IDs. Files keep IDs alone; this rule is for what I read.
- **No internal codes** in what I read: no row numbers ("3a"), file names (`R0-023`), field names, or arrows (`→`, `->`) standing for edits. Say what they mean: "the paper's reading record", "the list of papers found in the first search".
- **Method terms** (criterion, review question, snowballing round, gate, baseline…): the first time one appears in a session, give its meaning in a few words, from `ai/glossary.md`.
- **Check before asking:** read the card as if you had never seen the files. If any word needs a file open to be understood, rewrite it.

### Example
An invented case, for illustration only.

Bad:
> P21: which criteria? — *I1 + I4*: "add I4 for SQ3. R0-023 and P21.md Reference -> 'I1, I4'".

Good:
> The reader found that Doe 2019, *Checklists on Night Shifts* (P21), in the review because it reports a checklist used in practice, also measures error rates before and after. That directly answers the question "do checklists reduce errors outside surgery" (SQ3).
> Why it matters: if counted, the paper's measurements are extracted and used as evidence when that question is answered.
> **Should this paper also count as evidence for that question?**
> - *Count it for both (Recommended)*: it stays in for its original reason, and the fields for that question get filled in its reading record. The reader quotes the passage on page 7.
> - *Original reason only*: no change; the passage stays in the record as a note.
