---
name: source-fetch-quirks
description: Where per-outlet publication metadata actually lives (seahawks.com serves two JSON-LD blocks; ESPN exposes only byline time) so published_at is pinned to the right item
metadata:
  type: reference
---

Metadata-extraction traps observed 2026-09-09 (run `20260909T210706Z`). Access and blocking
behaviour is **not** duplicated here: it belongs in each team's registry, under `## Access limits`
in the `beat-writers/README.md` and in the `handling_note` column of `sources.csv`. Read those
first; this note only covers where the timestamp hides once a page is in hand.

- **seahawks.com articles carry two JSON-LD blocks.** One is the article's own `NewsArticle` with
  the correct `datePublished` and byline; the other is an unrelated photo-gallery `WebPage` block
  with its own dates. Match the block whose `headline` equals the article title. Grepping the first
  `datePublished` in the page returns the wrong date more often than not.
- **ESPN story pages** expose no article JSON-LD on the rendered path, so the displayed byline time
  (Eastern) is the only timestamp. Record it with the correct offset and note the limitation.
  Game-week stories are often joint bylines with the opponent's beat reporter, so attribute each
  claim to the reporter who covers that team.
- **fox13seattle.com** exposes a clean `datePublished` with a Pacific offset plus an author meta
  tag.

**How to apply:** consult before pinning `published_at` on any reader run. Never substitute
`dateModified` for publication time. If a page's structure no longer matches this note, correct
the note in the same run rather than working around it.
