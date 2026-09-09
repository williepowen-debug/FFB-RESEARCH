---
name: source-fetch-quirks
description: Per-outlet retrieval quirks for reader runs (seahawks.com dual JSON-LD blocks, ESPN bot challenge, FOX 13 metadata) so timestamps are pinned correctly
metadata:
  type: reference
---

Retrieval quirks observed on 2026-09-09 (run 20260909T210706Z, reader-sea):

- **seahawks.com articles** carry two JSON-LD blocks: the article's own `NewsArticle` (correct
  `datePublished`, author John Boyle when bylined) plus an unrelated photo-gallery `WebPage` block
  with its own dates. Always match the block whose `headline` equals the article title; do not
  take the first `datePublished` you grep. Direct `curl` with a browser UA works.
- **seahawks.com author archive** (`/author/john-boyle`) renders only a profile, no article list;
  reach Boyle items via `/news/` index instead.
- **ESPN** returns an HTTP 202 bot-challenge shell to `curl`; WebFetch renders fine. Only the
  displayed byline time (ET) is available, so record it with `-04:00`/`-05:00` and say so in notes.
- **fox13seattle.com** exposes clean JSON-LD `datePublished` (PDT offset) and `fox.author` meta;
  `curl` works.
- Repo has no `players/` profiles for SEA players, so `player_ids` stays blank in SEA rows
  (consistent with prior SEA batches).

**How to apply:** use before pinning `published_at` for any SEA/NE reader run; re-verify quirks
if a fetch looks different.
