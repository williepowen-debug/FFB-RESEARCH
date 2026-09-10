# NE–SEA evidence audit: methods and provenance

Supporting data for the [September 9 audit finding](../../../games/NE-at-SEA-evidence-audit.md).
Historical season: **2025**, including postseason through February 8, 2026. Collected September 9,
2026 ET after the scheduled Week 1 kickoff. No 2026 game-play observations are included.

## Inputs and reproduction

[context-provenance.json](context-provenance.json) records the five exact download URLs, SHA-256
hashes and computation timestamp. Save those inputs locally and run:

```bash
python3 weekly/2026/week-01/research/ne-sea/audit/compute_context.py PBP.csv.gz FTN.csv PFR_SEASON.csv PFR_WEEK.csv NGS.csv.gz OUTPUT_DIRECTORY
```

The script uses Python's standard library and imports the corrected [baseline filter](../compute_baseline.py).
Both scripts exclude two-point attempts explicitly: these rows can contain finite EPA. The
previous baseline admitted them; this audit regenerates that baseline and its cited tables.
Stevenson's 37 ordinary targets now agree with the earlier vendor count. The temporary 38-target
interpretation was a filter error, not an unresolved source disagreement.
Upstream release assets can change: compare input hashes before claiming exact reproduction.
CSV output is deterministic for identical inputs; the manifest computation time changes.

| Output | Definition and limits |
|---|---|
| [FTN tendencies](ftn-tendencies.csv) | Matched 2025 run/pass plays with finite EPA, excluding kneels/spikes/deleted plays and two-point attempts. Under center uses known U/S/P locations; motion uses known flags; play action uses known flags on dropbacks. Report missing fields separately. |
| [FTN rusher splits](ftn-rusher-splits.csv) | Dropbacks grouped by actual charted rusher count: 1–3, 4, 5+, and 0/unknown. Sacks/dropbacks is a sack rate, **not pressure rate**. The subjective QB-fault flag is retained for transparency, not adopted as blocker responsibility. |
| [Scoring opportunities](historical-scoring-opportunities.csv) | Plays starting at the opponent's 20/5 or closer; designed carries exclude scrambles, targets require an assigned receiver. Counts are historical opportunities, not routes or 2026 role shares. |
| [Opponent context](opponent-context.csv), [detail](opponent-detail.csv) | One-step adjustment described below; regular season only. |
| [PFR pressure](pfr-pressure.csv), [reconciliation](pfr-reconciliation.csv) | Source pressures, hits, hurries and sacks. Preserve published pressure percentage; sacks/pressures is separately calculated. Maye season versus weekly pressure counts conflict by one. |
| [NGS passing](ngs-passing.csv) | NFL Next Gen Stats via nflverse; 2025 REG week=0 season aggregates for the two QBs. Time to throw differs from PFR pocket time and from snap pace. |
| [Stevenson postseason](stevenson-postseason.csv) | All four NE playoff games. Box-score filter retains valid run/pass/kneel/spike play types, excludes two-point attempts; sums official rushing/receiving fields. This differs deliberately from the EPA filter. |

The script verifies 272 regular-season games, unique FTN keys, complete NE/SEA eligible-play joins,
PFR sack reconciliation and within-source pressure components. POST includes the Super Bowl;
POST and SB are overlapping views. They must never be summed as independent samples.

Opponent adjustment: for each opponent, calculate its relevant unit's EPA against every **other**
team, excluding all games against the focal team. Weight those baselines by the focal team's
eligible plays against that opponent. Subtract `(weighted opponent EPA − league EPA)` from the
focal team's raw EPA. Defense is expressed as opponent offensive EPA: lower is better.
This is a descriptive schedule check, not a fitted predictive model. It does not adjust for
opposing QB availability, changed lineups, venue, injuries or game state, and supplies no win
probability or uncertainty interval. Do not replace raw results with this number silently.

## Source definitions and reuse

- [nflverse play-by-play dictionary](https://nflreadr.nflverse.com/articles/dictionary_pbp.html).
- [FTN loader](https://nflreadr.nflverse.com/reference/load_ftn_charting.html) and
  [dictionary](https://nflreadr.nflverse.com/articles/dictionary_ftn_charting.html).
- [PFR advanced-stat loader](https://nflreadr.nflverse.com/reference/load_pfr_advstats.html) and
  [passing dictionary](https://nflreadr.nflverse.com/articles/dictionary_pfr_passing.html).
- [NGS loader](https://nflreadr.nflverse.com/reference/load_nextgen_stats.html).

**FTN Data via nflverse**, licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
The two `ftn-*.csv` files and FTN-derived tables/figures in the linked finding are adaptations
under that license: changes are filtering, joining to play-by-play, grouping and calculating
counts/rates. This statement does not relicense unrelated repository material.

PFR's original web table returned an access restriction; these are explicitly its archived
nflverse snapshots, not a claim of direct webpage verification. NFL/NGS is the same origin when
quoted by a team reporter; nflverse hosting does not create an additional independent source.
FTN and PFR use different charting definitions. Never splice their denominators together.

## Official player-table audit

[Official biography provenance](official-biography-provenance.csv) identifies 19 downloaded club
biographies, original URLs, retrieval date and HTML hashes. [Career counts](official-career-counts.csv)
contains 87 normalized season/career rows for 18 players; Price has no completed NFL season row.
HTML table headings were checked before mapping duplicated ATT/YDS/TD columns to passing,
rushing or receiving. Career sums were checked wherever all annual fields were populated.
Source blanks remain blank, not independently verified zeros. Club labels can use current
franchise names for historical seasons (for example, Chargers); they do not establish relocation dates.

Available count fields in the corresponding profiles were compared with these snapshots:
564 displayed count cells matched after correction (including GP/GS and populated fumble fields).
Targets, return tables, college history, passer ratings, contracts, scouting claims and most
postseason lines are outside this NFL count audit. Prior source labels remain historical
attributions where the club table lacks the field. Price's complete 2025 college production was
separately checked against Notre Dame's official biography; older college rows remain qualified.

[Source rate conflicts](source-rate-conflicts.csv) preserves 11 career receiving-average displays
that disagree with the publisher's own yards/receptions. Use count-based arithmetic rounded to
one decimal (half up), not the inconsistent display. This does not claim every published rate
was audited. Original HTML is not committed; hashes identify the captured versions, while the
normalized facts and original source URLs provide the reviewable snapshot.

## Unavailable measures

The selected play-by-play has no usable NE/SEA play-clock sample (all selected values are zero).
Time to throw is not pace. FTN supplies motion, QB location and play action here, but no complete
11/12/21 personnel, individual blocker-loss/quick-pressure, coverage-assignment or route chart.
Those remain unknown until a compatible charted source or identifiable full-game film is available.
