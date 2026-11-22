---
id: SQ3.coverage
row: 4a
by: synthesizer
status: proposed
inputs: [sls/1-protocol/SQ3.md, sls/1-protocol/step.md, sls/3-reading/step.md, sls/3-reading/P12.md, sls/3-reading/P45.md, sls/3-reading/P46.md, sls/3-reading/P48.md, sls/3-reading/P49.md, sls/3-reading/P53.md, sls/3-reading/P70.md, sls/3-reading/P73.md, sls/3-reading/P77.md, sls/2-search/R0.md]
---
# Coverage of SQ3

Saved as `sls/4-synthesis/SQ3.coverage.md`. Which papers serve this question, what each added, and whether the question has what it needs (`research/sls/4-synthesis/step.md`).

## Rule
- **Kind:** kinds.
- **Unit:** a kind of interposition mechanism below the language (e.g. a transparent monitor on the IPC path, a recorder that receives every message, a port or capability that can be redirected to a proxy), with its reported cost. A mechanism already recorded counts as new again if a different cost or limit is reported.
- **Enough when:** at least 10 papers serving it are read, in the reading order, then 3 in a row add nothing new (10 + 3).

## Read
In the reading order of SQ3.md (capability kernels, synchronous-IPC kernels, multiserver systems, processors; then papers it does not name).
| # | Paper | Contributes | New? |
|---|---|---|---|
| 1 | P53 | An intervening domain on a key's path buffers messages transparently; keepers receive the exceptions of unmodified BSD binaries; cost: queue domains impose "considerable context switch overhead" (pipe 0.56 of Mach 2.5), and routing every trap to the keeper "severely penalizes all trivial system calls" (pp. 7, 9–10, 12, 14, 16) | new |
| 2 | P77 | A filter process or the kernel's indirector "can be transparently interposed in front of most objects" because all capabilities take the same arguments; cost 1.6 µs per trivial invocation against 0.7 µs for Linux getppid (pp. 174, 180) | new (same kind as P53, different cost) |
| 3 | P46 | Candidate only: stacked pagers and communication servers built on IPC and mapping; the paper does not say sender or receiver stay unchanged and gives no cost (p. 76) | nothing new |
| 4 | P48 | Kernel redirection of messages crossing a clan boundary to its chief: two cycles per IPC claimed for direct messages, but two extra messages per redirected round trip, "a significant overhead"; abandoned; general IPC redirection "failed to gain traction" (p. 139) | new |
| 5 | P49 | Serves only by its criterion: no component between sender and receiver is described for Minix 3 or Singularity; per-process send bitmaps filter, they do not interpose (p. 48) | nothing new |
| 6 | P12 | Serves only by its criterion: after a translation miss the kernel moves or copies the object, keeping its location transparent; no interposition, no cost (pp. 7, 21) | nothing new |
| 7 | P45 | Shadow endpoints inserted by the system on every remote channel, keeping the channel interface so "no changes are required" to applications; placement changed by editing a manifest; cost: remote against local message latency (pp. 2, 6–7, 10) | new |
| 8 | P70 | Serves only by its criterion: the kernel routes a message to a distributed object's group name to "a constituent of its choosing" and forwards messages for migrated objects; no cost isolated (pp. 20, 70, 79) | nothing new (the record finds no interposition mechanism) |
| 9 | P73 | At the language-machine level: encapsulations (trace, advise) wrap a function and survive its redefinition, methods can be wrapped, and invisible pointers forward references; cost not stated (pp. 153, 175, 309) | new |

## Status
open: 9 read, fewer than 10; 5 added a new mechanism or cost. The three papers the reading order puts first (P203, P278, P183) are unread.

## To read next
All rows *(inferred from screening)*: linked by their I1 criterion and their reason in `sls/2-search/R0.md` (no *Serves* column), as SQ3.md lists them.
| # | Paper | Why next (inferred from screening) |
|---|---|---|
| 1 | P203 | Transparent monitors between source and destination on synchronous IPC: named first |
| 2 | P278 | Publishing: a recorder that transparently stores all messages |
| 3 | P183 | Adaptive monitoring between components of microkernel OSs |
| 4 | P43 | Port-based kernel (Guide on Mach 3.0) |
| 5 | P200 | Chorus: port-based kernel |
| 6 | P199 | Mach ports in macOS: port-based kernel, a later decade |
| 7 | P51 | Spring's doors |
| 8 | P52 | SawMill multiserver system |

## Deferred
none: SQ3.md links no other included paper to this question.

## Audit
not saturated yet.
