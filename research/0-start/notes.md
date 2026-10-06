---
id: notes
row: 0
by: me
status: provisional
inputs: []
---
# Notes

What I already thought about the problem before the review, as I wrote it. Checked against the literature in row 6a, not trusted. Numbers in brackets refer to the references at the end.

## Observation
- `Message Abstractions (OOP/Actors) are used` is true in `Languages/Agents/Network`, but not in `OS/Hardware/Low level programming`.
- Name of this gap in the literature, if any: the *semantic gap* (source: Myers [4])

## Motivation
- Why solving it matters:
  - **Premise.** The machine model shapes how programs are written [5][6]. Today's hardware pushes programmers towards threads and shared memory. Changing the hardware under the abstractions changes the programs written on top of it.
  - **Semantic gap.** Programs are written in objects and messages, but below the virtual machine the system is threads, addresses, loads and stores [4]. The model the programmer writes is not the model that executes [7]. Goal: message semantics hold from the language down to the hardware, with no layer in between that works differently. The system stays inspectable at every level, as Smalltalk is above its virtual machine [21].
  - **Shared-state concurrency.** In shared-memory programs, 97% of non-deadlock concurrency bugs are atomicity or order violations on shared state [8]. In the actor model each actor owns its state and processes one message at a time [16][17]. This removes data races and gives per-actor atomicity by construction.
  - **Parallel hardware.** With the end of Dennard scaling and Moore's law, single-processor performance has stalled and hardware is now parallel [9]. Independent actors map onto many cores.
  - **No central coordinator.** Networks work with protection and control at the endpoints [10]. Operating systems can already be built as message-passing parts that share no state [11]. This thesis explores whether the middle layer can be removed entirely.
- Scope (design stances, not problems this thesis solves):
  - Deadlock remains possible. Out of scope.
  - Atomicity across actors is the program's responsibility, through protocols, not the system's.
  - Messages arriving in different orders and producing different results is the intended semantics, not a defect. Counter-evidence to address: in Go, message passing is as easy to get wrong as shared memory, and causes about 58% of blocking bugs [12].
- Why it has not been done, or why earlier attempts failed:
  - Intel iAPX 432: object-based hardware that moved into microcode and hardware much of what other systems do in software. On early benchmarks it ran 10–26 times slower than the VAX 11/780 [13, p. 309]. A procedure call took 982 cycles, about ten times a call on the MC68010 or VAX, with object orientation "only a minor factor" [13, p. 309]. The bad Ada compiler cost 25–35% of throughput and implementation inefficiencies another 5–10%, losses "essentially unrelated to instruction set complexity or object orientation" [13, p. 337]. Even after fixes it stayed 1–4 times slower than conventional processors. The authors call this the inherent cost of *the 432's style* of object orientation, and say other approaches to object-based architecture are possible [13, pp. 336–337].
  - SOAR (Smalltalk On A RISC): a RISC processor with a few Smalltalk-specific features, about twice as fast as the same RISC without them [14][18]. Later, compiler techniques for dynamic languages (dynamic compilation, inlining of message sends) reached high performance on ordinary hardware [19], removing the need for language-specific processors.
  - J-Machine / Message-Driven Processor: hardware mechanisms for communication, synchronisation and naming, built as a research multicomputer [15].
  - Lisp machines: special-purpose machines that declined as Lisp moved to stock hardware [20].
  - What is different now (hypotheses, not results; RQ3 tests them):
    - **H1, the context changed.** Earlier special machines lost to general-purpose processors that kept getting faster for free [19][20]. That improvement has stopped, which reopens room for specialised architectures [9].
    - **H2, the 432's losses were avoidable.** Most of them came from the compiler and implementation details, not from object orientation [13]. This design can avoid those specific mistakes.
    - **H3, the target is different.** Earlier attempts made one processor run objects faster. This design targets many cores with no shared state, where shared memory has become a scaling cost [11].
    - Which of these hold: open (answered by RQ3).

## Stakeholders
| Stakeholder | Goal |
|---|---|
| Programmers | Write concurrent programs whose model is the one the machine executes |
| Operating system, processor and language designers | Share one primitive, the message send, from hardware to language |
| Research community | Know whether a full-stack message-based system is possible and how it performs, whether the answer is yes or no |

## Design problem
- Improve the execution of object, actor and message programs by designing a message-based machine (instruction set, language, simulator) that satisfies message semantics from hardware to language, one owner per piece of state, and no central coordinator, in order to help programmers and system designers write programs whose model is the one the machine executes.

## Knowledge questions
| ID | Type | Typical form [3] | Question | Could the answer be "no"? | Evidence that would answer it |
|---|---|---|---|---|---|
| RQ3 | Design, evaluation, or analysis of a particular instance | "How good is Y?" / "What is property X of Y?" | How does the message-based machine perform compared with von Neumann baselines on (a) actor programs and (b) the current system model simulated on top of it? | yes | Metrics: open (defined in step 2). Baselines: open. First in simulation, finally on real hardware. |
| RQ5 | Feasibility study or exploration | "Does X even exist?" / "Is it possible to accomplish X at all?" | Is it possible to build a system that is object, actor and message based from hardware to language, with no central coordinator? | yes | The simulator runs actor programs end to end, including the functions an operating system normally provides (open: protection, scheduling, resource allocation?). |

- RQ5 is the main question. RQ3 makes the answer useful.

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
2. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
3. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
4. Myers (1982). *Advances in Computer Architecture* (2nd edition). Wiley.
5. Backus (1978). *Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs*. Communications of the Association for Computing Machinery 21(8), 613–641. (1977 Turing Award lecture)
6. Iverson (1980). *Notation as a Tool of Thought*. Communications of the Association for Computing Machinery 23(8), 444–465. (1979 Turing Award lecture)
7. Chisnall (2018). *C Is Not a Low-level Language: Your Computer Is Not a Fast PDP-11*. Association for Computing Machinery Queue 16(2).
8. Lu, Park, Seo, Zhou (2008). *Learning from Mistakes: A Comprehensive Study on Real World Concurrency Bug Characteristics*. 13th International Conference on Architectural Support for Programming Languages and Operating Systems.
9. Hennessy, Patterson (2019). *A New Golden Age for Computer Architecture*. Communications of the Association for Computing Machinery 62(2), 48–60.
10. Saltzer, Reed, Clark (1984). *End-to-End Arguments in System Design*. Association for Computing Machinery Transactions on Computer Systems 2(4), 277–288.
11. Baumann, Barham, Dagand, Harris, Isaacs, Peter, Roscoe, Schüpbach, Singhania (2009). *The Multikernel: A New OS Architecture for Scalable Multicore Systems*. 22nd Symposium on Operating Systems Principles.
12. Tu, Liu, Song, Zhang (2019). *Understanding Real-World Concurrency Bugs in Go*. 24th International Conference on Architectural Support for Programming Languages and Operating Systems.
13. Colwell, Gehringer, Jensen (1988). *Performance Effects of Architectural Complexity in the Intel 432*. Association for Computing Machinery Transactions on Computer Systems 6(3), 296–339.
14. Ungar (1987). *The Design and Evaluation of a High Performance Smalltalk System*. Massachusetts Institute of Technology Press. (1986 ACM Doctoral Dissertation Award)
15. Dally, Fiske, Keen, Lethin, Noakes, Nuth, Davison, Fyler (1992). *The Message-Driven Processor: A Multicomputer Processing Node with Efficient Mechanisms*. Institute of Electrical and Electronics Engineers Micro 12(2), 23–39.
16. Hewitt, Bishop, Steiger (1973). *A Universal Modular ACTOR Formalism for Artificial Intelligence*. 3rd International Joint Conference on Artificial Intelligence, 235–245.
17. Agha (1986). *Actors: A Model of Concurrent Computation in Distributed Systems*. Massachusetts Institute of Technology Press.
18. Ungar, Patterson (1987). *What Price Smalltalk?* Institute of Electrical and Electronics Engineers Computer 20(1), 67–74.
19. Chambers, Ungar, Lee (1989). *An Efficient Implementation of SELF, a Dynamically-Typed Object-Oriented Language Based on Prototypes*. Object-Oriented Programming, Systems, Languages and Applications (SIGPLAN Notices 24(10)), 49–70.
20. Steele, Gabriel (1993). *The Evolution of Lisp*. 2nd History of Programming Languages Conference.
21. Goldberg, Robson (1983). *Smalltalk-80: The Language and Its Implementation*. Addison-Wesley.
