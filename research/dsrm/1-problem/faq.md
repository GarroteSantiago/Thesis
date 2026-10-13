# FAQ

**My observation is not a question. How do I turn it into one?**
- Write it in one of the shapes in `../../../ai/kickstart.md`, *Shapes of an observation*: a problem seen in practice, future work from a paper, or a gap of application, neglect or confusion, or a challenged assumption.
- Split it into two kinds of question [1]:
  - one **design problem** (build something);
  - several **knowledge questions** (learn something), generated from Shaw's types [2].
- The history question ("why hasn't this been done?") is not a knowledge question. It is answered by reading, not by building, and used here as motivation.
- Philosophy: *separation of concerns*. Building and knowing are different jobs.

**How do I know a question is good?**
- The answer could be "no" (*falsifiability*).
- You can name the evidence that would answer it.

**Does my gap have a name?**
- Often it does: look in the SLS literature for an established term for the distance your observation describes. Naming it ties the problem to the knowledge base.

**Who are my stakeholders?**
- Anyone affected by the problem or the artifact [1]. Candidates:
  - the practitioners who would use or build on the artifact, if the idea is adopted;
  - the research community, which gains knowledge either way;
  - you, as a researcher who wants to know whether this is possible.
- You do not need a stakeholder analysis. One or two names answer the examiner's "so what?".

**What does a full worked example look like?**
- The cache:
  - Problem: memory is slower than the processor [3].
  - Key insight: programs reuse the same data, called locality [4].
  - Evaluation: the hit rate is high only when the working set fits in the cache.

---

## References
1. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
2. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
3. Wulf, McKee (1995). *Hitting the Memory Wall: Implications of the Obvious*. Association for Computing Machinery Special Interest Group on Computer Architecture, Computer Architecture News 23(1).
4. Denning (2005). *The Locality Principle*. Communications of the Association for Computing Machinery 48(7).
