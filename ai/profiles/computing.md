---
name: computing
for: Computer science, software and computer engineering, information systems with a technical artifact
---
# Profile: computing

## For
Computer science, software and computer engineering, information systems with a technical artifact: a system, a language, an algorithm, an architecture, a tool.

## Literature sources
- **Search (row 2a):** Google Scholar, to avoid bias toward one publisher [1]; the ACM Digital Library, IEEE Xplore and DBLP for the field's venues.
- **Snowballing (rows 2c):** OpenAlex (`api.openalex.org`) and Semantic Scholar, through `curl`, for reference lists and citing papers; the paper itself when they are incomplete.
- **Existing reviews (row 1a):** the same sources, searching for "survey", "systematic review", "mapping study" on the topic.

## Review guidelines
Kitchenham and Charters [2] and Wohlin [1], as in `research/sls/README.md`. Nothing on top.

## Artifact kinds
A system or prototype, a language or notation, an algorithm, an architecture, a method or process for building software, a tool.

## Build layers
Cheapest first; each is demonstrated and evaluated before the next. Layers 3 and 4 are optional.

| Layer | Form | Check |
|---|---|---|
| 1. Paper design | Spec document: the artifact's parts, interfaces and behaviour, diagrams | Consistency review, worked examples by hand |
| 2. Executable model | Code and tests | Test suite, problem instances run end to end |
| 3. Formal specification | TLA+ / Alloy / Coq model | Model checker or proof |
| 4. Prototype | The artifact on the platform it is meant for | Runs on that platform, measured against the baselines |

Besides the layers, the builder also produces the problem instances, any tools the layers need, and figures.

## Research question types
Shaw's types [3]:

| Type | Typical form |
|---|---|
| Method or means of development | "How can we do X?" / "What is a better way to do X?" |
| Method for analysis or evaluation | "How can I evaluate the quality of X?" |
| Design, evaluation, or analysis of a particular instance | "How good is Y?" / "What is property X of Y?" |
| Generalization or characterization | "What, exactly, do we mean by X?" / "What are the important characteristics of X?" |
| Feasibility study or exploration | "Does X even exist?" / "Is it possible to accomplish X at all?" |

## Validation types
Shaw's types [3]: *analysis* (proof, empirical model, controlled experiment), *evaluation* (checked against stated criteria), *experience* (someone else used it on real examples), *example* (a worked example, toy or realistic), *persuasion* (weak). Blatant assertion is not acceptable. The question type decides which are enough: a working example answers "is it possible?"; "is it better?" needs analysis or evaluation.

## Threat categories
Wohlin et al. [4]: conclusion, internal, construct, external.

## Examples
- **Observation:** "Type checkers catch whole classes of bugs in application code, but not in build scripts."
- **Review question:** "Which build systems check scripts before running them, and how?"
- **Inclusion criterion:** "Included if it describes a checker for build or configuration scripts."
- **Objective:** "Rejects every script in the benchmark that fails at run time, with no false alarms on the scripts that pass."

---

## References
1. Wohlin (2014). *Guidelines for Snowballing in Systematic Literature Studies*. Conference on Evaluation and Assessment in Software Engineering.
2. Kitchenham, Charters (2007). *Guidelines for Performing Systematic Literature Reviews in Software Engineering*. Keele University and Durham University technical report.
3. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
4. Wohlin et al. (2012). *Experimentation in Software Engineering*. Springer.
