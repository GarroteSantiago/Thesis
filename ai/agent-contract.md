# Agent contract

What every agent in `.claude/agents/` does, whatever its role. The agent's own file adds only its role.

## You receive
From the step skill that dispatched you:
- **Row:** the flow row you run (e.g. `3a`), defined in `ai/flow-sls.md` or `ai/flow-dsrm.md`.
- **Inputs:** the exact files you read. Paths are relative to `research/` unless they start with `ai/` or `artifact/`.
- **Outputs:** the exact files you write.

## You do
1. Read the row in its flow file, then every input file. Read nothing else from `research/`; your view of the research is the inputs.
2. For each output, copy its template from `ai/template/` (the table in `ai/template/README.md` maps output to template) and fill every `{placeholder}`.
3. Set the frontmatter: `id`, `row`, `by:` your agent name, `status: proposed`, `inputs:` the files you read.
4. Write only the output files. Every other file, and every `status`, belongs to me.

## Your output is done when
- Every output file exists and has every section of its template.
- No `{placeholder}` or `[ ]` is left. A field you cannot fill says why, in one line.
- Every claim about a paper carries its P ID and page, or the reference and page for papers not yet in the review.
- Every fact comes from a file or source you actually read in this run. A fact you cannot trace to one is left out and named in your report.

## You return
A short report to the skill:
- Each file written, with one line on what it holds.
- Open issues: fields you could not fill, sources you could not reach, decisions you found that are mine to make.
