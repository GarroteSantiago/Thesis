# FAQ

**My questions are "can it be done?" What evidence proves that?**
- Proof by construction: you show it is possible by building it. Shaw accepts a working example for feasibility [1].
- Evidence from strongest to weakest:
  1. Formal proof, for example in Temporal Logic of Actions [3]
  2. Controlled measurement
  3. Working build
  4. Worked scenario
  5. Argument

**How do I choose the evidence type?**
- The question type decides it [1]:
  - Characterization → analysis or survey
  - Feasibility → construction
  - Method → demonstration
  - Evaluation → measurement against a baseline
- Philosophy: *match evidence to the claim*.

**Do I need performance numbers at all?**
- Yes, but they are secondary. Show the design is *not hopelessly slow*, because of the Intel 432's history [4].
- Use actor benchmarks [5] against a normal processor.

**What are threats to validity?**
- Honest reasons your results might be wrong. Example: "the simulator is not real hardware" [2].

**What is a proof of concept, and where does it go?**
- A small working demo showing an idea is possible. It does not prove the idea is good or complete.
- Sorting:
  - someone else built it → a matrix row (`3-literature.md`);
  - you built it and it answers a question → this results log;
  - it answers no question → exploration notes.

---

## References
1. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
2. Wohlin et al. (2012). *Experimentation in Software Engineering*. Springer.
3. Lamport (2002). *Specifying Systems: The TLA+ Language and Tools*. Addison-Wesley.
4. Colwell, Gehringer, Jensen (1988). *Performance Effects of Architectural Complexity in the Intel 432*. Association for Computing Machinery Transactions on Computer Systems 6(3).
5. Imam, Sarkar (2014). *Savina: An Actor Benchmark Suite*. Workshop on Programming based on Actors, Agents, and Decentralized Control.
