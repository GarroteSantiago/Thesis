---
name: dsrm-6-communicate
description: DSRM activity 6. For one thesis section, take my outline, draft it, check citations, raise committee questions, and finalize it in my words.
disable-model-invocation: true
argument-hint: "ch{n}-{section} | contribution"
---
# DSRM 6 — Communicate

Runs rows 11a–11e of `ai/flow-dsrm.md` for one section, following `ai/running.md`. Chapters are listed in `research/README.md`. Without an argument, show which sections exist and their status, and ask me which.

## Rows
1. **11a** — mine (*Rows by me*). Show me the accepted files the chapter is built from. Write `ch{n}-{section}.outline.md` from my claims and sources.
2. **11b** — dispatch `drafter`. Inputs: the outline and its sources. Output: `ch{n}-{section}.draft.md`.
3. **11c, 11d** — in parallel: dispatch `citation-checker` (output `ch{n}-{section}.citations.md`) and `examiner` (output `ch{n}-{section}.examiner.md`). Input: the draft and its sources.
4. **11e** — mine, and a gate. Present the draft, every citation flag and every examiner question. Write `ch{n}-{section}.md` from the draft with exactly my edits (*Rows by me*), then record the decision.
5. **Hole (↺)** — if an examiner question or my edits expose a hole, ask me: back to DSRM 2 or 3, recorded as a gate.

## `contribution`
Write `contribution.md` from my choice of contribution type and reason (*Rows by me*), and record it as a gate.

Done when the section's final file is decided.
