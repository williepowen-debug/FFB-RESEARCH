# ARCH handoff — NE at SEA pre-kickoff pass, September 9

## Completed

- Frozen two-team run `20260909T210706Z`: NE and SEA; publication window 2026-09-06T21:07:15Z through 2026-09-09T21:07:06Z, contiguous with the September 6 supplemental readiness window. Preflight, assignments, and active-source selection are in this directory.
- Readers: 24 atomic observations (NE 12, SEA 12, both at the cap), eight source reports, all eight sources `checked`. Overflow withheld at the cap is documented in each run report; none of it adds a claim beyond the rowed clusters.
- ARCHITECT spot checks: six observations re-verified against their sources (NE `-001`, `-008`, `-009`; SEA `-001`, `-006`, `-011`), covering an official item, an independent reported item, and a provenance-sensitive item per team. Zero failures; every publication timestamp matched the item's own metadata.
- Syntheses: [NE](../../syntheses/2026-09-09/NE.md) (12 rows, 9 clusters, 1 escalate, 1 review) and [SEA](../../syntheses/2026-09-09/SEA.md) (12 rows, 10 clusters, 0 escalate, 4 review). [Priority board](../../priority/2026-09-09/priority-board.csv): 6 rows.
- Ledger dispositions: NE 3 rows (1 promoted, 2 deferred); SEA 5 rows (2 promoted, 3 deferred). The September 6 board rows `sig-2026-ne-20260906-001`, `-002`, and `sig-2026-sea-20260906-001` are resolved; their next checks are answered by this run.
- Promotion: [`wm-2026-w01-ne-sea-001`](../../../../weekly/2026/week-01/games/NE-at-SEA.md) now carries both teams' final designations, elevations and roster moves, the reported depth orders, an updated decision table, and betting context. No seasonal team record, hypothesis row, or player record changed.

## Decision changes

| Change | Current treatment |
|---|---|
| NE Henderson | OUT (official). Do not start. Stevenson leads by availability; Kiner and Larison behind. Week 1 usage is a Henderson-absent sample and does not test the timeshare. |
| NE line | Ben Brown OUT is a reserve loss; starting five reported intact by the team site only. |
| SEA safeties | Okada OUT; Emmanwori questionable and reported unlikely. Thomas or Finley expected beside Love. Seasonal safety hypothesis and secondary finding held pending usage. |
| SEA backfield | Full healthy group available; no split established. Price decision row updated; seasonal hypothesis held. |
| SEA Horton | Questionable; inactive list decides whether route-share readings are against a thinner room. |

## News sweep and market context

- A broad web sweep at about 21:20Z found no injury or role item beyond the registered-source batches; every outlet recirculates the same official designations. One search hit about a Seattle "offensive anchor" was a January 2026 playoff story and was discarded.
- Game-day inactive lists post at about 6:50 PM ET and were not available.
- Betting context (DraftKings via ESPN, FanDuel, VSiN) is recorded in the matchup record as unregistered market framing, not evidence. Spread SEA -3 to -3.5, total 44.5; Stevenson is the shortest anytime-TD price.

## Coverage limits and next pass

- Boston Herald pages are blocked for the fetch tool but readable by direct HTTP; ESPN served a bot challenge on one page, so one ESPN timestamp is byline display time. Both are recorded in the run reports and observation notes.
- No SEA player profiles exist in `players/`, so `player_ids` are blank for both batches.
- Next pass is the postgame pilot in [usage-tracking.md](../../../../weekly/2026/week-01/usage-tracking.md): immediate factual triage after the final, then the gamebook-first completion pass. Open deferred ledger rows to target: `til-2026-ne-20260909-002`, `-003`; `til-2026-sea-20260909-002`, `-003`, `-005`.

## Validation

Schedule, intelligence, repository, catalog-current and whitespace checks are run at closeout; results are in the pull request.
