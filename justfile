# Thesis task runner. The workflow's recipes; this thesis's own recipes go in project.just, which upgrades never touch.
import? 'project.just'

# Default recipe (runs if you just type 'just')
default: help

# Display help
help:
    @just --list

# Check the research files against the workflow rules (ai/checks.md)
check:
    python3 ai/tools/research.py check

# Regenerate research/views/ from the research files (ai/checks.md)
views:
    python3 ai/tools/research.py views

# Where the thesis stands: last commit, work in progress, progress per step (ai/status.md)
status:
    python3 ai/tools/research.py status

# Upload the paper PDFs in research/papers/ to the "papers" GitHub release
papers-push:
    #!/usr/bin/env bash
    set -euo pipefail
    gh repo view >/dev/null 2>&1 || { echo "No GitHub repository linked (or gh not logged in): the PDFs stay in research/papers/ on this computer."; exit 0; }
    shopt -s nullglob
    pdfs=(research/papers/*.pdf)
    if [ ${#pdfs[@]} -eq 0 ]; then echo "No PDFs in research/papers/."; exit 0; fi
    gh release view papers >/dev/null 2>&1 || gh release create papers --title "Papers" --notes "PDFs of the papers read in the SLS (research/papers/)."
    gh release upload papers "${pdfs[@]}" --clobber
    echo "Uploaded ${#pdfs[@]} PDF(s) to the papers release."

# Download the paper PDFs from the "papers" GitHub release into research/papers/
papers-pull:
    #!/usr/bin/env bash
    set -euo pipefail
    gh repo view >/dev/null 2>&1 || { echo "No GitHub repository linked (or gh not logged in): the PDFs stay in research/papers/ on this computer."; exit 0; }
    if ! gh release view papers >/dev/null 2>&1; then echo "No papers release yet."; exit 0; fi
    gh release download papers --dir research/papers --pattern '*.pdf' --clobber
    echo "Downloaded the papers release into research/papers/."

# Git commit with message
commit message:
    git add -A
    git commit -m "{{ message }}"

# Assemble the accepted final sections into build/thesis.docx and build/thesis.pdf (ai/export.md)
export:
    python3 ai/tools/research.py export

# Run the guard hook's built-in tests (ai/spec/README.md)
guard-test:
    python3 ai/tools/guard.py --test
