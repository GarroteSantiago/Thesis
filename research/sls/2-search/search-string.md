---
id: search-string
row: 2a
by: snowballer
status: accepted
inputs: [sls/1-protocol/criteria.md, sls/1-protocol/SQ1.md, sls/1-protocol/SQ2.md, sls/1-protocol/SQ3.md, sls/1-protocol/SQ4.md, sls/1-protocol/SQ5.md, sls/1-protocol/SQ6.md, sls/1-protocol/SQ7.md, sls/1-protocol/SQ8.md, sls/1-protocol/SQ9.md, sls/1-protocol/SQ10.md, sls/1-protocol/SQ11.md, sls/1-protocol/SQ12.md, sls/1-protocol/SQ13.md, sls/1-protocol/SQ14.md, sls/1-protocol/SQ15.md, sls/1-protocol/SQ16.md, sls/1-protocol/SQ17.md, sls/1-protocol/SQ18.md, sls/1-protocol/SQ19.md, 0-start/seeds.md]
---
# Search string

The string is the OR of 19 blocks. Each block targets one inclusion criterion and the SQs it serves, so the start set covers the counter-evidence questions SQ8 to SQ19 and not only message-based machines. Each block was run on its own, because one combined query is too long for the API and would rank the counter-evidence blocks below the large hardware blocks.

## String
```
B1   ("message-driven processor" OR "message-driven architecture" OR "message-passing processor" OR "message passing processor" OR "message-passing architecture" OR "message passing architecture" OR "message-passing hardware" OR "hardware message passing" OR "hardware support for message passing" OR "message passing instructions" OR "actor processor" OR "actor architecture" OR "actor machine" OR "active messages" OR "object-oriented multiprocessor")
OR
B1k  (microkernel OR multikernel OR "message-based operating system" OR "message-passing operating system" OR "object-oriented operating system" OR "actor operating system") AND ("message passing" OR "message-passing" OR IPC OR "inter-process communication" OR "interprocess communication" OR messages)
OR
B1a  ("actor model" OR "actor-based" OR "actor language" OR "actor languages") AND (hardware OR processor OR "instruction set" OR microarchitecture OR FPGA OR "operating system" OR kernel) AND (message OR messages OR concurrent OR concurrency)
OR
B1s  (Smalltalk OR "object-oriented") AND (processor OR microcode OR microcoded OR "instruction set" OR "hardware support" OR "computer architecture") AND (hardware OR performance OR evaluation)
OR
B1m  ("J-Machine" OR "M-Machine" OR "message-driven" OR "Cosmic Cube" OR "fine-grain concurrent") AND (multicomputer OR processor OR node OR mechanisms)
OR
B2   ("object-oriented architecture" OR "object-based architecture" OR "object-oriented processor" OR "object-oriented computer" OR "capability-based architecture" OR "capability architecture" OR "language-directed architecture" OR "high-level language architecture" OR "high-level language computer" OR ("semantic gap" AND ("computer architecture" OR "instruction set")) OR "Smalltalk processor" OR "Lisp machine" OR "iAPX 432" OR "Intel 432")
OR
B3   ("concurrency bug" OR "concurrency bugs" OR "concurrency defects" OR "concurrency errors" OR "blocking bugs" OR deadlock) AND ("message passing" OR "message-passing" OR actor OR actors OR channel OR channels OR "shared memory") AND ("empirical study" OR "empirical analysis" OR "real-world" OR "bug study" OR characteristics)
OR
B4   ("reduced instruction set" OR RISC OR "complex instruction set" OR CISC) AND ("semantic gap" OR "high-level language" OR "high level language")
OR
B5   (duality OR dual OR equivalence) AND ("message passing" OR "message-oriented" OR "message-based") AND ("shared memory" OR "procedure-oriented" OR "operating system")
OR
B6   (actor OR actors OR "message passing" OR "message-passing") AND ("shared state" OR "shared memory" OR locks OR "mixing concurrency" OR benchmark OR "runtime performance" OR scalability) AND (Akka OR Scala OR Erlang OR "actor runtime" OR "actor model" OR Savina OR Go)
OR
B7   ("many-core" OR manycore OR "single-chip cloud computer" OR transputer OR "on-chip network") AND ("non-coherent" OR "without cache coherence" OR "no cache coherence" OR "message passing" OR "message-passing" OR channels)
OR
B8   ("cache coherence" OR "shared memory" OR "operating system") AND (scalability OR scaling OR "scale to") AND ("many-core" OR manycore OR multicore OR "dark silicon")
OR
B9   ("impossibility of distributed consensus" OR "logically centralized" OR "centralized scheduler" OR "decentralized scheduler" OR "distributed scheduler" OR "centralized coordination" OR "decentralized coordination") AND ("operating system" OR cluster OR "software-defined networking" OR consensus OR scheduling)
OR
B10  (reflection OR reflective OR metacircular OR "meta-circular" OR "self-hosting" OR "written in itself") AND ("virtual machine" OR interpreter OR "reflective tower" OR Smalltalk OR Lisp)
OR
B11  (virtualizable OR "trap-and-emulate" OR "system call interposition" OR "virtual machine monitor" OR IOMMU OR "interposition agents") AND (requirements OR overhead OR performance OR coverage)
OR
B12  ("capability hardware" OR "capability-based" OR "capability architecture" OR CHERI OR "object addressing" OR "tagged architecture" OR "iAPX 432") AND (performance OR overhead OR cost OR evaluation)
OR
B13  ("domain-specific architecture" OR "domain-specific architectures" OR "domain-specific accelerator" OR "hardware specialization" OR "specialized architecture" OR "Dennard scaling" OR "dark silicon" OR "end of Moore") AND (adoption OR programmability OR ecosystem OR "software compatibility" OR economics OR "general-purpose")
OR
B14  ("programming language" OR "programming model" OR "execution model" OR "machine model") AND ("code quality" OR defects OR "program correctness" OR "how programmers") AND ("empirical study" OR "controlled experiment" OR "large-scale study")
OR
B15  (interposition OR proxy OR transparent OR "capability invocation") AND (microkernel OR "message passing" OR "message-based")
```

Field searched: title and abstract (OpenAlex `title_and_abstract.search`, which stems words). No date restriction, as `criteria.md` sets none.

## Blocks and the questions they serve
| Block | Serves | Criterion |
|---|---|---|
| B1 | SQ1–SQ5: message mechanisms in processors and hardware | I1(a)(b) |
| B1k | SQ1–SQ4: message-passing kernels | I1(c) |
| B1a | SQ1–SQ5: actor hardware and actor operating systems | I1 |
| B1s | SQ1, SQ5, SQ6: Smalltalk and object-oriented processors | I1, I2 |
| B1m | SQ1, SQ5, SQ13: message-driven multicomputer nodes (system names from `seeds.md` and SQ13) | I1 |
| B2 | SQ1, SQ2, SQ5, SQ6, SQ18: object-based and language-directed architectures | I1, I2 |
| B3 | SQ7, SQ11: empirical concurrency-defect studies | I3 |
| B4 | SQ9: reduced instruction sets versus high-level-language support | I4 |
| B5 | SQ10: duality of message passing and shared memory | I4 |
| B6 | SQ11, SQ12: actor runtimes, mixing models, costs | I4 |
| B7 | SQ13: many-cores without coherence | I1, I4 |
| B8 | SQ14: coherence and kernel scaling to many cores | I4 |
| B9 | SQ15: agreement and central versus decentralised coordination | I4 |
| B10 | SQ16: reflection and self-definition | I4 |
| B11 | SQ17: virtualisation and system-call interposition | I4 |
| B12 | SQ18: cost of capability and object hardware | I4 |
| B13 | SQ19: specialised architectures after Dennard scaling | I4 |
| B14 | SQ8: does the language or model change defects | I4 |
| B15 | SQ3: putting a component between sender and receiver in message-based systems (added at gate 2b, decision D7 = b) | I1, I4 |

## Iterations
The first versions of four blocks returned too many unrelated works and were narrowed before the final run:
- B1 matched 271,626 works with generic terms (`actor`, `processor`); replaced by the phrase list above (2,689).
- B9 matched 63,207 with `consensus`/`agreement` alone; narrowed to the phrases above (5,444).
- B11 matched 292,772 with `interposition` and `security`; narrowed (885).
- B2 matched image-retrieval papers through "semantic gap"; the phrase now requires "computer architecture" or "instruction set".
- B1a (first version: 248,009, mostly sociology "actor" papers) and B1s (first version: 2,070, mostly pure-language papers) were narrowed as shown.

One exploratory query, `"message-driven processor"` (a sub-phrase of B1, 27 results), was run while testing the API; its three relevant hits are in `R0.md`, marked as such.

## Screening scope
- **Fully screened (gate 2b, decision D2 = c):** every result of B1k (278 counted, 279 returned by paging), B3 (264), B4 (172), B5 (88) and B14 (99). These blocks are small and precise, and they serve the thinnest parts of the start set (kernels, defect studies, SQ9, SQ10, SQ8).
- **First 12 by relevance and first 12 by citations:** all other blocks, B1, B1a, B1s, B1m, B2, B6 to B13, and B15 (766 results, above the 300 limit set at gate 2b for a full screen). Results below rank 12 in these blocks were not screened.
- Records that are the same work (reprints, proceedings and SIGPLAN/SIGARCH copies, report and journal versions, repeated repository deposits) are merged into one row in `R0.md`, with the other records listed.
- Hits from other fields that the stemmed match pulled in (sociology, law, seismology and others) and unrelated computing topics are listed in `R0.md` as X1, so every screened hit has a verdict. Preprints, datasets and software deposits are listed as X5.
- Database: OpenAlex only (gate 2b, decision D3 = a).

## Where and when
| Database | Date run | Results |
|---|---|---|
| OpenAlex, block B1 | 2026-10-06 | 2,689 |
| OpenAlex, block B1k | 2026-10-06 | 278 |
| OpenAlex, block B1a | 2026-10-06 | 414 |
| OpenAlex, block B1s | 2026-10-06 | 8,851 |
| OpenAlex, block B1m | 2026-10-06 | 1,376 |
| OpenAlex, block B2 | 2026-10-06 | 2,294 |
| OpenAlex, block B3 | 2026-10-06 | 264 |
| OpenAlex, block B4 | 2026-10-06 | 172 |
| OpenAlex, block B5 | 2026-10-06 | 88 |
| OpenAlex, block B6 | 2026-10-06 | 4,032 |
| OpenAlex, block B7 | 2026-10-06 | 1,713 |
| OpenAlex, block B8 | 2026-10-06 | 1,349 |
| OpenAlex, block B9 | 2026-10-06 | 5,444 |
| OpenAlex, block B10 | 2026-10-06 | 4,104 |
| OpenAlex, block B11 | 2026-10-06 | 885 |
| OpenAlex, block B12 | 2026-10-06 | 3,772 |
| OpenAlex, block B13 | 2026-10-06 | 984 |
| OpenAlex, block B14 | 2026-10-06 | 99 |
| OpenAlex, block B15 | 2026-10-06 | 766 |
| OpenAlex, exploratory `"message-driven processor"` | 2026-10-06 | 27 |
| Semantic Scholar | 2026-10-06 | Not run: the API returned HTTP 429 (rate limit without an API key) on every attempt; not retried after gate 2b chose OpenAlex only |
| DBLP | 2026-10-06 | Not run: the search API returned a bot-check page instead of results |
