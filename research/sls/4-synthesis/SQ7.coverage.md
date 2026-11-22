---
id: SQ7.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ7.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P5.md, sls/3-reading/P9.md, sls/2-search/R0.md]
---
# Coverage of SQ7

Saved as `sls/4-synthesis/SQ7.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: a count or proportion of concurrency defects of a kind (e.g. deadlock, message-protocol violation, message-order defect, data race) reported for message-passing or for shared-memory programs, or a comparison between them.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new (10 + 3).

## Read
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P9 | 171 real Go bugs: message passing causes 49 of 85 blocking bugs (~58%), shared memory 69 of 86 non-blocking bugs (~80%); kinds include channel-protocol violations and 3 message-order bugs from `select`. Limit: Go programs mix both models; no system with single-owner state (pp. 5–7, 9–11) | new |
| 2 | P5 | Shared-memory baseline: 105 bugs in 4 C/C++ applications, 74 non-deadlock (51 atomicity, 24 order) and 31 deadlocks; 101 of 105 need at most two threads; no message-passing counts, and one message-queue bug sits inside the population (pp. 330–336) | new |

## Status
open: 2 read, fewer than 10; both added findings. Round 0 holds only 4 serving papers, so the question stays open until later rounds bring more.

## To read next
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P78 | Actor concurrency bugs in real-world software (message-passing side) |
| 2 | P79 | Channel-related blocking bugs in real Go systems |

## Deferred
none.

## Audit
not saturated yet.
