# Miami Dolphins 2026 roster-change datasets

These CSV files preserve the 2025-to-2026 transition as row-level data rather than embedding the entire baseline in prose.

- `departures.csv`: major veterans removed by trade, release, or contract expiration, including the 2025 Jaelan Phillips trade that preceded the formal offseason.
- `veteran-additions.csv`: non-draft additions relevant to the 2026 transition, including reserve/future signings, waiver claims, separately signed rookies, and players later released or waived. The filename is retained for repository continuity, but the table's scope is broader than vested veterans.
- `retentions.csv`: extensions, re-signings, and the exclusive-rights tender that define the retained core.
- `draft-class.csv`: all 13 selections from the official 2026 draft tracker.
- `undrafted-free-agents.csv`: the original 11-player UDFA class and known subsequent status changes.

`current_status` is time-sensitive. Update it at cutdowns and after transactions; do not delete the acquisition row. Contract values labeled `reported` are not official team disclosures.
