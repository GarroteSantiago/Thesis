---
name: sls-1-protocol
description: SLS step 1. Freeze step 0, draft and challenge the review protocol, then freeze it. With "change", record a change to a frozen protocol.
disable-model-invocation: true
argument-hint: "[change]"
---
# SLS 1 — Protocol

Runs rows 1a–1c of `ai/flow-sls.md`, following `ai/running.md`.

## Before 1a: freeze step 0
If any `research/0-start/` file is `provisional`, run a gate for row 0 (`ai/gate.md`): I accept each file, and step 0 is frozen from then on (`ai/kickstart.md`). `observation.md` must be accepted; 1a does not start without it.

## Rows
1. **1a** — dispatch `protocol-critic`. Inputs: the accepted `0-start/*.md`.
2. **1b** — dispatch `skeptic`. Inputs: `0-start/*.md` and the SQ files from 1a. Outputs: new counter-evidence `SQ{n}.md` files and `sls/1-protocol/protocol.skeptic.md`.
3. **1c** — gate. Once every file is decided, the protocol is frozen.

## With `change`
The protocol is frozen. Ask me what changes and why, write `sls/1-protocol/changes/{date}-{slug}.md` from its template in my words, apply the change to the protocol file, and record the decision as a gate.

Done when 1c is done, or the change is recorded.
