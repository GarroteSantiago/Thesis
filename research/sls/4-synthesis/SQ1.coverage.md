---
id: SQ1.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ1.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P8.md, sls/3-reading/P10.md, sls/3-reading/P12.md, sls/3-reading/P21.md, sls/3-reading/P33.md, sls/3-reading/P45.md, sls/3-reading/P46.md, sls/3-reading/P48.md, sls/3-reading/P49.md, sls/3-reading/P53.md, sls/3-reading/P64.md, sls/3-reading/P65.md, sls/3-reading/P66.md, sls/3-reading/P69.md, sls/3-reading/P70.md, sls/3-reading/P72.md, sls/3-reading/P73.md, sls/3-reading/P74.md, sls/3-reading/P77.md, sls/3-reading/P102.md, sls/2-search/R0.md]
---
# Coverage of SQ1

Saved as `sls/4-synthesis/SQ1.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** kinds.
- **Unit:** a kind of message-based system: the level where the send is a primitive (an instruction, a hardware or microcode mechanism, or the kernel's own means of communication), combined with how the mechanism works. A paper also adds a new unit if it shows a new kind of path, added later, that is not a message.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new (10 + 5).
- **From the reading order:** several papers on one system count as one reading; only the strongest is read for it. Abstract-only records (P74) are linked but do not count (gate 3c).

## Read
Papers with an accepted record that serve this question, in the reading order of SQ1.md (records on the same system are grouped and counted as one reading).
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P10 | Object-based processor (Intel 432): Send is an "interprocess communication primitive" in the instruction set, with IPC, scheduling and dispatching in microcode and hardware, beside memory-to-memory data instructions (pp. 297–298, 306–307) | new (reading 1: Intel 432) |
| – | P72 | Same system: instructions send to and receive from port objects, IPC "in hardware and microcode"; calls, scalar and fault paths are not messages (pp. 159, 162, 171) | covered by P10 (same system, counted with it) |
| – | P74 | Abstract only: names only the 432's segmentation and instruction set (abstract) | not counted (abstract only, gate 3c) |
| 2 | P12 | Message-driven multicomputer node: SEND in the instruction set, hardware buffering and dispatch, "There is no receive instruction" (pp. 1, 6, 9); later non-message path at language level: calls of known type compiled to direct function invocation (p. 20) | new (reading 2: MDP/J-Machine; a kind and a later-path kind) |
| – | P65 | Same system: send instructions, hardware task creation on arrival, dispatch in four cycles (p. 2) | covered by P12 (same system) |
| – | P64 | Same system, 1989 design: SEND instructions, two hardware priority queues, task per message (pp. 7–9, 13) | covered by P12 (same system) |
| – | P69 | Same system, 1987 design: transmit instruction, message unit with hard-wired EXECUTE (pp. 189, 191–192, 194) | covered by P12 (same system) |
| – | P70 | Same system with kernel and language: Cosmos services as message protocols; later path "reduction of method calls to function calls" (pp. 2, 4, 49, 70–76, 176) | covered by P12 (same system; the later path is P12's) |
| 3 | P8 | Multikernel: the kernel's inter-core communication is "explicit messages" over URPC on coherent memory with polling; a replica shared under spinlocks allowed by the model, not built (pp. 5, 7, 9, 18) | new (reading 3) |
| 4 | P46 | Synchronous-IPC microkernel with recursive address spaces (L4); first-generation port microkernel with external pager (Mach, Chorus); later path: servers and drivers reintegrated into the kernel (pp. 70–75) | new (reading 4: L4 family; two kinds and a later-path kind) |
| – | P48 | L4 family over 20 years: synchronous IPC as the only mechanism at first; later added notifications, semaphores, virtual IRQs, shared buffers replacing long IPC (pp. 133, 136–139) | counted with P46 as one reading; adds a new later-path kind (asynchronous notification and shared buffers added to a synchronous kernel) |
| 5 | P21 | Many-core chip with per-tile on-die message buffers and no hardware coherence; messages are a library over on-die shared memory with hardware support (MPMT, INVDMB), no send instruction (pp. 173–178) | new (reading 5) |
| 6 | P53 | Capability kernel: key invocation is the only means of invoking objects, no kernel buffering, exceptions as messages to keepers; later path in KeyNIX: a shared segment for UNIX tables (pp. 3, 7, 9, 11) | new (reading 6) |
| 7 | P77 | Capability kernel (EROS): capability invocation the only system call (pp. 173–174); reports Mach's later path: system calls added beside mach_msg for performance (p. 182) | new (reading 7): the kernel kind is covered by P53, the later path (extra system calls beside the message call) is new |
| 8 | P66 | Multicomputer node with a user-level protected SEND instruction, hardware destination translation (GTLB), register-mapped receive queue and dispatch via DIP to an event thread; messages between nodes only (pp. 3–7) | new (reading 8) |
| 9 | P73 | Microcoded language machine whose send is a microcode-dispatched call of the receiving object; "no new features are added to Lisp for message sending" (pp. 285, 309) | new (reading 9) |
| 10 | P102 | Factored OS: microkernel messaging among server fleets on separate cores, asynchronous sends to named mailboxes (pp. 5–6, 8) | covered by P8 (same level and mechanism: kernel messages between cores of one chip; fleets are OS structure) |
| 11 | P45 | Satellite kernels per NUMA domain and per programmable device of another instruction set, talking by contract-typed channels with software isolation (pp. 1–3, 6–7) | new (reading 11): heterogeneous satellite kernels with language-isolated channels |
| 12 | P33 | Message-driven nodes (J-Machine, Monsoon) with SEND in the execution unit; a design-only proposal of processor support for user-level handlers; Active Messages themselves a user-level layer (pp. 431, 436, 438–439) | covered by P12 (the built kinds are P12's; the proposal is not a built system) |
| 13 | P49 | Minix 3 multiserver OS with rendezvous fixed-length messages and interrupts as messages; Singularity, a language-protected microkernel with typed channels (pp. 47–50) | covered by P46 and P45 |

## Status
open: 13 readings counted (20 records, same-system records folded, P74 not counted), 10 of them added a new kind; the last 2 readings added nothing new, and the rule needs 5 in a row. Besides, 13 papers named earlier in the reading order (P96, P51, P200, P42, P274, P159, P221, P58, P59, P63, P276, P152, P250) are unread, so the order has not yet been followed and no run can close the question until they are read.

## To read next
Every row is linked to SQ1 by its criterion (I1) and its reason in `sls/2-search/R0.md`, which has no *Serves* column: all are *(inferred from screening)*.

**A. Named in the reading order, still unread** (read first, in this order):
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P96 | Transputer: a channel processor, a kind not yet in *Read* |
| 2 | P51 | Spring: object-oriented microkernel with doors as IPC |
| 3 | P200 | Chorus from its designers' experience; Read has it only through P46's third-party account |
| 4 | P42 | ELXSI System 6400: messages for parallelism, shared memory added later: a later-path kind not yet in *Read* (contradiction trigger) |
| 5 | P274 | Alewife: message passing and shared memory both in hardware |
| 6 | P159 | Hardware support for IPC (XPC): a hardware IPC accelerator for a kernel, not yet in *Read* |
| 7 | P221 | SkyBridge: fast microkernel IPC with hardware help |
| 8 | P58 | Java processor with object-oriented instructions |
| 9 | P59 | jHISC object-oriented instruction set |
| 10 | P63 | PUMA: hardware support for object-oriented programming |
| 11 | P276 | QNX message-passing microkernel |
| 12 | P152 | Message coprocessor with smart bus and shared memory: a communication coprocessor, not yet in *Read* |
| 13 | P250 | Sylvan: microcoded kernel-support processor |

**B. Screening suggests a level or mechanism not yet in *Read*** (then, levels alternating, while SQ1 is open):
| # | Paper | Why (inferred from screening) |
|---|---|---|
| 14 | P32 | MANNA node: computation processor plus communication processor |
| 15 | P39 | NLTSS message-passing OS on the Cray Y-MP: message-based distributed OS, a kind in the unit list not yet in *Read* |
| 16 | P87 | 8-core MPSoC on FPGA with hardware message passing and shared memory |
| 17 | P153 | SHOSHIN message-based distributed OS |
| 18 | P270 | IPC through dual-ported mailbox memories with a hardware controller |
| 19 | P34 | Distributed message-passing operating systems |
| 20 | P273 | Communications processor that turns memory reads and writes into messages |
| 21 | P35 | Thesis on implementation structures for message-passing OS architectures |
| 22 | P89 | Hardware message queues between two processors with an RTOS mechanism |
| 23 | P61 | muChoices object-oriented nano-kernel on bare hardware |
| 24 | P101 | Message-passing many-core processor with replay support |
| 25 | P151 | Choices parallel object-oriented OS |
| 26 | P54 | Actor language on a massively parallel message-passing architecture |
| 27 | P246 | JavaOS: an OS in an object language |
| 28 | P68 | Thesis: objects communicating only by messages on fine-grain computers |
| 29 | P191 | StarfishOS: state-partitioned microkernel on CXL |
| 30 | P57 | Position paper on object-oriented architectures closing the semantic gap |
| 31 | P50 | Determinator: shared-nothing spaces with deterministic IPC |
| 32 | P158 | Microkernel IPC accelerated with hardware watchpoints |
| 33 | P247 | CoMOS component-messaging OS for multi-processor sensor devices |
| 34 | P171 | IPC that bypasses privileged software |
| 35 | P278 | Publishing: distributed message-based system with a message recorder |
| 36 | P223 | Software-managed TLB for zero-copy microkernel communication |
| 37 | P207 | Inter-core signals and shared memory in a microkernel: possible later-path kind |
| 38 | P234 | Apiary OS for FPGAs |

**C. Kernel-level systems not yet read whose screening names only a microkernel, multikernel or kernel IPC** (likely kinds already in *Read*; read only while SQ1 stays open after A and B; all are kernel level, so levels cannot alternate; listed by P ID because the round file gives neither decade nor whether each is a full design): P36, P38, P40, P41, P43, P52, P88, P149, P150, P154, P155, P156, P157, P160, P161, P162, P163, P164, P165, P166, P167, P169, P170, P173, P174, P175, P176, P177, P178, P179, P180, P181, P182, P183, P184, P185, P187, P189, P190, P192, P193, P194, P195, P197, P198, P199, P201, P202, P203, P205, P206, P208, P209, P210, P211, P212, P213, P215, P216, P217, P218, P220, P222, P225, P226, P227, P228, P230, P236, P237, P238, P239, P241, P243, P244, P249, P252, P277 (78 papers; P277 is a cluster system whose screening proposed X3).

Total to read next: 116 (A 13, B 25, C 78).

## Deferred
Not needed for SQ1 under its reading order's rule that several papers on one system count as one reading. None has a screening reason suggesting a kind not yet in *Read*, so no contradiction trigger applies.
| Paper | Why deferred |
|---|---|
| P75 | Intel 432 book: same system as P10 and P72 |
| P71 | Optimist compiler for the MDP: same system as P12 |
| P214 | Message-driven programming on the J-Machine: same system as P12 |
| P37 | seL4 IPC design: L4 family (P46, P48) |
| P44 | seL4 verification including the IPC fast path: L4 family |
| P172 | Liedtke on IPC performance: L4 family (named in SQ1.md) |
| P188 | Verification of L4 IPC: L4 family (named in SQ1.md) |
| P196 | L4.Sec reference manual: L4 family |
| P204 | L4/MIPS internals: L4 family (named in SQ1.md) |
| P232 | L4-based real-time systems: L4 family |
| P233 | L4 lazy queueing and direct process switch: L4 family (named in SQ1.md) |
| P235 | seL4 IPC fast path: L4 family |
| P248 | Fiasco-SMP: L4 family |
| P251 | L4 reference manual for MIPS: L4 family (named in SQ1.md) |
| P168 | MINIX message mechanism: same system as Minix 3 in P49 |
| P224 | Barrelfish on the SCC: same systems as P8 and P21 |
| P104 | SCC from the programmer's view: same system as P21 |
| P99 | Book on Transputers: same system as P96 (read only if P96 does not describe the mechanism) |
| P231 | RHODOS IPC: same system as P36 |
| P240 | RHODOS migration: same system as P36 |
| P186 | Second record of microkernel support for SR: same system as P185 |
| P242 | mTags: same system as P228 |
| P229 | Determinator virtual memory: same system as P50 |
| P245 | Real-Time Mach priority inversion: same system as P170 |

## Audit
not saturated yet.
