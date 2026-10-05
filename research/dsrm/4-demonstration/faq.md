# FAQ

**How is demonstration different from evaluation?**
- Demonstration: the artifact solves an instance of the problem [1]. It shows the artifact *works*.
- Evaluation: compare the objectives with what was observed in the demonstration [1]. It shows *how well*.
- Evaluation reads its observations from here, so log what you saw, not only whether it passed.

**What is a good problem instance for this thesis?**
- A small actor program that the target area (operating systems, hardware) cannot express directly today, run on the simulator.
- Start with a toy instance, then a realistic one, for example a program from an actor benchmark suite [2].

**What is a proof of concept, and where does it go?**
- A small working demo showing an idea is possible. It does not prove the idea is good or complete.
- It is a demonstration. Log it here, and evaluate it in step 5 if it serves an objective.

---

## References
1. Peffers et al. (2007). *A Design Science Research Methodology for Information Systems Research*. Journal of Management Information Systems 24(3).
2. Imam, Sarkar (2014). *Savina: An Actor Benchmark Suite*. Workshop on Programming based on Actors, Agents, and Decentralized Control.
