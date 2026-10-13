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
        # This thesis's own tools (LaTeX, a PDF viewer, a reference manager…): a list in project-tools.nix,
        # e.g. `{ pkgs }: with pkgs; [ texlive.combined.scheme-full zathura ]`. That file is the project's:
        # upgrades never touch it. Flakes only see files git tracks, so `git add project-tools.nix` once.
        projectTools = if builtins.pathExists ./project-tools.nix then import ./project-tools.nix { inherit pkgs; } else [ ];
      in
      {
        # What the workflow itself runs (ai/), plus this thesis's own tools (project-tools.nix).
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3 # the AI log hooks, `just check`, `just views`, `just status`
            just # the task runner (justfile)
            git # history: one commit per gate, the ID rule, `just status`
            gh # `just papers-push` / `papers-pull`: the PDFs on the GitHub release
            curl # agents download papers and query bibliographic APIs
            pandoc # `just export`: the thesis as .docx and .pdf
            typst # `just export`: the PDF engine pandoc uses (much lighter than LaTeX)
          ] ++ projectTools;

          shellHook = ''
            echo "Thesis environment ready. Run 'just' for the commands."
          '';
        };
      }
    );
}
