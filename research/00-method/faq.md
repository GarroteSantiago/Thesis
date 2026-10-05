# FAQ — general

**What methodology is this?**
- Design Science Research: learn by building an artifact and testing it [3].
- The *artifact* is what you create: here, the actor machine's instruction set, language, and simulator.

**Where is the iteration?**
- Filling writes into empty blanks. Iterating **rewrites filled blanks**, because a later step taught you something.
- This is Simon's *generate–test cycle* [4]. Hevner calls design a *search process* [3].
- Git history is the iteration record. If it only adds text and never changes earlier text, you are filling, not iterating.

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
