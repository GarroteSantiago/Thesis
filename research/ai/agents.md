# Agents

Workers called by the step skills (`skills.md`). Each one proposes; I decide at the gate.

| Agent | Used in | Does |
|---|---|---|
| `protocol-critic` | SLS 1 | Drafts the protocol from step 0; checks that SQs are answerable, criteria can be applied without ambiguity, and the form covers every SQ |
| `snowballer` | SLS 2 | Proposes the search string and start set; fetches backward and forward candidates; pre-screens each against I/X |
| `reader` | SLS 3 | Drafts the record for each paper: five Cs, Q scores, extraction fields, concepts, with pages |
| `synthesizer` | SLS 4, SLS 5, DSRM 1 | Proposes concepts; drafts SQ answers and gap; drafts the problem in DSRM 1 from the observation and the gap |
| `designer` | DSRM 3 | For each open decision: options, trade-offs against objectives and prior art; critiques my proposals |
| `builder` | DSRM 3 | Produces the current layer in its form (below) |
| `demonstrator` | DSRM 4 | Proposes demonstrations; writes problem instances; runs or traces them |
| `evaluator` | DSRM 5 | Measures against baselines; drafts evaluations and threats to validity |
| `drafter` | DSRM 6 | Turns my outline and claims into section prose |
| `examiner` | DSRM 6 | Plays the committee: asks the questions I will face at the defense |
| `skeptic` | Any step | Looks for counter-evidence and attacks claims, gaps, objectives and results |
| `citation-checker` | Any step | Checks that each cited claim appears in the source at the cited page |

## Builder output per layer
Layers from `dsrm/3-design/step.md`. The layer itself lives outside `research/`, in `artifact/L<n>/`; `dsrm/3-design/L<n>.md` describes it.

| Layer | Form | Check |
|---|---|---|
| 1. Paper design | Spec document: instruction set, message format, actor lifecycle, diagrams | Consistency review, worked traces by hand |
| 2. Executable model / simulator | Code and tests | Test suite, actor programs run end to end |
| 3. Formal specification | TLA+ / Alloy / Coq model | Model checker or proof |
| 4. Hardware prototype | HDL (Verilog / VHDL / Chisel), FPGA build | HDL simulation, synthesis reports, board runs |

Besides the layers themselves, the builder also produces benchmark programs, the toolchain (assembler, language front end) and figures.
