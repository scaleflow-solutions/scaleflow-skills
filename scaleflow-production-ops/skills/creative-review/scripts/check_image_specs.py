#!/usr/bin/env python3
"""
ScaleFlow Creative Review - Image Technical QA Script

Performs technical quality assurance checks on generated images,
validating resolution, format, file size, DPI, color mode, and
suggesting suitable platforms based on dimensions.

Usage:
    python check_image_specs.py --images hero.png banner.jpg
    python check_image_specs.py --images ./output/ --min-width 1920 --min-height 1080
    python check_image_specs.py --images *.png --expected-format PNG --json
"""

import argparse
import json
import math
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print(
        "ERROR: Pillow is required. Install with: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(2)


# ---------------------------------------------------------------------------
# Platform dimension mapping for auto-suggestions
# ---------------------------------------------------------------------------
PLATFORM_DIMENSIONS = {
    (1080, 1080): ["Instagram Feed", "LinkedIn", "Facebook"],
    (1080, 1350): ["Instagram Feed (4:5)"],
    (1080, 1920): [
        "Instagram Story",
        "Instagram Reel",
        "TikTok",
        "YouTube Shorts",
    ],
    (1920, 1080): ["YouTube", "Web Banner", "LinkedIn Banner"],
    (1200, 627): ["LinkedIn Shared Post"],
    (1200, 675): ["Twitter/X"],
}

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".bmp"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _gcd(a: int, b: int) -> int:
    """Return greatest common divisor using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return a


def compute_aspect_ratio(width: int, height: int) -> str:
    """Return a human-readable aspect ratio string like '16:9'."""
    divisor = _gcd(width, height)
    return f"{width // divisor}:{height // divisor}"


def get_dpi(img: Image.Image) -> int | None:
    """
    Attempt to extract DPI from the image.
    Checks the 'dpi' info key first, then falls back to EXIF tag 282/283
    (XResolution / YResolution).
    Returns the horizontal DPI as an integer, or None if unavailable.
    """
    info = img.info or {}

    # Many formats store dpi directly
    if "dpi" in info:
        dpi_val = info["dpi"]
        if isinstance(dpi_val, (tuple, list)) and len(dpi_val) >= 1:
            try:
                return int(round(dpi_val[0]))
            except (TypeError, ValueError):
                pass

    # Try EXIF
    try:
        exif_data = img.getexif()
        if exif_data:
            # Tag 282 = XResolution
            x_res = exif_data.get(282)
            if x_res is not None:
                if isinstance(x_res, tuple):
                    return int(round(x_res[0] / x_res[1])) if x_res[1] else None
                return int(round(float(x_res)))
    except Exception:
        pass

    return None


def get_bit_depth(img: Image.Image) -> str:
    """Return a human-readable bit depth string."""
    mode_bits = {
        "1": "1-bit",
        "L": "8-bit",
        "P": "8-bit",
        "RGB": "8-bit",
        "RGBA": "8-bit",
        "CMYK": "8-bit",
        "YCbCr": "8-bit",
        "LAB": "8-bit",
        "HSV": "8-bit",
        "I": "32-bit",
        "F": "32-bit",
        "I;16": "16-bit",
        "I;16L": "16-bit",
        "I;16B": "16-bit",
        "LA": "8-bit",
        "PA": "8-bit",
        "RGBa": "8-bit",
    }
    return mode_bits.get(img.mode, "unknown")


def has_alpha(img: Image.Image) -> bool:
    """Return True if the image has an alpha channel."""
    return img.mode in ("RGBA", "LA", "PA", "RGBa")


def suggest_platforms(width: int, height: int) -> list[str]:
    """Return a list of platform suggestions based on exact dimension matches."""
    return PLATFORM_DIMENSIONS.get((width, height), [])


def collect_image_paths(paths: list[str]) -> list[Path]:
    """
    Given a list of file/directory paths, return a flat list of image file
    Paths. Directories are scanned (non-recursively) for image extensions.
    """
    result: list[Path] = []
    for p_str in paths:
        p = Path(p_str)
        if p.is_dir():
            for child in sorted(p.iterdir()):
                if child.is_file() and child.suffix.lower() in IMAGE_EXTENSIONS:
                    result.append(child)
        elif p.is_file():
            result.append(p)
        else:
            print(f"WARNING: path does not exist, skipping: {p}", file=sys.stderr)
    return result


# ---------------------------------------------------------------------------
# Core check logic
# ---------------------------------------------------------------------------
def check_image(
    filepath: Path,
    min_width: int,
    min_height: int,
    max_file_size_mb: float,
    expected_format: str | None,
    min_dpi: int,
) -> dict:
    """
    Run all QA checks on a single image file and return a results dict.
    """
    result: dict = {
        "file": str(filepath),
        "error": None,
        "dimensions": None,
        "aspect_ratio": None,
        "format": None,
        "color_mode": None,
        "has_alpha": None,
        "file_size_mb": None,
        "dpi": None,
        "bit_depth": None,
        "suitable_for": [],
        "checks": {},
        "status": "SKIPPED",
    }

    # File size (before opening with Pillow)
    try:
        size_bytes = filepath.stat().st_size
        size_mb = round(size_bytes / (1024 * 1024), 2)
        result["file_size_mb"] = size_mb
    except OSError as exc:
        result["error"] = f"Cannot read file: {exc}"
        return result

    # Open image
    try:
        img = Image.open(filepath)
        img.load()  # force full decode to catch corruption
    except Exception as exc:
        result["error"] = f"Cannot open image: {exc}"
        return result

    width, height = img.size
    result["dimensions"] = {"width": width, "height": height}
    result["aspect_ratio"] = compute_aspect_ratio(width, height)
    result["format"] = img.format
    result["color_mode"] = img.mode
    result["has_alpha"] = has_alpha(img)
    result["bit_depth"] = get_bit_depth(img)
    result["suitable_for"] = suggest_platforms(width, height)

    dpi_value = get_dpi(img)
    result["dpi"] = dpi_value

    # --- Checks ---
    checks: dict[str, dict] = {}

    # Resolution
    res_pass = width >= min_width and height >= min_height
    checks["resolution"] = {
        "pass": res_pass,
        "detail": f"{width}x{height} >= {min_width}x{min_height}"
        if res_pass
        else f"{width}x{height} < {min_width}x{min_height}",
    }

    # File size
    size_pass = size_mb <= max_file_size_mb
    checks["file_size"] = {
        "pass": size_pass,
        "detail": f"{size_mb} MB <= {max_file_size_mb} MB"
        if size_pass
        else f"{size_mb} MB > {max_file_size_mb} MB",
    }

    # Format
    if expected_format:
        fmt_pass = (img.format or "").upper() == expected_format.upper()
        checks["format"] = {
            "pass": fmt_pass,
            "detail": f"Expected {expected_format.upper()}, got {img.format}"
            if not fmt_pass
            else f"{img.format}",
        }
    else:
        checks["format"] = {"pass": True, "detail": "No format requirement"}

    # DPI
    if dpi_value is not None:
        dpi_pass = dpi_value >= min_dpi
        checks["dpi"] = {
            "pass": dpi_pass,
            "detail": f"{dpi_value} >= {min_dpi}"
            if dpi_pass
            else f"{dpi_value} < {min_dpi}",
        }
    else:
        # No DPI info available — treat as pass with note
        checks["dpi"] = {"pass": True, "detail": "DPI info not available (skipped)"}

    result["checks"] = checks
    all_passed = all(c["pass"] for c in checks.values())
    result["status"] = "PASSED" if all_passed else "FAILED"

    return result


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------
def format_text_report(results: list[dict]) -> str:
    """Format results as a human-readable text report."""
    lines: list[str] = []
    lines.append("")
    lines.append("IMAGE TECHNICAL QA REPORT")

    for r in results:
        lines.append("\u2550" * 50)

        lines.append(f"File: {r['file']}")

        if r["error"]:
            lines.append(f"  ERROR: {r['error']}")
            lines.append(f"  Status: SKIPPED")
            continue

        dims = r["dimensions"]
        w, h = dims["width"], dims["height"]
        lines.append(f"  Dimensions:    {w} x {h}")
        lines.append(f"  Aspect ratio:  {r['aspect_ratio']}")
        lines.append(f"  Format:        {r['format']}")

        mode_str = r["color_mode"]
        if r["has_alpha"]:
            mode_str += " (has alpha)"
        lines.append(f"  Color mode:    {mode_str}")

        lines.append(f"  File size:     {r['file_size_mb']} MB")

        dpi_str = str(r["dpi"]) if r["dpi"] is not None else "N/A"
        lines.append(f"  DPI:           {dpi_str}")
        lines.append(f"  Bit depth:     {r['bit_depth']}")

        platforms = r.get("suitable_for", [])
        if platforms:
            lines.append(f"  Suitable for:  {', '.join(platforms)}")
        else:
            lines.append(f"  Suitable for:  (no exact platform match)")

        lines.append(f"  {'─' * 14}")

        checks = r["checks"]

        # Resolution
        c = checks["resolution"]
        mark = "\u2713" if c["pass"] else "\u2717"
        status = "PASS" if c["pass"] else "FAIL"
        lines.append(f"  {mark} Resolution:  {status} ({c['detail']})")

        # File size
        c = checks["file_size"]
        mark = "\u2713" if c["pass"] else "\u2717"
        status = "PASS" if c["pass"] else "FAIL"
        lines.append(f"  {mark} File size:   {status} ({c['detail']})")

        # Format
        c = checks["format"]
        mark = "\u2713" if c["pass"] else "\u2717"
        status = "PASS" if c["pass"] else "FAIL"
        lines.append(f"  {mark} Format:      {status}" + (f" ({c['detail']})" if c["detail"] != "No format requirement" else ""))

        # DPI
        c = checks["dpi"]
        mark = "\u2713" if c["pass"] else "\u2717"
        status = "PASS" if c["pass"] else "FAIL"
        lines.append(f"  {mark} DPI:         {status} ({c['detail']})")

        lines.append(f"  Status: {r['status']}")

    lines.append("\u2550" * 50)

    # Summary
    total = len(results)
    errors = sum(1 for r in results if r["error"])
    passed = sum(1 for r in results if r["status"] == "PASSED")
    failed = sum(1 for r in results if r["status"] == "FAILED")
    skipped = sum(1 for r in results if r["status"] == "SKIPPED")

    lines.append("")
    lines.append(f"SUMMARY: {total} image(s) checked — {passed} passed, {failed} failed, {skipped} skipped")
    lines.append("")

    return "\n".join(lines)


def format_json_report(results: list[dict]) -> str:
    """Format results as a JSON string."""
    report = {
        "report": "IMAGE TECHNICAL QA REPORT",
        "images": results,
        "summary": {
            "total": len(results),
            "passed": sum(1 for r in results if r["status"] == "PASSED"),
            "failed": sum(1 for r in results if r["status"] == "FAILED"),
            "skipped": sum(1 for r in results if r["status"] == "SKIPPED"),
        },
    }
    return json.dumps(report, indent=2)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ScaleFlow Creative Review — Image Technical QA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python check_image_specs.py --images hero.png banner.jpg\n"
            "  python check_image_specs.py --images ./output/ --min-width 1920\n"
            "  python check_image_specs.py --images *.png --expected-format PNG --json\n"
        ),
    )
    parser.add_argument(
        "--images",
        nargs="+",
        required=True,
        help="One or more image file paths, or a directory containing images.",
    )
    parser.add_argument(
        "--min-width",
        type=int,
        default=1080,
        help="Minimum acceptable width in pixels (default: 1080).",
    )
    parser.add_argument(
        "--min-height",
        type=int,
        default=1080,
        help="Minimum acceptable height in pixels (default: 1080).",
    )
    parser.add_argument(
        "--max-file-size-mb",
        type=float,
        default=20,
        help="Maximum file size in megabytes (default: 20).",
    )
    parser.add_argument(
        "--expected-format",
        type=str,
        default=None,
        help='Expected image format, e.g. "JPEG", "PNG" (optional).',
    )
    parser.add_argument(
        "--min-dpi",
        type=int,
        default=72,
        help="Minimum DPI (default: 72).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results in JSON format.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    image_paths = collect_image_paths(args.images)

    if not image_paths:
        print("ERROR: No image files found for the given input.", file=sys.stderr)
        return 1

    results: list[dict] = []
    for img_path in image_paths:
        # Skip non-image files passed explicitly
        if img_path.suffix.lower() not in IMAGE_EXTENSIONS:
            print(
                f"WARNING: '{img_path}' does not have a recognized image extension, skipping.",
                file=sys.stderr,
            )
            continue

        result = check_image(
            filepath=img_path,
            min_width=args.min_width,
            min_height=args.min_height,
            max_file_size_mb=args.max_file_size_mb,
            expected_format=args.expected_format,
            min_dpi=args.min_dpi,
        )
        results.append(result)

    if not results:
        print("ERROR: No valid image files to process.", file=sys.stderr)
        return 1

    # Output
    if args.json_output:
        print(format_json_report(results))
    else:
        print(format_text_report(results))

    # Exit code: 0 if all passed, 1 if any failed
    any_failed = any(r["status"] == "FAILED" for r in results)
    return 1 if any_failed else 0


if __name__ == "__main__":
    sys.exit(main())
