# Repository Utilities

These scripts use only Python's standard library.

## Validate schedule data

```bash
python scripts/validate_schedule.py
```

The validator checks the CSV schemas, all 272 games, team/abbreviation integrity, one game per team per week, 17 games and one bye per team, agreement between the canonical CSV and all 32 team-local schedule views, date/time formatting, neutral-site flags, and allowed status values.

Alternative paths or seasons can be supplied with `--schedule`, `--teams`, and `--season`. Use `--skip-team-files` when validating a standalone data export without the repository tree.

## Generate a weekly workspace

Preview the files first:

```bash
python scripts/generate_week.py 1 --dry-run
```

Generate them:

```bash
python scripts/generate_week.py 1
```

The generator creates:

```text
weekly/2026/week-01/
├── README.md
└── games/
    ├── AWAY-at-HOME.md
    └── ...
```

It refuses to overwrite generated files unless `--force` is supplied. Each matchup file links back to both team research folders and includes sections for injuries, matchup analysis, fantasy implications, evidence, and invalidation/watch items.
