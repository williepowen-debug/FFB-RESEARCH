#!/usr/bin/env python3
"""Validate structured records, references, links, schemas, and catalog freshness."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import unquote

from record_utils import (
    REPO_ROOT,
    FrontMatterError,
    is_managed_record_path,
    markdown_files,
    parse_front_matter,
    record_files,
    render_catalog,
)


LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
TYPE_CHECKS = {
    "array": list,
    "boolean": bool,
    "integer": int,
    "null": type(None),
    "number": (int, float),
    "object": dict,
    "string": str,
}
REQUIRED_SECTIONS = {
    "research_finding": ["Finding", "Fantasy implication", "Evidence", "Sources", "Assessment"],
    "team_overview": ["Fantasy-relevant snapshot", "Offensive identity", "Defensive matchup profile", "Coaching and scheme", "Sources"],
    "player_profile": ["Durable player profile", "Current situation", "Fantasy assessment", "Sources"],
    "coaching_profile": ["Responsibilities", "Scheme and tendencies", "Fantasy implications", "Sources"],
    "beat_writer_registry": ["Reliability history", "Usage notes"],
    "injury_update": ["Reported facts", "Source timeline", "Fantasy implication", "Assessment"],
    "league_format": ["Format summary", "Roster and lineup", "Scoring", "Strategic implications", "Sources"],
    "weekly_matchup": ["Game environment", "Matchup analysis", "Fantasy decisions", "Open questions and next checks", "Sources"],
    "depth_chart": ["Offense", "Defense", "Special teams", "Recent changes", "Sources"],
}


def load_json(path: Path, failures: list[str]) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"{path.relative_to(REPO_ROOT)}: invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        failures.append(f"{path.relative_to(REPO_ROOT)}: top level must be an object")
        return {}
    return data


def matches_type(value: Any, expected: str) -> bool:
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, TYPE_CHECKS[expected])


def validate_schema_value(value: Any, rule: dict[str, Any], label: str, failures: list[str]) -> None:
    if "const" in rule and value != rule["const"]:
        failures.append(f"{label}: must equal {rule['const']!r}")
    if "enum" in rule and value not in rule["enum"]:
        failures.append(f"{label}: {value!r} is not an allowed value")

    expected_types = rule.get("type")
    if expected_types:
        if isinstance(expected_types, str):
            expected_types = [expected_types]
        if not any(matches_type(value, expected) for expected in expected_types):
            failures.append(f"{label}: expected type {expected_types}, found {type(value).__name__}")
            return
    if value is None:
        return

    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0):
            failures.append(f"{label}: string is too short")
        pattern = rule.get("pattern")
        if pattern and not re.fullmatch(pattern, value):
            failures.append(f"{label}: {value!r} does not match {pattern!r}")
        if rule.get("format") == "date":
            try:
                date.fromisoformat(value)
            except ValueError:
                failures.append(f"{label}: {value!r} is not an ISO date")
    if isinstance(value, list):
        if len(value) < rule.get("minItems", 0):
            failures.append(f"{label}: needs at least {rule['minItems']} item(s)")
        if "maxItems" in rule and len(value) > rule["maxItems"]:
            failures.append(f"{label}: allows at most {rule['maxItems']} item(s)")
        if rule.get("uniqueItems"):
            encoded = [json.dumps(item, sort_keys=True) for item in value]
            if len(encoded) != len(set(encoded)):
                failures.append(f"{label}: items must be unique")
        item_rule = rule.get("items")
        if item_rule:
            for index, item in enumerate(value):
                validate_schema_value(item, item_rule, f"{label}[{index}]", failures)
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in rule and value < rule["minimum"]:
            failures.append(f"{label}: must be >= {rule['minimum']}")
        if "maximum" in rule and value > rule["maximum"]:
            failures.append(f"{label}: must be <= {rule['maximum']}")


def validate_against_schema(metadata: dict[str, Any], schema: dict[str, Any], label: str, failures: list[str]) -> None:
    required = set(schema.get("required", []))
    missing = sorted(required - metadata.keys())
    if missing:
        failures.append(f"{label}: missing metadata keys {missing}")
    properties = schema.get("properties", {})
    if schema.get("additionalProperties") is False:
        extras = sorted(metadata.keys() - properties.keys())
        if extras:
            failures.append(f"{label}: unexpected metadata keys {extras}")
    for key, value in metadata.items():
        if key in properties:
            validate_schema_value(value, properties[key], f"{label}:{key}", failures)


def validate_links(failures: list[str]) -> None:
    for path in markdown_files(REPO_ROOT):
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            if "<" in target or ">" in target:
                continue
            target = unquote(target).split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(REPO_ROOT.resolve())
            except ValueError:
                failures.append(f"{path.relative_to(REPO_ROOT)}: link escapes repository: {raw_target}")
                continue
            if not resolved.exists():
                failures.append(f"{path.relative_to(REPO_ROOT)}: broken relative link {raw_target}")


def main() -> int:
    failures: list[str] = []
    schemas_dir = REPO_ROOT / "schemas"
    controlled = load_json(schemas_dir / "controlled-values.json", failures)
    schema_paths = sorted(schemas_dir.glob("*.schema.json"))
    schemas: dict[str, dict[str, Any]] = {}
    for path in schema_paths:
        schema = load_json(path, failures)
        record_type = schema.get("properties", {}).get("record_type", {}).get("const")
        if not record_type:
            failures.append(f"{path.relative_to(REPO_ROOT)}: missing record_type const")
        else:
            schemas[record_type] = schema

    expected_types = set(controlled.get("record_types", []))
    if set(schemas) != expected_types:
        failures.append(
            f"schemas: record types {sorted(schemas)} do not match controlled values {sorted(expected_types)}"
        )

    with (REPO_ROOT / "league/teams.csv").open(newline="", encoding="utf-8") as handle:
        team_ids = {row["abbr"] for row in csv.DictReader(handle)}

    ids: list[str] = []
    supersedes_by_path: list[tuple[Path, list[str]]] = []
    record_count = 0
    for path in record_files(REPO_ROOT, include_templates=True):
        relative = path.relative_to(REPO_ROOT)
        is_template = relative.parts[0] == "templates"
        try:
            metadata, body = parse_front_matter(path)
        except FrontMatterError as exc:
            failures.append(f"{relative}: malformed front matter: {exc}")
            continue
        if metadata is None:
            if is_managed_record_path(path):
                failures.append(f"{relative}: managed research record is missing front matter")
            continue
        record_count += 0 if is_template else 1
        record_type = metadata.get("record_type")
        schema = schemas.get(record_type)
        if not schema:
            failures.append(f"{relative}: unknown record_type {record_type!r}")
            continue
        validate_against_schema(metadata, schema, str(relative), failures)

        if metadata.get("schema_version") != controlled.get("schema_version"):
            failures.append(f"{relative}: unsupported schema_version {metadata.get('schema_version')!r}")
        if not is_template:
            unknown_teams = sorted(set(metadata.get("team_ids", [])) - team_ids)
            if unknown_teams:
                failures.append(f"{relative}: unknown team_ids {unknown_teams}")
            record_id = metadata.get("record_id")
            if record_id:
                ids.append(record_id)
            if metadata.get("status") != "draft":
                for key in ("record_id", "valid_as_of", "last_verified", "confidence"):
                    if metadata.get(key) is None:
                        failures.append(f"{relative}: non-draft record requires {key}")
                if "<" in str(metadata.get("title", "")):
                    failures.append(f"{relative}: non-draft title contains a placeholder")
            supersedes_by_path.append((relative, metadata.get("supersedes", [])))

        headings = {
            line.lstrip("#").strip()
            for line in body.splitlines()
            if line.startswith("## ")
        }
        for required in REQUIRED_SECTIONS.get(record_type, []):
            if required not in headings:
                failures.append(f"{relative}: missing required section '## {required}'")

        formats = metadata.get("fantasy_formats", [])
        invalid_formats = sorted(set(formats) - set(controlled.get("fantasy_formats", [])))
        if invalid_formats:
            failures.append(f"{relative}: invalid fantasy_formats {invalid_formats}")

    duplicates = sorted(record_id for record_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        failures.append(f"duplicate record_ids: {duplicates}")
    known_ids = set(ids)
    for relative, supersedes in supersedes_by_path:
        missing = sorted(set(supersedes) - known_ids)
        if missing:
            failures.append(f"{relative}: supersedes unknown record_ids {missing}")

    validate_links(failures)

    catalog_path = REPO_ROOT / "catalog.jsonl"
    expected_catalog = render_catalog(REPO_ROOT)
    actual_catalog = catalog_path.read_text(encoding="utf-8") if catalog_path.is_file() else None
    if actual_catalog != expected_catalog:
        failures.append("catalog.jsonl is stale; run python scripts/generate_catalog.py")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        print(f"Repository validation failed with {len(failures)} error(s).", file=sys.stderr)
        return 1

    print(
        f"OK: {record_count} research records, {len(schema_paths)} schemas, "
        f"{len(ids)} stable IDs, valid links, and a current catalog."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
