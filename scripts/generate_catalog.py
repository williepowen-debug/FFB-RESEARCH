#!/usr/bin/env python3
"""Generate or verify the repository-wide JSON Lines record catalog."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__:
    from .record_utils import REPO_ROOT, render_catalog
else:
    from record_utils import REPO_ROOT, render_catalog


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "catalog.jsonl")
    parser.add_argument("--check", action="store_true", help="fail if the catalog is stale")
    args = parser.parse_args()

    expected = render_catalog(REPO_ROOT)
    if args.check:
        actual = args.output.read_text(encoding="utf-8") if args.output.is_file() else None
        if actual != expected:
            print(
                f"ERROR: {args.output.relative_to(REPO_ROOT)} is stale; "
                "run python scripts/generate_catalog.py",
                file=sys.stderr,
            )
            return 1
        count = expected.count("\n")
        print(f"OK: catalog is current ({count} record{'s' if count != 1 else ''}).")
        return 0

    args.output.write_text(expected, encoding="utf-8")
    count = expected.count("\n")
    print(f"Wrote {count} record{'s' if count != 1 else ''} to {args.output.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
