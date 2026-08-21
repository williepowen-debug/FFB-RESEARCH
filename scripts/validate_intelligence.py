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
ASSIGNMENT_HEADERS = [
    "run_id", "reader_id", "season", "team_ids", "source_ids", "reader_lane", "window_start",
    "window_end", "output_directory", "status", "notes",
]
RUN_REPORT_HEADERS = [
    "run_id", "reader_id", "team_id", "window_start", "window_end", "observation_cap",
    "elapsed_minutes", "source_id", "access_outcome", "items_inspected",
    "observations_emitted", "duplicate_clusters", "conflicts", "time_sensitive_items",
    "meaningful_overflow", "no_meaningful_update", "spot_check_observation_ids",
    "spot_check_failures", "corrections", "notes",
]
LEDGER_HEADERS = [
    "ledger_id", "review_date", "team_id", "synthesis_record_id", "observation_ids",
    "routing_level", "signal_type", "entity_or_unit", "evidence_effect", "target_ids",
    "target_path", "disposition", "next_review_trigger", "status", "resolved_date",
    "resolution_synthesis_id", "supersedes_ledger_id", "notes",
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
ACCESS_OUTCOMES = {"checked", "no_new_material", "inaccessible", "failed_endpoint"}
LEDGER_ROUTING_LEVELS = {"review", "escalate"}
EVIDENCE_EFFECTS = {"supports", "challenges", "mixed", "contextual", "unresolved"}
LEDGER_DISPOSITIONS = {"promoted", "deferred", "no_change"}
LEDGER_STATUSES = {"open", "resolved", "superseded"}
OBSERVATION_ID_RE = re.compile(r"^obs-[0-9]{4}-[a-z0-9]+-[0-9]{8}t[0-9]{6}z-[0-9]{3}$")
RUN_ID_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z$")
SIGNAL_ID_RE = re.compile(r"^sig-[0-9]{4}-[a-z0-9]+-[0-9]{8}-[0-9]{3}$")
LEDGER_ID_RE = re.compile(r"^til-[0-9]{4}-[a-z0-9]+-[0-9]{8}-[0-9]{3}$")


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def valid_timestamp(value: str) -> bool:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return "T" in value and (value.endswith("Z") or "+" in value[10:] or "-" in value[10:])


def parse_timestamp(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def nonnegative_integer(value: str) -> bool:
    try:
        return int(value) >= 0
    except ValueError:
        return False


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
            result[row["abbr"]] = {
                item["source_id"] for item in csv.DictReader(handle)
                if item.get("status", "active") == "active"
            }
    return team_ids, result


def validate_intelligence(root: Path = REPO_ROOT) -> list[str]:
    failures: list[str] = []
    observations: dict[str, dict[str, str]] = {}
    observation_runs: dict[str, str] = {}
    assignments: dict[tuple[str, str, str], dict[str, str]] = {}
    assigned_run_ids: set[str] = set()

    for path in sorted(root.glob("intelligence/*/runs/*/assignments.csv")):
        relative = path.relative_to(root)
        path_run_id = relative.parts[3]
        for index, row in enumerate(read_csv(path, ASSIGNMENT_HEADERS, failures), start=2):
            label = f"{relative}:{index}"
            run_id = row.get("run_id", "")
            reader_id = row.get("reader_id", "")
            team_ids = split_ids(row.get("team_ids", ""))
            assigned_run_ids.add(run_id)
            if run_id != path_run_id or not RUN_ID_RE.fullmatch(run_id):
                failures.append(f"{label}: run_id must match the run directory")
            if not reader_id:
                failures.append(f"{label}: reader_id is required")
            if not team_ids:
                failures.append(f"{label}: team_ids is required")
            start = parse_timestamp(row.get("window_start", ""))
            end = parse_timestamp(row.get("window_end", ""))
            if start is None or end is None:
                failures.append(f"{label}: retrieval window must use ISO 8601 timestamps")
            elif start >= end:
                failures.append(f"{label}: window_start must precede window_end")
            if row.get("status") != "frozen":
                failures.append(f"{label}: assignment status must be 'frozen'")
            try:
                season = int(row.get("season", ""))
            except ValueError:
                failures.append(f"{label}: season must be an integer")
                season = 0
            known_teams, active_sources = source_ids_by_team(root, season)
            expected_output = f"intelligence/{season}/runs/{run_id}/{reader_id}"
            if row.get("output_directory") != expected_output:
                failures.append(f"{label}: output_directory must match the assigned run and reader")
            allowed_sources = set().union(*(active_sources.get(team_id, set()) for team_id in team_ids))
            unknown_sources = sorted(set(split_ids(row.get("source_ids", ""))) - allowed_sources)
            if unknown_sources:
                failures.append(f"{label}: assignment contains unregistered or inactive sources {unknown_sources}")
            for team_id in team_ids:
                if team_id not in known_teams:
                    failures.append(f"{label}: unknown team_id {team_id!r}")
                key = (run_id, reader_id, team_id)
                if key in assignments:
                    failures.append(f"{label}: duplicate assignment for {reader_id} and {team_id}")
                assignments[key] = row

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
            observation_runs[observation_id] = run_id
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
            assignment = assignments.get((run_id, row.get("reader_id", ""), team_id))
            if run_id in assigned_run_ids and assignment is None:
                failures.append(f"{label}: observation has no matching frozen assignment")
            elif assignment is not None:
                published = parse_timestamp(row.get("published_at", ""))
                window_start = parse_timestamp(assignment.get("window_start", ""))
                window_end = parse_timestamp(assignment.get("window_end", ""))
                if published is not None and window_start is not None and window_end is not None:
                    if not window_start <= published <= window_end:
                        failures.append(f"{label}: published_at falls outside the frozen window")
                if row.get("source_id", "") not in split_ids(assignment.get("source_ids", "")):
                    failures.append(f"{label}: source_id is outside the frozen assignment")
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

    report_keys: set[tuple[str, str, str]] = set()
    for path in sorted(root.glob("intelligence/*/runs/*/*/run-report.csv")):
        relative = path.relative_to(root)
        path_run_id = relative.parts[3]
        path_reader_id = relative.parts[4]
        rows = read_csv(path, RUN_REPORT_HEADERS, failures)
        grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for index, row in enumerate(rows, start=2):
            label = f"{relative}:{index}"
            key = (row.get("run_id", ""), row.get("reader_id", ""), row.get("team_id", ""))
            grouped.setdefault(key, []).append(row)
            report_keys.add(key)
            if key[0] != path_run_id or key[1] != path_reader_id:
                failures.append(f"{label}: run_id and reader_id must match the report directory")
            assignment = assignments.get(key)
            if assignment is None:
                failures.append(f"{label}: run report has no matching frozen assignment")
            else:
                for field in ("window_start", "window_end"):
                    if row.get(field) != assignment.get(field):
                        failures.append(f"{label}: {field} does not match the frozen assignment")
                if row.get("source_id", "") not in split_ids(assignment.get("source_ids", "")):
                    failures.append(f"{label}: source_id is outside the frozen assignment")
            if row.get("access_outcome") not in ACCESS_OUTCOMES:
                failures.append(f"{label}: invalid access_outcome")
            for field in (
                "observation_cap", "elapsed_minutes", "items_inspected", "observations_emitted",
                "duplicate_clusters", "conflicts", "time_sensitive_items", "meaningful_overflow",
            ):
                if not nonnegative_integer(row.get(field, "")):
                    failures.append(f"{label}: {field} must be a nonnegative integer")
            if row.get("spot_check_failures", "") and not nonnegative_integer(row["spot_check_failures"]):
                failures.append(f"{label}: spot_check_failures must be blank or a nonnegative integer")
            if row.get("no_meaningful_update") not in {"true", "false"}:
                failures.append(f"{label}: no_meaningful_update must be 'true' or 'false'")
            for observation_id in split_ids(row.get("spot_check_observation_ids", "")):
                observation = observations.get(observation_id)
                if observation is None:
                    failures.append(f"{label}: unknown spot-check observation {observation_id!r}")
                elif observation.get("team_id") != key[2]:
                    failures.append(f"{label}: spot-check observation belongs to another team")

        for key, team_rows in grouped.items():
            assignment = assignments.get(key)
            if assignment is None:
                continue
            assigned_sources = split_ids(assignment.get("source_ids", ""))
            reported_sources = [row.get("source_id", "") for row in team_rows]
            if Counter(reported_sources) != Counter(assigned_sources):
                failures.append(
                    f"{relative}: run report must account for every assigned source exactly once"
                )
            caps = {row.get("observation_cap", "") for row in team_rows}
            if len(caps) != 1:
                failures.append(f"{relative}: observation_cap must be consistent across source rows")
            actual_rows = [
                row for observation_id, row in observations.items()
                if observation_runs.get(observation_id) == key[0]
                and row.get("reader_id") == key[1] and row.get("team_id") == key[2]
            ]
            if caps and nonnegative_integer(next(iter(caps))):
                if len(actual_rows) > int(next(iter(caps))):
                    failures.append(f"{relative}: observation batch exceeds its cap")
            emitted = sum(int(row["observations_emitted"]) for row in team_rows if nonnegative_integer(row.get("observations_emitted", "")))
            if emitted != len(actual_rows):
                failures.append(f"{relative}: observations_emitted does not match the batch")

    for key in assignments:
        if key not in report_keys:
            failures.append(
                f"intelligence run {key[0]}: missing run report for reader {key[1]} team {key[2]}"
            )

    synthesis_ids: dict[str, set[str]] = {}
    synthesis_teams: dict[str, set[str]] = {}
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
            synthesis_teams[record_id] = set(metadata.get("team_ids", []))

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

    ledger_rows: dict[str, tuple[dict[str, str], str]] = {}
    open_targets: dict[tuple[str, tuple[str, ...], str, str], str] = {}
    for path in sorted(root.glob("teams/*/*/*/*/intelligence-ledger.csv")):
        relative = path.relative_to(root)
        for index, row in enumerate(read_csv(path, LEDGER_HEADERS, failures), start=2):
            label = f"{relative}:{index}"
            ledger_id = row.get("ledger_id", "")
            if not LEDGER_ID_RE.fullmatch(ledger_id):
                failures.append(f"{label}: invalid ledger_id")
            elif ledger_id in ledger_rows:
                failures.append(f"{label}: duplicate ledger_id {ledger_id!r}")
            ledger_rows[ledger_id] = (row, label)
            team_id = row.get("team_id", "")
            synthesis_id = row.get("synthesis_record_id", "")
            if synthesis_id not in synthesis_ids:
                failures.append(f"{label}: unknown synthesis_record_id {synthesis_id!r}")
            elif team_id not in synthesis_teams.get(synthesis_id, set()):
                failures.append(f"{label}: synthesis belongs to another team")
            referenced = set(split_ids(row.get("observation_ids", "")))
            if not referenced:
                failures.append(f"{label}: observation_ids is required")
            unknown = sorted(referenced - known_observation_ids)
            if unknown:
                failures.append(f"{label}: unknown observation_ids {unknown}")
            elif synthesis_id in synthesis_ids and not referenced.issubset(synthesis_ids[synthesis_id]):
                failures.append(f"{label}: ledger observations are not all present in synthesis")
            for observation_id in referenced & known_observation_ids:
                if observations[observation_id].get("team_id") != team_id:
                    failures.append(f"{label}: observation {observation_id!r} belongs to another team")
            if row.get("routing_level") not in LEDGER_ROUTING_LEVELS:
                failures.append(f"{label}: invalid routing_level")
            if row.get("signal_type") not in SIGNAL_TYPES:
                failures.append(f"{label}: invalid signal_type")
            if row.get("evidence_effect") not in EVIDENCE_EFFECTS:
                failures.append(f"{label}: invalid evidence_effect")
            disposition = row.get("disposition", "")
            status = row.get("status", "")
            if disposition not in LEDGER_DISPOSITIONS:
                failures.append(f"{label}: invalid disposition")
            if status not in LEDGER_STATUSES:
                failures.append(f"{label}: invalid status")
            if disposition == "deferred" and status != "open":
                failures.append(f"{label}: deferred ledger item must be open")
            if disposition in {"promoted", "no_change"} and status != "resolved":
                failures.append(f"{label}: promoted/no_change ledger item must be resolved")
            resolved_date = row.get("resolved_date", "")
            resolution_synthesis_id = row.get("resolution_synthesis_id", "")
            if status == "resolved":
                if not valid_date(resolved_date):
                    failures.append(f"{label}: resolved item requires resolved_date")
                if resolution_synthesis_id not in synthesis_ids:
                    failures.append(f"{label}: resolved item requires a valid resolution_synthesis_id")
            elif resolved_date or resolution_synthesis_id:
                failures.append(f"{label}: unresolved item cannot have resolution fields")
            if not valid_date(row.get("review_date", "")):
                failures.append(f"{label}: review_date must be YYYY-MM-DD")
            target_ids = split_ids(row.get("target_ids", ""))
            if not target_ids:
                failures.append(f"{label}: target_ids is required")
            target_value = row.get("target_path", "")
            target_path = root / target_value
            known_target_ids: set[str] = set()
            try:
                inside_root = target_path.resolve().is_relative_to(root.resolve())
            except (OSError, RuntimeError):
                inside_root = False
            if not target_value or not inside_root or not target_path.is_file():
                failures.append(f"{label}: target_path must reference an existing repository file")
            elif target_path.suffix == ".csv":
                try:
                    with target_path.open(newline="", encoding="utf-8") as handle:
                        for target_row in csv.DictReader(handle):
                            for field in ("question_id", "record_id"):
                                if target_row.get(field):
                                    known_target_ids.add(target_row[field])
                except (OSError, csv.Error) as exc:
                    failures.append(f"{label}: cannot read target_path: {exc}")
            elif target_path.suffix == ".md":
                try:
                    metadata, _ = parse_front_matter(target_path)
                    if metadata and metadata.get("record_id"):
                        known_target_ids.add(str(metadata["record_id"]))
                except FrontMatterError as exc:
                    failures.append(f"{label}: malformed target record: {exc}")
            missing_targets = sorted(set(target_ids) - known_target_ids)
            if missing_targets:
                failures.append(f"{label}: target_ids not found in target_path {missing_targets}")
            if status == "open":
                open_key = (
                    team_id, tuple(sorted(target_ids)), row.get("signal_type", ""),
                    row.get("entity_or_unit", "").strip().lower(),
                )
                if open_key in open_targets:
                    failures.append(
                        f"{label}: duplicate open ledger target already used by {open_targets[open_key]}"
                    )
                open_targets[open_key] = ledger_id

    for ledger_id, (row, label) in ledger_rows.items():
        supersedes_id = row.get("supersedes_ledger_id", "")
        if not supersedes_id:
            continue
        if supersedes_id == ledger_id:
            failures.append(f"{label}: ledger item cannot supersede itself")
        elif supersedes_id not in ledger_rows:
            failures.append(f"{label}: unknown supersedes_ledger_id {supersedes_id!r}")
        elif ledger_rows[supersedes_id][0].get("status") != "superseded":
            failures.append(f"{label}: superseded ledger item must have status 'superseded'")
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
