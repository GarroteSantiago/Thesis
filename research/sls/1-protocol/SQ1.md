---
id: SQ1
row: 1a
by: protocol-critic
status: accepted
inputs: [0-start/observation.md]
---
# SQ1

## Question
Which computer systems provide sending a message (to an object, actor, process or core) as a primitive below the programming language, that is in the operating system kernel, the instruction set or the hardware, and at which of these levels does each system's message semantics hold, and which systems started message-based at a level and later added paths that are not messages?

## Why it matters to the observation
The observation claims message abstractions stop above the operating system and hardware. This question tests that claim against the systems that tried to go lower, and maps how far down each one got.

## Origin
observation

## Kind
kinds, because the observation's claim is tested by how far down each kind of attempt got and which kinds later added paths that are not messages, not by a catalogue of every kernel with an IPC path: one system of a kind places the message send at the same level, by the same mechanism, as the others of that kind. (`research/sls/1-protocol/step.md`, *How much each question needs*)

Census or kinds is my decision at gate 1c; kinds is recommended. Estimate from `sls/2-search/R0.md`: the 160 papers included through I1 all serve this question (counted as the included rows whose decision names I1; P67 left out, its decision changed to exclude at 3c). Grouping them by the system their title or screening reason names gives about 112 distinct systems, with the L4 family and the Mach family counted once each (about 120 if their variants, such as seL4, Fiasco or Real-Time Mach, count apart). Under census: about 110–120 papers to read from round 0 alone, plus one for each new system a later round finds. Under kinds: round 0 shows about 20 kinds across the three levels, so about 30–40 papers, one or two per kind, then 5 in a row with no new kind.

## Unit
A kind of message-based system: the level where the send is a primitive (an instruction, a hardware or microcode mechanism, or the kernel's own means of communication, as in I1), combined with how the mechanism works. Examples: an object-based processor with port send and receive operations; a message-driven multicomputer node; a many-core chip with on-die message buffers and no coherence; a channel processor; a hardware IPC accelerator for a kernel; a communication coprocessor; a synchronous-IPC microkernel; a port-based microkernel; a capability kernel; a multikernel; a message-based distributed operating system. A paper also adds a new unit if it shows a new kind of path, added later, that is not a message.

## Enough when
At least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new. 10 + 5 rather than 10 + 3: the systems span four decades and three levels, and a run of kernel papers says nothing about processors.

## Reading order
Levels alternating (instruction set, hardware or microcode mechanism, kernel), and within each level different groups and decades; full designs with an evaluation before position papers and short IPC notes. Start with the seeds and the system papers most other papers build on: the Intel 432 (P10, then P75), the Message-Driven Processor and the J-Machine (P12, P65), the multikernel (P8), L4 (P46, P48). Then: the Single-chip Cloud Computer (P21), KeyKOS and EROS (P53, P77), the Transputer (P96), Spring (P51), Chorus (P200), the ELXSI System 6400, which added shared memory later (P42), the M-Machine (P66), Alewife (P274), the Lisp Machine (P73), hardware IPC support (P159, P221), object and Java processors (P58, P59, P63), QNX (P276), fos and Helios (P102, P45), the message coprocessor and Sylvan (P152, P250). After these, any paper describing a system of a kind not yet covered. Several papers on one system count as one reading for this question (e.g. the L4 family: P46, P48, P172, P188, P204, P233, P251): only the strongest is read for it.
