---
id: change-2026-10-16-system-families
row: 1c
by: me
status: accepted
inputs: [sls/1-protocol/SQ1.md, sls/1-protocol/SQ2.md, sls/1-protocol/SQ3.md, sls/1-protocol/SQ4.md, sls/1-protocol/SQ5.md]
---
# Protocol change: system-families

Saved as `sls/1-protocol/changes/2026-10-16-system-families.md`.

## What changed
- `sls/1-protocol/SQ1.md` to `SQ5.md`, *Reading order*: added — "Papers are grouped by system family (a system and its later versions, e.g. L4: L4, Fiasco, seL4). Per family, read: its foundational paper; its retrospective, if one exists; and a later paper only if its screening suggests it changes this question's answer (a new mechanism, a large change in message cost, an escape route added or removed). Other papers of the family are deferred. Several papers of one family count as one reading."
- `ai/project.md`, *Rules for this thesis*: the same rule, with this file as its source.
- It applies to every family (L4, Mach, the Intel 432, the Transputer, the Message-Driven Processor…), not only microkernels. It settles the synthesizer's proposal at 4a to count one reading per system for SQ2.

## Why
"microkernel is a very specific architecture, i dont know if seeing multiple implementations of the same solution brings something to the table. Maybe we should try getting the foundational paper of that architecture and use that one to work, only bring more if there are some which revolutionazed something really big about it."

## Papers affected
None excluded or re-screened. Variants of families already covered move from "read next" to "deferred" in the coverage of SQ1–SQ5; they stay counted as found.
