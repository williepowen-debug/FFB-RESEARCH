---
name: ne-source-access-notes
description: How to actually retrieve NE registered sources (Boston Herald blocked for WebFetch but curl works; where item timestamps live on patriots.com, ESPN, Herald)
metadata:
  type: reference
---

Access notes for New England Patriots registered sources, verified 2026-09-09 reader run.

- Boston Herald (`local-writer-andrew-callahan`, `local-writer-doug-kyed`): WebFetch returns
  "unable to fetch from www.bostonherald.com". `curl -sL -A "Mozilla/5.0 ..."` on the index and
  article URLs returns full HTML (200) including JSON-LD `datePublished`, `author` name, and
  `articleBody`. Article HTML is heavy with inline scripts; strip `<script>`/`<style>` before
  extracting paragraphs. Herald posts by Julian Cardillo appear on the Patriots index but he is not
  a registered source.
- patriots.com articles: JSON-LD `datePublished` present in raw HTML via curl; displayed byline
  time is ET. Transcript pages carry a placeholder-looking `datePublished` (e.g. 09:00Z) that does
  not match the presser time — note that in observation notes. The structured
  `/team/injury-report/` page has no item timestamp; use the dated "Week N Injury Report" article.
- ESPN story pages: JSON-LD `datePublished` matches the displayed ET time; Reiss game-week stories
  are often joint bylines with the opponent's NFL Nation reporter.
- Pats Chat iHeart landing page lists episode titles/dates only (metadata_only endpoint).

**How to apply:** In NE reader runs, go straight to curl for Herald pages instead of retrying
WebFetch, and pull timestamps from JSON-LD rather than page text.
