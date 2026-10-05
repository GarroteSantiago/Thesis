# FAQ

**My observation is not a question. How do I turn it into one?**
- Write it as a gap: "X is true in area A, but not in area B."
- Split it into two kinds of question [1]:
  - one **design problem** (build something);
  - several **knowledge questions** (learn something), generated from Shaw's types [2].
- Always add a history question.
- Philosophy: *separation of concerns*. Building and knowing are different jobs.

**How do I know a question is good?**
- The answer could be "no" (*falsifiability*).
- You can name the evidence that would answer it.

**Does my gap have a name?**
- Yes: the *semantic gap*, the distance between what programmers think in (objects, actors, messages) and what hardware offers (addresses, loads, stores) [3].

**What history must my thesis answer?**
- Language-oriented hardware failed before [4].
- The Intel 432 was object-based hardware and was slow [5].
- Much of its slowness came from implementation choices, not only from the idea itself [5]. This is your opening.

**What does a full worked example look like?**
- The cache:
  - Problem: memory is slower than the processor [6].
  - Key insight: programs reuse the same data, called locality [7][8].
  - Evaluation: the hit rate is high only when the working set fits in the cache.
- Original sources: Wilkes [9] and Smith [10].

---


## References
1. Wieringa (2014). *Design Science Methodology for Information Systems and Software Engineering*. Springer.
2. Shaw (2003). *Writing Good Software Engineering Research Papers*. International Conference on Software Engineering.
3. Myers (1982). *Advances in Computer Architecture* (2nd edition). Wiley.
4. Ditzel, Patterson (1980). *Retrospective on High-Level Language Computer Architecture*. International Symposium on Computer Architecture.
5. Colwell, Gehringer, Jensen (1988). *Performance Effects of Architectural Complexity in the Intel 432*. Association for Computing Machinery Transactions on Computer Systems 6(3).
6. Wulf, McKee (1995). *Hitting the Memory Wall: Implications of the Obvious*. Association for Computing Machinery Special Interest Group on Computer Architecture, Computer Architecture News 23(1).
7. Denning (1968). *The Working Set Model for Program Behavior*. Communications of the Association for Computing Machinery 11(5).
8. Denning (2005). *The Locality Principle*. Communications of the Association for Computing Machinery 48(7).
9. Wilkes (1965). *Slave Memories and Dynamic Storage Allocation*. Institute of Electrical and Electronics Engineers Transactions on Electronic Computers 14(2).
10. Smith (1982). *Cache Memories*. Association for Computing Machinery Computing Surveys 14(3).
