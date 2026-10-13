# Status

What `/thesis status` tells me: where the thesis stands, in plain words. It reads; it never runs a row or changes a file.

## How
1. Run `just status` (`ai/tools/research.py status`). It reports, from the files and from git:
   - the entry point and profile;
   - the last commit: when, what, which files;
   - the work in progress: files changed or added since the last commit;
   - every step in the order of the entry point's route, done, in progress or not started, with counts;
   - how many files wait for my decision.
2. Turn it into the summary below. Follow *Talking to me* (`ai/gate.md`): no bare IDs, row numbers or file names; what they stand for.

## The summary
- **Where I am:** the current step, with one sentence on what it is for (from its `step.md`, *In plain words*). Steps 2 to 4 of the literature study are a loop: say which round, and whether the current paper batch is still being searched, read or organised.
- **Last saved:** what the last commit recorded, in one or two sentences, and how long ago ("yesterday you accepted 12 reading records").
- **In progress:** what the uncommitted files are ("4 reading records drafted by the AI, waiting for you"), or "nothing: everything is saved".
- **Distance to the current goal:** what is left before the current step is done, as counts ("251 of 278 papers still to read; then concepts; then the next search round"). When a count cannot be known yet (how many snowballing rounds remain), say so.
- **Distance to the end:** steps done out of the route's total, and the steps left, named.
- **Next:** the one command that continues the work (`/thesis`, or the step skill), and what it will do first.
