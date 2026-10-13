---
id: SQ7
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/notes.md]
---
# SQ7

## Question
What do empirical studies report about the number and kinds of concurrency defects, including deadlocks, message-protocol violations and message-order defects, in programs or systems where each piece of state has one owner and is changed only through messages, compared with programs or systems that share memory?

## Why it matters to the observation
The notes motivate the thesis by the share of concurrency bugs caused by shared state, and already name counter-evidence that message passing causes most blocking bugs in Go. This question collects both sides as published evidence.

## Origin
notes
