# September 6 league catch-up preflight

- Run: `20260906T193157Z`
- Frozen publication window: `2026-08-29T14:33:49Z` through `2026-09-06T19:31:57Z`.
- Scope: all 32 teams; one registered official source and one registered essential beat source per team, as frozen in assignments.csv.
- Pass: news catch-up covering roster transactions, availability, roles, and previously deferred evidence.
- ARCHITECT reviewed all 20 open ledger rows before freezing assignments. Priorities include MIA/CLE receiver transactions, NYG kicker confirmation, DEN mobility and usage, CAR backfield/receivers/Waller, NO line and skill roles, ARI availability, SF line/receiver roles, ATL usage, TEN allocation, and DET/WAS defensive usage. Also recheck prior promoted DET Pacheco and SF Kittle availability.
- Maximum 20 atomic observations per team; this is a cap, not a quota.
- Publication timestamps must belong to the exact source item; retrieval times are recorded separately. Missing or out-of-window dates do not support admission.
- Readers report actual source access; inaccessible evidence is a coverage gap, never evidence of no news.
- No rankings or lineup changes without reconciled evidence and a ledger disposition.
- Validation: validate_intelligence.py, validate_schedule.py, generate_catalog.py, validate_repository.py, generate_catalog.py --check, git diff --check.
