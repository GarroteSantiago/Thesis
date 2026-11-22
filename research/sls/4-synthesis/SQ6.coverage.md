---
id: SQ6.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ6.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P10.md, sls/3-reading/P11.md, sls/3-reading/P12.md, sls/3-reading/P13.md, sls/3-reading/P15.md, sls/3-reading/P22.md, sls/3-reading/P29.md, sls/3-reading/P33.md, sls/3-reading/P46.md, sls/3-reading/P49.md, sls/3-reading/P65.md, sls/3-reading/P70.md, sls/3-reading/P72.md, sls/3-reading/P77.md, sls/3-reading/P280.md, sls/2-search/R0.md]
---
# Coverage of SQ6

Saved as `sls/4-synthesis/SQ6.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: a reason stated for a machine being abandoned, not adopted, or made unnecessary, with who states it (its designers or a later evaluation).
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new (10 + 5). Abstract-only records (P13) do not count (gate 3c).

## Read
In the reading order of SQ6.md (named papers first), then the papers it does not name, families alternating. P29 is named in the order but its accepted record does not list SQ6, so it is not counted here.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P280 | Third parties (Ditzel on SYMBOL excepted): "there are no commercial direct or indirect execution high-level language machines"; justifications not examined, "ignored the view of the total system"; poor support for other languages; hardware debugging cost; better compilers and cheaper memory removed the motive; direct execution "will not become viable" (pp. 98–100, 103) | new |
| 2 | P10 | Third party: the 432 "as a commercial venture ... failed completely", probably because it "tried to do too many new things all at once", and its market "may still not be large enough or defined well enough" (p. 337) | new |
| 3 | P15 | Later account by participants with a stock-hardware interest: value "in the software and not in its enabling hardware"; general-purpose hardware "became good enough"; customers would not buy "expensive 'dedicated' computers"; the GC objection "proven wrong"; the AI winter; PERQ's price-performance (pp. 15, 28, 30, 34–35) | new |
| – | P13 | Abstract only: no reason for SOAR's fate; Smalltalk environments "require such expensive computers" is a motivation (abstract) | not counted (abstract only, gate 3c) |
| 4 | P33 | Third party (Active Messages authors): message-driven prototypes "could not utilize traditional processor design know-how", but "the problem is deeper": lack of locality makes the support "partly counter-productive"; the J-Machine "does not actually support the message driven programming model fully"; Monsoon needs much high-speed memory (pp. 435, 437) | new |
| 5 | P70 | Designer, 1991: no reason for non-adoption; the system is "still an evolving research and demonstration vehicle", with little "feedback from applications" (pp. 1, 115, 128) | nothing new (no reason for decline stated) |
| 6 | P72 | Third party (Levy, 1984): the 432 "has not been a commercial success", "probably due in part to premature (and somewhat overzealous) marketing", and initial performance problems (p. 186) | new (marketing) |
| 7 | P11 | Author as evaluator of earlier machines: coupling source semantics to hardware "usually resulted in increased cost and poor performance"; exploratory environments "suffer from poor cost-performance"; lack of fast implementations "severely curtailed" Smalltalk's acceptance (pp. 1, 10–11, 14, 17) | new |
| 8 | P12 | Designers: the MDP is a research chip; obstacles named are the lack of well-established parallel benchmarks, programs biased to their original machines, and a "very conservative" implementation (pp. 23–24) | new |
| 9 | P65 | Weak: no reason stated (the machine is "in daily use"); the designers propose folding its mechanisms into a RISC core instead (pp. 1, 12) | nothing new |
| 10 | P22 | Third party: chips "without caches or without a shared address space" are not common because coherence costs little, OSes already scale on it, and "Computer systems tend not to abandon compatibility to eliminate small costs"; argued; that these chips are message-based machines is the reader's inference (pp. 1, 8) | new (compatibility) |
| 11 | P46 | For message-based kernels, not machines (scope inferred): "the pure microkernel approach of the first generation was a failure", for inefficiency and inflexibility; stated by the designer of a competing kernel (pp. 73–74, 77) | new (limit: kernels) |
| 12 | P49 | For microkernels: "long discarded as unacceptable because of their lower performance"; "In the 1980s, performance counted for everything" (pp. 47, 50) | covered by P46 |
| 13 | P77 | Weak: KeyKOS "Development ceased in 1991 when the company closed" (a kernel); the i432's performance "suffers dramatically" from complexity, cited (pp. 170, 183) | new (business closure; the 432 claim is covered by P10, P72) |

## Status
open: 13 read; 10 added a new reason; the last paper (P77) added one, so the run is 0 and the rule needs 5. Seven papers named in the reading order are unread, including the compiler papers (P14, P60) for the "made unnecessary" side.

## To read next
All rows *(inferred from screening)*: `sls/2-search/R0.md` has no *Serves* column.
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P14 | SELF compiler techniques that made special hardware unnecessary |
| 2 | P60 | Do object-oriented languages need special hardware? |
| 3 | P1 | Myers's book: the 432 and SWARD, reasons for their design and performance |
| 4 | P76 | Book on high-level-language architecture |
| 5 | P84 | History of RISC research and why it replaced complex instruction sets |
| 6 | P189 | IBM Workplace OS: development experience of a multiserver OS |
| 7 | P42 | ELXSI System 6400, which added shared memory later |

Total to read next: 7. P13's full text is still needed for it to count.

## Deferred
none: SQ6 is open.

## Audit
not saturated yet.
