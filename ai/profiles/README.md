# Profiles

A profile holds what changes from one field of study to another: where its papers are found, what kind of artifact gets built and how each version of it is checked, which kinds of research question and evidence the field accepts, and the examples used when explaining things to me. The method (the steps, the gates, the files) is the same for every profile.

The project's profile is named in `ai/project.md` (`profile:`). Every agent and skill reads it (`ai/agent-contract.md`).

## Profiles shipped with the skill
| Profile | For |
|---|---|
| `computing.md` | Computer science, software and computer engineering, information systems with a technical artifact |
| `general.md` | Any other field, or when unsure: a neutral starting point to adapt |

Profiles shipped with the skill are updated by `setup.sh --upgrade`. A profile built for this project is a new file here, with its own name, and is never touched by an upgrade.

## Choosing one
At setup the `thesis` skill shows the profiles in this folder, each with its *For* line, and asks which fits, with a decision card (`ai/gate.md`). If none fits, it offers to build one, starting from the closest.

## Building one
`/thesis profile` builds a new profile with me, as a row by me (`ai/running.md`): the content is mine, the skill writes it down.
1. Copy the closest profile to `ai/profiles/{name}.md`, with `name:` and `for:` set.
2. Go through its sections one at a time. For each, show what the closest profile says, and ask what is different in my field: where I search for papers, what I would build, how my field checks that it works, what counts as evidence. Offer the shipped content as a default, marked as such.
3. A section I cannot answer yet keeps the shipped content, with a line saying it is a default to revisit.
4. Set `profile: {name}` in `ai/project.md`, and commit.

A profile can be changed later the same way. If the change touches work already done (e.g. new build layers after a layer was accepted), say which files it affects before writing it.

## Sections of a profile
Every profile has these sections, in this order. Skills and agents look them up by heading.

| Section | Used by |
|---|---|
| *For* | choosing a profile |
| *Literature sources* | `snowballer` (row 2a, 2c), `protocol-critic` (row 1a, existing reviews) |
| *Review guidelines* | `protocol-critic`, the Method chapter: guidelines the field expects on top of Kitchenham and Charters and Wohlin |
| *Artifact kinds* | `synthesizer` (row 6b), `designer` |
| *Build layers* | `builder` (row 8c), `dsrm-3-design` (which layer is next) |
| *Research question types* | `synthesizer` (row 6b), the `RQ{n}.md` *Type* field |
| *Validation types* | row 7a, the `O{n}.md` *Validation type* field, `evaluator` |
| *Threat categories* | `evaluator` (row 10a), the `T{n}.md` *Category* field |
| *Examples* | everything meant for me (`ai/gate.md`, *Talking to me*) |
