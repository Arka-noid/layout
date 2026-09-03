# AGENTS.md

## Scope

- Generic playground for photonic layout design — no fixed PDK, product, or process assumptions.
- Sample/test scripts here are throwaway exploration, not production components.
- Feel free to add, rewrite, or delete scripts freely; nothing in this repo is load-bearing yet.

## Layout convention

- `scripts/` — layout-generation scripts, one file per design/experiment.
- `outputs/` — generated artifacts (`.gds` and similar), written by the scripts in `scripts/`.
- A script writes into `outputs/` via a path resolved relative to its own location (e.g. `Path(__file__).resolve().parent.parent / "outputs"`), so it works regardless of the working directory it's run from.
- `src/layout/` — reusable package code (shared components, cross-sections, helpers), importable as `import layout`. Standard `src/` layout, discovered via the `[tool.hatch.build.targets.wheel]` config in `pyproject.toml`. Empty for now; scripts import from here once something is worth sharing.

## Environment

- Python environment managed with [uv](https://docs.astral.sh/uv/); dependencies live in `pyproject.toml` / `uv.lock`.
- Run scripts with `uv run python <script>.py`; add dependencies with `uv add <package>`.
- Core library: [gdsfactory](https://gdsfactory.github.io/gdsfactory/) for parametric photonic/silicon-photonics layout, GDS export, and simulation glue.
- gdsfactory requires an active PDK before building components — the generic PDK is activated via `gf.gpdk.PDK.activate()`.
