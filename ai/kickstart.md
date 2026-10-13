# Kickstart

The pipeline starts from step 0: what I bring before any AI work. It lives in `research/0-start/`, apart from the method steps, because it is my input, not the output of any step.

## In plain words
Before the AI does anything, I write down where the thesis starts: the problem I noticed, the goal I was given, the thing already built, or the solution I saw working. Optionally, the papers I already know and what I already think. The AI does not write any of it. Once the review begins it is frozen, as an honest record of where the work started: what I thought before reading.

## Step 0
One required file, depending on the entry point (`entry-points.md`), and two optional ones.

| File | Entry point | Required | Holds |
|---|---|---|---|
| `observation.md` | Problem-centred | yes | The problem I noticed, in one of the shapes below |
| `objectives.md` | Objective-centred | yes | My draft objectives: what a better solution must achieve, and who needs it |
| `artifact.md` | Design-centred | yes | The artifact I build on, and the new use I see for it |
| `context.md` | Context-initiated, client engagement | yes | The client, their need, the setting, and what I bring |
| `solution.md` | Context-initiated, retroactive | yes | The solution seen working, where, and the evidence |
| `seeds.md` | any | no | References I already know. Seeds for the start set (row 2a), not results. |
| `notes.md` | any | no | Anything I already think about the problem, as I wrote it. Input for DSRM 1, not a commitment. |

Exactly one of the required files exists; which one fixes the entry point.

## Shapes of an observation
A problem-centred thesis starts from an observation. It can take one of these shapes. At step 0, a shape that rests on the literature (application, neglect, confusion, problematization) is a hunch: the review confirms it or not at the gap (row 5a), and the skeptic tests it (row 5b).

| Shape | Sentence | Source |
|---|---|---|
| Problem seen in practice | "In {setting}, {people} {fail at / struggle with} {what}, which I saw when {…}." | Peffers et al.: "observation of the problem" [2] |
| Future work from a paper | "{Paper} suggests {future research}, and it has not been done." | Peffers et al.: "suggested future research in a paper from a prior project" [2] |
| Application | "{X} is established in {area A}, but not used in {area B}." | Sandberg and Alvesson, *application spotting*: a theory or perspective is missing in a specific area [3] |
| Neglect | "{Topic} is overlooked / under-researched / lacks empirical support." | Sandberg and Alvesson, *neglect spotting*, in its three versions [3] |
| Confusion | "Studies of {topic} disagree: {A} reports …, {B} reports …." | Sandberg and Alvesson, *confusion spotting*: the evidence is contradictory [3] |
| Problematization | "Work on {topic} assumes {assumption}; I doubt it because …." | Sandberg and Alvesson, *problematization*: challenging the assumptions underlying existing theory [3] |

Sandberg and Alvesson found the three gap-spotting shapes to be the most common way of building research questions, and argue that problematization is more likely to produce interesting results [3].

| # | Who | Input | Output | Gate |
|---|---|---|---|---|
| **0** | Me | — | `0-start/*.md` | **Start.** Frozen when row 1a runs. |

Everything else about the problem (motivation, design problem, RQs, hypotheses, stances, stakeholders) is built in DSRM 1, after the SLS, from step 0 and the literature (rows 6a–6d, `flow-dsrm.md`). Peffers et al. build the problem from knowledge of the state of the problem [2]; step 0 comes before that knowledge.

## Rules
- **Step 0 is never edited after it is frozen.** It records where the work started.
- **`notes.md` is checked, not trusted.** DSRM 1 marks each of its claims confirmed, to revise or contradicted by the literature (row 6a).

## Safeguards
- **Protocol bias:** if step 0 or `notes.md` argues for a conclusion, SQs drawn from it would only look for support. `skeptic` adds SQs that look for evidence against it (row 1b, `flow-sls.md`).
- **Start set bias:** snowballing only from `seeds.md` mostly finds more of the same. The start set also uses a database search string (row 2a), as Wohlin recommends a varied start set [1].
- **Tailoring bias** (design-centred and context-initiated): when the artifact or its results exist before the problem is written, the problem and objectives can be bent to fit them. The skeptic checks for it (rows 6c, 7b), and context-initiated objectives are marked retroactive (`entry-points.md`).

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
2. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
3. Sandberg, Alvesson (2011). *Ways of Constructing Research Questions: Gap-Spotting or Problematization?* Organization 18(1), 23–44.
