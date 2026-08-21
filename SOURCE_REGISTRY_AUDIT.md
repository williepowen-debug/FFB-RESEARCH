# Source Registry Completeness Audit

Use this process whenever a team source registry is created or materially refreshed. The goal is
not merely to list familiar beat writers. It is to capture the smallest dependable source rotation
that covers every fantasy-relevant information lane without confusing access, reporting, analysis,
or team-controlled content.

## Required outputs

The published team directory contains `README.md`, `registry.md`, `sources.csv`, and
`endpoints.csv`. During discovery, copy
`templates/beat-writer-candidate-ledger.csv` to a temporary working file. The ledger is an audit
tool, not a required published artifact, but every plausible candidate must receive a disposition
before the registry is considered complete.

Allowed dispositions are:

- `include`: current, differentiated, and useful enough for essential or valuable monitoring.
- `exclude`: evaluated but redundant, inactive, insufficiently original, or outside scope. Record
  the reason.
- `unverified`: potentially useful but current assignment or original work is not yet established.
  A registry cannot close with an important lane depending on an unverified candidate.

## Coverage-lane matrix

Fill every lane with at least one included source, or explicitly record why the lane is unavailable
or immaterial for that team.

| Lane | What qualifies |
|---|---|
| Official record | Team roster, transactions, injury reports, depth charts, press conferences, and NFL gamebooks |
| Daily independent beat | Credentialed practice access, injuries, personnel usage, and locker-room reporting |
| National or major local reporting | Independent organizational sourcing and broader league context |
| Local television and radio | Original interviews, breaking news, or repeated firsthand camp observation |
| Film and scheme analysis | Evidence-based review of roles, alignments, blocking, routes, coverages, and coaching design |
| Position usage and fantasy signal | Reps, rotations, packages, targets, carries, and role competition interpreted for fantasy questions |
| Transactions and organization | Contracts, cap, roster mechanics, front-office decisions, and ownership or coaching context |
| Team-controlled analysis | In-house notebooks, interviews, broadcast analysis, and direct press-conference feeds, clearly labeled non-independent |

A single source may fill several lanes. Filling a lane does not automatically justify inclusion:
the source must still add information not reliably supplied by a stronger source.

## Discovery sequence

1. **Establish the current beat.** Search the current season, recent camp, and outlet staff or
   author pages. Verify assignments using an outlet biography or repeated current bylines; do not
   rely on reputation, social profiles alone, or last season's beat.
2. **Map the outlet ecosystem.** Inspect the major newspaper, national outlet, local television,
   sports radio, independent subscription network, official team site, and established specialist
   communities. Search the outlet's staff/about page as well as its team landing page.
3. **Search by information lane.** Use combinations such as:
   - `<team> credentialed reporter <season>`
   - `<team> training camp observations <season>`
   - `<team> film breakdown` or `<team> scheme analysis`
   - `<team> daily podcast` and `<team> newsletter`
   - `<team> roster contracts transactions reporter`
   - `<team> official press conferences` and `<team> official film breakdown`
4. **Verify differentiated value.** Find current examples showing original reporting, firsthand
   observation, interviews, or substantive analysis. Aggregation and fandom alone do not qualify.
5. **Classify independence and handling.** Separate reporting from opinion, analysis from fact,
   and team-controlled access from independent confirmation. Note paywalls and corroboration needs.
6. **Record departures and replacements.** Preserve useful former-role context in `sources.csv`,
   but never present an old assignment as current.

## Adversarial omission pass

After drafting the registry, start a fresh search intended to disprove its completeness:

- Search `best <team> reporters`, `best <team> podcast`, and `best <team> film analysis`.
- Inspect current training-camp attribution threads and fan/community recommendations as discovery
  leads. They are not sufficient evidence by themselves; verify candidates at primary outlets.
- Search each known outlet for other current contributors and recurring co-hosts.
- Ask which source would reveal a role change first if every listed beat writer missed it.
- Compare the new candidate list against the registry and disposition every new name.

This pass must be conducted after the initial registry exists. Repeating the original queries does
not count.

## Completion gates

### Coverage gate

Every matrix lane has an included source or a written `unavailable`/`immaterial` explanation. The
rotation includes both official records and independent reporting, plus differentiated analysis
where it exists.

### Candidate gate

Every plausible candidate is marked `include`, `exclude`, or `unverified` with evidence and a
reason. No important lane depends on an unverified candidate. Every included source appears in
`sources.csv`, has at least one usable endpoint in `endpoints.csv`, and is represented consistently
in `registry.md` and `writer_ids` when the source is a person.

## Closeout

Run the adversarial pass once more after edits, then regenerate the catalog and execute the full
repository validation gate in `TEAM_BUILD.md`. In the work summary, name any sources added by the
omission pass and any lane explicitly left unavailable. Never claim that a registry contains every
possible voice; claim that all defined lanes and plausible current candidates were audited.
