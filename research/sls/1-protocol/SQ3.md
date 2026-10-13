---
id: SQ3
row: 1a
by: protocol-critic
status: accepted
inputs: [0-start/observation.md]
---
# SQ3

## Question
Which message-based systems below the language level let a component (a proxy, monitor, filter or load balancer) be placed between a sender and a receiver without changing either, by what mechanism, and at what cost?

## Why it matters to the observation
The observation notes that networks allow interposition because parts communicate only through messages, while low-level machines expose shared state where no layer can be put in between. This question asks whether earlier attempts below the language kept that property.

## Origin
observation

## Kind
kinds, because the observation needs the mechanisms by which messages below the language let a component be placed between sender and receiver, and what each costs; which systems have them matters only as examples of each mechanism. (`research/sls/1-protocol/step.md`, *How much each question needs*)

Census or kinds is my decision at gate 1c; kinds is recommended. Estimate from `sls/2-search/R0.md`: 3 included papers name this question in their screening reason (P183, P203, P278); about 10 more are capability, port-based or multiserver kernels where such interposition may be described (P43, P46, P48, P49, P51, P52, P53, P77, P199, P200), counted by the kind of system their screening reason names. Census would have to check every system SQ1 finds, because titles and abstracts rarely say whether a component can be placed in between: about 110–120 papers from round 0, the same set as SQ1's census. Under kinds: about 13–15 papers.

## Unit
A kind of interposition mechanism below the language (e.g. a transparent monitor on the IPC path, a recorder that receives every message, a port or capability that can be redirected to a proxy), with its reported cost. A mechanism already recorded counts as new again if a different cost or limit is reported.

## Enough when
At least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new.

## Reading order
The three papers whose screening reason names interposition first: transparent monitors on synchronous IPC (P203), the Publishing recorder of all messages (P278), adaptive monitoring in microkernels (P183). Then kinds of system alternating: capability kernels (P53, P77), port-based kernels (P43, P200, P199), synchronous-IPC kernels (P46, P48), Spring's doors (P51), multiserver systems (P52, P49), and processors whose messages go through ports or names the hardware resolves (P10, P12); different decades within each.
