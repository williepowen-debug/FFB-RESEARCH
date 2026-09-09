# Seattle Seahawks source-monitoring guide

This directory tracks official records, current reporters, analysts, and data sources for fantasy-relevant Seahawks injuries, roles, usage, scheme, and roster construction. The candidate ledger preserves both discovery passes and explicit exclusions.

Start with official records and independent observations, then use film analysis to interpret them and measured usage to test conclusions. Team and radio employees are not independent confirmation. Attribute every report and follow aggregation to its origin.

## Files

- [registry.md](registry.md) — the schema-governed registry record (`bw-2026-sea-registry-001`): rotation, coverage lanes, handling rules, and `writer_ids`.
- [sources.csv](sources.csv) — one row per registered source with its stable `source_id`, class, priority, status, access, and handling note. Observations cite these IDs.
- [endpoints.csv](endpoints.csv) — retrievable URLs per source, with access level and automation suitability.
- [candidates.csv](candidates.csv) — the durable audit ledger: every candidate considered, with evidence, disposition (`include`, `exclude`, `unverified`), and verification date.

Refresh this directory using [SOURCE_REGISTRY_AUDIT.md](../../../../../../SOURCE_REGISTRY_AUDIT.md): ecosystem discovery, then a fresh adversarial omission pass, then construction and cross-file reconciliation. Never rename or delete a `source_id`; retire it with `status` and `ended_on` so historical frozen runs keep their provenance.

## Access limits

Retrieval behaviour observed on 2026-09-09. These are documented limitations, not reasons to drop
a source:

- `espn.com` article pages return a bot challenge to scripted requests but render through the
  standard fetch tool. They expose no article JSON-LD on that path, so only the displayed byline
  time (Eastern) is available; record the offset and say so in the observation note.
- `seahawks.com` article pages respond to scripted requests and carry usable article metadata, but
  the author archive at `/author/john-boyle` renders a profile with no article list. Reach a
  bylined item through the `/news/` index instead.
- `fox13seattle.com` responds normally and exposes clean article metadata.
- `seattletimes.com`, `thenewstribune.com` and The Athletic are paywalled. Summarise in original
  language and retain claim-level attribution; never reproduce paid text.

Per-outlet metadata extraction traps, as opposed to access, are recorded in the reader agent's
memory at [`.claude/agent-memory/reader/`](../../../../../../.claude/agent-memory/reader/).
