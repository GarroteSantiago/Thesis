---
profile: {name of a profile in ai/profiles/, without .md}
title: {the thesis title, or "untitled" for now}
author: {my name as it goes on the cover}
citation_style: default
reference_doc: none
---
# Project settings

Saved as `ai/project.md`, at setup. This thesis's own file: the skills read it and never change it without asking me, and upgrades never touch it. The other project-owned files are `project-tools.nix` (my own tools) and `project.just` (my own `just` recipes).

- `citation_style`: `default` (Chicago author-date), or the path to a `.csl` file for the style my university requires (`ai/export.md`).
- `reference_doc`: `none`, or the path to a `.docx` with my university's styles, used as the template of the exported document (`ai/export.md`).

## Profile
{Why this profile fits the thesis, in one line.}

## University AI policy
{What my university or programme says about using AI in a thesis, and where it says it (link or document); or "not checked yet: to check before writing chapters". The Method chapter states how AI was used, from the AI log and `research/views/ai-usage.md`.}

## Rules for this thesis
Rules that refine the workflow for this thesis only, each with where it was decided (a protocol change, a decision file). Every skill and agent reads them; where one differs from a step's own instructions, the rule here wins, and the skill says so when it applies it (`ai/running.md`). Or "none".

{- **Rule, in one sentence.** Which steps or rows it changes, and how. Source: `research/...`.}

## Notes for this thesis
Knowledge specific to this thesis that helps the work but is not a rule: likely papers for the start set, known current solutions to check, terms of the field. Agents may use it as a lead, never as evidence. Or "none".

{- Note.}
