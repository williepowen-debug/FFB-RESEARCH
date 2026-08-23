# Preseason Game Intelligence Runbook

Use this runbook for preseason game monitoring. It extends `INTELLIGENCE_PIPELINE.md`; it does not
replace the reader, synthesis, ledger, or validation contracts.

## Purpose

Preseason game evidence is useful but easy to overread. The process goal is to preserve role,
availability, and usage signals while preventing short samples, reserve-on-reserve production, and
missing gamebooks from changing canonical team records too early.

## Default Shape

Run preseason games in two passes:

1. **Immediate pass**: same day or next morning. Use this for injuries, held-out starters, official
   inactive context, unexpected first-team exposure, obvious depth-chart shocks, and time-sensitive
   fantasy decisions.
2. **Completion pass**: 24 to 48 hours later, or later if data is delayed. Use this for gamebooks,
   participation, snaps, routes, carries, targets, first-read evidence, pass-rush packages, pressure
   charting, and independent postgame notebooks.

The immediate pass should normally be smaller. Do not use it to resolve route-share, backfield,
pressure-front, or coverage-role hypotheses unless the evidence is official, measured, and
complete enough to meet the promotion bar.

## Preflight

Before freezing assignments, copy `templates/preseason-game-preflight.txt` into the run directory as
`preflight.md`. ARCHITECT completes the checklist and decides whether the run is an immediate pass,
a completion pass, or a wait.

Required checks:

- official recap freshness and timestamp;
- inactive, unavailable, or held-out-starter context;
- NFL game center, gamebook, or official participation availability;
- snap, route, target, carry, alignment, or pressure data availability;
- independent timestamped postgame reporting;
- open team ledger triggers that could be resolved by the new evidence.

If gamebook, participation, and independent reporting are unavailable, default to an immediate
triage pass or wait. A zero-observation result is acceptable when the preflight explains the access
gap.

## Assignment Scope

Freeze assignments with `templates/reader-assignment.csv`. Put the pass type in `notes`, for
example `Pass: immediate` or `Pass: completion`.

Immediate-pass assignments should prioritize:

- official injuries and availability;
- starter participation or explicitly held-out starters;
- one-drive first-team usage only when unit context is clear;
- official transaction or depth-chart consequences;
- evidence that could affect same-week drafts, waivers, trades, or rankings.

Completion-pass assignments should start from open ledger rows and target only the sources needed
to resolve them. Include official or measured data before interpreting role changes.

## Synthesis Rules

Team syntheses must separate:

- starter versus reserve unit context;
- one-play production versus repeatable role;
- opponent-unit quality;
- held-out player effects;
- official facts versus team-employed interpretation;
- postgame recaps versus measured participation.

Use `log` for bounded depth evidence and isolated plays. Use `review` when the evidence could
change a hypothesis but still needs charting, healthy-unit context, or independent support. Use
`escalate` only for material, time-sensitive fantasy changes supported by official evidence,
measured usage, or strong independent reporting.

## Ledger-First Follow-Up

Every completion pass starts by reading open team ledger rows. If a trigger occurred, ARCHITECT
must resolve the row, promote the finding, or supersede it with a new row. If the trigger did not
occur, leave the row open and do not duplicate the same target.

Useful completion-pass targets include:

- `deferred/open` rows from the latest preseason game pass;
- zero-observation teams where source freshness blocked the first run;
- teams with held-out starters that invalidated the initial sample;
- open injury or availability triggers that affect Week 1 roles.

## Promotion Bar

Do not update canonical team offense, defense, player, or weekly records from preseason game
evidence unless one of these is true:

- the evidence resolves an open ledger trigger;
- official or measured usage changes a stable role assumption;
- a player availability change has direct weekly or draft consequences;
- independent reporting plus game context materially changes confidence in a hypothesis.

Otherwise preserve the evidence in the synthesis and team ledger.

## Closeout

Before closeout, run the normal intelligence validation gate:

```bash
python3 scripts/validate_intelligence.py
python3 scripts/generate_catalog.py
python3 scripts/validate_repository.py
python3 scripts/generate_catalog.py --check
git diff --check
```

The closeout report should say which pass ran, which ledgers were resolved or left open, which
teams still need a completion pass, and whether any canonical records changed.
