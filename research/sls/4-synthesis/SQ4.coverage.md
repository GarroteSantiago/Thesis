---
id: SQ4.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ4.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P8.md, sls/3-reading/P12.md, sls/3-reading/P15.md, sls/3-reading/P33.md, sls/3-reading/P45.md, sls/3-reading/P46.md, sls/3-reading/P48.md, sls/3-reading/P49.md, sls/3-reading/P53.md, sls/3-reading/P64.md, sls/3-reading/P65.md, sls/3-reading/P66.md, sls/3-reading/P69.md, sls/3-reading/P70.md, sls/3-reading/P77.md, sls/3-reading/P102.md, sls/2-search/R0.md]
---
# Coverage of SQ4

Saved as `sls/4-synthesis/SQ4.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** evidence.
- **Unit:** a finding: how one of the four functions (protection, scheduling, resource allocation, naming) is provided in a system of message-passing parts that share no state, whether it relies on a central coordinator or on replicated parts that must agree, or what it costs.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 5 in a row add nothing new (10 + 5).

## Read
In the reading order of SQ4.md (named papers first), then the papers it does not name, machines and kernels alternating.
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P8 | Protection per core plus seL4-style capabilities kept consistent on all cores; memory by unmap (one-phase) and retype (two-phase) commit among monitors; local scheduling; a name service; two-phase commit ≈14k–28k cycles over 2–32 cores (pp. 8–11, 14) | new |
| 2 | P53 | Naming "intrinsically decentralized" by capabilities; protection by keys only the kernel creates; scheduling through meters from one prime meter; allocation through space banks under a master bank; no costs (pp. 3–6) | new |
| 3 | P77 | Protection by capabilities plus a user-level reference monitor that interposes forwarding objects between compartments; storage by one space bank that "owns all system storage" (pp. 172–174, 179); processes may share an address space | new (the reference monitor; the central bank is P53's) |
| 4 | P102 | All four functions as server fleets: a name-server directory cached per microkernel, a privilege fleet invalidated by message, scheduling as layout, memory by a fleet; costs argued only (pp. 5–8) | new |
| 5 | P70 | Per-node protection; per-node hardware scheduling, load management "yet to be adequately addressed"; distributed-object allocation serialised at one node; home-node naming a "fanout bottleneck"; no costs measured (pp. 5, 57–58, 63–64, 68, 73, 100, 119–120, 176) | new |
| 6 | P45 | Protection by software isolation per kernel; one scheduler per kernel with placement at process start; memory per kernel; naming "the only component of Helios that relies on centralized control", costing two remote channels per local connection setup (pp. 4–6, 8) | new |
| 7 | P12 | Per-node protection and hardware dispatch, load balancing an "open question", per-node translation with a global namespace from the kernel; message buffers "automatically allocated on the receiving node" (pp. 2–3, 5–7, 9, 15, 18, 20) | new (buffer allocation by hardware) |
| 8 | P64 | Per-node segmented protection, hardware dispatch that "removes the overhead associated with a software scheduler", per-node translation, automatic receive buffers (pp. 1, 7, 9, 12) | covered by P12 and P70 |
| 9 | P65 | Hardware queue as the "one primitive mechanism for low-level task scheduling"; translation tables "inadequate" for a global name space; no protection mechanism, a TLB pair proposed (pp. 2, 10–11) | new (designers' own verdict on naming; absence of protection) |
| 10 | P69 | Per-node base/limit and type checks, but READ and WRITE messages from any sender reach physical memory; two-level hardware scheduling; global object identifiers (pp. 189–194) | new (a protection gap) |
| 11 | P66 | Protection by restricting sends to the program's own address space through the GTLB, restricted DIPs and guarded pointers; naming by a software table cached in the GTLB; buffer reservation per send with return-to-sender (pp. 3, 7) | new |
| 12 | P46 | Protection by one address space per server and driver, with a small trusted base; memory by recursive address spaces with coexisting memory servers that must "cooperate"; drivers at user level; basic scheduling in the kernel (pp. 70–72, 75–76) | new |
| 13 | P48 | Protection by capabilities on endpoints and kernel objects; a central in-kernel scheduler, per-core queues on early x86 against a global one on embedded multicores; allocation through Untyped memory and retype; naming moved from global thread IDs to capability-named endpoints (pp. 137–143); components may share memory | new |
| 14 | P49 | Minix 3: MMU address spaces plus per-process IPC bitmaps; scheduling in the microkernel; one data-store name server; a process manager. Singularity: one root name server; protection by language safety (pp. 47–50) | new (IPC bitmaps; central servers otherwise covered by P45) |
| 15 | P33 | On distributed-memory multicomputers: kernel checks of destination and length on each send; "primitive" run-to-completion scheduling; pre-allocated resources; naming not addressed (pp. 433–435, 438) | new |
| 16 | P15 | Argument only, quoted from Hewitt and Smith: actor transmission is "an inter-domain call efficiently providing an intrinsic protection on actor machines"; no system or cost (p. 62). Its limit matters: it is a claim, not evidence | new (as an argument) |

## Status
open: 16 read; 15 added a new finding; the last 5 (P66, P46, P48, P49, P33, P15 in order) all added something, so the run is 0 and the rule needs 5. Twelve papers named in the reading order are unread, among them the four whose screening names this question (P167, P194, P230, P240).

## To read next
All rows *(inferred from screening)*: `sls/2-search/R0.md` has no *Serves* column.

**A. Named in the reading order, still unread:**
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P167 | Load distribution on microkernels: resource allocation, names SQ4 |
| 2 | P194 | Load distribution on Mach: names SQ4 |
| 3 | P238 | Naming: object identification in the Lego message-based kernel |
| 4 | P240 | RHODOS process migration: names SQ4 |
| 5 | P230 | Distributed process management on multicores: names SQ4 |
| 6 | P39 | NLTSS: message-based OS of the 1980s |
| 7 | P153 | SHOSHIN message-based OS |
| 8 | P211 | Popcorn Linux: inter-core messaging in a multikernel |
| 9 | P225 | Replicated-kernel Linux with a single system image |
| 10 | P175 | PIKA: network stack for multikernels without cache coherence |
| 11 | P191 | StarfishOS: state-partitioned microkernel |
| 12 | P50 | Determinator: shared-nothing spaces |

**B. Other multikernel, capability-kernel and distributed message-based OS papers** (SQ4.md counts these among its serving papers without naming them; read only while SQ4 stays open): P34 (distributed message-passing OSs), P35 (message-passing OS structures), P36 (RHODOS microkernel), P150 (message-based OS for parallel programming), P169 (hotplug in a multikernel), P173 (virtualisation over a multikernel), P174 (MySyS multikernel), P222 (MyThOS many-core OS), P224 (Barrelfish on the SCC), P241 (multi-kernel embedded OS), P252 (OS kernels on multi-core) (11 papers).

Total to read next: 23 (A 12, B 11).

## Deferred
none: SQ4 is open.

## Audit
not saturated yet.
