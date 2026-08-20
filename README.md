This is the file tree of the repo
```Text
Thesis
├── chapters/                              # Código fuente de los capítulos en LaTeX
│   ├── 00_abstract.tex
│   ├── 01_introduction.tex
│   ├── 02_literature_review.tex
│   ├── 03_foundation.tex
│   ├── 04_ontology.tex
│   ├── 05_language.tex
│   ├── 06_os_design.tex
│   ├── 07_hardware.tex
│   ├── 08_implementation.tex
│   └── 09_evaluation.tex
├── design/                                # Especificaciones de diseño conceptual
│   ├── architecture/
│   ├── comparison/
│   ├── language/
│   └── ontology/
├── evaluation/                            # Validación empírica de la tesis
│   ├── benchmarks/                        # Scripts de rendimiento y métricas
│   ├── comparison/                        # Datos comparativos con otros sistemas
│   └── validation/                        # Pruebas de corrección formal/funcional
├── implementation/                        # Repositorio de código fuente real
│   ├── examples/                          # Programas de ejemplo en tu lenguaje
│   ├── language/                          # Compilador / Intérprete / Herramientas
│   ├── os/                                # Kernel / Runtime / Drivers
│   └── tests/                             # Test suites de la implementación
├── research/                              # Estado del arte y notas bibliográficas
│   ├── 01_von_neumann/
│   │   ├── notes.md
│   │   └── papers/                        # PDFs o enlaces de lectura
│   ├── 02_actor_model/
│   │   ├── notes.md
│   │   └── papers/
│   ├── 03_smalltalk_kay/
│   │   ├── notes.md
│   │   └── papers/
│   ├── 04_capability_hardware/
│   │   ├── notes.md
│   │   └── papers/
│   ├── 05_message_passing_isa/
│   │   ├── notes.md
│   │   └── papers/
│   ├── 06_hardware_software_codesign/
│   │   ├── notes.md
│   │   └── papers/
│   └── references.bib                     # Archivo BibTeX centralizado para citas
├── .envrc                                 # Configuración de direnv (use flake)
├── .gitignore                             # Filtro de artefactos LaTeX, Nix y OS
├── flake.lock                             # Lockfile de dependencias Nix
├── flake.nix                              # Entorno reproducible (TexLive, compilers, etc.)
├── justfile                               # Tareas de automatización (compilar, testear)
├── README.md                              # Guía del proyecto y documentación general
└── thesis.tex                             # Archivo raíz principal de LaTeX
```
