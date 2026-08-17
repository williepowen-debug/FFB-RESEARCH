# Strength Of Schedule Research

This workspace stores 2026 schedule-difficulty research for both real-football context and fantasy-football decision making.

Use this folder for league-wide schedule comparisons that cut across teams. Team-specific conclusions can later link back here from team overviews, weekly matchups, rankings, or player notes.

## Files

| File | Purpose |
|---|---|
| `sources.csv` | Source registry for schedule-strength inputs and methodology notes. |
| `overall-sos.csv` | Team-level schedule difficulty using broad team-strength measures. |
| `position-sos.csv` | Fantasy schedule difficulty by offensive position group. |
| `early-season-sos.csv` | First-five-played-games fantasy SOS for hot-start and cold-start targeting. |
| `playoff-sos.csv` | Fantasy playoff-window schedule difficulty by team and position. |
| `schedule-wrinkles.csv` | Non-opponent schedule friction: bye week, rest, travel, neutral sites, short weeks, and clusters. |
| `watchlists.csv` | Actionable schedule-derived player/unit watchlists with draft, streaming, sell-high, buy-low, and patience labels. |
| `adp-research.csv` | Source-attributed ADP, rank, and cost context for watchlist players and units. |
| `snapshots/` | Dated narrative interpretations that preserve what we believed at a point in time. |
| `changelog.md` | Chronological log of source/data/take changes and why they matter. |

## Research Layers

### 1. Real-Football SOS

Use this for broad team context, not direct fantasy valuation.

Recommended inputs:

- Prior-season opponent win percentage.
- Market or projection-based opponent strength.
- Current-season opponent strength once enough games have been played.
- Home/road split and neutral-site adjustments.

### 2. Fantasy Full-Season SOS

Use this for draft, trade, and roster construction work. Track each fantasy-relevant position separately:

- `QB`
- `RB`
- `WR`
- `TE`
- `DST`
- `K`, only if the league format makes kickers material
- `IDP`, only when the source methodology supports IDP

Preferred metric: average fantasy points allowed by 2026 opponents to the target position, adjusted for scoring format when available.

### 3. Fantasy Playoff SOS

Track the weeks that actually matter for the league format. Default windows:

- `weeks_14_17` for leagues with Week 14 quarterfinals or two-week playoff rounds.
- `weeks_15_17` for common fantasy semifinal/final windows.
- Avoid using Week 18 for managed redraft conclusions unless the league explicitly plays through Week 18.

### 4. Schedule Friction

Opponent quality is not the whole schedule. Track:

- Bye week timing.
- Thursday/short-week games.
- Teams coming off a bye.
- Consecutive road games.
- Cross-country travel.
- International or neutral-site games.
- Bad-weather venue exposure during fantasy playoffs.

## Interpretation Rules

- Separate measured facts from fantasy inference.
- Do not call a player a buy/sell based only on a team-level SOS rank.
- Prefer position-specific SOS over opponent win percentage for fantasy decisions.
- Recheck any fantasy SOS based on 2025 points allowed after enough 2026 data exists.
- Record scoring format. PPR, half-PPR, standard, best ball, DFS, and TE premium can point to different conclusions.
- Record the playoff window used. A team can have a difficult full season and a favorable playoff stretch, or the reverse.

## Versioning

Treat the CSVs as the current working data and the snapshots as dated research takes.

When the underlying data or interpretation changes:

1. Update the relevant CSV rows.
2. Add a dated note to `changelog.md`.
3. Add a new file under `snapshots/` when the change affects draft, waiver, trade, or ranking strategy.
4. Mark the prior take as superseded in the new snapshot rather than editing the old snapshot's conclusion.

Use these confidence labels in snapshots:

- `baseline`: preseason schedule-derived view; useful for targeting and watchlists, but not enough for standalone player recommendations.
- `confirmed`: supported by actual 2026 defensive or usage data.
- `superseded`: replaced by a later snapshot.

Promote a snapshot conclusion into a structured `research_finding` record only when it needs to be cited from team, player, weekly, or rankings work.

## Fill Order

1. Add source rows to `sources.csv`.
2. Add broad team-level rows to `overall-sos.csv`.
3. Add position-level full-season rows to `position-sos.csv`.
4. Add playoff-window rows to `playoff-sos.csv`.
5. Add schedule-friction rows to `schedule-wrinkles.csv`.
6. Promote stable conclusions into structured research records only after methodology and source coverage are clear.
