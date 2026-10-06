# Template

The shape of every file the workflow produces. The folders mirror `research/`, where the filled copies are saved. Each template is the spec of its file: frontmatter, sections, and a `{placeholder}` with what goes there.

## How to use
1. Copy the template to the path in *Saved as* (relative to `research/`), replacing `{n}`, `{k}` and the other names.
2. Fill every `{placeholder}`. A produced file has none left (`../files.md`).
3. Set the frontmatter: `id`, `row`, `by`, `inputs`. `status` starts as `proposed` (`provisional` for step 0).

Templates are the only files allowed to contain placeholders.

## Files
| Template | Saved as | Row | Who |
|---|---|---|---|
| `0-start/observation.md` | `0-start/observation.md` | 0 | me |
| `0-start/seeds.md` | `0-start/seeds.md` (optional) | 0 | me |
| `0-start/notes.md` | `0-start/notes.md` (optional) | 0 | me |
| `sls/1-protocol/need.md` | `sls/1-protocol/need.md` | 1a | `protocol-critic` |
| `sls/1-protocol/SQ.md` | `sls/1-protocol/SQ{n}.md` | 1a, 1b | `protocol-critic`, `skeptic` |
| `sls/1-protocol/criteria.md` | `sls/1-protocol/criteria.md` | 1a | `protocol-critic` |
| `sls/1-protocol/quality.md` | `sls/1-protocol/quality.md` | 1a | `protocol-critic` |
| `sls/1-protocol/extraction-form.md` | `sls/1-protocol/extraction-form.md` | 1a | `protocol-critic` |
| `sls/1-protocol/change.md` | `sls/1-protocol/changes/{date}-{slug}.md` | after 1c | me |
| `sls/2-search/search-string.md` | `sls/2-search/search-string.md` | 2a | `snowballer` |
| `sls/2-search/R.md` | `sls/2-search/R0.md`, `R{k}-backward.md`, `R{k}-forward.md` | 2a, 2c | `snowballer` |
| `sls/3-reading/P.md` | `sls/3-reading/P{n}.md` | 3a | `reader` |
| `sls/4-synthesis/C.md` | `sls/4-synthesis/C{n}.md` | 4a | `synthesizer` |
| `sls/5-gap/SQ.answer.md` | `sls/5-gap/SQ{n}.answer.md` | 5a | `synthesizer` |
| `sls/5-gap/gap.md` | `sls/5-gap/gap.md` | 5a | `synthesizer` |
| `sls/5-gap/solutions.md` | `sls/5-gap/solutions.md` | 5a | `synthesizer` |
| `sls/5-gap/history.md` | `sls/5-gap/history.md` | 5a | `synthesizer` |
| `sls/5-gap/limitations.md` | `sls/5-gap/limitations.md` | 5a | `synthesizer` |
| `dsrm/1-problem/motivation.md` | `dsrm/1-problem/motivation.md` | 6a | `synthesizer` |
| `dsrm/1-problem/revision.md` | `dsrm/1-problem/revision.md` (if notes exist) | 6a | `synthesizer` |
| `dsrm/1-problem/design-problem.md` | `dsrm/1-problem/design-problem.md` | 6b | `synthesizer` |
| `dsrm/1-problem/RQ.md` | `dsrm/1-problem/RQ{n}.md` | 6b | `synthesizer` |
| `dsrm/1-problem/H.md` | `dsrm/1-problem/H{n}.md` | 6b | `synthesizer` |
| `dsrm/1-problem/stances.md` | `dsrm/1-problem/stances.md` | 6b | `synthesizer` |
| `dsrm/1-problem/stakeholders.md` | `dsrm/1-problem/stakeholders.md` | 6b | `synthesizer` |
| `dsrm/2-objectives/O.md` | `dsrm/2-objectives/O{n}.md` | 7a | me |
| `dsrm/2-objectives/metrics.md` | `dsrm/2-objectives/metrics.md` | 7a | me |
| `dsrm/2-objectives/baselines.md` | `dsrm/2-objectives/baselines.md` | 7a | me |
| `dsrm/3-design/DEC.options.md` | `dsrm/3-design/DEC{n}.options.md` | 8a | `designer` |
| `dsrm/3-design/DEC.md` | `dsrm/3-design/DEC{n}.md` | 8b | me |
| `dsrm/3-design/L.md` | `dsrm/3-design/L{n}.md` | 8c | `builder` |
| `dsrm/4-demonstration/D.md` | `dsrm/4-demonstration/D{n}.md` | 9a | `demonstrator` |
| `dsrm/4-demonstration/D-run.md` | `dsrm/4-demonstration/D{n}-run{k}.md` | 9c | `demonstrator` |
| `dsrm/5-evaluation/E.md` | `dsrm/5-evaluation/E{n}.md` | 10a | `evaluator` |
| `dsrm/5-evaluation/T.md` | `dsrm/5-evaluation/T{n}.md` | 10a | `evaluator` |
| `dsrm/6-communicate/section.outline.md` | `dsrm/6-communicate/ch{n}-{section}.outline.md` | 11a | me |
| `dsrm/6-communicate/section.draft.md` | `dsrm/6-communicate/ch{n}-{section}.draft.md` | 11b | `drafter` |
| `dsrm/6-communicate/section.md` | `dsrm/6-communicate/ch{n}-{section}.md` | 11e | me |
| `dsrm/6-communicate/contribution.md` | `dsrm/6-communicate/contribution.md` | 11e | me |
| `reviews/skeptic.md` | `{file}.skeptic.md`, next to the reviewed file | 1b, 5b, 6c, 7b, 10b | `skeptic` |
| `reviews/citations.md` | `{file}.citations.md`, next to the checked file | 3b, 11c | `citation-checker` |
| `reviews/examiner.md` | `{file}.examiner.md`, next to the draft | 11d | `examiner` |
| `ai-log/decision.md` | `ai-log/decisions/{date}-{row}-{id}.md` | every gate | me |

Built layers (`artifact/L{n}/`) have no template: their form depends on the layer (`../agents.md`).
