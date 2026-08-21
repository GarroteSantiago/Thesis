{
  description = "Actor-Based Thesis Environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (final: prev: {
              # Usamos python313 porque isbnlib aún no soporta python 3.14
              python313 = prev.python313.override {
                packageOverrides = pythonFinal: pythonPrev: {
                  # Forzamos el parche de habanero directamente en su derivación
                  habanero = pythonPrev.habanero.overrideAttrs (oldAttrs: {
                    propagatedBuildInputs = (oldAttrs.propagatedBuildInputs or [ ]) ++ [
                      pythonFinal.packaging
                    ];
                  });
                  # isbnlib usa la API obsoleta pkg_resources en vez de importlib.metadata.
                  # La parcheamos directamente en el fuente para evitar la dependencia de setuptools.
                  isbnlib = pythonPrev.isbnlib.overrideAttrs (oldAttrs: {
                    postPatch = (oldAttrs.postPatch or "") + ''
                      substituteInPlace isbnlib/registry.py \
                        --replace \
                          "from pkg_resources import iter_entry_points" \
                          "from importlib.metadata import entry_points as _ep; iter_entry_points = lambda g: _ep(group=g)"
                    '';
                  });
                  # Añadimos isbnlib a papis para que el importer de ISBN funcione
                  papis = pythonPrev.papis.overrideAttrs (oldAttrs: {
                    propagatedBuildInputs = (oldAttrs.propagatedBuildInputs or [ ]) ++ [
                      pythonFinal.isbnlib
                    ];
                  });
                };
              };
              # Forzamos a que papis se vuelva a compilar con python313 + isbnlib
              papis = final.python313.pkgs.toPythonApplication final.python313.pkgs.papis;
            })
          ];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # LaTeX (includes latexmk, biber)
            texlive.combined.scheme-full

            # PDF reading (zathura includes PDF support by default)
            zathura

            # Diagrams
            graphviz
            mermaid-cli

            # CLI tools
            ripgrep
            fzf
            git
            just

            # Bibliography corregido mediante Overlay
            papis
          ];

          shellHook = ''
            echo "=== Thesis Environment Ready ==="
            echo "Run 'just' for available commands"
            echo "================================="
          '';
        };
      }
    );
}
