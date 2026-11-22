---
id: SQ9.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ9.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P10.md, sls/3-reading/P11.md, sls/3-reading/P12.md, sls/3-reading/P15.md, sls/3-reading/P29.md, sls/3-reading/P33.md, sls/3-reading/P64.md, sls/3-reading/P65.md, sls/3-reading/P69.md, sls/3-reading/P70.md, sls/3-reading/P72.md, sls/3-reading/P77.md, sls/3-reading/P261.md, sls/3-reading/P280.md, sls/2-search/R0.md]
---
# Coverage of SQ9

Saved as `sls/4-synthesis/SQ9.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: a measurement or argument that raising the hardware interface towards the language harms, or does not harm, performance, cost, generality or compiler optimisation, or a statement of whether such an argument applies to a message send or method dispatch.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new (10 + 3).

## Read
The named papers closest to a send first (all read ones are in the last group of SQ9.md's order), then the others, the two sides alternating.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P11 | Compiling to a low-level instruction set instead of bytecodes gives "an approximate doubling in speed"; bytecode decoding "takes either substantial hardware or substantial time"; the send was not raised into hardware, and instant lookup hardware would gain at most 23%; four specialised features were "mistakes" (pp. 2, 34–35, 47, 68, 70, 126) | new |
| 2 | P261 | Several SOAR features "could easily be performed by the compiler at marginal increased time and space costs" (1–3%), but software tag tests would cost an estimated 26%; applies to a send only partly (no send instruction) (pp. 3, 6–7, 10) | new |
| 3 | P15 | Argued: Lisp machines stopped paying once stock hardware caught up ("expensive 'dedicated' computers"; GC parity after 1989); the other side: VAX calls could not model Lisp calls (pp. 11, 25, 34–35); on a send only Hewitt and Smith's quoted claim (p. 62) | new |
| 4 | P280 | Against, argued: more logic and hardware bugs; compilers not "greatly" simplified; a language-tailored instruction set is "constrictive"; compaction gains small; raise the level "only when there are specific advantages"; does not say whether this applies to a send (pp. 98–99, 101–102) | new |
| 5 | P10 | Against, measured: the raised interface took chip space (decode unit fills a chip, no data registers) and gave 982-cycle protected calls; "Even if ... interprocess communication, procedure calls were free" the 432 would still be slow; measured on the call, not on Send (pp. 298–299, 301, 309, 316, 318) | new |
| 6 | P12 | For, argued, about a send as primitive: general mechanisms "competitive with processing nodes specialized to a single model"; tags faster than test-and-branch (pp. 1–2, 7, 23) | new |
| 7 | P29 | Against, measured: about 1/20 of a VAX in time and more code than 68000 Pascal or VAX C, against benefits argued but not measured; send not studied (pp. 17, 21, 23) | new (code size) |
| 8 | P69 | For, argued: executing messages directly removes interpretation overhead; only EXECUTE need be hard-wired, others run "almost as efficiently" (pp. 189, 191) | new |
| 9 | P33 | Against, about a send directly: message-driven hardware is "partly counter-productive"; software handlers "can exploit and optimize special cases"; one fast primitive "more versatile" than special hardware; modest support cuts handling to "a handful of instructions, but not to one" (pp. 431, 435, 437, 439) | new |
| 10 | P64 | For, argued: "general mechanisms ... rather than hardwiring mechanisms for a specific model of computation" (pp. 1–2, 13) | covered by P12 |
| 11 | P72 | Against, argued: a byte access "potentially requires four references"; 64 KB segments force special compiler code; variable instructions of 10 to over 300 bits; none concerns the send (pp. 166, 184–186) | new |
| 12 | P65 | For, with a measured cost: without hardware support communication goes to software "with prohibitive overhead"; one MDP node 8% faster to 20% slower than a 386SX; claim that the mechanisms fit a RISC core "without affecting sequential performance" (pp. 1, 7, 11–12) | new |
| 13 | P77 | Against special hardware: "capability systems can perform well without resorting to specialized hardware assists"; CAP's language-grain capabilities outran its hardware; EROS fast partly because of a minimal "semantic gap" (pp. 182–183) | new |
| 14 | P70 | Mixed, designer's arguments: hardware tags spare the compiler type analysis; fixed hardware limits (queues, 512 bindings, 16 tags); a message-based call costs 100–140 instructions; floating point by messages inefficient (pp. 11, 57, 114, 117–118, 125) | new |

## Status
open: 14 read; 13 added a finding; the last 4 all added one, so the run is 0 and the rule needs 3. None of the ten measured comparisons the reading order puts first (P17, P85, P81, P263, P264 against; P257, P265, P266, P256, P258 for) is read.

## To read next
All rows *(inferred from screening)*: `sls/2-search/R0.md` has no *Serves* column.

**A. Named in the reading order, still unread:**
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P17 | The RISC case against raising the instruction set (against) |
| 2 | P257 | Argument for language-directed architectures (for) |
| 3 | P85 | Hennessy: microcoded vs reduced instruction sets for compilers (against) |
| 4 | P265 | Architecture closing the gap to the user interface (for) |
| 5 | P81 | VAX-11 and RISC I comparison (against, measured) |
| 6 | P266 | Hardware support for interpreters (for) |
| 7 | P263 | Usefulness of M68000 complex instructions (against, measured) |
| 8 | P256 | Adaptive interpretation to exploit complex instructions (for) |
| 9 | P264 | Instruction-set complexity and memory (against, measured) |
| 10 | P258 | Thesis on an instruction set reducing the semantic gap (for) |
| 11 | P14 | SELF compiler: software instead of special hardware (close to a send) |
| 12 | P60 | Do object-oriented languages need special hardware? (close to a send) |
| 13 | P4 | C and the hardware's machine model |
| 14 | P7 | End-to-end arguments against moving function down |

**B. Other round-0 papers whose screening names SQ9** (read only while SQ9 stays open): P80 (RISCs for high-level-language support), P82 (CISC, RISC and interpretive designs), P83 (Katevenis's RISC dissertation), P84 (history of RISC), P259 (RISC principles for high-level-language computers), P260 (performance analysis of RISCs), P262 (microprogrammed vs RISC for symbolic processing) (7 papers).

Total to read next: 21 (A 14, B 7).

## Deferred
none: SQ9 is open.

## Audit
not saturated yet.
