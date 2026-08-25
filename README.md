# FFB Research

A season-aware NFL research workspace built to support fantasy-football decisions.

## Start here

Use `BOOTSTRAP.md` when starting work on a laptop, desktop, or agent session. The repo workflow is:

```bash
cd /home/willi/FFB-RESEARCH
git rev-parse --show-toplevel
git status -sb
git branch --show-current
git worktree list
git fetch origin --prune
git switch main
git pull --ff-only
git status -sb
git rev-parse HEAD
git rev-parse origin/main
```

Treat GitHub `main` as the source of truth. Start feature work from an up-to-date `main`, merge
completed work back to `main` through GitHub, then pull `main` on each machine. Treat each startup
stage as a gate: inspect before changing state, and stop if synchronization or commit equality
fails. See `BOOTSTRAP.md` for recovery mode and the full post-merge cleanup invariant.

## Structure

```text
teams/<conference>/<division>/<team>/<season>/
├── offense/
├── defense/
├── coaching-staff/
├── special-teams/
└── beat-writers/

players/                    Canonical player records independent of team assignment
weekly/<season>/            Injuries, matchups, waivers, rankings, and weekly decisions
league/teams.csv            Canonical team names, abbreviations, venues, time zones, and paths
league/schedule/2026.csv    Canonical 2026 regular-season schedule
league/                     League-wide data, methodology, transactions, and formats
intelligence/               Reader intake, team synthesis, and priority routing
templates/                  Standard research and decision templates
schemas/                    Record schemas, controlled values, and ID conventions
catalog.jsonl               Generated index of structured research records
scripts/                    Validation, catalog, and weekly-workspace utilities
```

The initial team scaffold covers all 32 NFL teams for the 2026 season. Empty research areas use `.gitkeep` files until material is added.

## Organizing principle

Store durable knowledge—player traits, coaching tendencies, scheme, and historical usage—in team, player, or league records. Store fast-changing state—injuries, depth charts, matchups, projections, weather, and start/sit conclusions—in `weekly/<season>/`.

Player profiles in `players/` are canonical. Team folders should link to them rather than duplicate an enduring player record.

## Schedule data and utilities

The master schedule is `league/schedule/2026.csv`; team-local `schedule.md` files are readable views. Dates and kickoff times are Eastern. Explicitly flexible games are marked `flex_pending`, and genuinely unassigned dates/times remain blank with `date_time_tbd`.

```bash
python scripts/validate_schedule.py
python scripts/generate_week.py 1 --dry-run
python scripts/generate_week.py 1
```

See `league/schedule/README.md` and `scripts/README.md`.

## Research standard

Use the templates in `templates/`. Important findings should identify the evidence, source, publication and verification dates, applicable season/week, confidence, fantasy implication, and what would invalidate the conclusion.

Substantive Markdown records use structured YAML front matter governed by `schemas/`. This preserves readable research while allowing agents and scripts to validate, filter, and retrieve records through `catalog.jsonl`.

```bash
python scripts/generate_catalog.py
python scripts/validate_repository.py
```

See `AGENTS.md`, `schemas/README.md`, `league/methodology/README.md`, and `SOURCE_POLICY.md` before adding research.

Source-monitoring agents follow [the reader and synthesis pipeline](INTELLIGENCE_PIPELINE.md):
collect atomic observations, reconcile them by team, and promote only material signals into the
durable or weekly research layers.
