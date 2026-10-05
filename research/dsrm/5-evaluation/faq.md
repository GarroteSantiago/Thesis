# FAQ

**What are Shaw's validation types?** [1]
- **Analysis:** rigorous analysis shows the result is satisfactory: formal proof, empirical model, controlled experiment.
- **Evaluation:** the result is checked against stated criteria, with a descriptive, qualitative, or empirical model.
- **Experience:** someone other than you used the result on real examples.
- **Example:** a worked example, toy or realistic, of how it works.
- **Persuasion:** "I thought hard about this and believe it." Shaw counts this as weak.
- **Blatant assertion:** no serious attempt to validate. Not acceptable.

**Shaw's "evaluation" and Peffers' "Evaluation" — same thing?**
- No. Peffers' Evaluation is this activity. Shaw's *evaluation* is one kind of evidence you may use inside it. Say so in the Method chapter.

**My questions are "can it be done?" What evidence answers that?**
- A working example: Shaw accepts one for feasibility [1].
- A formal proof, for example in Temporal Logic of Actions [3], counts as analysis and is stronger.

**How do I choose the validation type?**
- The question type decides what is acceptable [1]. Match the evidence to the claim.

**Do I need performance numbers at all?**
- Yes, but they are secondary. Show the design is *not hopelessly slow*, because of the Intel 432's history [4].
- Use actor benchmarks [5] against a normal processor.

**What are threats to validity?**
- Honest reasons your results might be wrong, sorted into four categories [2]:
  - **Conclusion:** is the link between what you did and what you observed real, or chance?
  - **Internal:** did something other than your design cause the result?
  - **Construct:** do your measures really measure the objective? Example: "the simulator is not real hardware."
  - **External:** does the result hold outside your test cases?

---

## References
1. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
2. Wohlin et al. (2012). *Experimentation in Software Engineering*. Springer.
3. Lamport (2002). *Specifying Systems: The TLA+ Language and Tools*. Addison-Wesley.
4. Colwell, Gehringer, Jensen (1988). *Performance Effects of Architectural Complexity in the Intel 432*. Association for Computing Machinery Transactions on Computer Systems 6(3).
5. Imam, Sarkar (2014). *Savina: An Actor Benchmark Suite*. Workshop on Programming based on Actors, Agents, and Decentralized Control.
