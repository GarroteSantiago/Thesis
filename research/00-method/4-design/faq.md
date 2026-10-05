# FAQ

**How do I build?**
- Cheapest layer first:
  1. Paper design
  2. Software simulator
  3. Formal specification
  4. Hardware prototype on a Field-Programmable Gate Array (a chip you can rewire with code), or a model in the gem5 simulator [1]
- Philosophy: *iterative and incremental development*. Each layer finds flaws cheaply before the next one.

**What should each build be called in the thesis?**
- A *prototype*. Each build–test loop is a *build–evaluate cycle* [2].

**Can I go back to design without redoing everything?**
- Yes. Design → evaluation → design is a valid loop on its own.
- Re-check only the steps that depend on what you changed (see the dependency rule in `README.md`).

---

## References
1. Binkert et al. (2011). *The gem5 Simulator*. Association for Computing Machinery Special Interest Group on Computer Architecture, Computer Architecture News 39(2).
2. Hevner, March, Park, Ram (2004). *Design Science in Information Systems Research*. Management Information Systems Quarterly 28(1).
