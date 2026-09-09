---
name: ne-source-timestamp-locations
description: Where New England registered sources put real publication timestamps (patriots.com transcript placeholder dates; injury-report page has none) and how to parse Herald article HTML
metadata:
  type: reference
---

Timestamp and parsing notes for New England registered sources, verified 2026-09-09.

Access and blocking behaviour is **not** duplicated here. The Boston Herald and MassLive
retrieval limitations live in the registry, under `## Access limits` in
`teams/AFC/East/New-England-Patriots/2026/beat-writers/README.md` and in the `handling_note`
column of that directory's `sources.csv`. Read those first.

- **patriots.com articles** carry a usable article `datePublished`; the displayed byline time is
  Eastern. Two traps: transcript pages carry a placeholder-looking `datePublished` (such as
  09:00Z) that does not match the actual press-conference time, so flag it in the observation
  note; and the structured `/team/injury-report/` page carries no item timestamp at all, so the
  supporting item for a designation is the dated "Week N Injury Report" article, not that page.
- **Boston Herald article HTML** is heavy with inline scripts. Strip `<script>` and `<style>`
  before extracting paragraphs. Article metadata includes `datePublished`, the author name, and
  the article body.
- **Herald bylines are not all registered.** The Patriots index carries posts by writers outside
  the registry; check the byline against `sources.csv` before attributing an observation.
- **Pats Chat** landing pages list episode titles and dates only, which is why the endpoint is
  registered as metadata-only. Do not attribute claims to an episode you did not hear.

**How to apply:** pull timestamps from article metadata rather than page text, and treat a
placeholder or absent timestamp as a reason to find the dated article, not to estimate.
