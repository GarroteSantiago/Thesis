---
id: SQ8.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ8.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P5.md, sls/3-reading/P8.md, sls/3-reading/P9.md, sls/3-reading/P12.md, sls/3-reading/P22.md, sls/3-reading/P65.md, sls/3-reading/P70.md, sls/3-reading/P280.md, sls/2-search/R0.md]
---
# Coverage of SQ8

Saved as `sls/4-synthesis/SQ8.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: a measurement or argument that the hardware's execution model, or the language, libraries, tools or training, shapes how programs are designed or how correct they are.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new (10 + 3).

## Read
The named paper read first, then the others with measurements first and the language and hardware sides alternating.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P280 | Argument: ease of programming has "no difference inherent in the machine organization itself"; differences come from the cost of implementing a language and its tools; cheap error checking is expected ("one would expect") to give more reliable software (pp. 98, 101) | new |
| 2 | P9 | Language side, from 171 bugs: causes traced to Go's features and libraries and to "the lack of a clear understanding in new Go features"; no hardware factor examined (pp. 2, 6, 9–10, 12) | new |
| 3 | P8 | Hardware side, argument: in a shared-memory OS the knowledge for efficient sharing "is encoded implicitly in its implementation", tying it to one hardware design; programmers reason about "messages sent by the cache-coherence protocol" (pp. 2, 4) | new |
| 4 | P5 | Language and primitive side: order intentions not easily expressed or enforced by locks or transactional memory; "Most programmers think sequentially"; 29 of 57 Mozilla reports mention no tool (pp. 329, 333, 338) | new |
| 5 | P22 | Hardware side, argument: with coherence "programmers can concentrate on choreographing independent work"; removing it "shifts the complexity from hardware to software" (pp. 1, 9) | new |
| 6 | P70 | Hardware shapes language and code, designer's statement: target costs shaped CST's design, and MDP queues impose a rule that methods may not loop without a send (p. 12) | new |
| 7 | P12 | Designers' assertion: "most parallel programs are very biased by the mechanisms (or lack thereof) of the machines for which they were initially written"; fine-grain parallelism hard to extract from C or FORTRAN (pp. 18, 24) | new |
| 8 | P65 | Designers' argument: "Requiring coarse-grain communication complicates programming"; data placement costs programming effort (pp. 5, 7) | covered by P12 |

## Status
open: 8 read, fewer than 10; 7 added a finding. Most findings are arguments; the only measured ones (P9, P5) are on the language side. The named measurement studies (P147, P148) are unread.

## To read next
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P147 | Large-scale study of language and defects (measurement, language side) |
| 2 | P4 | C is not a low-level language: hardware shaped by the language's machine model |
| 3 | P148 | Multiple languages and code quality (measurement) |
| 4 | P2 | Backus: the von Neumann model shapes languages and programs (essay) |
| 5 | P3 | Iverson: notation shapes thought (language side, essay) |

Round 0 holds only these and P280, so the question stays open until later rounds bring more.

## Deferred
none.

## Audit
not saturated yet.
