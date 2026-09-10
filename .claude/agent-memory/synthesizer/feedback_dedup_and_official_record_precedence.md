---
name: dedup-and-official-record-precedence
description: Reconciliation craft — collapse same-item lane duplicates by URL not dedup_key, let the official book override a reporter's situational phrasing, and treat an unobserved situation as a null finding rather than a fired trigger
metadata:
  type: feedback
---

Three reconciliation rules that a `dedup_key`-first pass will miss. Extends
[[architect-routing-and-handoff]].

**1. Collapse same-item lane duplicates by `source_url` + `published_at`, not by `dedup_key`.**
When one registered writer is assigned to both the official and the beat lane, the two readers emit
the *same article* twice — and they assign it **different `dedup_key`s**, because each reader keys on
its own lane's framing (club-as-publisher vs. reporter). Grouping by `dedup_key` alone counts one
item as two clusters and silently inflates the corroboration count.

**Why:** SEA Week 1 postgame (2026-09-10): three seahawks.com articles produced six observation rows
across the two lanes, none of which shared a `dedup_key` with its own twin. Both readers flagged the
likely duplication in `notes` — read those before clustering.

**How to apply:** after the `dedup_key` pass, re-group on `(source_url, published_at)` and report the
collapsed count in Run metrics. Also check whether several rows trace to one *speaker* on one
occasion (a presser, a radio hit): one speaker recirculated across outlets is one origin, however
many outlets carry it.

**2. The official book outranks a reporter's situational phrasing, and the difference can be
load-bearing.**
A beat writer described a negated touchdown as "third-and-goal"; the gamebook logged it 3rd-and-4 at
the opponent 7, and team statistics recorded **zero goal-to-go trips** in the game. Accepting the
reporter's wording would have manufactured a goal-to-go rep that the official record says never
existed — and an open ledger trigger asked specifically about inside-five usage.

**How to apply:** whenever a reported claim names a down, distance, field position, or situation that
an open trigger depends on, verify it against the book before it enters the synthesis. Preserve both
accounts and state the resolution; do not silently drop the reporter's version.

**3. An unobserved situation is a null finding, not a fired trigger.**
When the eligible sample is zero — no goal-to-go snaps, no carries inside the 10 — the trigger has
**not** occurred and the ledger row stays open. Report `eligible_plays = 0` explicitly rather than
letting a completed game imply the question was answered. An unobserved scoring situation cannot
resolve a scoring role.

**How to apply:** in Run metrics, split each prior trigger into its clauses and mark each *occurred*,
*did not occur*, or *cannot occur from this game*. Triggers routinely fire only partially; saying so
is what lets ARCHITECT re-defer instead of closing a row on absent evidence.

**Nuance on the catalog warning:** the parent note says `validate_repository.py` will report
`catalog.jsonl` stale after you add a synthesis. With parallel team synthesizers it may instead come
back clean, because a teammate regenerated it moments earlier and picked up your record too. Either
outcome is fine — still never regenerate it yourself; just confirm your `record_id` is present and
say which of the two you saw.
