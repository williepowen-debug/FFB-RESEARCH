---
name: source-fetch-quirks
description: Where per-outlet publication metadata actually lives (seahawks.com serves two JSON-LD blocks; ESPN box scores are unbylined and undated; NFL gamebook PDFs carry only a CDN upload stamp) so published_at is pinned to the right item
metadata:
  type: reference
---

Metadata-extraction traps observed 2026-09-09 (run `20260909T210706Z`) and extended
2026-09-10 (run `20260910T222845Z`). Access and blocking
behaviour is **not** duplicated here: it belongs in each team's registry, under `## Access limits`
in the `beat-writers/README.md` and in the `handling_note` column of `sources.csv`. Read those
first; this note only covers where the timestamp hides once a page is in hand.

- **seahawks.com articles carry two JSON-LD blocks.** One is the article's own `NewsArticle` with
  the correct `datePublished` and byline; the other is an unrelated photo-gallery `WebPage` block
  with its own dates. **Match the block whose `headline` equals the article title** - that rule has
  held every time. Do not rely on block order: on 2026-09-09 the gallery block came first, on
  2026-09-10 the `NewsArticle` came first on all three articles checked. Order is not stable in
  either direction, so never grep for the first `datePublished`. The `NewsArticle` block also
  exposes `author`, which is the cheapest way to check a club-site byline against `sources.csv`
  before attributing; club-site bylines are frequently unregistered.
- **ESPN story pages** expose no article JSON-LD on the rendered path, so the displayed byline time
  (Eastern) is the only timestamp. Record it with the correct offset and note the limitation.
  Game-week stories are often joint bylines with the opponent's beat reporter, so attribute each
  claim to the reporter who covers that team.
- **ESPN box-score pages carry no byline and no timestamp at all** (checked 2026-09-10 on
  `/nfl/boxscore/_/gameId/...`). They are a spot-check instrument, not an attributable source:
  where the only registered ESPN identity is a named reporter, an unbylined box score cannot be
  attributed to them. Use the gamebook for the claim and record the box score as a spot check.
- **ESPN scripted retrieval fails where the fetch tool succeeds.** A curl request with a browser
  user-agent returned HTTP 202 with a zero-byte body (the documented bot challenge) while the
  fetch tool rendered the same URL in full. Try the fetch tool before recording ESPN as
  inaccessible.
- **A "Sources:" headline is not proof the outlet did the sourcing, and a big outlet's byline may
  not be a person at all.** Verified 2026-09-10: ESPN's "Sources: A.J. Brown believed to have high
  ankle sprain" was bylined **"Multiple Authors"** and its lede credited NFL Network's Ian Rapoport
  and Mike Garafolo. Attributing it to the registry's ESPN reporter would have invented independent
  corroboration for a claim the head coach had just declined to confirm. Read the lede's sourcing
  clause and the byline together before attributing: "sources told <other outlet>" makes the piece a
  relay whose origin is unregistered, however authoritative the host domain.

- **Check the byline on every outlet, not just the ones with a known problem.** Same run: the Boston
  Herald and NBC Sports Boston each ran a Patriots story under a byline absent from the team's
  `sources.csv`, on the same day, alongside registered writers' work. Section and author landing
  pages mix registered and unregistered bylines freely. The cheap guard is to read
  `author.name` out of the article JSON-LD for every candidate and diff it against `sources.csv`
  before reading the body, rather than after drafting a row.

- **NFL official gamebook PDFs carry no internal publication date.** `pdfinfo` shows only
  Creator/Producer `ActiveReports 19` — no `CreationDate`. The only retrievable stamp is the CDN
  asset creation time: `crt=<epoch>` inside the `Server-Timing` `content-info` response header,
  which matches the `v<epoch>` segment of the `static.www.nfl.com/image/upload/...` URL. That is
  an upload time, not a publisher-declared publication time, so declare it explicitly and let
  ARCHITECT rule on intake eligibility. `Last-Modified` is not a substitute. Team sites often
  publish their own dated "Gamebook" article linking a team-hosted copy of the same PDF, which
  can serve as a publication anchor if one is needed.
- **nbcsportsboston.com** serves a single clean `NewsArticle` JSON-LD block with `datePublished`
  in a `-04:00` Eastern offset plus the author's name and author URL, so the byline is verifiable
  from metadata alone (checked 2026-09-10). Plain curl with a browser user-agent is enough; the
  insiders page and the team section both list article URLs with a numeric ID suffix that sorts
  by recency.

- **What an NFL gamebook PDF actually contains**, before declaring a participation gap: extract with
  `pdftotext -layout` (without `-layout` the two-team side-by-side stat tables interleave into
  nonsense). It carries a **Playtime Percentage** table the book itself labels *Unofficial* -
  real per-player offense/defense/special-teams snap counts, including the quarterback split when
  a starter is lost mid-game - plus `** Injury Update:` lines inside the play-by-play giving
  timing and official in-game designation (`return is Questionable`, `is Out of the game`) but
  **never a body part or diagnosis**; for that you need the club. `Did Not Play` and `Not Active`
  are separate lists, so an active healthy scratch is distinguishable from an inactive. Two
  caveats. First, the playtime snap total and `Total Offensive Plays` in Final Team Statistics
  measure different things and will not match: page 3 counts **statistical plays** (pass attempts +
  rushes + sacks); the playtime table counts **snaps**, which also include plays that were snapped
  and run and then wiped out by a **live-ball** penalty. They reconcile exactly once you add those
  back (SEA 48+2=50, NE 67+4=71 in the 2026 Week 1 opener). **Discriminator: did the book log a play
  RESULT before the penalty line?** If yes the ball was snapped; if the `PENALTY ... - No Play` line
  stands alone it was a dead-ball foul and no snap occurred. Do not judge by the foul's name -
  *Offensive Offside* reads dead-ball but is logged with a full play result. Cross-check by confirming
  one team's offensive snap total equals the other's defensive total and that every offensive lineman
  sits at 100%. Use snaps for participation share and statistical plays for statistical rates; say
  which base you used. Second, the table gives snap **volume**
  only, with no alignment labels, so it cannot establish who played nickel or slot.
- **fox13seattle.com** exposes a clean `datePublished` with a Pacific offset plus an author meta
  tag. **It also republishes Associated Press wire copy under the same URL shape**, so the byline
  must be checked, not assumed from the section (verified 2026-09-10: two Seahawks injury stories
  on the same event, one bylined Curtis Crabtree, one AP by Anne M. Peterson). The tell is the
  `fox.author` meta being empty while `fox.publisher` reads `Associated Press` and
  `fox.page_content_author_secondary` carries the wire reporter's name; the JSON-LD `author` shows
  the wire name too. Wire copy is unregistered and cannot be attributed to the local reporter.

**How to apply:** consult before pinning `published_at` on any reader run. Never substitute
`dateModified` for publication time. If a page's structure no longer matches this note, correct
the note in the same run rather than working around it.
