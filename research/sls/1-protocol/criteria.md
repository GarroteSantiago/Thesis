---
id: criteria
row: 1a
by: protocol-critic
status: changed
inputs: [0-start/observation.md, 0-start/notes.md, sls/1-protocol/SQ*.md]
---
# Selection criteria

A paper is included if it meets at least one inclusion criterion and no exclusion criterion. Each verdict names the criterion that decided it. There is no restriction on publication date. "Message-based" in these criteria means: meets I1.

Terms used in the criteria and the SQs:
- **Below the programming language:** in the operating system kernel, the instruction set, microcode or hardware; not in a language runtime, library or virtual machine hosted on a conventional kernel (as in X2).
- **Written in its own objects and messages:** the level's code is objects receiving messages in the system's own model, not a lower language, microcode or hardware outside that model.
- **Without changing either:** neither the sender's nor the receiver's code, nor how they name each other, is modified to place the component between them.

| ID | Inclusion criterion |
|---|---|
| I1 | A paper is included if it describes, implements, simulates or evaluates a processor, instruction set, microarchitecture, multicomputer node or operating system kernel in which sending a message, invoking a method on an object, or delivering a message to an actor is a primitive of that level, i.e. one of: (a) an instruction of the instruction set; (b) a hardware or microcode mechanism; (c) for a kernel, the stated means by which the kernel and its system services, or the kernel's own parts, communicate (as in microkernels, multikernels, or operating systems written in an object or actor language that run without an underlying conventional kernel). The paper must name the mechanism with at least one of these terms: message, message passing, send, mailbox, actor, active message, inter-process communication (IPC), method invocation. (SQ1–SQ5) |
| I2 | A paper is included if it is a retrospective, evaluation or historical account of at least one computer architecture that its authors describe as directed at a high-level language, object-based, object-oriented or message-driven, and it reports either measured performance of that architecture or a stated reason for its performance, adoption, abandonment, or becoming unnecessary. (SQ5, SQ6) |
| I3 | A paper is included if it is an empirical study of concurrency defects (bugs) in real programs or systems (not only examples written by the authors) and it reports counts or proportions of defects either split by communication mechanism (shared memory versus message passing) or for programs or systems built on message passing only, or for programs or systems built on shared memory only, as the comparison baseline for SQ7. Programs whose defects are reported as accesses to shared variables count as shared-memory programs even if the paper does not use that term. (SQ7) |
| I4 | A paper is included if it reports evidence or an argument that directly answers one of SQ8–SQ19, whether or not it mentions messages or objects. (SQ8–SQ19) |

| ID | Exclusion criterion |
|---|---|
| X1 | A paper is excluded if it meets none of I1, I2, I3, I4. |
| X2 | A paper included only through I1 is excluded if message passing appears only at the application, library, language runtime, virtual machine or network-protocol level, running on a processor whose instruction set and hardware have no message mechanism and on a kernel that fails I1(c) (e.g. an actor library, the Erlang virtual machine, a Message Passing Interface library, a Smalltalk virtual machine hosted on Unix or Windows). Does not apply to papers that meet I2 or I3. |
| X3 | A paper is excluded if the system is a cluster or network of separate computers, each with a processor whose instruction set and hardware have no message mechanism and a kernel that fails I1(c), and the message mechanism lies only in the network interface or interconnect between them. |
| X4 | A paper is excluded if the hardware it presents is stated to serve only a fixed function or domain (e.g. neural-network inference, signal processing, packet switching, graphics) and is not stated to run general programs. Does not apply to papers included through I4. |
| X5 | A paper is excluded if it is not one of: journal article; conference or workshop paper longer than 2 pages; book or book chapter; doctoral or master's thesis; technical report of a university, company research laboratory or standards body; magazine article of a professional society (Association for Computing Machinery, Institute of Electrical and Electronics Engineers, USENIX); architecture or system reference manual published by the system's manufacturer. Patents, slides, posters, extended abstracts of 2 pages or fewer, blog posts, forum posts, encyclopaedia entries and product brochures are excluded. |
| X6 | A paper is excluded if its full text is in neither English nor Spanish. |
| X7 | A paper is excluded if its full text cannot be obtained from the publisher, an author's or institution's web page, arXiv, Semantic Scholar, the Internet Archive, or the university library. The sources tried are recorded with the verdict. |
| X8 | A paper is excluded if it reports the same system and the same results as another included paper. The one with more pages is kept; the other is excluded unless it reports at least one measurement, design element or stated reason absent from the kept one. |
| X9 | A paper is excluded if its title or abstract presents it as a survey, review, overview or taxonomy of other work and it reports no measurement and states no reason under I2 of its own. Its reference list is still used for snowballing. |
