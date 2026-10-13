---
id: SQ9
row: 1b
by: skeptic
status: accepted
inputs: [0-start/observation.md, 0-start/notes.md]
---
# SQ9

## Question
What evidence and arguments show that narrowing the semantic gap by raising the hardware interface towards the language harms performance, cost, generality or compiler optimisation, and do those arguments apply to a message send as the machine's primitive?

## Why it matters to the observation
The notes treat the semantic gap as a defect to close. The reduced instruction set argument (Patterson and Ditzel, 1980, *The Case for the Reduced Instruction Set Computer*) was made against exactly that goal. If its reasoning carries over to message sends, the observation describes a deliberate trade-off, not an oversight.

## Origin
counter-evidence (added by skeptic)

## Kind
evidence, because the question asks what the evidence and arguments say about the costs of raising the hardware interface, and whether they carry over to a message send: findings and counter-arguments. (`research/sls/1-protocol/step.md`, *How much each question needs*)

## Unit
A finding: a measurement or argument that raising the hardware interface towards the language harms, or does not harm, performance, cost, generality or compiler optimisation, or a statement of whether such an argument applies to a message send or method dispatch.

## Enough when
At least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new.

## Reading order
Both sides alternating, measured comparisons first. Against raising the interface: the RISC case (P17), Hennessy (P85), the VAX-11 and RISC I comparison (P81), the M68000 complex instructions study (P263), instruction-set complexity and memory (P264). For it: the argument for language-directed architectures (P257), the architecture closing the gap to the user interface (P265), hardware support for interpreters (P266), adaptive interpretation (P256), the semantic-gap instruction set thesis (P258). Then the papers closest to a message send or method dispatch: SOAR (P11, P261), SELF's compiler (P14), whether object-oriented languages need special hardware (P60), C and the hardware's machine model (P4), end-to-end arguments (P7), Lisp (P15), and Ditzel and Patterson's retrospective (P280). Round 0 holds 25 papers that serve it (counted as the included rows whose screening reason names this question).
