---
name: ne-source-timestamp-locations
description: Where New England registered sources put real publication timestamps (patriots.com JSON-LD vs byline cross-check; injury-report and transactions pages have no item timestamp) and how to parse Herald article HTML
metadata:
  type: reference
---

Timestamp and parsing notes for New England registered sources. Verified 2026-09-09;
patriots.com entries re-verified and corrected 2026-09-10.

Access and blocking behaviour is **not** duplicated here. The Boston Herald and MassLive
retrieval limitations live in the registry, under `## Access limits` in
`teams/AFC/East/New-England-Patriots/2026/beat-writers/README.md` and in the `handling_note`
column of that directory's `sources.csv`. Read those first.

- **patriots.com articles** carry a usable article `datePublished` in JSON-LD, and the displayed
  byline time is the same instant rendered in Eastern. Cross-check the two before pinning; when
  they agree the timestamp is real.
  - *Transcript pages are not reliably placeholder-stamped.* An earlier version of this note said
    they carry a placeholder `datePublished` (such as 09:00Z). Checked again 2026-09-10: the
    9/10 Vrabel press-conference transcript carried `2026-09-10T18:57:00.471Z`, matching its
    displayed "02:57 PM" Eastern byline exactly. Treat a transcript timestamp as real when it
    matches the byline, and flag it only when the two disagree or the time is implausible for a
    press conference.
  - The structured `/team/injury-report/` page carries no item timestamp at all, so the supporting
    item for a designation is the dated "Week N Injury Report" article, not that page.
  - The structured `/team/transactions/` page is the same shape: entries are dated `MM/DD` only,
    with no item-level timestamp and no JSON-LD (re-confirmed 2026-09-10). A transaction there
    cannot support an in-window `published_at` on its own; find the dated announcement article.
  - Watch `dateModified` on fast-moving official posts: the Week 1 inactives article was modified
    13 minutes after publication. Never substitute it.
- **Evan Lazar files two postgame pieces in the same 24 hours, and their numbers differ for two
  different reasons. Separate them before reporting a self-conflict.** Verified 2026-09-10 (run
  `20260910T222845Z`), corrected the same day after ARCHITECT reconciled it:
  - *Snap counts are NOT a revision.* The same-night "Game Observations" piece had Stevenson at
    57-of-67 and the next-afternoon "After Further Review" film piece at 60-of-71. Both are correct
    on different bases: 67 is statistical offensive plays (pass attempts + rushes + sacks), 71 is
    actual snaps, which also counts plays run but wiped out by a live-ball penalty. Three of the
    four negated snaps had Stevenson on the field, so 57+3 = 60 and the two reconcile exactly. The
    hazard is mixing bases, never the source.
  - *Pressure rate IS a revision.* 28.6% "on initial viewing" became 38.1% on film — the same metric
    on the same base, re-measured. Take the film number.

  **How to apply:** when one source publishes two numbers for the same thing, first ask whether the
  denominators differ. Reconstruct both denominators and try to reconcile before writing "conflict"
  in a row note — a reader batch asserting that a registered source contradicted itself propagates
  into synthesis as a source-reliability problem that may not exist. Flagging the discrepancy is
  still right; asserting a verdict on it is not. An official gamebook's playtime-versus-plays
  reconciliation is the fastest way to settle it.

- **Boston Herald article HTML** is heavy with inline scripts. Strip `<script>` and `<style>`
  before extracting paragraphs. Article metadata includes `datePublished`, the author name, and
  the article body.
- **Herald bylines are not all registered.** The Patriots index carries posts by writers outside
  the registry; check the byline against `sources.csv` before attributing an observation. This is a
  routine hit, not an edge case: an unregistered byline turned up in the Patriots section on both
  2026-09-09 and 2026-09-10. Read the JSON-LD `author.name`, not the rendered page furniture.
- **Pats Chat** landing pages list episode titles and dates only, which is why the endpoint is
  registered as metadata-only. Do not attribute claims to an episode you did not hear.

**How to apply:** pull timestamps from article metadata rather than page text, and treat a
placeholder or absent timestamp as a reason to find the dated article, not to estimate.
