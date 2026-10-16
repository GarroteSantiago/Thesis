---
id: SQ4
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/notes.md]
---
# SQ4

## Question
How do operating systems and machines built from message-passing parts that share no state provide protection, scheduling, resource allocation and naming, and which of these functions still rely on a central coordinator, or on replicated parts that must agree, and what does each cost?

## Why it matters to the observation
The notes aim for a system with no central coordinator and leave open how it would provide the functions an operating system normally provides (protection, scheduling, resource allocation). Published systems show which of these have been done without shared state, and which have not.

## Origin
notes

## Kind
evidence, because the question asks how each function is provided, whether it relies on a coordinator or on agreement, and what that costs: findings about functions, not a list of systems. (`research/sls/1-protocol/step.md`, *How much each question needs*)

## Unit
A finding: how one of the four functions (protection, scheduling, resource allocation, naming) is provided in a system of message-passing parts that share no state, whether it relies on a central coordinator or on replicated parts that must agree, or what it costs.

## Enough when
At least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new. 10 + 5 rather than 10 + 3: four functions, and two eras whose systems differ in kind (distributed message-based operating systems of the 1980s and 1990s, multikernels on one chip since 2009).

## Reading order
Functions and eras alternating, designs with measurements first. Start with the multikernel (P8, replicated state kept by agreement), then capability protection in KeyKOS and EROS (P53, P77), load distribution on microkernels (P167, P194), fos (P102), the Cosmos operating system on the J-Machine (P70), naming in the Lego kernel (P238), Helios (P45), RHODOS process migration (P240), distributed process management on multicores (P230), NLTSS and SHOSHIN (P39, P153), Popcorn Linux (P211, P225), PIKA (P175), StarfishOS (P191), Determinator (P50). Round 0 holds about 22 papers that serve it: 4 name it in their screening reason (P167, P194, P230, P240), the others are multikernel, capability-kernel and distributed message-based operating system papers.

Papers are grouped by system family (a system and its later versions, e.g. L4: L4, Fiasco, seL4). Per family, read: its foundational paper; its retrospective, if one exists; and a later paper only if its screening suggests it changes this question's answer (a new mechanism, a large change in message cost, an escape route added or removed). Other papers of the family are deferred. Several papers of one family count as one reading. (`changes/2026-10-16-system-families.md`)
