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

## Kind
kinds, because the observation needs which kinds of escape route below the language remain and why designers kept them; the same few kinds (shared memory, interrupts, traps, privileged instructions, microcode) recur across systems, so listing them per system adds pages, not answers. (`research/sls/1-protocol/step.md`, *How much each question needs*)

Census or kinds is my decision at gate 1c; kinds is recommended, and the choice should follow SQ1's: under census this question reads the same papers as SQ1's census. Estimate from `sls/2-search/R0.md`: every one of the 160 papers included through I1 serves it, since it asks about the systems SQ1 finds; 7 of them name it in their screening reason (P42, P48, P152, P156, P178, P207, P249). Under census: about 110–120 papers from round 0 (one per system, the same set as SQ1's census, and more where the escape routes appear only in a later paper on the same system). Under kinds: about 25–35 papers.

## Unit
A kind of mechanism kept below the language that is not a message send (e.g. shared memory, interrupts, traps, privileged instructions, microcode, global registers), together with the reason given for keeping it; or a kind of level found to be written in the system's own objects and messages. A mechanism already recorded counts as new again only with a reason not yet recorded.

## Enough when
At least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new. 10 + 5 rather than 10 + 3: as for SQ1, the systems span four decades and three levels, and the escape routes of a processor differ from those of a kernel.

## Reading order
Papers whose screening reason names an escape route first: the ELXSI System 6400 adding shared memory (P42), shared queues between host and message coprocessor (P152), messaging and interrupt mechanisms of a microkernel (P156), in-kernel synchronisation in a scalable microkernel (P178), signals and shared memory between cores (P207), servers moved into the Mach kernel (P249), and twenty years of L4 lessons (P48). Then processors (P10, P12 or P65, P21 or P104, P66, P73) alternating with kernels (P8, P53, P77, P51, P200), across decades. Design retrospectives and lessons-learned papers before papers on a single mechanism.

Papers are grouped by system family (a system and its later versions, e.g. L4: L4, Fiasco, seL4). Per family, read: its foundational paper; its retrospective, if one exists; and a later paper only if its screening suggests it changes this question's answer (a new mechanism, a large change in message cost, an escape route added or removed). Other papers of the family are deferred. Several papers of one family count as one reading. (`changes/2026-10-16-system-families.md`)
