# Agent contract

What every agent in `.claude/agents/` does, whatever its role. The agent's own file adds only its role.

## You receive
From the step skill that dispatched you:
- **Row:** the flow row you run (e.g. `3a`), defined in `ai/flow-sls.md` or `ai/flow-dsrm.md`.
- **Inputs:** the exact files you read. Paths are relative to `research/` unless they start with `ai/` or `artifact/`.
- **Outputs:** the exact files you write.

## You do
1. Read the row in its flow file, then `ai/project.md` (its *Rules for this thesis* bind you; its *Notes for this thesis* are leads, never evidence), then the profile it names (`ai/profiles/{profile}.md`), then every input file. Read nothing else from `research/`; your view of the research is the inputs. The profile tells you what is specific to this field: where papers are found, what gets built, what counts as evidence.
2. For each output, copy its template from `ai/template/` (the table in `ai/template/README.md` maps output to template) and fill every `{placeholder}`.
3. Set the frontmatter: `id`, `row`, `by:` your agent name, `status: proposed`, `inputs:` the files you read.
4. Write only the output files. Every other file, and every `status`, belongs to me.
5. **No personal data** leaves this computer: never send my email address or any other personal data to a web service, in a URL, header or body. If an API requires an email (e.g. Unpaywall), skip that API.

## Your output is done when
- Every output file exists and has every section of its template.
- No `{placeholder}` or `[ ]` is left. A field you cannot fill says why, in one line.
- Every claim about a paper carries its P ID and page, or the reference and page for papers not yet in the review.
- Every fact comes from a file or source you actually read in this run. A fact you cannot trace to one is left out and named in your report.

## You return
A short report to the skill:
- Each file written, with one line on what it holds.
- Open issues: fields you could not fill, sources you could not reach, decisions you found that are mine to make.
- Each decision that is mine, as a decision card (`ai/gate.md`, *Decision card*): one ```json block per decision, following `ai/spec/decision-card.schema.json`. It has two parts:
  - **Plain:** the situation, why it matters to the thesis, the question, and two to four options, each with a short label and what choosing it means. Written for someone who has never opened the research files: follow *Talking to me* in `ai/gate.md`.
  - **Edits:** for each option, the exact edits it makes, file by file.

  Mark the option you recommend, and why. The gate asks me with the plain part and applies the edits of the option I choose.

## The guard
A hook checks every tool call against these rules (`ai/spec/README.md`). If it refuses one, its reason says what rule the call broke: do the work the way the reason says, or report it as an open issue. Never look for another way to make the same change.
