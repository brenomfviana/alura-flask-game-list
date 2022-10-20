{
    description = "Flake of game list project";

    inputs = {
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let

        pkgsAllowUnfree = import nixpkgs {
          system = "x86_64-linux";
          config = { allowUnfree = true; };
        };

        config = {
          projectDir = ./.;
        };

      in
      {
        devShell = pkgsAllowUnfree.mkShell {
          buildInputs = with pkgsAllowUnfree; [
            gnumake
            poetry
            python3
          ];

          shellHook = ''
            export TMPDIR=/tmp

            test -f .venv/bin/activate || make poetry.install
            source .venv/bin/activate

            if ! test -f .env; then
              make config.env
            fi
            echo "Entering the nix devShell in alura-flask-game-list"
          '';
        };
      }
    );
}
