# FFB Research

A season-aware NFL research workspace built to support fantasy-football decisions.

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
templates/                  Standard research and decision templates
scripts/                    Schedule validation and weekly-workspace generation
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

See `league/methodology/README.md` and `SOURCE_POLICY.md` before adding research.
