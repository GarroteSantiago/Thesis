# FAQ

**What are Shaw's validation types?** [1] (the computing profile's; other profiles list their own in `ai/profiles/`)
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
- A formal proof or model check counts as analysis and is stronger.

**How do I choose the validation type?**
- The question type decides what is acceptable [1]. Match the evidence to the claim.

**Do I need performance numbers at all?**
- Only if an objective or the history of the field asks for them. If similar ideas failed before for cost reasons, show the design is *not hopelessly worse* than current solutions.
- Measure on benchmarks the field already uses, against the baselines in `2-objectives/baselines.md`.

**What are threats to validity?**
- Honest reasons your results might be wrong, sorted into four categories [2]:
  - **Conclusion:** is the link between what you did and what you observed real, or chance?
  - **Internal:** did something other than your design cause the result?
  - **Construct:** do your measures really measure the objective? Example: "the model is not the real platform."
  - **External:** does the result hold outside your test cases?

---

## References
1. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
2. Wohlin et al. (2012). *Experimentation in Software Engineering*. Springer.
