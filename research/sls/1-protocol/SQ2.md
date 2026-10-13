---
id: SQ2
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/observation.md]
---
# SQ2

## Question
In the systems found by SQ1, which mechanisms that are not message sends remain (for example shared memory, interrupts, traps, privileged instructions, microcode or global registers), and which levels of each system are written in the system's own objects and messages, and what reasons do the designers give for keeping each one?

## Why it matters to the observation
The observation says systems below the language rest on primitives that break their own rules, so they cannot define themselves. This question finds where each attempt kept such escape routes and how far its self-definition reached.

## Origin
observation
