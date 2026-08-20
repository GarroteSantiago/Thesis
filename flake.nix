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
        pkgs = nixpkgs.legacyPackages.${system};
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

            # Optional: Bibliography
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
