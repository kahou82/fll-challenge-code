# FLL Challenge — SPIKE Prime Code Library

Reusable code and block-logic templates for our FIRST LEGO League Challenge robot game runs, built with the LEGO SPIKE Prime app (block coding).

## Why this repo exists

- Save time each season by starting from proven building blocks (drive straight, turn, line square-up, etc.) instead of rebuilding from scratch.
- Keep a record of what worked/didn't work across missions and seasons.
- Give teammates something to look at and explain during judging (FIRST Core Values reward sharing/documentation).

**Important for judging:** these templates are starting points, not a black box. Teammates should understand and be able to explain how each block works and why — judges typically ask kids to walk through their code.

## How block code is stored here

The SPIKE app's block code lives in `.llsp3` project files, which are a binary/zip format the app itself creates — they can't be hand-written or diffed like text. So this repo uses two complementary things:

1. **`programs/`** — plain-language, step-by-step descriptions of each block sequence (what blocks, what order, what values). Recreate these by dragging blocks in the SPIKE app.
2. **`exports/`** — the actual `.llsp3` files exported from the SPIKE app, checked in as-is once a program is built and tested, so we always have a working backup.

`python-reference/` has optional Python versions of the same logic (SPIKE app also supports a Python mode using the same hardware API) — handy for planning logic quickly or for teammates who want to try text coding.

## Folder structure

```
fll-challenge-code/
├── README.md
├── docs/                     # how-tos, conventions, setup notes
├── programs/
│   └── templates/            # reusable block-logic templates (markdown)
├── exports/                  # exported .llsp3 files from the SPIKE app
└── python-reference/         # optional Python equivalents for planning
```

## Getting started

1. Open the SPIKE Prime app and connect/pair the hub.
2. Pick a template from `programs/templates/` and recreate the block sequence in a new SPIKE project.
3. Test on the robot, tune the numbers (speed, degrees, distance) for your robot and field.
4. Export the finished project (File → Save As / Export) into `exports/` with a clear name, e.g. `exports/mission1-2026.llsp3`.
5. If you changed a template's logic in a useful way, update the matching file in `programs/templates/`.

## Privacy note

This repo is public. Please don't commit real full names, photos, or other identifying info of team members — team number and season name are enough.
