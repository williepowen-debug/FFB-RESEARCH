# Agent memory

Persistent, file-based memory written by the desk agents defined in [`../agents/`](../agents/).
Each subdirectory is one agent role; `MEMORY.md` inside it is the index loaded at the start of
that agent's runs, and the sibling files hold one durable note each.

This directory is tracked deliberately. The notes are operational knowledge that is expensive to
rediscover — which outlets block the fetch tool and need a direct HTTP request, where each site
records the real publication timestamp, and how ARCHITECT calibrates routing levels — so keeping
it in the repository carries it to other machines and to fresh clones rather than stranding it on
whichever laptop happened to run the agent.

## What belongs here

- Retrieval mechanics for registered sources: blocked endpoints, working workarounds, where
  publication metadata actually lives, per-outlet parsing traps.
- Calibration and hand-off expectations between roles, with the reason recorded.

## What does not

This is a public repository, so [`../../SOURCE_POLICY.md`](../../SOURCE_POLICY.md) applies in
full: no credentials, no private league information, no personal data, and no paywalled article
text. Source *identity and access* notes are fine; copied article bodies are not.

Repository state does not belong here. Roster contents, which records exist, and how many sources
a registry holds are all queryable, and a note asserting them will drift out of sync silently. A
note in this directory once claimed the repository had no Seattle player profiles; seven were
added later the same day, and the note would have told the next reader run to leave `player_ids`
blank. Record mechanics and judgment, which do not rot that way.

Access and blocking behaviour also does not belong here. It lives in each team's
`beat-writers/README.md` under `## Access limits` and in the `handling_note` column of that
directory's `sources.csv`, next to the source it describes and under review. Keeping a second copy
here guarantees the two will diverge.

Durable research conclusions do not belong here either. Those go to the team modules, `players/`,
or `weekly/` as schema-governed records. Agent memory is about how to do the work, not what the
work concluded. Note dates and re-verify a quirk when a fetch starts behaving differently.
