---
id: SQ5
row: 1a
by: protocol-critic
status: accepted
inputs: [0-start/notes.md]
---
# SQ5

## Question
What performance have message-based or object-based processors, instruction sets and operating system kernels reported against conventional baselines, including the cost of one message send and the scaling with the number of cores, and to what causes are the differences attributed, by whom (the designers or a third party), and is each cause inherent to the design or due to its implementation?

## Why it matters to the observation
The notes cite the Intel 432 and SOAR results and hypothesise that the 432's losses were avoidable (H2) and that many cores without shared state change the picture (H3). This question gathers the measured evidence those hypotheses rest on, and the baselines and metrics later steps can reuse.

## Origin
notes

## Kind
evidence, because the question asks what has been measured and to what causes the differences are attributed: findings (measurements and causes), not a list of systems. (`research/sls/1-protocol/step.md`, *How much each question needs*)

## Unit
A finding: a measurement against a conventional baseline (including the cost of one message send or the scaling with the number of cores), or a cause given for a difference, with who gives it (designers or a third party) and whether it is called inherent to the design or due to its implementation.

## Enough when
At least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new. 10 + 5 rather than 10 + 3: processors and kernels are measured with different baselines and metrics, across five decades, by designers and by third parties.

## Reading order
Processors and kernels alternating, designers and third parties alternating, measured evaluations first. Start with the Intel 432 evaluations (P10, then the independent P29), the SOAR results (P13, P11), the J-Machine evaluation (P65), L4 IPC (P46, P172), then the argument that IPC cost is becoming irrelevant (P209), Active Messages' evaluation of message-driven machines (P33), the cache effects of microkernel structure (P202), measurements of message-based operating systems (P218, P243), the PEACE kernel on MANNA (P88), the Single-chip Cloud Computer (P21, P104), the multikernel's scaling (P8), hardware IPC support (P159, P221), Lisp machines (P15), and the books on high-level-language and object machines (P1, P76). Round 0 holds about 45 papers that serve it: the 13 included through I2, and about 30 processor and kernel papers whose screening reason names measured IPC or message cost or this question.
