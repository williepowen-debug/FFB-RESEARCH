# Intelligence workspace

This directory stores normalized reader batches, dated team synthesis snapshots, and league-level
priority queues. Read [the operating contract](../INTELLIGENCE_PIPELINE.md) before creating data.

Create season/run directories only when a real collection run begins. Do not commit credentials,
full-text article exports, or copied subscription content.

The first three-team trial follows [the manual pilot runbook](../THREE_TEAM_PILOT.md). Keep reader
intake and synthesis as separate review stages. Heavy automation is explicitly out of scope until
the pilot retrospective identifies safe, repeatable work.

Preseason game monitoring follows [the preseason game runbook](../PRESEASON_GAME_RUNBOOK.md). Add a
completed `preflight.md` to each preseason game run directory before freezing assignments, and use
team ledgers as the queue for completion passes.
