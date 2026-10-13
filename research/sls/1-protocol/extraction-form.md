---
id: extraction-form
row: 1a
by: protocol-critic
status: changed
inputs: [sls/1-protocol/SQ*.md]
---
# Data extraction form

Fields filled for every included paper (`sls/3-reading/P*.md`). Every SQ is served by at least one field.

- **Applies to:** a field applies to papers included under the criteria in its *Applies to* column; for I4, only the fields serving the SQs the paper answers. A field that does not apply is written `n/a (I3)` (the paper's criterion). `not stated` means the field applies but the paper is silent.
- **Values:** every number in *Cost of message primitives*, *Performance results* and *Scaling* is tagged `measured`, `simulated`, `design figure`, `analytical` or `read off` (estimated from a plot).

| Field | What to record | Serves | Applies to |
|---|---|---|---|
| Reference | Authors, year, title, venue, pages; P ID; criteria that included it (I1–I4). Pages cited in the record are those printed on `papers/P*.pdf` (else its PDF page); say which version it is (publisher, preprint, manuscript, reprint), give the publisher's page range and any offset. Content taken from an abstract only cites `abstract` | SQ1–SQ19 | all |
| Paper type | One or more of: design, implementation, evaluation, retrospective, empirical defect study, position or analytical argument; with page | SQ1–SQ19 | all |
| System | Name of each system the paper describes or evaluates, year built, built by whom; status: design only / simulated / FPGA / silicon / running kernel / deployed commercially; with page | SQ1, SQ5, SQ6 | I1, I2, I4 |
| Levels with message semantics | For each level (hardware, microcode, instruction set, kernel, runtime or virtual machine, language): is a message send the primitive at that level, yes / partly / no / not stated (yes means every state change at that level is caused by a message send, with no other path; partly means a message is a primitive at that level but other paths exist, naming which operations are message-only); for kernels and multicomputers, answered separately between cores or nodes and within a core (traps, interrupts, system calls); whether the system started message-based at a level and later added paths that are not messages; with page | SQ1 | I1, I2 |
| Receiving unit and state ownership | What receives messages (object, actor, process, core, domain, other); whether its state can be read or written by anything other than itself, and how; with page | SQ1, SQ2, SQ7 | I1, I2, I3 |
| Message mechanism | Synchronous or asynchronous; how the receiver is named; ordering and delivery guarantees; buffering; what happens when the receiver is busy; how the receiver selects behaviour (dispatch); with page | SQ1, SQ3 | I1, I2, I3 |
| Non-message primitives | Every mechanism the paper states the system keeps that is not a message send: shared or global memory, interrupts, traps, privileged instructions, microcode, global registers, direct memory access, I/O ports, other; at which level; the reason the paper gives for keeping each; with page | SQ2 | I1, I2 |
| Self-definition | Which levels are implemented in the system's own objects and messages, and which in a lower language, microcode or hardware outside the model; whether a running program can inspect or change those levels; what remains outside the system as a base (primitives, a level that is not reflected) and what that base costs or prevents; with page | SQ2, SQ16 | I1, I2, I4 |
| Interposition | Whether a third component can be placed between sender and receiver, or between a program and conventional hardware or kernel (virtual memory, virtualisation, system call interposition, input/output memory management), without changing either (yes / no / not stated); the mechanism; at which level; its cost; with page | SQ3, SQ17 | I1, I2, I4 |
| Operating system functions | For each of protection, scheduling, resource allocation (memory, devices), naming, failure handling: how the system provides it, and whether a central component (a single kernel, master core, global table or lock) is involved, yes / no / not stated (replicated parts that must agree count as coordination); what a decentralised version costs or gives up; with page | SQ4, SQ15 | I1, I4 |
| Cost of message primitives | Measured latency or cycles of one send, one dispatch, one context or actor switch; on what hardware or simulator; with page | SQ5 | I1, I2 |
| Performance results | Each result as: metric, workload, system, baseline (name, version, configuration), value for each, unit; with page | SQ5 | I1, I2, I4 |
| Scaling | Number of cores or nodes measured, metric, result at each count, baseline; with page | SQ5 | I1, I2, I4 |
| Attributed causes | Each cause the authors give for a performance result, quoted or close-paraphrased; who states it (designers or third party); whether it is inherent to the design or due to its implementation; whether a measurement isolates it; with page | SQ5, SQ6, SQ18 | I1, I2, I4 |
| Fate and reasons | What happened to the system (commercial product, research only, abandoned, superseded, still in use) and every reason the paper gives for it; who states it (designers or third party); with page | SQ6 | I1, I2, I4 |
| Concurrency defects | Study population (programs, systems, language), number of defects, defect categories used (every kind, including deadlocks, message-protocol violations and message-order defects), counts or proportions per communication mechanism (shared memory, message passing), and defects the paper claims a design prevents by construction; with page | SQ7 | I3 |
| What shapes programs | What the paper finds determines how programs are designed and how correct they are (hardware model, language, libraries, tools, training), and the kind of evidence; with page | SQ8 | I3, I4 |
| Hardware–language trade-off | Each argued or measured cost or benefit of raising the hardware interface toward the language or specialising it (performance, cost, generality, compiler optimisation), and whether it applies to a message send as the primitive; with page | SQ9 | I2, I4 |
| Model equivalence | Which model is built on which (messages on shared memory or the reverse); which properties (encapsulation, freedom from data races, interposition) and how much performance are kept or lost; with page | SQ10 | I3, I4 |
| Model mixing | Non-message mechanisms used in actor or message programs, how often, and the reasons developers give; with page | SQ11 | I3, I4 |
| Runtime limits | Where actor or message runtimes' costs and scaling limits come from; whether the hardware's shared-memory model is named as the cause, or a software technique removes it; with page | SQ12 | I4 |
| Many-core scaling | Core counts; whether there is shared memory or coherence; how inter-core communication works; the scaling result; the limits named (power, communication, serial fraction); with page | SQ13, SQ14 | I1, I4 |
| Adoption factors | For each specialised architecture: adopted or not, and the factors the paper gives (software compatibility, ecosystem, programmability, economics, kind of workload); with page | SQ6, SQ13, SQ19 | I2, I4 |
| Quality | Answer to each of Q1–Q9 in `quality.md`, with the page that supports it | SQ1–SQ19 | all |
| Notes | Anything relevant to an SQ that no field above captures; with page | SQ1–SQ19 | all |
