#!/usr/bin/env python3
"""Validate reader observations, synthesis provenance, and priority routing."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

if __package__:
    from .record_utils import REPO_ROOT, FrontMatterError, parse_front_matter
else:
    from record_utils import REPO_ROOT, FrontMatterError, parse_front_matter


OBSERVATION_HEADERS = [
    "observation_id", "team_id", "player_ids", "source_id", "source_url", "origin_url",
    "published_at", "retrieved_at", "evidence_lane", "evidence_kind", "claim_summary",
    "relationship", "related_observation_ids", "dedup_key", "confidence", "time_sensitivity",
    "fantasy_impact", "reader_id", "notes",
]
PRIORITY_HEADERS = [
    "signal_id", "team_id", "player_ids", "observation_ids", "synthesis_record_id",
    "escalation_level", "signal_type", "summary", "fantasy_implication", "next_action",
    "confidence", "status", "created_at", "last_updated",
]
EVIDENCE_LANES = {
    "injury", "availability", "transaction", "depth_chart", "practice_participation",
    "reps_rotation", "role", "usage", "scheme", "coaching", "contract", "roster",
    "performance", "other",
}
EVIDENCE_KINDS = {"official_fact", "reported_fact", "firsthand_observation", "analysis", "measured_data"}
RELATIONSHIPS = {"new", "confirm", "contradict", "update", "repeat"}
CONFIDENCE_LEVELS = {"low", "medium", "high"}
TIME_SENSITIVITY = {"low", "medium", "high", "immediate"}
FANTASY_IMPACT = {"none", "low", "medium", "high"}
ESCALATION_LEVELS = {"log", "review", "escalate"}
SIGNAL_TYPES = {
    "injury", "availability", "transaction", "depth_chart", "role", "usage", "scheme",
    "coaching", "contract", "performance", "conflict", "other",
}
PRIORITY_STATUSES = {"open", "monitoring", "resolved", "dismissed"}
OBSERVATION_ID_RE = re.compile(r"^obs-[0-9]{4}-[a-z0-9]+-[0-9]{8}t[0-9]{6}z-[0-9]{3}$")
RUN_ID_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z$")
SIGNAL_ID_RE = re.compile(r"^sig-[0-9]{4}-[a-z0-9]+-[0-9]{8}-[0-9]{3}$")


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def valid_timestamp(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return "T" in value and (value.endswith("Z") or "+" in value[10:] or "-" in value[10:])


def read_csv(path: Path, expected: list[str], failures: list[str]) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if list(reader.fieldnames or []) != expected:
                failures.append(f"{path}: headers do not match pipeline template")
            return list(reader)
    except (OSError, csv.Error) as exc:
        failures.append(f"{path}: invalid CSV: {exc}")
        return []


def source_ids_by_team(root: Path, season: int) -> tuple[set[str], dict[str, set[str]]]:
    teams_path = root / "league/teams.csv"
    if not teams_path.is_file():
        return set(), {}
    with teams_path.open(newline="", encoding="utf-8") as handle:
        teams = list(csv.DictReader(handle))
    team_ids = {row["abbr"] for row in teams}
    result: dict[str, set[str]] = {}
    for row in teams:
        path = root / row["folder_path"] / str(season) / "beat-writers/sources.csv"
        if not path.is_file():
            result[row["abbr"]] = set()
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            result[row["abbr"]] = {item["source_id"] for item in csv.DictReader(handle)}
    return team_ids, result


def validate_intelligence(root: Path = REPO_ROOT) -> list[str]:
    failures: list[str] = []
    observations: dict[str, dict[str, str]] = {}

    for path in sorted(root.glob("intelligence/*/runs/*/*/observations.csv")):
        relative = path.relative_to(root)
        try:
            season = int(relative.parts[1])
        except (IndexError, ValueError):
            failures.append(f"{relative}: invalid season directory")
            continue
        run_id = relative.parts[3]
        if not RUN_ID_RE.fullmatch(run_id):
            failures.append(f"{relative}: invalid run ID {run_id!r}")
        team_ids, source_map = source_ids_by_team(root, season)
        for index, row in enumerate(read_csv(path, OBSERVATION_HEADERS, failures), start=2):
            label = f"{relative}:{index}"
            observation_id = row.get("observation_id", "")
            if not OBSERVATION_ID_RE.fullmatch(observation_id):
                failures.append(f"{label}: invalid observation_id")
            elif observation_id in observations:
                failures.append(f"{label}: duplicate observation_id {observation_id!r}")
            observations[observation_id] = row
            team_id = row.get("team_id", "")
            if team_id not in team_ids:
                failures.append(f"{label}: unknown team_id {team_id!r}")
            if row.get("source_id", "") not in source_map.get(team_id, set()):
                failures.append(f"{label}: source_id is not registered for {team_id}")
            for field in ("source_url", "origin_url"):
                if not row.get(field, "").startswith(("https://", "http://")):
                    failures.append(f"{label}: {field} must be an HTTP(S) URL")
            for field in ("published_at", "retrieved_at"):
                if not valid_timestamp(row.get(field, "")):
                    failures.append(f"{label}: {field} must be an ISO 8601 timestamp with timezone")
            if row.get("evidence_lane") not in EVIDENCE_LANES:
                failures.append(f"{label}: invalid evidence_lane")
            if row.get("evidence_kind") not in EVIDENCE_KINDS:
                failures.append(f"{label}: invalid evidence_kind")
            if row.get("relationship") not in RELATIONSHIPS:
                failures.append(f"{label}: invalid relationship")
            if row.get("confidence") not in CONFIDENCE_LEVELS:
                failures.append(f"{label}: invalid confidence")
            if row.get("time_sensitivity") not in TIME_SENSITIVITY:
                failures.append(f"{label}: invalid time_sensitivity")
            if row.get("fantasy_impact") not in FANTASY_IMPACT:
                failures.append(f"{label}: invalid fantasy_impact")
            for field in ("claim_summary", "dedup_key", "reader_id"):
                if not row.get(field, "").strip():
                    failures.append(f"{label}: {field} is required")
            related = split_ids(row.get("related_observation_ids", ""))
            if row.get("relationship") == "new" and related:
                failures.append(f"{label}: new observation cannot reference related observations")
            if row.get("relationship") != "new" and not related:
                failures.append(f"{label}: non-new observation requires related_observation_ids")

    known_observation_ids = set(observations)
    for observation_id, row in observations.items():
        for related_id in split_ids(row.get("related_observation_ids", "")):
            if related_id not in known_observation_ids:
                failures.append(f"{observation_id}: unknown related observation {related_id!r}")

    synthesis_ids: dict[str, set[str]] = {}
    for path in sorted(root.glob("intelligence/*/syntheses/*/*.md")):
        relative = path.relative_to(root)
        try:
            metadata, _ = parse_front_matter(path)
        except FrontMatterError as exc:
            failures.append(f"{relative}: malformed front matter: {exc}")
            continue
        if not metadata or metadata.get("record_type") != "team_intelligence":
            failures.append(f"{relative}: synthesis must use record_type team_intelligence")
            continue
        record_id = metadata.get("record_id")
        referenced = set(metadata.get("observation_ids", []))
        unknown = sorted(referenced - known_observation_ids)
        if unknown:
            failures.append(f"{relative}: unknown observation_ids {unknown}")
        if record_id:
            synthesis_ids[record_id] = referenced

    seen_signals: list[str] = []
    for path in sorted(root.glob("intelligence/*/priority/*/priority-board.csv")):
        relative = path.relative_to(root)
        for index, row in enumerate(read_csv(path, PRIORITY_HEADERS, failures), start=2):
            label = f"{relative}:{index}"
            signal_id = row.get("signal_id", "")
            seen_signals.append(signal_id)
            if not SIGNAL_ID_RE.fullmatch(signal_id):
                failures.append(f"{label}: invalid signal_id")
            referenced = set(split_ids(row.get("observation_ids", "")))
            if not referenced:
                failures.append(f"{label}: observation_ids is required")
            unknown = sorted(referenced - known_observation_ids)
            if unknown:
                failures.append(f"{label}: unknown observation_ids {unknown}")
            synthesis_id = row.get("synthesis_record_id", "")
            if synthesis_id not in synthesis_ids:
                failures.append(f"{label}: unknown synthesis_record_id {synthesis_id!r}")
            elif not referenced.issubset(synthesis_ids[synthesis_id]):
                failures.append(f"{label}: priority observations are not all present in synthesis")
            if row.get("escalation_level") not in ESCALATION_LEVELS:
                failures.append(f"{label}: invalid escalation_level")
            if row.get("signal_type") not in SIGNAL_TYPES:
                failures.append(f"{label}: invalid signal_type")
            if row.get("confidence") not in CONFIDENCE_LEVELS:
                failures.append(f"{label}: invalid confidence")
            if row.get("status") not in PRIORITY_STATUSES:
                failures.append(f"{label}: invalid status")
            for field in ("summary", "fantasy_implication", "next_action"):
                if not row.get(field, "").strip():
                    failures.append(f"{label}: {field} is required")
            for field in ("created_at", "last_updated"):
                if not valid_timestamp(row.get(field, "")):
                    failures.append(f"{label}: {field} must be an ISO 8601 timestamp with timezone")
    duplicates = sorted(value for value, count in Counter(seen_signals).items() if value and count > 1)
    if duplicates:
        failures.append(f"duplicate signal_ids: {duplicates}")
    return failures


def main() -> int:
    failures = validate_intelligence()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        print(f"Intelligence validation failed with {len(failures)} error(s).", file=sys.stderr)
        return 1
    observation_count = sum(1 for path in REPO_ROOT.glob("intelligence/*/runs/*/*/observations.csv") for _ in list(csv.DictReader(path.open(encoding="utf-8"))))
    print(f"OK: intelligence pipeline valid ({observation_count} observations).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
