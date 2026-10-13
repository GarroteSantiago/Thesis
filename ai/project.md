---
profile: computing
title: untitled
author: Santiago Garrote
citation_style: default
reference_doc: none
---
# Project settings

Saved as `ai/project.md`, at setup. This thesis's own file: the skills read it and never change it without asking me, and upgrades never touch it. The other project-owned files are `project-tools.nix` (my own tools) and `project.just` (my own `just` recipes).

- `citation_style`: `default` (Chicago author-date), or the path to a `.csl` file for the style my university requires (`ai/export.md`).
- `reference_doc`: `none`, or the path to a `.docx` with my university's styles, used as the template of the exported document (`ai/export.md`).

## Profile
The artifact is a computing system (an actor machine's instruction set, language and simulator), built in layers from a paper design toward hardware.

## University AI policy
Not checked yet: to check before writing chapters.

## Rules for this thesis
Rules that refine the workflow for this thesis only, each with where it was decided (a protocol change, a decision file). Every skill and agent reads them; where one differs from a step's own instructions, the rule here wins, and the skill says so when it applies it (`ai/running.md`).

None. The key-papers rule (`research/sls/1-protocol/changes/2026-10-12-key-papers.md`) is now the workflow's own (`research/sls/3-reading/step.md`, *Rules*).

## Notes for this thesis
Leads from the FAQs of the first workflow version, never verified: agents may use them as leads, never as evidence.

- **Possible start-set papers** (beyond `research/0-start/seeds.md`): Kay (1993), *The Early History of Smalltalk*, Second History of Programming Languages Conference; Woodruff et al. (2014), *The CHERI Capability Model*, International Symposium on Computer Architecture.
- **Likely current solutions to check:** Intel 432 (Organick (1983), *A Programmer's View of the Intel 432 System*, McGraw-Hill), Transputer (Whitby-Strevens (1985), *The Transputer*, International Symposium on Computer Architecture), J-Machine, CHERI.
- **History the thesis must answer:** language-oriented hardware failed before (Ditzel, Patterson (1980), *Retrospective on High-Level Language Computer Architecture*, International Symposium on Computer Architecture); the Intel 432 was slow, much of it from implementation choices (Colwell et al. 1988, in the seeds).
- **Terms not settled in the field:** actor, object, message-driven, capability. Keyword searches miss papers.
- **Layers and demonstrations:** the later layers could be a Field-Programmable Gate Array (FPGA: a chip you can rewire with code) prototype or a model in the gem5 simulator (Binkert et al. (2011), *The gem5 Simulator*, Computer Architecture News 39(2)). Problem instances: small actor programs, then programs from the Savina actor benchmark suite (Imam, Sarkar (2014), *Savina: An Actor Benchmark Suite*, AGERE workshop).
- **Evidence:** a formal proof, for example in TLA+, a language for specifying systems (Lamport (2002), *Specifying Systems*, Addison-Wesley), counts as analysis, the stronger kind of evidence. Performance is secondary: show the design is not hopelessly slow, given the Intel 432's history, using actor benchmarks against a normal processor.
