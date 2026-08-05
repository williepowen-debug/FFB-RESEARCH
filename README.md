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

players/                 Canonical player records independent of team assignment
weekly/<season>/         Injuries, matchups, waivers, rankings, and weekly decisions
league/                  League-wide data, methodology, transactions, and formats
templates/               Standard research and decision templates
```

The initial team scaffold covers all 32 NFL teams for the 2026 season. Empty research areas use `.gitkeep` files until material is added.

## Organizing principle

Store durable knowledge—player traits, coaching tendencies, scheme, and historical usage—in team, player, or league records. Store fast-changing state—injuries, depth charts, matchups, projections, weather, and start/sit conclusions—in `weekly/<season>/`.

Player profiles in `players/` are canonical. Team folders should link to them rather than duplicate an enduring player record.

## Research standard

Use the templates in `templates/`. Important findings should identify the evidence, source, publication and verification dates, applicable season/week, confidence, fantasy implication, and what would invalidate the conclusion.

See `league/methodology/README.md` and `SOURCE_POLICY.md` before adding research.
