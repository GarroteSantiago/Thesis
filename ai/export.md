# Export

How the thesis becomes one document. `just export` (`ai/tools/research.py export`), or `/thesis export`.

## The rule
**The research files are the source; the exported document is a copy.** Every edit to the text is made in the final section files (`research/dsrm/6-communicate/ch{n}-{section}.md`), through DSRM 6, so every change keeps its decision and its log. The exported files in `build/` are regenerated from scratch on every export and are not in git. Editing them is allowed for a look, never as the thesis: those edits are lost at the next export and are not on the record.

## What it does
1. Takes every final section with status `accepted` or `changed`, ordered by chapter number, then by section name (a section name starting with a number sets the order: `ch2-1-background` before `ch2-2-related-work`).
2. Writes `build/thesis.md`: one heading per chapter, named as in `research/README.md`, *Thesis chapters*; one subheading per section; the title and author from `ai/project.md`.
3. Builds the bibliography of every paper cited as `[@P12, p. 4]`, into `research/views/references.json` (generated, committed, so later exports work offline):
   - the paper's DOI, from the reading record's `doi:` frontmatter, its reference, or its row in the round file;
   - its full reference looked up from the DOI at `doi.org`, once, then kept;
   - with no DOI, or offline, a reference built from the reference text, reported so I can check it.

   Sources outside the review (method papers, standards) go in `research/references.bib`, written by hand, and are cited by their key.
4. Runs pandoc: `build/thesis.docx` (with my university's `.docx` template if `reference_doc` names one) and `build/thesis.pdf` (typst engine), with the citation style in `citation_style`.
5. Reports: sections exported, papers cited, references to check, and any P ID written without the `[@…]` form, which therefore has no bibliography entry.

## Not covered yet
Front matter (abstract, acknowledgements, table of contents settings), figures, and university cover pages. Until they are, add them in the exported copy at the very end, after the last export.
