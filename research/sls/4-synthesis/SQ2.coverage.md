---
id: SQ2.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ2.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P8.md, sls/3-reading/P10.md, sls/3-reading/P12.md, sls/3-reading/P21.md, sls/3-reading/P33.md, sls/3-reading/P45.md, sls/3-reading/P46.md, sls/3-reading/P48.md, sls/3-reading/P49.md, sls/3-reading/P53.md, sls/3-reading/P64.md, sls/3-reading/P65.md, sls/3-reading/P66.md, sls/3-reading/P69.md, sls/3-reading/P70.md, sls/3-reading/P72.md, sls/3-reading/P73.md, sls/3-reading/P74.md, sls/3-reading/P77.md, sls/3-reading/P102.md, sls/2-search/R0.md]
---
# Coverage of SQ2

Saved as `sls/4-synthesis/SQ2.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** kinds.
- **Unit:** a kind of mechanism kept below the language that is not a message send (e.g. shared memory, interrupts, traps, privileged instructions, microcode, global registers), together with the reason given for keeping it; or a kind of level found to be written in the system's own objects and messages. A mechanism already recorded counts as new again only with a reason not yet recorded.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new (10 + 5). Abstract-only records (P74) do not count (gate 3c).

## Read
In the reading order of SQ2.md: the named lessons paper first, then processors alternating with kernels, then the papers the order does not name.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P48 | Shared buffers (long IPC complex, "rarely used"), kernel–user shared message registers (portability, cost), in-kernel fixed-policy scheduler (no user-level scheduler "without imposing high overhead"), in-kernel timer and interrupt-controller drivers, interrupts disabled in the kernel and a big lock (simplicity, verification); kernel in assembler/C/C++ (pp. 136–139, 142–147) | new |
| 2 | P10 | Shared memory in a "pure memory-to-memory architecture" (chip size, faster process swap, "conceptual unity and simplicity"); microcode as sole creator of protected pointers (unforgeable); I/O only through the Interface Processor; unprotected branch instructions never generated (pp. 302, 311, 315–317) | new (new reasons for shared memory; microcode and I/O kinds) |
| 3 | P8 | Coherent shared memory under every message ("the only inter-core communication mechanism available"); traps and system calls into the CPU driver; hardware-routed interrupts; IPIs and MONITOR/MWAIT to wake a receiver; application shared memory because "most current programs" need it; CPU driver outside the message model (pp. 8–11, 14) | new |
| 4 | P12 | Presence and type tags with fault handlers ("makes software more efficient and robust"), segment descriptors (relocation, protection), translation table (global naming), diagnostic port (supervisory commands), local READ/WRITE (pp. 3, 5–8) | new |
| 5 | P53 | Privileged in-kernel low-level drivers ("Except where performance compels otherwise"), shared segments in KeyNIX (state shared between UNIX keepers), loads and stores as "isomorphic to read and write messages", trap instruction kept for binary compatibility (pp. 4–5, 9–11) | new |
| 6 | P21 | On-die shared memory (MPB) "to increase performance of a message passing programming model"; cache management (MPMT, INVDMB) for software coherency; off-chip memory via LUT (pp. 174–176) | new |
| 7 | P77 | Per-trap kernel entry (Pentium's "irregular" saved state); drivers and store in the kernel "To simplify security assurance"; mode bit disabling invocation "For emulation"; levels in its own processes: storage allocation, virtual copy, process construction (pp. 170, 173, 178–180) | new |
| 8 | P66 | Shared memory over a global address space because it "simplifies programming"; register writes across clusters and global condition-code registers for parallelism and barriers; traps in a dedicated thread to avoid cancelling issued operations; sync bit per word (pp. 3–6) | new (global registers first recorded) |
| 9 | P73 | Shared Lisp objects instead of "special restricted mechanisms for inter-process communication"; locking; sequence breaks; hand-microcoded subprimitives; unrestricted access to internal state because "the Lisp Machine is an interactive system" (pp. 172, 282, 429) | new |
| 10 | P65 | Presence tags ("natural to associate the synchronization tag with the data"), priority interrupts with separate register sets for "Fast interrupt processing", name translation, send faults; no hardware barrier because software suffices (pp. 2, 5–6, 9–10) | new (new reasons for tags and interrupts) |
| 11 | P46 | I/O ports in driver address spaces; grant/map/demap kept in the kernel ("required to implement memory managers and pagers"); shared memory between the Unix server and its clients; DMA as a path no kernel can stop; kernel-mode extensions to save switches (pp. 72–73, 75–76) | new |
| 12 | P72 | Shared system memory (no reason); CALL/RETURN with preallocated hardware contexts (per-call allocation "was time-consuming"); local stack storage objects (garbage collection "prohibitive for short-lived objects"); hardware branch to fault handlers; type managers partly in hardware; "There are no special privileges" (pp. 159–160, 168–169, 172–173, 180, 184–185) | new |
| 13 | P64 | Tags for "synchronization on data availability"; ENTER/XLATE for a global address space and "the freedom to experiment with different address translation mechanisms"; segmented memory for relocation and protection (pp. 7, 9–10, 12–13) | new (minor: new reasons for tags and translation) |
| 14 | P69 | Memory-based instructions (fast context switches); type, overflow and translation traps (dynamic typing, uniform local and remote access); associative table (global names, one-cycle method lookup); level in its own terms: every message above EXECUTE is ROM code the user can redefine (pp. 189, 191–192, 194, 196) | new |
| 15 | P70 | System calls for Cosmos utilities (function-call overhead); fixed MDP code; per-node globals "because of flaws in the MDP architecture"; CST locks; CST runtime written in CST, Cosmos and MDP runtime in assembly (pp. 51–52, 54, 57, 60–61, 74–75, 180) | new |
| 16 | P33 | Interrupts as "the only way to signal an asynchronous event"; polling on the CM-5 because interrupts cost too much; kernel traps where there is no user-level network access; DMA for large messages; memory-mapped FIFOs; busy-wait flags (pp. 432–439) | new |
| 17 | P45 | System calls for process-private resources because "Local message-passing is slower than a system call"; timer, interrupt controller and traps for scheduling; shared memory and DMA under remote messages (PCI-E accesses "stall the initiating CPU"); interrupts steered to one kernel; kernel in Sing# except per-device assembly (pp. 2, 4–7) | new |
| 18 | P49 | Kernel calls for privileged operations, since user-mode drivers "cannot execute privileged instructions"; clock driver in the microkernel; Singularity's shared object heap ("the system would be very slow" otherwise); mutexes in the microkernel; Singularity "almost entirely in Sing#" (pp. 47–50) | new |
| 19 | P102 | Application shared memory ("in a small application, it can be quite useful"); microkernel name and privilege caches (fast lookups); static privileges as a "privilege fixed point" to prevent dependency cycles; OS services written as message servers, microkernel outside (pp. 2, 5–7) | new |
| – | P74 | Abstract only: names no escape route (abstract) | not counted (abstract only, gate 3c) |

## Status
open: 19 read, all 19 added a mechanism with a reason not yet recorded; the run of papers adding nothing new is 0, and the rule needs 5. Six papers the reading order puts first (P42, P152, P156, P178, P207, P249) and two named kernels (P51, P200) are unread. Because any new reason for a known mechanism counts as new, saturation is unlikely while each system brings its own reasons.

## To read next
Every row is linked to SQ2 because SQ2 asks about the systems SQ1 finds: all included I1 papers serve it (SQ2.md), and `sls/2-search/R0.md` has no *Serves* column, so all are *(inferred from screening)*.

**A. Named in the reading order, still unread:**
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P42 | ELXSI System 6400 added shared memory later; screening names an escape route |
| 2 | P152 | Shared queues between host and message coprocessor |
| 3 | P156 | Messaging and interrupt mechanisms of a microkernel |
| 4 | P178 | In-kernel synchronisation in a scalable microkernel |
| 5 | P207 | Signals and shared memory between cores |
| 6 | P249 | Servers moved into the Mach kernel |
| 7 | P51 | Spring (named kernel) |
| 8 | P200 | Chorus (named kernel) |

**B. Systems of kinds SQ1 has not yet covered, processors and kernels alternating** (new escape routes are likeliest there): P96, P276, P274, P39, P159, P153, P221, P34, P58, P35, P59, P61, P63, P151, P250, P191, P32, P50, P87, P246, P89, P247, P270, P278, P273, P101, P54, P68, P57, P158, P171, P223, P234 (33 papers; each is described in SQ1.coverage.md, *To read next* A and B).

**C. The other I1 papers, kernel level, by P ID** (read only while SQ2 stays open after A and B; retrospectives such as P189 and P181 first within the group): P189, P181, P36, P37, P38, P40, P41, P43, P44, P52, P71, P75, P88, P99, P149, P150, P154, P155, P157, P160, P161, P162, P163, P164, P165, P166, P167, P168, P169, P170, P172, P173, P174, P175, P176, P177, P179, P180, P182, P183, P184, P185, P186, P187, P188, P190, P192, P193, P194, P195, P196, P197, P198, P199, P201, P202, P203, P204, P205, P206, P208, P209, P210, P211, P212, P213, P214, P215, P216, P217, P218, P220, P222, P224, P225, P226, P227, P228, P229, P230, P231, P232, P233, P235, P236, P237, P238, P239, P240, P241, P242, P243, P244, P245, P248, P251, P252, P277 (98 papers). SQ2's reading order has no rule that several papers on one system count as one reading, so the papers deferred for SQ1 on that ground stay here.

Total to read next: 139 (A 8, B 33, C 98).

## Deferred
| Paper | Why deferred |
|---|---|
| P104 | The reading order takes "P21 or P104" for the SCC; P21 is read. |

## Audit
not saturated yet.
