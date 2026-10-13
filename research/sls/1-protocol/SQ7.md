---
id: SQ7
row: 1a
by: protocol-critic
status: accepted
inputs: [0-start/notes.md]
---
# SQ7

## Question
What do empirical studies report about the number and kinds of concurrency defects, including deadlocks, message-protocol violations and message-order defects, in programs or systems where each piece of state has one owner and is changed only through messages, compared with programs or systems that share memory?

## Why it matters to the observation
The notes motivate the thesis by the share of concurrency bugs caused by shared state, and already name counter-evidence that message passing causes most blocking bugs in Go. This question collects both sides as published evidence.

## Origin
notes

## Kind
evidence, because the question asks what empirical studies report about defect counts and kinds on both sides: findings (counts, proportions, kinds of defect), not a list of studies. (`research/sls/1-protocol/step.md`, *How much each question needs*)

## Unit
A finding: a count or proportion of concurrency defects of a kind (e.g. deadlock, message-protocol violation, message-order defect, data race) reported for message-passing or for shared-memory programs, or a comparison between them.

## Enough when
At least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new.

## Reading order
Both sides alternating: the study that splits the same programs by mechanism first (Go, P9), then the shared-memory baseline (P5), actor bugs (P78), Go channel bugs (P79), then new studies from later rounds, message-passing and shared-memory in turn, different languages and decades. Round 0 holds only these 4 serving papers (the I3 includes), fewer than the 10 the rule needs: all are read, and the question stays open until later rounds bring more.
