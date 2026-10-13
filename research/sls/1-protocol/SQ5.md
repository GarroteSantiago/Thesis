---
id: SQ5
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/notes.md]
---
# SQ5

## Question
What performance have message-based or object-based processors, instruction sets and operating system kernels reported against conventional baselines, including the cost of one message send and the scaling with the number of cores, and to what causes are the differences attributed, by whom (the designers or a third party), and is each cause inherent to the design or due to its implementation?

## Why it matters to the observation
The notes cite the Intel 432 and SOAR results and hypothesise that the 432's losses were avoidable (H2) and that many cores without shared state change the picture (H3). This question gathers the measured evidence those hypotheses rest on, and the baselines and metrics later steps can reuse.

## Origin
notes
