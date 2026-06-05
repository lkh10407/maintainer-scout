from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .reporting import render_markdown
from .scanner import scan_repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="maintainer-scout",
        description="Audit open-source repository maintenance signals.",
    )
    parser.add_argument("path", nargs="?", default=".", help="Repository path to scan.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--fail-under",
        type=int,
        default=0,
        metavar="SCORE",
        help="Exit with status 1 when the score is below this value.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"maintainer-scout: path is not a directory: {root}", file=sys.stderr)
        return 2

    report = scan_repository(root)
    if args.format == "json":
        print(json.dumps(report.to_dict(), indent=2, sort_keys=True))
    else:
        print(render_markdown(report))

    return 1 if report.score < args.fail_under else 0

