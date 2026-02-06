#!/usr/bin/env python3
"""Lightweight validation for the Meridian theme."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "dripyard_meridian.info.yml",
    "dripyard_meridian.libraries.yml",
    "dripyard_meridian.theme",
    "templates/html.html.twig",
    "templates/page.html.twig",
    "templates/node.html.twig",
    "css/base.css",
    "css/layout.css",
    "css/components.css",
    "js/meridian.js",
]

REQUIRED_INFO_KEYS = [
    "name:",
    "type:",
    "core_version_requirement:",
    "base theme:",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def check_info_keys() -> None:
    info_path = ROOT / "dripyard_meridian.info.yml"
    content = info_path.read_text(encoding="utf-8")
    missing = [key for key in REQUIRED_INFO_KEYS if key not in content]
    if missing:
        fail("Missing info.yml keys: " + ", ".join(missing))


def check_non_empty_files() -> None:
    for rel_path in ["css/base.css", "css/layout.css", "css/components.css", "js/meridian.js"]:
        if (ROOT / rel_path).stat().st_size < 20:
            fail(f"{rel_path} looks empty")


def check_templates() -> None:
    page_template = (ROOT / "templates/page.html.twig").read_text(encoding="utf-8")
    if "page.content" not in page_template:
        fail("page.html.twig must render page.content")


def run_lint() -> None:
    check_required_files()
    check_info_keys()
    check_non_empty_files()


def run_test() -> None:
    check_templates()


def main() -> None:
    if len(sys.argv) < 2:
        fail("Usage: python scripts/validate.py [lint|test]")

    command = sys.argv[1]
    if command == "lint":
        run_lint()
    elif command == "test":
        run_test()
    else:
        fail(f"Unknown command: {command}")

    print("OK")


if __name__ == "__main__":
    main()
