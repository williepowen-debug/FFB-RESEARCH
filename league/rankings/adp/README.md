# ADP Snapshots

Date-stamped market-price snapshots pulled by `scripts/fetch_adp.py`. Each run writes
new dated CSVs; never overwrite or hand-edit a prior snapshot — history is the point.

## Files

- `<date>-ffc-<N>team-<scoring>.csv` — Fantasy Football Calculator public API.
  Real drafts in the named format; includes `high`/`low`/`stdev` per player, which
  supports availability-window math for specific draft slots.
- `<date>-espn-adp.csv` — ESPN fantasy read API. `espn_live_adp` is where ESPN
  drafters actually take players; `espn_ppr_rank`/`espn_standard_rank` are the
  default lobby list ESPN displays, which anchors casual rooms.

## Interpretation rules

- These are market prices, not values. League-specific value (custom scoring)
  is computed in league-format records under `league/scoring-formats/`.
- Compare `espn_live_adp` against `espn_ppr_rank` to see where ESPN drafters
  already bump players off the default list; compare both against FFC to see
  platform bias.
- Cite the snapshot date and sample window when quoting a price in a record.

## Refresh

```bash
python3 scripts/fetch_adp.py            # 12-team PPR, current year
python3 scripts/fetch_adp.py --scoring half-ppr --teams 10
```
