#!/usr/bin/env python3
"""
validate_copy_lengths.py
========================

Validates copy text against platform character limits for the ScaleFlow Copy Engine.

Reads an array of copy items (JSON) and checks each item's text length against
the hard character limit for its declared platform. Produces a formatted report
and exits with code 0 (all pass) or 1 (any fail).

Usage examples:
    python validate_copy_lengths.py --input copy_items.json
    python validate_copy_lengths.py --input copy_items.json --strict
    python validate_copy_lengths.py --input copy_items.json --json
    cat copy_items.json | python validate_copy_lengths.py
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

# ---------------------------------------------------------------------------
# Platform character limits
# ---------------------------------------------------------------------------

PLATFORM_LIMITS: dict[str, int] = {
    "instagram_feed": 2200,
    "instagram_story": 40,
    "instagram_reel": 100,
    "instagram_bio": 150,
    "twitter": 280,
    "tiktok": 150,
    "tiktok_bio": 80,
    "linkedin_post": 3000,
    "linkedin_headline": 120,
    "youtube_title": 100,
    "youtube_description": 5000,
    "facebook_post": 63206,
    "facebook_ad_headline": 40,
    "facebook_ad_primary": 125,
    "pinterest": 500,
    "threads": 500,
    "on_screen_text": 25,       # Per text card, 3-5 words
    "headline": 60,             # General headline best practice
    "tagline": 50,              # Short and punchy
    "cta_button": 25,           # Button text
    "email_subject": 60,
    "sms": 160,
}

STRICT_THRESHOLD = 0.80  # Warn when usage exceeds 80 %

# ---------------------------------------------------------------------------
# Validation logic
# ---------------------------------------------------------------------------

def validate_item(item: dict[str, Any], strict: bool = False) -> dict[str, Any]:
    """Validate a single copy item against its platform limit.

    Parameters
    ----------
    item : dict
        Must contain ``platform`` and ``text``. May contain ``format`` and ``label``.
    strict : bool
        When True, items exceeding 80 % of the limit are flagged with a warning.

    Returns
    -------
    dict
        Result object with keys: platform, label, char_count, limit, status,
        and optionally warning.
    """
    platform = item.get("platform", "").strip().lower()
    text = item.get("text", "")
    label = item.get("label", "")
    fmt = item.get("format", "")

    char_count = len(text)

    if platform not in PLATFORM_LIMITS:
        return {
            "platform": platform,
            "format": fmt,
            "label": label,
            "char_count": char_count,
            "limit": None,
            "status": "UNKNOWN",
            "message": f"Unknown platform '{platform}'",
        }

    limit = PLATFORM_LIMITS[platform]
    passed = char_count <= limit

    result: dict[str, Any] = {
        "platform": platform,
        "format": fmt,
        "label": label,
        "char_count": char_count,
        "limit": limit,
        "status": "PASS" if passed else "FAIL",
    }

    if strict and passed and char_count > limit * STRICT_THRESHOLD:
        result["warning"] = f"Over {int(STRICT_THRESHOLD * 100)}% of limit ({char_count}/{limit})"

    return result


def validate_all(items: list[dict[str, Any]], strict: bool = False) -> list[dict[str, Any]]:
    """Validate a list of copy items."""
    return [validate_item(item, strict=strict) for item in items]

# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_report(results: list[dict[str, Any]]) -> str:
    """Return a human-readable validation report."""
    lines: list[str] = []
    lines.append("COPY LENGTH VALIDATION")
    lines.append("\u2550" * 50)

    pass_count = 0
    fail_count = 0
    unknown_count = 0

    for r in results:
        platform = r["platform"]
        label = r["label"] or r["format"] or "-"
        char_count = r["char_count"]
        limit = r["limit"]
        status = r["status"]

        if status == "PASS":
            icon = "\u2713 PASS "
            pass_count += 1
        elif status == "FAIL":
            icon = "\u2717 FAIL "
            fail_count += 1
        else:
            icon = "? UNKNOWN"
            unknown_count += 1

        if limit is not None:
            detail = f"{char_count:>5} / {limit} chars"
        else:
            detail = f"{char_count:>5} chars  (no limit found)"

        lines.append(f"{icon} {platform:<20s} {label:<18s} {detail}")

        if r.get("warning"):
            lines.append(f"       WARNING: {r['warning']}")

        if r.get("message"):
            lines.append(f"       NOTE: {r['message']}")

    lines.append("\u2500" * 50)

    total = len(results)
    if fail_count == 0 and unknown_count == 0:
        lines.append(f"Result: ALL PASSED ({pass_count}/{total})")
    else:
        parts: list[str] = []
        if fail_count:
            parts.append(f"{fail_count} FAILED")
        if unknown_count:
            parts.append(f"{unknown_count} UNKNOWN")
        parts.append(f"{pass_count} passed")
        lines.append(f"Result: {', '.join(parts)} (out of {total})")

    return "\n".join(lines)


def format_json(results: list[dict[str, Any]]) -> str:
    """Return machine-readable JSON output."""
    summary = {
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "PASS"),
        "failed": sum(1 for r in results if r["status"] == "FAIL"),
        "unknown": sum(1 for r in results if r["status"] == "UNKNOWN"),
        "all_passed": all(r["status"] == "PASS" for r in results),
    }
    output = {
        "summary": summary,
        "results": results,
    }
    return json.dumps(output, indent=2)

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate copy text against platform character limits.",
        epilog=(
            "Supported platforms: "
            + ", ".join(sorted(PLATFORM_LIMITS.keys()))
        ),
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        default=None,
        help="Path to a JSON file containing an array of copy items. "
             "If omitted, reads from stdin.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as machine-readable JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Warn about items that exceed 80%% of the platform limit.",
    )
    return parser


def load_input(path: str | None) -> list[dict[str, Any]]:
    """Load copy items from a file path or stdin."""
    if path is not None:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    else:
        data = json.load(sys.stdin)

    if not isinstance(data, list):
        print("Error: input JSON must be an array of copy items.", file=sys.stderr)
        sys.exit(2)

    return data


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    items = load_input(args.input)
    results = validate_all(items, strict=args.strict)

    if args.json_output:
        print(format_json(results))
    else:
        print(format_report(results))

    any_fail = any(r["status"] != "PASS" for r in results)
    sys.exit(1 if any_fail else 0)


if __name__ == "__main__":
    main()
