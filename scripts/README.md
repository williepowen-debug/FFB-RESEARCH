# Repository Utilities

These scripts use only Python's standard library.

## Validate the full repository

```bash
python scripts/generate_catalog.py
python scripts/validate_repository.py
python scripts/generate_catalog.py --check
```

The repository validator checks front matter, JSON Schemas, controlled values, immutable record-ID format, duplicate IDs, team references, supersession references, required sections, relative links, and catalog drift. `catalog.jsonl` is generated from Markdown metadata and must not be edited manually.

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

It refuses to overwrite generated files unless `--force` is supplied. Each matchup is a schema-valid draft record with a stable record ID, game ID, links to both team research folders, and sections for environment, matchup analysis, decisions, sources, and invalidation/watch items.
