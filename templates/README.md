# Templates

To build out a whole team module, read [`TEAM_BUILD.md`](../TEAM_BUILD.md) first. It codifies the
Core-tier layout, per-file record types and required sections, the ID scheme, canonical CSV
headers, build order, and the validation gate.

Copy the closest template before adding a new record:

- `research-finding.md`
- `team-overview.md`
- `player-profile.md`
- `coaching-profile.md`
- `beat-writer-registry.md`
- `beat-writer-candidate-ledger.csv` — copy to a team registry as durable `candidates.csv`
- `reader-observations.csv` — immutable per-reader intake batch
- `reader-assignment.csv` — bounded source, team, lane, and retrieval-window assignment
- `team-intelligence.md` — dated team-level reconciliation and routing record
- `intelligence-priority-board.csv` — league-level review and escalation queue
- `injury-update.md`
- `weekly-matchup.md`
- `depth-chart.md`

Delete unused prompts, preserve the metadata needed for auditing, and link related player, team, league, and weekly records.

Every template contains valid draft front matter. Replace placeholder team/player values, assign an immutable `record_id`, and add dates before changing a record to `active`. See `schemas/README.md` and `schemas/ID_CONVENTIONS.md`.
