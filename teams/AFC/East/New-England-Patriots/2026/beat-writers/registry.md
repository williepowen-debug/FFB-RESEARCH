---
schema_version: 1
record_id: bw-2026-ne-registry-001
record_type: beat_writer_registry
title: "New England Patriots 2026 Source Registry"
team_ids: ["NE"]
player_ids: []
season: 2026
week: null
status: active
time_horizon: seasonal
valid_as_of: 2026-09-09
last_verified: 2026-09-09
confidence: high
source_ids: []
supersedes: []
writer_ids: ["local-writer-mike-reiss", "local-writer-andrew-callahan", "local-writer-doug-kyed", "local-writer-christopher-price", "local-writer-nicole-yang", "local-writer-ben-volin", "local-writer-chad-graff", "local-writer-mark-daniels", "local-writer-greg-bedard", "local-writer-mike-giardi", "local-writer-phil-perry", "local-writer-tom-curran", "local-writer-taylor-kyles", "local-writer-brian-hines", "local-writer-bernd-buchmasser", "local-writer-evan-lazar", "local-writer-paul-perillo", "local-writer-alex-barth"]
---

# New England Patriots 2026 Source Registry

This registry prioritizes sources that can establish or explain changes in availability, role,
usage, scheme, and roster construction. See [sources.csv](sources.csv),
[endpoints.csv](endpoints.csv), [candidates.csv](candidates.csv), and the
[monitoring guide](README.md).

This rotation was rebuilt on 2026-09-09 under `SOURCE_REGISTRY_AUDIT.md`. The prior version was a
legacy 10-source registry with no candidate ledger; the audit re-verified every existing entry and
added the outlets and specialist lanes it had missed.

## Essential monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| New England Patriots communications | New England Patriots | official | Transactions, roster, injury reports, transcripts, practice reports | Source of record for team announcements; team-produced analysis is not independent |
| NFL gamebooks and participation records | NFL | official | Participation, starters, statistics, play-by-play | Preferred postgame source of record |
| Mike Reiss | ESPN NFL Nation | reporting | Daily beat reporting, availability, roster and organizational context | ESPN bio re-verified as its Patriots NFL Nation reporter |
| Chad Graff | The Athletic | reporting | Sourced beat reporting, organization, roster and coaching context | Paywalled; separate reporting from podcast opinion |
| Andrew Callahan | Boston Herald | reporting | Practice observations, roster, scheme and sourced reporting | Separate reported facts from columnist analysis |
| Doug Kyed | Boston Herald | reporting | Highest-volume daily beat, personnel, transactions and league sourcing | Date podcast claims and corroborate consequential reports |
| Christopher Price | Boston Globe | reporting | Training-camp observations, personnel and team context | Globe content is paywalled; summarize in original language |
| Nicole Yang | Boston Globe | reporting | Beat reporting, player roles, roster moves and features | Favor direct observations and sourced facts for role conclusions |
| Mark Daniels | MassLive | reporting | Daily beat and camp-day reporting, injuries and roster | masslive.com blocks automated retrieval; open in a browser |
| Greg A. Bedard | Boston Sports Journal | reporting | Independent subscription reporting, organization and scheme | Subscription; separate reporting from column framing |
| Phil Perry | NBC Sports Boston | reporting | Snap, role and usage interpretation; free and high cadence | Distinguish projection from reported fact |
| Taylor Kyles | CLNS Media | film_analysis | All-22 film, scheme, roles and daily camp reports | Analysis, not a reporting substitute |
| Evan Lazar | New England Patriots (Patriots.com) | film_analysis | Detailed film, matchup and injury-report analysis | Team-employed; corroborate consequential role conclusions |

## Valuable monitoring

| Name or source | Outlet | Source class | Primary value | Handling note |
|---|---|---|---|---|
| Ben Volin | Boston Globe | reporting | Senior NFL reporting and Patriots organizational context | Commentary is not transaction confirmation |
| Mike Giardi | Boston Sports Journal | reporting | Second credentialed subscription reporter; practice observation | Subscription; shares the BSJ byline with Bedard |
| Tom E. Curran | NBC Sports Boston | reporting | Organizational sourcing and contract-negotiation context | Often framed as perception; time-stamp audio and video |
| Brian Hines | Pats Pulpit | reporting | Film breakdown, snap counts, roster and draft study | Fan-facing outlet; separate observation from advocacy |
| Bernd Buchmasser | Pats Pulpit | contract_data | Salary cap, contracts and roster mechanics | Third-party interpretation; cross-check Over the Cap |
| Paul Perillo | New England Patriots (Patriots.com) | team_analysis | Numbered daily practice observations and rep detail | Team-employed; omissions are editorial choices |
| Alex Barth | 98.5 The Sports Hub | reporting | Sports-radio lane, firsthand camp notebooks, podcast | Domain blocks automated retrieval |
| Patriots Unfiltered | New England Patriots | team_analysis | Practice discussion, interviews and team context | Team-produced; time-stamp audio claims |
| Pro Football Reference | Sports Reference | data | Game logs, snap counts and historical splits | Manual retrieval; verify consequential discrepancies |
| Over the Cap | Over the Cap | contract_data | Contracts, cap charges, dead money, roster mechanics | Unofficial terms; treat as an estimate |

## Coverage lanes

| Lane | Covered by |
|---|---|
| Official record | Patriots communications; NFL gamebooks |
| Daily independent beat | Reiss; Graff; Callahan; Kyed; Price; Yang; Daniels; Bedard; Giardi |
| National or major local reporting | Reiss; Graff; Volin |
| Local television and radio | Perry; Curran (NBC Sports Boston); Barth (98.5 The Sports Hub) |
| Film and scheme analysis | Kyles; Lazar; Hines |
| Position usage and fantasy signal | Perry; Kyles; Perillo; Pro Football Reference |
| Transactions and organization | Buchmasser; Over the Cap; Kyed; Graff; Curran |
| Team-controlled analysis | Patriots Unfiltered; Lazar; Perillo |

No lane is uncovered. The contract and cap lane is carried by Over the Cap and Bernd Buchmasser
rather than by a dedicated independent cap specialist: Miguel Benzan (@patscap) remains the
best-known Patriots cap analyst and his 2026 projections are quoted elsewhere, but no current
primary outlet page for him could be verified, so he is logged as `unverified` in
[candidates.csv](candidates.csv) and no lane depends on him.

## Reliability history

The rotation was audited and rebuilt on 2026-09-09. Priority reflects verified role, access and
differentiation, not a blanket reliability grade. No repo-local record of confirmed early reports,
corrections, or misses has been accumulated yet.

### Mike Reiss

- Strongest coverage areas: roster status, availability, organizational context, daily beat reporting.
- Known limitations: national-platform articles may be updated after initial publication; ESPN article pages intermittently refuse automated retrieval.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified assignment and access.
- Evidence for assessment: the ESPN Press Room biography identifies Reiss as "NFL Nation Reporter: New England Patriots", re-verified 2026-09-09.

### Chad Graff

- Strongest coverage areas: sourced organizational reporting, roster construction, coaching context.
- Known limitations: paywalled; podcast opinion sits alongside reported work.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified assignment.
- Evidence for assessment: The Athletic's author page states he has been its senior writer covering the Patriots since 2022 and won the PFWA's 2022 Bob Oates beat-writing award, verified 2026-09-09.

### Boston Herald beat rotation

- Strongest coverage areas: practice observation, personnel competition, transactions and scheme.
- Known limitations: reporting and analysis can appear in the same article or podcast; the domain refuses the standard fetch tool.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current beat assignments.
- Evidence for assessment: Callahan's Herald author bio states he became the Herald's Patriots beat writer in 2019, and Callahan and Kyed together account for 88 of the Patriots bylines on the Herald's Week 1 team landing page, verified 2026-09-09.

### Boston Globe beat rotation

- Strongest coverage areas: camp observation, player roles, roster and organizational context.
- Known limitations: paywall; multiple bylines require claim-level attribution.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on current beat assignments.
- Evidence for assessment: current Globe staff profiles and the Globe Patriots landing page carry Price, Yang and Volin bylines through the 2026 season preview, verified 2026-09-09.

### Independent and subscription reporting

- Strongest coverage areas: organizational sourcing, practice observation, coaching intent.
- Known limitations: Boston Sports Journal is a subscription outlet whose search and author pages sit behind a verification wall; MassLive refuses automated retrieval entirely.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; essential based on verified assignments.
- Evidence for assessment: BSJ's front page carries a Bedard column dated 2026-09-09 and a Bedard/Giardi Week 1 on-site credit from Lumen Field; MassLive's 2026-09-09 staff predictions piece identifies Mark Daniels as its Patriots beat reporter.

### Film, usage and cap specialists

- Strongest coverage areas: alignment and scheme detail, rep and rotation counts, cap mechanics.
- Known limitations: Lazar and Perillo are team-employed; Kyles, Hines and Buchmasser work at fan-facing outlets; none is a substitute for reported fact.
- Confirmed early reports: none scored yet.
- Corrections or misses: none scored yet.
- Current reliability assessment: unscored; carried for differentiated analysis the beat rotation does not supply.
- Evidence for assessment: CLNS identifies Kyles as its lead NFL analyst covering schemes and tendencies through a Patriots lens and his author archive carries numbered 2026 camp reports; the Pats Pulpit masthead lists Hines as its beat writer and Buchmasser as site manager with a stated cap specialty, both publishing on 2026-09-09; the Patriots.com author pages for Lazar and Perillo carry current Week 1 and Day 20 camp output.

## Usage notes

Start with official records, then use independent practice reporting to explain changes and game
usage to test whether preseason observations held. Attribute the individual reporter rather than
only the outlet. For a material fantasy conclusion, prefer one official or measured source plus
one independent reporting source; do not let a team-controlled source (Lazar, Perillo, Patriots
Unfiltered) stand alone on a role or availability conclusion. Time-stamp podcast and live-blog
claims. Shared podcast appearances between outlets are not corroboration. When a source's domain
blocks automated retrieval, record the access limit rather than dropping the claim.
