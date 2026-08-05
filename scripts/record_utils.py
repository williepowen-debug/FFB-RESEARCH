#!/usr/bin/env python3
"""Shared, dependency-free utilities for structured Markdown records."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_FIELDS = (
    "record_id",
    "record_type",
    "title",
    "team_ids",
    "player_ids",
    "season",
    "week",
    "status",
    "time_horizon",
    "valid_as_of",
    "last_verified",
    "confidence",
    "source_ids",
    "supersedes",
)


class FrontMatterError(ValueError):
    """Raised when a Markdown metadata block is malformed."""


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"null", "~"}:
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if value.startswith(("[", "{", '"')):
        try:
            return json.loads(value)
        except json.JSONDecodeError as exc:
            raise FrontMatterError(f"invalid JSON-style value {value!r}: {exc.msg}") from exc
    if value.lstrip("-").isdigit():
        return int(value)
    return value


def parse_front_matter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        closing = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise FrontMatterError("opening '---' has no closing delimiter") from exc

    metadata: dict[str, Any] = {}
    for line_number, line in enumerate(lines[1:closing], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            raise FrontMatterError(f"line {line_number} must be 'key: value'")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if not key or " " in key:
            raise FrontMatterError(f"line {line_number} has invalid key {key!r}")
        if key in metadata:
            raise FrontMatterError(f"line {line_number} duplicates key {key!r}")
        metadata[key] = parse_scalar(raw_value)
    body = "\n".join(lines[closing + 1 :])
    if text.endswith("\n"):
        body += "\n"
    return metadata, body


def is_managed_record_path(path: Path, root: Path = REPO_ROOT) -> bool:
    relative = path.relative_to(root)
    parts = relative.parts
    if path.suffix.lower() != ".md" or path.name.lower() == "readme.md":
        return False
    if parts[0] == "templates":
        return True
    if parts[0] == "players":
        return True
    if parts[0] == "weekly" and "games" in parts:
        return True
    if parts[0] == "teams" and any(
        area in parts
        for area in ("offense", "defense", "coaching-staff", "special-teams", "beat-writers")
    ):
        return True
    if parts[0] == "league" and path.name != "schedule.md":
        return True
    return False


def markdown_files(root: Path = REPO_ROOT) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts
    )


def record_files(root: Path = REPO_ROOT, include_templates: bool = False) -> list[Path]:
    records: list[Path] = []
    for path in markdown_files(root):
        relative = path.relative_to(root)
        if not include_templates and relative.parts[0] == "templates":
            continue
        try:
            metadata, _ = parse_front_matter(path)
        except FrontMatterError:
            if is_managed_record_path(path, root):
                records.append(path)
            continue
        if metadata is not None or is_managed_record_path(path, root):
            records.append(path)
    return records


def catalog_entries(root: Path = REPO_ROOT) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in record_files(root):
        metadata, _ = parse_front_matter(path)
        if metadata is None:
            continue
        entry = {field: metadata.get(field) for field in CATALOG_FIELDS}
        entry["path"] = path.relative_to(root).as_posix()
        entries.append(entry)
    return sorted(entries, key=lambda item: (item["record_id"] or "", item["path"]))


def render_catalog(root: Path = REPO_ROOT) -> str:
    lines = [
        json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for entry in catalog_entries(root)
    ]
    return "\n".join(lines) + ("\n" if lines else "")
