# This thesis's own tools, added to the workflow environment (flake.nix). Upgrades never touch this file.
{ pkgs }:
let
  # Python 3.13 because isbnlib does not support Python 3.14 yet
  python = pkgs.python313.override {
    packageOverrides = pyFinal: pyPrev: {
      # habanero needs packaging at run time
      habanero = pyPrev.habanero.overrideAttrs (old: {
        propagatedBuildInputs = (old.propagatedBuildInputs or [ ]) ++ [ pyFinal.packaging ];
      });
      # isbnlib uses the deprecated pkg_resources API instead of importlib.metadata:
      # patch the source to avoid depending on setuptools
      isbnlib = pyPrev.isbnlib.overrideAttrs (old: {
        postPatch = (old.postPatch or "") + ''
          substituteInPlace isbnlib/registry.py \
            --replace \
              "from pkg_resources import iter_entry_points" \
              "from importlib.metadata import entry_points as _ep; iter_entry_points = lambda g: _ep(group=g)"
        '';
      });
      # isbnlib in papis, so its ISBN importer works
      papis = pyPrev.papis.overrideAttrs (old: {
        propagatedBuildInputs = (old.propagatedBuildInputs or [ ]) ++ [ pyFinal.isbnlib ];
      });
    };
  };
  papis = python.pkgs.toPythonApplication python.pkgs.papis;
in
with pkgs;
[
  texlive.combined.scheme-full # LaTeX (includes latexmk, biber)
  zathura # PDF reading
  graphviz # diagrams
  mermaid-cli # diagrams
  ripgrep # search
  fzf # search
  papis # bibliography, with the patches above
]
