# FAQ

**How do I build?**
- Cheapest layer first:
  1. Paper design
  2. Executable model
  3. Formal specification
  4. Prototype on the real platform the artifact is meant for
- Philosophy: *iterative and incremental development*. Each layer finds flaws cheaply before the next one.

**What should each build be called in the thesis?**
- A *prototype*. Each build–test loop is a *build–evaluate cycle* [1].

**Can I go back to design without redoing everything?**
- Yes. Evaluation → design is one of Peffers' iteration arcs [2].
- Re-check the later steps that used the old design (see "Re-check after iterating" in `../README.md`).

---

## References
1. Hevner, March, Park, Ram (2004). *Design Science in Information Systems Research*. Management Information Systems Quarterly 28(1).
2. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
