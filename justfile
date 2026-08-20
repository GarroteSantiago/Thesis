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

# Git commit with message
commit message:
    git add -A
    git commit -m "{{ message }}"

# Full build + preview
watch: build
    latexmk -pvc -pdf thesis.tex
