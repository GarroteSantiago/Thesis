---
id: SQ5.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ5.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P8.md, sls/3-reading/P10.md, sls/3-reading/P11.md, sls/3-reading/P12.md, sls/3-reading/P13.md, sls/3-reading/P15.md, sls/3-reading/P21.md, sls/3-reading/P29.md, sls/3-reading/P33.md, sls/3-reading/P45.md, sls/3-reading/P46.md, sls/3-reading/P48.md, sls/3-reading/P49.md, sls/3-reading/P53.md, sls/3-reading/P64.md, sls/3-reading/P65.md, sls/3-reading/P66.md, sls/3-reading/P69.md, sls/3-reading/P70.md, sls/3-reading/P72.md, sls/3-reading/P73.md, sls/3-reading/P77.md, sls/3-reading/P102.md, sls/3-reading/P261.md, sls/3-reading/P280.md, sls/2-search/R0.md]
---
# Coverage of SQ5

Saved as `sls/4-synthesis/SQ5.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: a measurement against a conventional baseline (including the cost of one message send or the scaling with the number of cores), or a cause given for a difference, with who gives it (designers or a third party) and whether it is called inherent to the design or due to its implementation.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new (10 + 5). Abstract-only records (P13) do not count (gate 3c).

## Read
In the reading order of SQ5.md (named papers first), then the papers it does not name, processors and kernels alternating.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P10 | 432 10x–26x slower than a VAX-11/780 (Berkeley data); procedure call 982 cycles, about 10x; compiler loses 25–35% and alignment 5–10% (implementation, third party, isolated); residual 2–3x "inherent cost" (not isolated); no Send latency, no scaling (pp. 301, 309–310, 312–337) | new |
| 2 | P29 | 432 at about 1/20 of a VAX-11/780 (third party); cause isolated by modified programs: parameter and global access in release 2 (implementation); no message cost (pp. 18, 20, 23) | new (the isolated cause; the ratio itself is the data P10 cites) |
| – | P13 | Abstract only: announces a performance estimate for Smalltalk-80 with SOAR, no figures (abstract) | not counted (abstract only, gate 3c) |
| 3 | P11 | SOAR at a median 107% of the Dorado against 40% for a 68010 compiler; in-line caching 23% of time; causes by the designer, isolated by omission: windows, tags, direct pointers, scavenging; a 400-to-510 ns cycle loss called implementation (pp. 37, 46–48, 66, 71–72) | new |
| 4 | P65 | One-way overhead 11 cycles/msg against 109–3200 on CM-5, nCUBE/2, DELTA; barriers 4.4–16.5 µs against 109–3587 µs; one node 8% faster to 20% slower than a 386SX; speed-ups about 135–400 at 512 nodes; causes by designers (pp. 4, 6–9, 11) | new |
| 5 | P46 | Mach vs Ultrix up to +66% cycles, 50% AIM III loss for OSF/1 (third parties); Mach IPC 115 µs vs L4 5 µs; "At least 73%" of the penalty IPC, hardware "only 3%–7%"; cause the basic architecture and implementation (pp. 73–75, 77) | new |
| 6 | P33 | Active Messages start-up 30 µs vs 160 µs (nCUBE/2), 23 vs 86 µs (CM-5); vendor cost from buffer management (implementation); message-driven processors' poor processing from lack of locality, called inherent, argued (pp. 432–437) | new |
| 7 | P21 | Messages under 16 KB 15x faster through on-die buffers than DDR3; NAS LU and BT "effectively linear" to 32 and 36 cores, no external baseline; send cost in cycles not given (pp. 175–180) | new |
| 8 | P8 | URPC 450 vs L4 424 cycles; unmap at 32 cores ≈18k vs ≈29k (Linux) vs ≈45k (Windows) cycles; web server 18,697 vs 8,924 requests/s; causes by designers, implementation or design, not isolated (pp. 10, 13, 15–16) | new |
| 9 | P15 | No measurement; third-party causes for Lisp machines: the Dolphin "a slow machine that ran the Interlisp virtual machine", the 3600 collector's bad performance "possibly due to paging" (implementation, inferred) (pp. 24, 27) | new |
| 10 | P12 | Delivery plus dispatch "< 2 µs" vs 5 ms (iPSC-1) or 300 µs (iPSC-2), configurations not given; 3–4x area and 2–3x speed lost to standard cells (implementation, designers) (pp. 2, 10–11, 16) | new |
| 11 | P64 | Design figures: "< 3µs" vs 5 ms on an iPSC; 4-word send in 4 cycles; causes inherent, not isolated (pp. 2–3, 5–6, 8–9) | covered by P12 |
| 12 | P69 | Simulated: under ten cycles per message vs about 300 µs on 1980s multicomputers, attributed to the design (pp. 190, 195–196) | covered by P12 |
| 13 | P70 | Simulated: a call ~100 instructions (81–162); OS overhead ~70% of active time (implementation); only baseline a dataflow system on the same machine; network limit at 343 nodes analytically (pp. 50, 104–110, 113–114) | new |
| 14 | P48 | One-way IPC across eleven kernel–processor pairs 1993–2013, seL4 188 cycles on ARM11; in-register transfer 10% / 4% faster; ports cost 12% over thread IDs; causes: context-switch hardware, ABI, compilers (pp. 135, 137–138, 146) | new |
| 15 | P53 | KeyKOS vs Mach 2.5 ratios (getpid 0.4 … disk 6.5); one send under 500 cycles; causes by designers: domain-per-inode (implementation, "we were mistaken"), I/O design (inherent) (pp. 7, 13–16) | new |
| 16 | P77 | EROS vs Linux 2.2.5 on the same Pentium II, favourable on 6 of 7; round-trip IPC 2.38–3.21 µs; causes by designers, one isolated (node-tree traversal 3.67 vs 5.10 µs) (pp. 171, 180–183) | new |
| 17 | P45 | Local send ~10 µs, remote 22–128 µs; +28% and +39% against other Helios set-ups, not another OS; causes copying (inherent) and a dispatcher lock (implementation) (pp. 9–11) | new |
| 18 | P49 | User-mode drivers lose "less than 10 percent" against in-kernel ones (designers); microkernel slightly slower by design; Minix 3 "has not been optimized"; no send cost (pp. 47, 49–50) | new |
| 19 | P66 | Simulated remote read 138 vs local 3 cycles, write 74 vs 2; one-hop delivery 5 cycles; cause: page-table search and reply decode, called implementation (pp. 8–9) | new |
| 20 | P72 | 432 CALL from 300 µs to under 100 µs between versions; third party attributes it to context preallocation and stack storage (implementation); no Send cost (pp. 185–186) | new |
| 21 | P73 | Designers: execution time often set by paging; generic instructions make speed data-dependent; call cost tied to the architecture (pp. 484–485) | new |
| 22 | P102 | No fos measurement; cites 15–45 cycles per core-to-core message on Raw and Tilera; measured on Linux 2.6.24.7 that lock contention dominates the page allocator (pp. 3–4, 8–9) | new |
| 23 | P261 | SOAR 2.5x a 68010 and about the Dorado's speed, causes windows, tags, in-line caches, all cited from Ungar's dissertation (pp. 1, 3, 6, 8, 10) | covered by P11 |
| 24 | P280 | Third-party causes for language-directed machines: B6700 and MU5 slow on FORTRAN; direct execution redoes binding each time; on SYMBOL more hardware did not mean proportionally faster (pp. 98, 100, 102) | new |

## Status
open: 24 read; 21 added a new finding; the last paper (P280) added one, so the run is 0 and the rule needs 5. Eleven papers named in the reading order are unread.

## To read next
All rows *(inferred from screening)*: `sls/2-search/R0.md` has no *Serves* column.

**A. Named in the reading order, still unread:**
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P172 | L4 IPC performance (kernel, designer) |
| 2 | P209 | Argument that IPC cost is becoming irrelevant |
| 3 | P202 | Cache effects of microkernel structure: names SQ5 |
| 4 | P218 | Measurements of message-based OSs: names SQ5 |
| 5 | P243 | Performance of an OS of communicating processes: names SQ5 |
| 6 | P88 | PEACE kernel on MANNA, with performance figures |
| 7 | P104 | The SCC from the programmer's view |
| 8 | P159 | Hardware IPC support (XPC) |
| 9 | P221 | SkyBridge fast IPC |
| 10 | P1 | Myers's book: 432 and SWARD with reasons for their performance |
| 11 | P76 | Book on high-level-language architecture |

**B. Other kernel and processor papers whose screening names IPC cost, speed or efficiency** (read only while SQ5 stays open): P41 (microkernel IPC vs MPI), P43 (evaluation of Guide on Mach IPC), P52 (IPC problems of multiserver systems), P149 (efficient microkernel IPC), P152 (measured message coprocessor), P158 (IPC with hardware watchpoints), P164 (fast IPC algorithm), P171 (IPC bypassing privileged software), P177 (reducing the IPC penalty), P201 (efficiency of microkernel RTOSs), P215 (intertask messaging efficiency), P217 (fast component interaction), P223 (zero-copy communication cost), P226 (stub-code cost), P231 (RHODOS IPC performance), P235 (seL4 fast path speed), P236 (user-level servers at kernel-level performance) (17 papers).

Total to read next: 28 (A 11, B 17). P13 has a record from its abstract; its full text is still needed (university library) for it to count.

## Deferred
none: SQ5 is open.

## Audit
not saturated yet.
