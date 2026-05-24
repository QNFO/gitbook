#!/usr/bin/env python3
r"""
sync_releases.py - Sync QWAV releases from Obsidian/releases to QNFO/gitbook repo.

Reads all .md files from G:\My Drive\Obsidian\releases\YYYY\MM\,
normalizes filenames, copies to gitbook repo structure, and generates
SUMMARY.md for GitBook table of contents.

Usage:
    python sync_releases.py [--dry-run] [--since YYYY-MM]

Options:
    --dry-run    Print what would be copied without writing files
    --since      Only sync releases from this month onward (default: all)
"""

import os
import sys
import shutil
import argparse
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# === CONFIGURATION ===
SOURCE_ROOT = Path(r"G:\My Drive\Obsidian\releases")
TARGET_ROOT = Path(r"G:\My Drive\projects\2026\05\gitbook-integration\content\releases")
SUMMARY_PATH = Path(r"G:\My Drive\projects\2026\05\gitbook-integration\content\SUMMARY.md")
README_SOURCE = Path(r"G:\My Drive\QWAV\README.md")
README_TARGET = Path(r"G:\My Drive\projects\2026\05\gitbook-integration\content\README.md")

# Languages for translation announcement
TARGET_LANGUAGES = {
    "zh": "Chinese",
    "es": "Spanish",
    "fr": "French",
    "ar": "Arabic",
    "ru": "Russian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "de": "German",
    "ko": "Korean",
    "hi": "Hindi",
}


def normalize_filename(name):
    """Normalize filenames for GitBook compatibility."""
    name = name.strip()
    # Replace problematic characters with hyphens
    name = re.sub(r'[:?*"<>|]', '-', name)
    # Collapse multiple hyphens
    name = re.sub(r'-+', '-', name)
    if not name.endswith('.md'):
        name += '.md'
    return name


def scan_releases(since=None):
    """Scan Obsidian/releases and return dict of {year: {month: [file_paths]}}."""
    releases = defaultdict(lambda: defaultdict(list))

    if not SOURCE_ROOT.exists():
        print("ERROR: Source directory not found: " + str(SOURCE_ROOT))
        return releases

    for filepath in sorted(SOURCE_ROOT.rglob("*.md")):
        # Skip files in .space directory
        if '.space' in str(filepath):
            continue

        rel = filepath.relative_to(SOURCE_ROOT)
        parts = rel.parts
        if len(parts) < 2:
            continue

        year_str = parts[0]
        month_str = parts[1]

        # Validate year/month format
        if not (year_str.isdigit() and month_str.isdigit()):
            continue

        # Apply --since filter
        if since:
            file_date = year_str + "-" + month_str
            if file_date < since:
                continue

        releases[year_str][month_str].append(filepath)

    return releases


def generate_summary(releases, target_root):
    """Generate GitBook SUMMARY.md from release structure."""
    lines = [
        "# Table of Contents",
        "",
        "* [QNFO Research Home](README.md)",
        "* [About QNFO](ABOUT.md)",
        "* [License](LICENSE.md)",
        "",
        "## Research Publications",
        "",
    ]

    for year in sorted(releases.keys(), reverse=True):
        lines.append("### " + year)
        for month in sorted(releases[year].keys(), reverse=True):
            month_int = int(month)
            if month_int == 0 or month == "00":
                month_name = "Foundational"
            elif 1 <= month_int <= 12:
                month_name = datetime(int(year), month_int, 1).strftime("%B")
            else:
                month_name = "Month " + month

            lines.append("* [" + month_name + " " + year + "](releases/" + year + "/" + month + "/README.md)")

            for filepath in sorted(releases[year][month]):
                title = filepath.stem
                safe_name = normalize_filename(filepath.name)
                rel_path = "releases/" + year + "/" + month + "/" + safe_name
                lines.append("  * [" + title + "](" + rel_path + ")")

        lines.append("")

    # Translation notice
    lines.append("## Translations")
    lines.append("")
    lines.append("This documentation is available in multiple languages via GitBook AI translations:")
    lines.append("")
    for code, name in sorted(TARGET_LANGUAGES.items()):
        lines.append("* " + name + " (" + code + ")")
    lines.append("")
    lines.append("Use the language selector in the top navigation to switch languages.")

    return "\n".join(lines)


def generate_month_readme(year, month, files):
    """Generate README.md for a month directory."""
    month_int = int(month)
    if month_int == 0 or month == "00":
        heading = "# " + year + " - Foundational Publications"
        subheading = str(len(files)) + " foundational and early publications from " + year + "."
    elif 1 <= month_int <= 12:
        month_name = datetime(int(year), month_int, 1).strftime("%B")
        heading = "# " + month_name + " " + year + " - Research Publications"
        subheading = str(len(files)) + " publications from " + month_name + " " + year + "."
    else:
        heading = "# " + year + "/" + month + " - Research Publications"
        subheading = str(len(files)) + " publications."

    lines = [
        heading,
        "",
        subheading,
        "",
        "## Papers",
        "",
    ]
    for filepath in sorted(files):
        title = filepath.stem
        lines.append("* [" + title + "](" + normalize_filename(filepath.name) + ")")
    lines.append("")
    return "\n".join(lines)


def copy_releases(releases, target_root, dry_run=False):
    """Copy release files from source to target directory structure.
    Returns (copied_count, skipped_count)."""
    copied = 0
    skipped = 0

    for year, months in releases.items():
        for month, files in months.items():
            month_dir = target_root / str(year) / str(month)
            if not dry_run:
                month_dir.mkdir(parents=True, exist_ok=True)

            # Generate month README
            readme_content = generate_month_readme(str(year), str(month), files)
            readme_path = month_dir / "README.md"
            if not dry_run:
                readme_path.write_text(readme_content, encoding='utf-8')
            copied += 1

            for src in files:
                dest_name = normalize_filename(src.name)
                dest = month_dir / dest_name

                if not dry_run:
                    content = src.read_text(encoding='utf-8')
                    license_footer = (
                        "\n\n---\n"
                        "*Published by [QNFO](https://github.com/QNFO) under the "
                        "[QNFO Content License Agreement v1.1](https://github.com/QNFO/license). "
                        "Non-commercial use only. Attribution required.*\n"
                        "*Original: " + str(src.relative_to(SOURCE_ROOT)) + "*\n"
                    )
                    content += license_footer
                    dest.write_text(content, encoding='utf-8')

                copied += 1

    return copied, skipped


def main():
    parser = argparse.ArgumentParser(description="Sync QWAV releases to GitBook repo")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print what would be copied without writing files")
    parser.add_argument("--since", type=str, default=None,
                        help="Only sync releases from YYYY-MM onward")
    args = parser.parse_args()

    print("=" * 60)
    print("QWAV -> GitBook Release Sync")
    print("=" * 60)

    releases = scan_releases(args.since)
    if not releases:
        print("No releases found.")
        return

    total_files = sum(len(files) for year_data in releases.values()
                      for files in year_data.values())
    total_months = sum(len(months) for months in releases.values())
    print("Found: " + str(total_files) + " files across " + str(total_months) + " months")

    if args.dry_run:
        print("\n[DRY RUN] Would copy:")
        for year in sorted(releases.keys()):
            for month in sorted(releases[year].keys()):
                files = releases[year][month]
                print("  " + year + "/" + month + ": " + str(len(files)) +
                      " files -> " + str(TARGET_ROOT / year / month))
    else:
        copied, skipped = copy_releases(releases, TARGET_ROOT, dry_run=False)
        print("\nCopied: " + str(copied) + " files (including README.md per month)")

        summary = generate_summary(releases, TARGET_ROOT)
        SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
        SUMMARY_PATH.write_text(summary, encoding='utf-8')
        print("Generated: " + str(SUMMARY_PATH))

        if README_SOURCE.exists():
            content = README_SOURCE.read_text(encoding='utf-8')
            translation_notice = (
                "\n\n---\n"
                "## Translations\n\n"
                "This documentation is available in 10+ languages via GitBook AI translations. "
                "Use the language selector in the top navigation bar to switch languages.\n\n"
            )
            content += translation_notice
            README_TARGET.parent.mkdir(parents=True, exist_ok=True)
            README_TARGET.write_text(content, encoding='utf-8')
            print("Copied: README.md")

        license_src = Path(r"G:\My Drive\QWAV\LICENSE")
        license_dst = Path(r"G:\My Drive\projects\2026\05\gitbook-integration\content\LICENSE.md")
        if license_src.exists():
            shutil.copy2(str(license_src), str(license_dst))
            print("Copied: LICENSE")

    print("\nDone.")


if __name__ == "__main__":
    main()
