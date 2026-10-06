# Thesis task runner

# Default recipe (runs if you just type 'just')
default: help

# Display help
help:
    @just --list

# Build thesis PDF
build:
    latexmk -pdf thesis.tex

# Live preview (recompile on save)
preview:
    latexmk -pvc -pdf thesis.tex

# Clean auxiliary files
clean:
    latexmk -c
    rm -f thesis.pdf

# Regenerate all diagrams
diagrams:
    dot -Tpng design/ontology/ontology.dot -o design/ontology/ontology.png
    echo "✓ Ontology diagram"
    @if [ -f design/language/sequence.mmd ]; then \
        mmdc -i design/language/sequence.mmd -o design/language/sequence.png; \
        echo "✓ Sequence diagram"; \
    fi

# Search in thesis
search term:
    rg "{{ term }}" chapters/ research/ --type tex --type md

# Count words
wordcount:
    @echo "Total words:"
    @wc -w chapters/*.tex | tail -1

# List all citations
citations:
    @rg -o '@\w+{[^}]+}' chapters/ | sort | uniq

# Check the research files against the workflow rules (ai/checks.md)
check:
    python3 ai/tools/research.py check

# Regenerate research/views/ from the research files (ai/checks.md)
views:
    python3 ai/tools/research.py views

# Upload the paper PDFs in research/papers/ to the "papers" GitHub release
papers-push:
    #!/usr/bin/env bash
    set -euo pipefail
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
    if ! gh release view papers >/dev/null 2>&1; then echo "No papers release yet."; exit 0; fi
    gh release download papers --dir research/papers --pattern '*.pdf' --clobber
    echo "Downloaded the papers release into research/papers/."

# Git commit with message
commit message:
    git add -A
    git commit -m "{{ message }}"

# Full build + preview
watch: build
    latexmk -pvc -pdf thesis.tex
