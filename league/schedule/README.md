# 2026 NFL Schedule Data

`2026.csv` is the canonical regular-season schedule for this repository. Team-local `schedule.md` files are human-readable views; scripts and agents should treat this CSV as the source of truth.

Strength-of-schedule research belongs in `strength-of-schedule/`. Use that workspace for overall schedule difficulty, fantasy position-specific schedule difficulty, fantasy playoff-window analysis, and schedule-friction notes.

## Fields

| Field | Meaning |
|---|---|
| `season` | NFL season year |
| `week` | Regular-season week, 1–18 |
| `date_et` | Scheduled calendar date in Eastern Time; blank when officially TBD |
| `kickoff_et` | Scheduled kickoff in Eastern Time; blank when officially TBD |
| `away_team`, `home_team` | Full team names using `league/teams.csv` |
| `away_abbr`, `home_abbr` | Stable abbreviations from the team registry |
| `venue`, `venue_city` | Scheduled venue, including international sites |
| `neutral_site` | `true` for international/neutral-site games |
| `schedule_status` | `scheduled`, `flex_pending`, or `date_time_tbd` |
| `source_url` | Official NFL weekly schedule |
| `last_verified` | Date this row was last checked |

Week 18 dates and kickoff times remain blank because the NFL assigns them after Week 17. Games explicitly designated for late-season flexible scheduling use `flex_pending`.

## Sources

- [Official NFL 2026 schedule](https://www.nfl.com/schedules/2026/)
- [NFL Football Operations international slate](https://operations.nfl.com/programs-initiatives/international-growth/nfl-international-games)
- [FFToday schedule grid](https://www.fftoday.com/nfl/schedule.php) as a cross-check

## Validation and weekly generation

From the repository root:

```bash
python scripts/validate_schedule.py
python scripts/generate_week.py 1 --dry-run
python scripts/generate_week.py 1
```

See `scripts/README.md` for details.
