# Players

This directory holds canonical player records independent of current team assignment.

Use `players/<player-name>/profile.md` and start from `templates/player-profile.md`. Team depth charts and weekly files should link to the canonical profile. Record trades, releases, and other team changes in the profile history instead of creating competing profiles.

Each profile carries a stable `player_ids` entry (`local-player-<name-slug>-<first-known-year>`) that team findings, weekly records, and intelligence observations use to reference the player. Assign that ID once and never reuse it.

Known metadata inconsistency: profiles created on 2026-09-09 populate `team_ids` with the player's current club, while the twelve earlier profiles leave it empty. A team filter over `catalog.jsonl` therefore returns only the newer records. Backfill the legacy profiles on their next verification pass rather than in bulk, since each one needs its current team re-verified first. The dashes in the table below mark that gap.

## Index

| Player | Pos | Team | Last verified | Confidence |
|---|---|---|---|---|
| [AJ Barner](aj-barner/profile.md) | TE | SEA | 2026-09-09 | medium |
| [A.J. Brown](aj-brown/profile.md) | WR | NE | 2026-09-09 | high |
| [Ashton Jeanty](ashton-jeanty/profile.md) | RB | — | 2026-08-26 | high |
| [Bijan Robinson](bijan-robinson/profile.md) | RB | — | 2026-08-17 | high |
| [Cooper Kupp](cooper-kupp/profile.md) | WR | SEA | 2026-09-09 | medium |
| [Corey Kiner](corey-kiner/profile.md) | RB | NE | 2026-09-09 | medium |
| [DeMario Douglas](demario-douglas/profile.md) | WR | NE | 2026-09-09 | medium |
| [Drake London](drake-london/profile.md) | WR | — | 2026-08-17 | high |
| [Drake Maye](drake-maye/profile.md) | QB | NE | 2026-09-09 | high |
| [Elijah Arroyo](elijah-arroyo/profile.md) | TE | SEA | 2026-09-09 | medium |
| [Emanuel Wilson](emanuel-wilson/profile.md) | RB | SEA | 2026-09-09 | medium |
| [George Holani](george-holani/profile.md) | RB | SEA | 2026-09-09 | medium |
| [George Kittle](george-kittle/profile.md) | TE | — | 2026-08-26 | high |
| [Hunter Henry](hunter-henry/profile.md) | TE | NE | 2026-09-09 | medium |
| [Jadarian Price](jadarian-price/profile.md) | RB | SEA | 2026-09-09 | medium |
| [James Cook III](james-cook/profile.md) | RB | — | 2026-08-20 | high |
| [Jaxon Smith-Njigba](jaxon-smith-njigba/profile.md) | WR | SEA | 2026-09-09 | high |
| [Jeremiyah Love](jeremiyah-love/profile.md) | RB | — | 2026-08-26 | medium |
| [Josh Allen](josh-allen/profile.md) | QB | — | 2026-08-20 | high |
| [Josh Sweat](josh-sweat/profile.md) | Edge defender | — | 2026-08-26 | high |
| [Kyle Pitts Sr.](kyle-pitts/profile.md) | TE | — | 2026-08-17 | high |
| [Kyle Williams](kyle-williams/profile.md) | WR | NE | 2026-09-09 | medium |
| [Makai Lemon](makai-lemon/profile.md) | WR | — | 2026-08-26 | medium |
| [Malik Nabers](malik-nabers/profile.md) | WR | — | 2026-08-26 | high |
| [Mike Evans](mike-evans/profile.md) | WR | — | 2026-08-26 | high |
| [Rashid Shaheed](rashid-shaheed/profile.md) | WR (KR/PR) | SEA | 2026-09-09 | medium |
| [Rhamondre Stevenson](rhamondre-stevenson/profile.md) | RB | NE | 2026-09-09 | medium |
| [Romeo Doubs](romeo-doubs/profile.md) | WR | NE | 2026-09-09 | medium |
| [Sam Darnold](sam-darnold/profile.md) | QB | SEA | 2026-09-09 | high |
| [TreVeyon Henderson](treveyon-henderson/profile.md) | RB | NE | 2026-09-09 | medium |
| [Zach Charbonnet](zach-charbonnet/profile.md) | RB | SEA | 2026-09-09 | medium |
