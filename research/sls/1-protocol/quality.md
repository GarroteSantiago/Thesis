---
id: quality
row: 1a
by: protocol-critic
status: accepted
inputs: [sls/1-protocol/SQ*.md]
---
# Quality assessment checklist

`n/a` is used only when the source was not read (abstract-only record) or the question cannot apply to the paper's kind, and always with the reason. `no` means the paper fails the question.

| ID | Question asked of each paper | Scale |
|---|---|---|
| Q1 | Does the paper state its aim or contribution explicitly (in the abstract or introduction)? yes: stated in one place as a goal or contribution list; partly: has to be inferred from several places; no: not stated. | yes / partly / no / n/a |
| Q2 | Is the system's communication mechanism described in enough detail to reimplement it: message format, naming or addressing of the receiver, delivery and ordering guarantees, and what happens when the receiver is busy? yes: all four; partly: one to three; no: none. For papers with no system (I3 studies), the studied programs and their communication mechanisms count instead. | yes / partly / no / n/a |
| Q3 | Does the evidence come from a working artefact? yes: silicon, FPGA, or a kernel or system that runs real programs; partly: simulator or emulator; no: design or argument only. For I3 studies: yes: defects taken from real bug trackers or commit histories; partly: from benchmark suites; no: from examples only. Analytical models count as no (design or argument). | yes / partly / no / n/a |
| Q4 | Is every performance or defect claim measured against a named baseline? yes: each claim names its baseline (system, version, configuration); partly: some claims do; no: none do, or no measured claim is made. A hypothetical baseline counts as partly. For I3 studies: yes if the counts are compared with another named study or population; partly if only some are. | yes / partly / no / n/a |
| Q5 | Is the measurement setup reported: workloads or programs used and why they were chosen, hardware or simulator configuration, number of runs or sample size? yes: all three; partly: one or two; no: none, or nothing measured. For I3 studies: the sampling procedure (sources, search terms, screening) replaces the hardware or simulator configuration. | yes / partly / no / n/a |
| Q6 | Does every quantitative claim in the abstract and conclusions have a table, figure or text passage in the body that reports it? yes: all; partly: some; no: none, or no data in the body. | yes / partly / no / n/a |
| Q7 | Are causes attributed to results (e.g. "the slowdown comes from X") supported by a measurement that isolates that cause, such as an ablation or a breakdown? yes: every attributed cause; partly: some; no: none, or causes only asserted. | yes / partly / no / n/a |
| Q8 | Does the paper discuss limitations or threats to validity? yes: a section or paragraph dedicated to them; partly: mentioned in passing; no: not discussed. | yes / partly / no / n/a |
| Q9 | Is the evaluation independent of the system's designers? yes: no author is listed as a designer or builder of the evaluated system in the paper or its cited design papers; partly: some authors are; no: all authors are, or the paper does not evaluate a system. For I3 studies: yes if no author developed the studied programs. | yes / partly / no / n/a |
