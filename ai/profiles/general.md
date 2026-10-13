---
name: general
for: Any other field, or when unsure: a neutral starting point to adapt
---
# Profile: general

## For
Any field where the thesis designs something and tests it: a method, a guideline, a programme, a process, a tool, a model. Health, education, management, design, the social sciences. A starting point: adapt it with `/thesis profile`.

## Literature sources
- **Search (row 2a):** Google Scholar, to avoid bias toward one publisher [1]; Scopus or Web of Science through the university library when available; the field's own database: PubMed (health), ERIC (education), PsycINFO (psychology), EconLit or SSRN (economics, business).
- **Snowballing (row 2c):** OpenAlex (`api.openalex.org`) and Semantic Scholar, through `curl`, for reference lists and citing papers; the paper itself when they are incomplete.
- **Existing reviews (row 1a):** the same sources, searching for "systematic review", "scoping review", "meta-analysis" on the topic.

## Review guidelines
Kitchenham and Charters [2] and Wohlin [1], as in `research/sls/README.md`. Many fields also expect the review to be reported following PRISMA 2020 [3]: the Method chapter reports the numbers of papers found, screened, excluded (with reasons) and included, which the round files and decision files already hold.

## Artifact kinds
Hevner et al.'s four kinds [4]: *constructs* (a vocabulary, a classification), *models* (how parts of a situation relate), *methods* (a procedure, a guideline, a programme), *instantiations* (a working tool or a real implementation).

## Build layers
Cheapest first; each is demonstrated and evaluated before the next. Layers 3 and 4 are optional.

| Layer | Form | Check |
|---|---|---|
| 1. Paper design | A written description of the artifact: its parts, how it is used, by whom, diagrams | Consistency review, walkthrough of worked examples by hand |
| 2. Mock-up | A version people can look at or try: a draft guideline, a paper prototype, a simulated session, slides | Walkthrough with experts or intended users |
| 3. Pilot | The artifact used for real, at small scale, in a controlled setting | Pilot study, measured against the baselines |
| 4. Field use | The artifact used in the setting it is meant for | Case study or field evaluation |

Besides the layers, the builder also produces the problem instances and any materials the layers need (forms, scripts, instructions).

## Research question types
Wieringa's knowledge questions [5]:

| Type | Typical form |
|---|---|
| Descriptive | "What happens when X is used?" / "How many, how often, when?" |
| Explanatory | "Why does X produce this effect?" (causes, mechanisms, reasons) |

The design problem itself ("improve X by designing Y") is not a research question (`research/dsrm/1-problem/step.md`).

## Validation types
Peffers et al.'s evaluation methods [6]: *logical argument*, *expert evaluation*, *technical experiment*, *subject-based experiment* (with people), *action research*, *prototype*, *illustrative scenario*, *case study*. Choose by what the objective claims: a claim about people's behaviour needs people; a claim about feasibility can rest on a prototype or scenario. Venable et al. [7] help choose when and where to evaluate: early and artificial (cheap, controlled) before late and naturalistic (real users, real setting).

## Threat categories
For measurements: Shadish, Cook and Campbell's four [8]: statistical conclusion, internal, construct, external. For qualitative evidence (interviews, observation, expert opinion): Lincoln and Guba's four [9]: credibility, transferability, dependability, confirmability.

## Examples
- **Observation:** "Checklists cut errors in surgery, but are rarely used in hospital night shifts."
- **Review question:** "Which checklists have been tried outside the operating room, and with what results?"
- **Inclusion criterion:** "Included if it reports a checklist used by clinical staff outside surgery."
- **Objective:** "Night-shift nurses complete the checklist in under two minutes, in at least 9 of 10 observed handovers."

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
2. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
3. Page et al. (2021). *The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews*. British Medical Journal 372:n71.
4. Hevner, March, Park, Ram (2004). *Design Science in Information Systems Research*. Management Information Systems Quarterly 28(1).
5. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
6. Peffers, Rothenberger, Tuunanen, Vaezi (2012). *Design Science Research Evaluation*. Design Science Research in Information Systems: Advances in Theory and Practice (DESRIST), Springer.
7. Venable, Pries-Heje, Baskerville (2016). *FEDS: A Framework for Evaluation in Design Science Research*. European Journal of Information Systems 25(1).
8. Shadish, Cook, Campbell (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Houghton Mifflin.
9. Lincoln, Guba (1985). *Naturalistic Inquiry*. Sage.
