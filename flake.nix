{
  description = "Thesis workflow environment";

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
        pkgs = import nixpkgs { inherit system; };
      in
      {
        # Only what the workflow itself runs (ai/): add your own tools (LaTeX, a reference manager…) here.
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3 # the AI log hooks, `just check`, `just views`, `just status`
            just # the task runner (justfile)
            git # history: one commit per gate, the ID rule, `just status`
            gh # `just papers-push` / `papers-pull`: the PDFs on the GitHub release
            curl # agents download papers and query bibliographic APIs
            pandoc # `just export`: the thesis as .docx and .pdf
            typst # `just export`: the PDF engine pandoc uses (much lighter than LaTeX)
          ];

          shellHook = ''
            echo "Thesis environment ready. Run 'just' for the commands."
          '';
        };
      }
    );
}
