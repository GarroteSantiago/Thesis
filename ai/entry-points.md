# Entry points

Peffers et al. define four entry points [1]: where design science research can start, depending on where the first push came from. In all four, every activity is carried out and the thesis presents them in the nominal order, problem to communication. Peffers shows this with one published project per entry point, each written up in that order [1] (*Peffers' examples*, below). What the entry point changes is what I bring at step 0 and which activity starts from it instead of from a blank page. The `thesis` skill asks which one applies before step 0 is written, using *Choosing one* below; from then on, the step 0 file that exists fixes it.

## Choosing one
Ask me these questions in order, with decision cards (`ai/gate.md`). The first *yes* decides. Say what each answer implies, from *What it means for the thesis* below, and give the matching example from *Peffers' examples*.

1. **Is there a client or an organisation where an artifact, or a method still being developed, can be put to work?** A company or institution that asked for help, and the thesis would develop the artifact in that setting and demonstrate it there. → **Context-initiated, client engagement.**
2. **Is there already something in use, seen to work, that nobody has studied with rigour?** A tool, method, programme or practice that someone (me, a company, an organisation) already uses, and the thesis would explain and evaluate it after the fact. → **Context-initiated, retroactive.**
3. **Is there already an artifact to build on, not yet thought through for this problem?** A standard, a tool, a technique from another field, a prototype, and the thesis would extend or adapt it to a new use. → **Design-centred.**
4. **Is it already clear what a solution must achieve?** A need stated by a company, a field or my own research: "a way to measure X", "usable without training", "cheaper than the current way", and the thesis designs the artifact that achieves it. → **Objective-centred.**
5. **Otherwise:** the thesis starts from something I noticed that seems wrong, missing or inconsistent. → **Problem-centred.** The most common start for a thesis.

If two seem to fit, choose by where the first push came from: a problem noticed, a goal given, a thing to build on, a client, or a thing seen working. When in doubt, problem-centred is the safest: every activity is built from the literature.

## What it means for the thesis
| Entry point [1] | Step 0: what I bring | What it means |
|---|---|---|
| Problem-centred | `observation.md`: what I noticed, and how | Every activity starts from the literature and the observation. The thesis argues the problem is real before solving it. |
| Objective-centred | `objectives.md`: what a solution must achieve, and who needs it | The review tests whether my objectives are reasonable and what already meets them. The problem is written to explain why they matter; DSRM 2 then starts from my draft objectives, revised in the light of the review. |
| Design-centred | `artifact.md`: the artifact I build on, and the new use I see for it | The review looks for the problem in the new use and for rival artifacts. The existing artifact is recorded as layer 0: the foundation the thesis builds on, and usually the baseline it is compared against. The thesis's own artifact is what is built on top of it. The risk to manage: a problem tailored to fit the artifact; the skeptic checks for it. |
| Context-initiated, client engagement | `context.md`: the client, their need, the setting, and the artifact or method I bring | The artifact is developed for the client's setting and demonstrated there, with the client's people. The risk to manage: one client is one case; the evaluation says how far the results carry beyond it. |
| Context-initiated, retroactive | `solution.md`: the solution seen working, where, and the evidence | Rigour is applied after the fact [1]: the review explains why it works and what else exists, the objectives are written knowing the results, the solution is described as layer 1, its design decisions reconstructed, and its observed uses recorded as the demonstrations. The risk to manage: objectives fitted to known results. Each objective says it is retroactive, the skeptic attacks it, and it is a threat to validity in the evaluation. |

Every entry point can also bring `seeds.md` (papers I already know) and `notes.md` (what I already think), both optional (`kickstart.md`).

## Peffers' examples
Peffers et al. illustrate each entry point with a published project, each one written up with all six activities in order [1]:

| Entry point | Example [1] | The first push | Where step 0 seeds the work |
|---|---|---|---|
| Problem-centred | A data warehouse for community health assessments | Gathering the data by hand was too slow and costly for most communities | DSRM 1, the problem |
| Objective-centred | A software reuse measure | Researchers needed to measure reuse rates for a case study, and no existing measure fit | DSRM 2: the objective, a usable reuse measure, existed before the problem was written |
| Design-centred | A video calling client for university networks | An existing voice calling standard, to be extended to video | DSRM 3: the design built on the existing standard |
| Context-initiated | An IT planning method at a software company | A company asked for help, and the project became "a proposed demonstration of the new methodology" | DSRM 4: the client's setting, where the method was demonstrated |

The fourth example is a client engagement. The definition also covers the retroactive case: "observing a practical solution that worked … if researchers work backwards to apply rigor to the process retroactively. This could be the by-product of a consulting experience" [1].

## Routes
Every route runs the same order after step 0: SLS 1–5 → DSRM 1 → 2 → 3–5 loop → 6. The entry activity starts from step 0 instead of from blank. The SLS after step 0 is this workflow's rule, not Peffers' (*My rules*, below).

### What changes in each activity
| Activity | Problem-centred | Objective-centred | Design-centred | Context, client engagement | Context, retroactive |
|---|---|---|---|---|---|
| SLS 1, row 1a | SQs from the observation | SQs also test the draft objectives: is each one reasonable, does something already meet it? | SQs also look for the problem in the new use and for rival artifacts | SQs also look at the client's problem in the literature and at rival methods | SQs also look for why the solution works and for rival solutions |
| DSRM 1, rows 6a–6b | From the observation and the gap | From the draft objectives and the gap: why they matter | From the artifact, its new use and the gap | From the client's need and the gap | From the solution, its evidence and the gap |
| DSRM 2, row 7a | I write the objectives | **Starts from step 0:** I revise my draft objectives, each shown with what the review found about it | I write the objectives; the existing artifact is offered as a baseline | I write the objectives, with the client's need | I write the objectives, each marked *retroactive* in its *Kind* |
| DSRM 3 | Decide and build | Decide and build | **Starts from step 0:** first `describe` the existing artifact as layer 0, the foundation; then decide and build on it | Decide and build, for the client's setting | First `describe` the solution as layer 1, its design decisions reconstructed; later passes only if the evaluation calls for them |
| DSRM 4 | Plan and run | Plan and run | Plan and run | **Starts from step 0:** plan and run in the client's setting, with the client's people | First `record` each observed use as a demonstration and its run, from `0-start/solution.md`; no new runs unless I ask |
| DSRM 5 | As written | As written | As written; the layer 0 baseline shows what the thesis added | As written; a threat states how far one client's results carry | Every retroactive objective gets a threat: written knowing the results |

## My rules for all entry points (not part of Peffers)
- Step 0 is always my input in `0-start/`, frozen before the SLS starts (`kickstart.md`). What it holds depends on the entry point.
- The SLS always runs right after step 0, because DSRM 1–3 need it (`research/README.md`).
- The kickstart safeguards apply whatever the entry point.

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
