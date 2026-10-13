# Glossary

Plain meanings of the words the workflow uses. Skills give the meaning of a term the first time it appears in a session (`ai/gate.md`, *Talking to me*). Each entry: the term, its ID letter if it has one, and one or two sentences a newcomer can follow.

## The workflow
| Term | Meaning |
|---|---|
| Gate | A checkpoint where the AI stops and I decide: accept what it made, change it, or reject it. Nothing moves on without my decision. |
| Decision file | A short note written at each gate: what I decided about one file, what I changed and why. Kept in `research/ai-log/decisions/`. |
| AI log | The automatic record of everything the AI did in each session. It travels with the thesis, so the use of AI is open to inspection. |
| Status | The label on every file: *provisional* (my first draft, not yet confirmed), *proposed* (made by the AI, waiting for me), *accepted*, *changed* (accepted with my edits), *rejected*, *retired* (replaced, kept for the record). |
| ID | A short code naming one item, such as P12 for a paper or SQ3 for a review question. IDs are never reused or renumbered, so every reference stays valid. |
| Step 0 | What I bring before any AI work: the observation, problem, objective, artifact or solution that starts the thesis. Frozen once the review begins, as a record of where the work started. |
| Entry point | Where the thesis got its first push: a problem noticed, a goal given, an artifact to build on, a client to work with, or a solution seen working in practice (`ai/entry-points.md`). Every thesis still goes through all the steps; the entry point decides which one starts from what I bring. |
| Profile | The settings for a field of study: where its papers are found, what kind of thing gets built, how it is tested (`ai/profiles/`). |
| Agent | An AI helper with one job (reader, skeptic, examiner…). Agents propose; I decide. |
| Skeptic | The agent that argues against a claim and looks for evidence that it is wrong, so weaknesses surface before the defence. |

## Literature study (SLS)
| Term | Meaning |
|---|---|
| Systematic literature study | A review of published work done by fixed, written rules, so another person following the same rules would find the same papers. |
| Protocol | The written rules of the review, fixed before searching: the questions, which papers count, how papers are judged, what is taken from each. |
| Review question (SQ) | A question the literature review answers, such as "which tools already do X". Not the question the thesis itself answers. |
| Inclusion criterion (I) / exclusion criterion (X) | A rule saying when a paper counts for the review (I) or when it is left out (X). Each paper in the review has the criterion that let it in. |
| Quality checklist (Q) | Questions asked of every paper to judge how solid it is, such as "does it compare against something". Weak papers stay in but count less. |
| Extraction form | The list of facts taken from every paper, so all papers are read for the same things. |
| Search string | The keywords searched in a database to find the first papers. |
| Start set | The first papers of the review: my seed papers plus the results of the search string. |
| Snowballing | Finding more papers from the ones already in: the papers they cite (*backward*) and the papers that cite them (*forward*). |
| Round | One pass of snowballing over the papers added in the previous pass. |
| Stop rule | Snowballing ends when a round adds no new papers. |
| Reading record (P) | The notes on one paper: its summary, quality, the facts extracted, and the ideas it covers, each with its page. |
| Three passes | Reading in up to three depths: a skim, a careful read, a full reconstruction. Most papers stop at the first or second. |
| Citation check | Checking that every claim taken from a paper really is on the page cited. |
| Concept (C) | An idea several papers talk about. The review is organised by concepts, comparing what each paper says about them. |
| Concept matrix | A table of papers against concepts, showing who covers what. Empty areas hint at the gap. |
| Gap | What no paper covers, or covers only in part. The thesis aims at it. |

## Design science (DSRM)
| Term | Meaning |
|---|---|
| Design science | Research that learns by building something and testing it, rather than only observing. |
| Artifact | What the thesis builds: a method, model, tool, process, system or guideline. |
| Design problem | One sentence: improve this situation by designing this artifact so that it meets these requirements for these people. |
| Research question (RQ) | A question the thesis itself answers. A good one could turn out to be answered "no". |
| Hypothesis (H) | What I expect the answer to a research question to be, before testing it. |
| Stance | Something the thesis deliberately leaves out, and why. |
| Stakeholder | Anyone affected by the problem or by the artifact. |
| Objective (O) | What the artifact must achieve, stated so that two people would agree whether it did. Fixed before any result is seen. |
| Metric | What is measured to check an objective, with its unit. |
| Baseline | What the artifact is compared against, usually the current way of doing it. |
| Validation type | The kind of evidence used to show an objective is met: a measurement, a worked example, a proof, someone else using it… The profile lists the kinds for the field. |
| Design decision (DEC) | One choice in how the artifact is built, with the options considered and the reason for the choice. |
| Layer (L) | One version of the artifact, from cheapest to most complete: first on paper, then a working model, then the real thing. Each is tested before the next. Layer 0, when there is one, is an existing artifact the thesis builds on. |
| Demonstration (D) / run | Showing the artifact working on one concrete case (a *problem instance*). A run is one attempt. It answers "does it work?", not "how well?". |
| Evaluation (E) | Measuring how well the artifact meets an objective, compared with the baseline. |
| Threat to validity (T) | An honest reason the results might be wrong or might not hold elsewhere. |
| Iteration | Going back to redesign, or to rethink an objective, because an evaluation showed it was needed. |
| Outline | My list of claims for one section of the thesis, with their sources. The AI drafts prose from it and may not add claims. |
| Examiner | The agent that plays the thesis committee and asks the questions I will face at the defence. |
| Contribution type | What kind of novelty the thesis claims: a better solution to a known problem, a new solution to a new problem, a known solution moved to a new field, or a routine design. |
