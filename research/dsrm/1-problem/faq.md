# FAQ

**My observation is not a question. How do I turn it into one?**
- Write it as a gap: "X is true in area A, but not in area B."
- Split it into two kinds of question [1]:
  - one **design problem** (build something);
  - several **knowledge questions** (learn something), generated from Shaw's types [2].
- The history question ("why hasn't this been done?") is not a knowledge question. It is answered by reading, not by building, and used here as motivation.
- Philosophy: *separation of concerns*. Building and knowing are different jobs.

**How do I know a question is good?**
- The answer could be "no" (*falsifiability*).
- You can name the evidence that would answer it.

**Does my gap have a name?**
- Yes: the *semantic gap*, the distance between what programmers think in (objects, actors, messages) and what hardware offers (addresses, loads, stores) [3].

**Who are my stakeholders?**
- Anyone affected by the problem or the artifact [1]. Candidates:
  - designers of operating systems and processors, if the idea is adopted;
  - the research community, which gains knowledge either way;
  - you, as a researcher who wants to know whether this is possible.
- You do not need a stakeholder analysis. One or two names answer the examiner's "so what?".

**What does a full worked example look like?**
- The cache:
  - Problem: memory is slower than the processor [4].
  - Key insight: programs reuse the same data, called locality [5][6].
  - Evaluation: the hit rate is high only when the working set fits in the cache.
- Original sources: Wilkes [7] and Smith [8].

---

## References
1. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
2. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
3. Myers (1982). *Advances in Computer Architecture* (2nd edition). Wiley.
4. Wulf, McKee (1995). *Hitting the Memory Wall: Implications of the Obvious*. Association for Computing Machinery Special Interest Group on Computer Architecture, Computer Architecture News 23(1).
5. Denning (1968). *The Working Set Model for Program Behavior*. Communications of the Association for Computing Machinery 11(5).
6. Denning (2005). *The Locality Principle*. Communications of the Association for Computing Machinery 48(7).
7. Wilkes (1965). *Slave Memories and Dynamic Storage Allocation*. Institute of Electrical and Electronics Engineers Transactions on Electronic Computers 14(2).
8. Smith (1982). *Cache Memories*. Association for Computing Machinery Computing Surveys 14(3).
