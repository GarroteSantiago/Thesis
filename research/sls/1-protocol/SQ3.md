---
id: SQ3
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/observation.md]
---
# SQ3

## Question
Which message-based systems below the language level let a component (a proxy, monitor, filter or load balancer) be placed between a sender and a receiver without changing either, by what mechanism, and at what cost?

## Why it matters to the observation
The observation notes that networks allow interposition because parts communicate only through messages, while low-level machines expose shared state where no layer can be put in between. This question asks whether earlier attempts below the language kept that property.

## Origin
observation
