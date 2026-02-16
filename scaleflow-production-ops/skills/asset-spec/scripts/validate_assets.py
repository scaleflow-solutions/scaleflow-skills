#!/usr/bin/env python3
"""
ScaleFlow Asset Validator
=========================
Validates exported creative assets against an export specification table.

Usage:
    python validate_assets.py --spec specs.json --assets ./exports/
    python validate_assets.py --spec specs.json --assets ./exports/ --json
    python validate_assets.py --spec specs.json --assets ./exports/ --mapping mapping.json --verbose
"""

import argparse
import fnmatch
import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print(
        "ERROR: Pillow is required. Install with: pip install Pillow>=10.0.0",
        file=sys.stderr,
    )
    sys.exit(2)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VIDEO_EXTENSIONS = {".mp4"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".pdf"}

# Canonical format names mapped from file extensions
FORMAT_ALIASES = {
    ".jpg": "jpg",
    ".jpeg": "jpg",
    ".png": "png",
    ".webp": "webp",
    ".tiff": "tiff",
    ".tif": "tiff",
    ".pdf": "pdf",
    ".mp4": "mp4",
}

# Pillow format strings to our canonical names
PILLOW_FORMAT_MAP = {
    "JPEG": "jpg",
    "PNG": "png",
    "WEBP": "webp",
    "TIFF": "tiff",
    "PDF": "pdf",
    "MPO": "jpg",  # multi-picture JPEG variant
}

# Color-space expectations: spec value -> acceptable Pillow mode(s)
COLOR_SPACE_MODES = {
    "srgb": {"RGB", "RGBA"},
    "rgb": {"RGB", "RGBA"},
    "cmyk": {"CMYK"},
}

DIMENSION_TOLERANCE = 1  # pixels


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def file_size_mb(path: Path) -> float:
    """Return file size in megabytes."""
    return path.stat().st_size / (1024 * 1024)


def is_video(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS


def canonical_format(path: Path) -> str:
    return FORMAT_ALIASES.get(path.suffix.lower(), path.suffix.lower().lstrip("."))


def match_file_to_spec(filename: str, specs: list[dict], mapping: dict | None) -> dict | None:
    """Return the first spec that matches the given filename."""
    # Explicit mapping takes priority
    if mapping and filename in mapping:
        spec_name = mapping[filename]
        for spec in specs:
            if spec.get("asset_name") == spec_name:
                return spec

    # Fall back to filename_pattern glob matching
    for spec in specs:
        pattern = spec.get("filename_pattern")
        if pattern and fnmatch.fnmatch(filename, pattern):
            return spec

    # Try pattern matching with format extension appended
    for spec in specs:
        pattern = spec.get("filename_pattern")
        fmt = spec.get("format", "")
        if pattern:
            pattern_with_ext = f"{pattern}.{fmt}"
            if fnmatch.fnmatch(filename, pattern_with_ext):
                return spec

    return None


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_asset(file_path: Path, spec: dict) -> dict:
    """
    Validate a single asset file against its spec.

    Returns a result dict with per-check outcomes.
    """
    result = {
        "file": file_path.name,
        "spec_name": spec.get("asset_name", "Unknown"),
        "checks": [],
        "passed": True,
        "error": None,
    }

    checks = result["checks"]
    actual_size_mb = file_size_mb(file_path)

    # ------------------------------------------------------------------
    # Format check
    # ------------------------------------------------------------------
    expected_format = spec.get("format", "").lower()
    actual_format = canonical_format(file_path)
    format_ok = actual_format == expected_format
    checks.append(
        {
            "name": "Format",
            "passed": format_ok,
            "actual": actual_format.upper(),
            "expected": expected_format,
        }
    )
    if not format_ok:
        result["passed"] = False

    # ------------------------------------------------------------------
    # File size check
    # ------------------------------------------------------------------
    max_size = spec.get("max_file_size_mb")
    if max_size is not None:
        size_ok = actual_size_mb <= float(max_size)
        checks.append(
            {
                "name": "File size",
                "passed": size_ok,
                "actual": f"{actual_size_mb:.1f} MB",
                "expected": f"max {max_size} MB",
            }
        )
        if not size_ok:
            result["passed"] = False

    # ------------------------------------------------------------------
    # Video files: skip image-specific checks
    # ------------------------------------------------------------------
    if is_video(file_path):
        return result

    # ------------------------------------------------------------------
    # Image-specific checks (Pillow)
    # ------------------------------------------------------------------
    try:
        with Image.open(file_path) as img:
            # Dimensions
            expected_w = spec.get("width")
            expected_h = spec.get("height")
            if expected_w is not None and expected_h is not None:
                actual_w, actual_h = img.size
                dim_ok = (
                    abs(actual_w - int(expected_w)) <= DIMENSION_TOLERANCE
                    and abs(actual_h - int(expected_h)) <= DIMENSION_TOLERANCE
                )
                checks.append(
                    {
                        "name": "Dimensions",
                        "passed": dim_ok,
                        "actual": f"{actual_w}x{actual_h}",
                        "expected": f"{expected_w}x{expected_h}",
                    }
                )
                if not dim_ok:
                    result["passed"] = False

            # Pillow-reported format
            pillow_fmt = PILLOW_FORMAT_MAP.get(img.format, img.format)
            if pillow_fmt and expected_format:
                pf_ok = pillow_fmt == expected_format
                if not pf_ok:
                    # Only add if different from extension check
                    checks.append(
                        {
                            "name": "Internal format",
                            "passed": pf_ok,
                            "actual": img.format,
                            "expected": expected_format,
                        }
                    )
                    result["passed"] = False

            # Color space
            expected_cs = spec.get("color_space", "").lower()
            if expected_cs:
                acceptable = COLOR_SPACE_MODES.get(expected_cs, set())
                cs_ok = img.mode in acceptable if acceptable else True
                display_expected = spec.get("color_space", expected_cs)
                checks.append(
                    {
                        "name": "Color space",
                        "passed": cs_ok,
                        "actual": img.mode,
                        "expected": display_expected,
                    }
                )
                if not cs_ok:
                    result["passed"] = False

            # DPI
            min_dpi = spec.get("min_dpi")
            if min_dpi is not None:
                dpi_info = img.info.get("dpi")
                if dpi_info:
                    actual_dpi = int(round(min(dpi_info)))
                    dpi_ok = actual_dpi >= int(min_dpi)
                    checks.append(
                        {
                            "name": "DPI",
                            "passed": dpi_ok,
                            "actual": str(actual_dpi),
                            "expected": f"min {min_dpi}",
                        }
                    )
                    if not dpi_ok:
                        result["passed"] = False
                else:
                    # No DPI metadata embedded
                    checks.append(
                        {
                            "name": "DPI",
                            "passed": False,
                            "actual": "not set",
                            "expected": f"min {min_dpi}",
                        }
                    )
                    result["passed"] = False

    except Exception as exc:
        result["error"] = f"Could not read image: {exc}"
        result["passed"] = False

    return result


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

SEPARATOR = "\u2550" * 50
THIN_SEP = "\u2500" * 50


def print_report(results: list[dict], verbose: bool = False) -> None:
    """Print a human-readable validation report."""
    print()
    print("ASSET VALIDATION REPORT")
    print(SEPARATOR)

    for res in results:
        print(f"File: {res['file']}")
        print(f"Spec: {res['spec_name']}")

        if res.get("error"):
            print(f"  ERROR: {res['error']}")

        for chk in res["checks"]:
            if not verbose and chk["passed"]:
                # In non-verbose mode, still show all checks
                pass
            icon = "\u2713" if chk["passed"] else "\u2717"
            label = chk["name"]
            print(f"  {icon} {label + ':':13s} {chk['actual']} (expected {chk['expected']})")

        status = "PASSED" if res["passed"] else "FAILED"
        print(f"  Status: {status}")
        print(THIN_SEP)

    # Summary
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed
    print()
    print(f"Summary: {passed}/{total} assets passed, {failed} failed")
    print()


def print_json_report(results: list[dict]) -> None:
    """Print machine-readable JSON report."""
    report = {
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "failed": sum(1 for r in results if not r["passed"]),
        "results": results,
    }
    print(json.dumps(report, indent=2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate exported creative assets against an export spec."
    )
    parser.add_argument(
        "--spec",
        required=True,
        help="Path to the JSON file containing export specifications.",
    )
    parser.add_argument(
        "--assets",
        required=True,
        help="Path to the directory containing exported asset files.",
    )
    parser.add_argument(
        "--mapping",
        default=None,
        help="Optional JSON file mapping filenames to spec asset_name values.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output for all checks (including passing).",
    )

    args = parser.parse_args()

    # Load spec
    spec_path = Path(args.spec)
    if not spec_path.is_file():
        print(f"ERROR: Spec file not found: {spec_path}", file=sys.stderr)
        return 2

    try:
        with open(spec_path, "r", encoding="utf-8") as f:
            specs = json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERROR: Failed to read spec file: {exc}", file=sys.stderr)
        return 2

    if not isinstance(specs, list):
        print("ERROR: Spec JSON must be an array of spec objects.", file=sys.stderr)
        return 2

    # Load optional mapping
    mapping = None
    if args.mapping:
        mapping_path = Path(args.mapping)
        if not mapping_path.is_file():
            print(f"ERROR: Mapping file not found: {mapping_path}", file=sys.stderr)
            return 2
        try:
            with open(mapping_path, "r", encoding="utf-8") as f:
                mapping = json.load(f)
        except (json.JSONDecodeError, OSError) as exc:
            print(f"ERROR: Failed to read mapping file: {exc}", file=sys.stderr)
            return 2

    # Scan assets directory
    assets_dir = Path(args.assets)
    if not assets_dir.is_dir():
        print(f"ERROR: Assets directory not found: {assets_dir}", file=sys.stderr)
        return 2

    all_extensions = IMAGE_EXTENSIONS | VIDEO_EXTENSIONS
    asset_files = sorted(
        p for p in assets_dir.iterdir()
        if p.is_file() and p.suffix.lower() in all_extensions
    )

    if not asset_files:
        print("WARNING: No supported asset files found in the directory.", file=sys.stderr)
        return 0

    # Validate each file
    results: list[dict] = []
    unmatched: list[str] = []

    for file_path in asset_files:
        spec = match_file_to_spec(file_path.name, specs, mapping)
        if spec is None:
            unmatched.append(file_path.name)
            if args.verbose:
                results.append(
                    {
                        "file": file_path.name,
                        "spec_name": "UNMATCHED",
                        "checks": [],
                        "passed": False,
                        "error": "No matching spec found for this file.",
                    }
                )
            continue

        result = validate_asset(file_path, spec)
        results.append(result)

    # Report unmatched files
    if unmatched and not args.json_output:
        print(f"\nWARNING: {len(unmatched)} file(s) did not match any spec:", file=sys.stderr)
        for name in unmatched:
            print(f"  - {name}", file=sys.stderr)

    # Output
    if args.json_output:
        if unmatched:
            for name in unmatched:
                results.append(
                    {
                        "file": name,
                        "spec_name": "UNMATCHED",
                        "checks": [],
                        "passed": False,
                        "error": "No matching spec found for this file.",
                    }
                )
        print_json_report(results)
    else:
        print_report(results, verbose=args.verbose)

    # Exit code
    any_failed = any(not r["passed"] for r in results)
    return 1 if any_failed else 0


if __name__ == "__main__":
    sys.exit(main())
