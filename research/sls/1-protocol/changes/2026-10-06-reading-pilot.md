---
id: change-2026-10-06-reading-pilot
row: 1c
by: me
status: accepted
inputs: [sls/1-protocol/extraction-form.md, sls/1-protocol/quality.md, sls/1-protocol/criteria.md]
---
# Protocol change: reading-pilot

Saved as `sls/1-protocol/changes/2026-10-06-reading-pilot.md`.

## What changed
- `extraction-form.md`:
  - New *Applies to* column (I1–I4 per field); a field outside the paper's criteria is `n/a (I3)`, and `not stated` means the field applies but the paper is silent.
  - Values in *Cost of message primitives*, *Performance results* and *Scaling* are tagged measured / simulated / design figure / analytical / read off.
  - *Reference*: pages are those printed on `papers/P*.pdf` (else its PDF page), with the version (publisher, preprint, manuscript, reprint), the publisher's page range and any offset; abstract-only content cites `abstract`. Criteria I1–I4.
  - *Paper type*: one or more types, plus "position or analytical argument".
  - *Levels with message semantics*: adds `partly` (a message is a primitive at the level but other paths exist, naming the message-only operations), and for kernels and multicomputers separate answers between cores or nodes and within a core.
- `quality.md`:
  - Scale adds `n/a`, only for a source not read or a question that cannot apply, with the reason.
  - Q3: analytical models count as no.
  - Q4: a hypothetical baseline counts as partly. For I3, yes if the counts are compared with another named study.
  - Q5: for I3, the sampling procedure replaces the hardware setup.
  - Q9: for I3, yes if no author developed the studied programs.
- `criteria.md`, I3: adds "Programs whose defects are reported as accesses to shared variables count as shared-memory programs even if the paper does not use that term."

## Why
The reading pilot (P5, P8, P9, P10, P12, P13, P22, P33) showed the form and the checklist did not fit most papers:
- most fields did not apply to bug studies or analytical papers;
- readers cited five different kinds of page numbers;
- the strict yes/no on levels hid the differences the review is about;
- abstract-only and I3 records could only answer "no" to quality questions that could not apply.

Lu et al. (2008) met I3 only by inference, because it speaks of shared variables, not shared memory.

## Papers affected
The pilot records P5, P8, P9, P10, P12, P13, P22 and P33 were written under the previous form and are not re-read. Their fields are mapped to the new form at synthesis (4a). P5 meets I3 as changed. Every later record uses the new form.
