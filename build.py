#!/usr/bin/env python3
"""
Build script for 1882 Mail Transit Times visualization.

Reads 1882_TransitTimes_edit.csv and embeds it into index.html between
the __CSV_EMBED_START__ and __CSV_EMBED_END__ markers.

Usage: python3 build.py
"""

import re
import sys
from pathlib import Path

DIR = Path(__file__).parent
HTML_FILE = DIR / "index.html"
CSV_FILE = DIR / "data/1882_TransitTimes_edit.csv"

def build():
    if not CSV_FILE.exists():
        sys.exit(f"Error: {CSV_FILE} not found")
    if not HTML_FILE.exists():
        sys.exit(f"Error: {HTML_FILE} not found")

    csv_data = CSV_FILE.read_text(encoding="utf-8").strip()
    html = HTML_FILE.read_text(encoding="utf-8")

    # Replace everything between the embed markers
    pattern = (
        r"(// __CSV_EMBED_START__\n"
        r"// =+\n)"
        r"const CSV_DATA = `[\s\S]*?`;"
        r"(\n// __CSV_EMBED_END__)"
    )
    replacement = rf"\1const CSV_DATA = `{csv_data}`;\2"

    new_html, count = re.subn(pattern, replacement, html)

    if count == 0:
        sys.exit("Error: Could not find CSV embed markers in index.html")

    HTML_FILE.write_text(new_html, encoding="utf-8")
    lines = csv_data.count("\n") + 1
    print(f"Embedded {lines} rows from {CSV_FILE.name} into {HTML_FILE.name}")

if __name__ == "__main__":
    build()
