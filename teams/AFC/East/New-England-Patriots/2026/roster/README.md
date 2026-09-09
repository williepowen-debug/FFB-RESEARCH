# New England Patriots 2026 Roster Changes

Machine-readable transaction data supporting the 2026 module. Update status fields rather than deleting historical rows.

## Files

- [`departures.csv`](departures.csv): exits, releases, and outgoing trades, including cutdown releases that returned to the practice squad.
- [`veteran-additions.csv`](veteran-additions.csv): free-agent signings, incoming trades, waiver claims, and the practice-squad backs and punter elevated for Week 1. The `current_status_as_of_2026_08_05` header is the canonical cross-team column name; the values and `last_verified` reflect 2026-09-09.
- [`retentions.csv`](retentions.csv): re-signings and extensions (header only). The reported Christian Gonzalez extension (2026-09-07/08) is not yet rowed here; it is a reported fact in the [secondary finding](../defense/secondary.md).
- [`draft-class.csv`](draft-class.csv): all nine selections in the 2026 draft, with each pick's cutdown status.

## Headline changes

- Coming off a 2025 Super Bowl appearance, New England spent aggressively around Drake Maye.
- Traded for alpha receiver A.J. Brown (from Philadelphia, June 1) and signed Romeo Doubs; released Stefon Diggs; traded Kayshon Boutte to Houston on August 25 for safety Jaylen Reed and a 2028 seventh.
- Added guard Alijah Vera-Tucker and drafted tackle Caleb Lomu in Round 1; traded center Garrett Bradbury to Chicago. The official 2026-08-30 roster analysis lists the starting five as Will Campbell, Vera-Tucker, Jared Wilson, Mike Onwenu, and Morgan Moses, with Lomu a backup.
- Added edge Dre'Mont Jones and safety Kevin Byard; the only coordinator change is at defensive coordinator (Zak Kuhr for Terrell Williams).

## Late-August and Week 1 transactions (verified 2026-09-09)

- 2026-08-18: signed veteran interior lineman Greg Van Roten after Ben Brown was hurt in the preseason opener.
- 2026-08-25: traded WR Kayshon Boutte to Houston for S Jaylen Reed and a 2028 seventh-round pick.
- 2026-08-28 (transaction log 08/29): acquired RB Corey Kiner from Arizona for a 2028 seventh-round pick; released RB Hassan Haskins.
- 2026-08-30: initial 53-man roster set; 36 players released, including RB Jam Miller, OT James Hudson III, LB Bradyn Swinson, CB Kindle Vildor, and S Mike Brown; acquired OL Walter Rouse and a 2027 seventh from Minnesota for a 2027 sixth.
- 2026-08-31: claimed TE Cameron Latu (Philadelphia) and LB Darius Muasau (New York Giants) off waivers; released LB K.J. Britt and C Ben Brown (procedural); placed P Bryce Baringer and LB Khalil Jacobs on injured reserve; signed twelve players to the practice squad, including Larison, Haskins, Vildor, Mike Brown, and P Mitch Wishnowsky.
- 2026-09-01: re-signed C Ben Brown and LB Erick Hunter to the 53; Britt to the practice squad.
- 2026-09-09: elevated RB Lan Larison and P Mitch Wishnowsky for Week 1 at Seattle.

## Reserve lists as of 2026-09-09

| Player | Position | List | Date | Minimum absence | Source |
|---|---|---|---|---|---|
| Harold Landry III | EDGE/LB | Reserve/PUP | 2026-08-30 | four games; has not practiced this season | [official cutdown announcement](https://www.patriots.com/news/patriots-make-roster-moves-to-reach-the-53-man-roster-limit-x3970), [roster analysis](https://www.patriots.com/news/analysis-breaking-down-the-patriots-initial-53-man-roster-for-the-2026-season) |
| Marcus Bryant | OT | Injured reserve (designated to return) | 2026-08-30 | four games | same |
| Brenden Schooler | S/ST | Reserve/NFI | 2026-08-30 | four games | same |
| Bryce Baringer | P | Injured reserve | 2026-08-31 | four games | [official 2026-08-31 moves](https://www.patriots.com/news/patriots-make-a-series-of-transactions-practice-squad) |
| Khalil Jacobs | LB | Injured reserve | 2026-08-31 | four games | same |
| Julian Hill | TE | Injured reserve | before 2026-09-09 (placement date not retrieved) | four games | [official roster page](https://www.patriots.com/team/players-roster/) |
| Myles Montgomery | RB | Injured reserve | before 2026-09-09 (placement date not retrieved) | four games | official roster page |
| Jeremiah Webb | WR | Injured reserve | before 2026-09-09 (placement date not retrieved) | four games | official roster page |

Week 1 injury designations (Henderson OUT, Ben Brown OUT, Barmore no designation) live in the weekly record, not here.

Colleges are populated where confirmed by the official draft page or reputable recaps; a blank college field marks a value not yet verified to source standard.

Last verified: 2026-09-09 against the [official transaction log](https://www.patriots.com/team/transactions/), the [official roster page](https://www.patriots.com/team/players-roster/), and the dated announcements linked in each CSV row.
