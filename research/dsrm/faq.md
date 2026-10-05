# FAQ — general

**What methodology is this?**
- Design Science Research: learn by building an artifact and testing it [3].
- The process is the Design Science Research Methodology (DSRM) of Peffers et al. [8].
- The *artifact* is what you create: here, the actor machine's instruction set, language, and simulator.

**Why follow the sequence instead of jumping between steps?**
- The sequence is the paper's contribution: a common, recognizable process for design science work [8].
- It is *nominally* sequential: you may enter at a later activity, and you may iterate back [8]. It is never a free-for-all.

**Which entry point am I using?**
- Problem-centred: the research starts from an observed problem [8]. That is `1-problem/step.md` §1.1.

**Where is the iteration?**
- On Peffers' iteration arcs: from Evaluation or Communication back to Objectives or Design [8].
- Iterating **rewrites filled blanks**, because a later step taught you something. Filling writes into empty ones.
- This is Simon's *generate–test cycle* [4]. Hevner calls design a *search process* [3].
- Git history is the iteration record. If it only adds text and never changes earlier text, you are filling, not iterating.

**Where does the literature fit?**
- It is not a DSRM activity. Activities 1–3 draw on knowledge of the problem, of current solutions, and of theory [8].
- This is Hevner's *rigor cycle*: research draws on the knowledge base and adds to it [2].

**Is this a Minimum Viable Product cycle?**
- It is similar: build the smallest testable thing, learn, repeat [5].
- It is different:
  - it tests a research question, not user demand;
  - it must be grounded in literature [2];
  - it may change the question itself;
  - it produces knowledge, not a product.
- In the thesis, say *prototype* and *build–evaluate cycle*.

**How do I structure the repository?**
- Create a folder only when a real file needs it: "You Aren't Gonna Need It" [6][7].

**What is the best single book for this?**
- Wieringa [1].

---

## References
1. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
2. Hevner (2007). *A Three Cycle View of Design Science Research*. Scandinavian Journal of Information Systems 19(2).
3. Hevner, March, Park, Ram (2004). *Design Science in Information Systems Research*. Management Information Systems Quarterly 28(1).
4. Simon (1996). *The Sciences of the Artificial* (3rd edition). Massachusetts Institute of Technology Press.
5. Ries (2011). *The Lean Startup*. Crown Business.
6. Beck (2000). *Extreme Programming Explained: Embrace Change*. Addison-Wesley.
7. Wilson et al. (2017). *Good Enough Practices in Scientific Computing*. Public Library of Science Computational Biology 13(6).
8. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
