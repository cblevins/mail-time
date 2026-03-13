"""
build_transit.py
Produces transit-times-built.html — a fully self-contained static file
suitable for GitHub Pages or direct browser opening (no server required).

What it does:
  1. Reads about.md → converts to HTML
  2. Reads transit-times-merged.csv → re-embeds between CSV markers
  3. Reads transit-times.html (source template)
  4. Injects about HTML at <!-- __ABOUT_CONTENT__ -->
  5. Embeds rr_lines.geojson as a JS const at // __RR_DATA_INJECT__
  6. Replaces the fetch("rr_lines.geojson")... block with a data-only assignment
     (updateRRLayer() is called from the init block, not inline, so that all
     state variables are defined before it runs)
  7. Writes transit-times-built.html

Usage:
  python3 build_transit.py

Requirements:
  pip install markdown
"""

import json
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency: pip install markdown")

SRC     = "transit-times.html"
OUT     = "index.html"
ABOUT   = "about.md"
GEOJSON = "data/rr_lines.geojson"
CSV     = "data/transit-times-merged.csv"

# ── 1. Convert about.md → HTML ──────────────────────────────────────────────
print(f"Reading {ABOUT}...")
about_md = open(ABOUT, encoding="utf-8").read()
about_html = markdown.markdown(about_md, extensions=["extra"])

# ── 2. Read source template ──────────────────────────────────────────────────
print(f"Reading {SRC}...")
html = open(SRC, encoding="utf-8").read()

# ── 3. Re-embed CSV data from transit-times-merged.csv ───────────────────────
print(f"Reading {CSV}...")
csv_data = open(CSV, encoding="utf-8").read().strip()
csv_rows = csv_data.count("\n")
print(f"  {csv_rows} data rows found.")

CSV_START = "// __CSV_EMBED_START__\n// ============================================================\n"
CSV_END   = "\n// __CSV_EMBED_END__"
pattern = re.compile(
    r"([ \t]*// __CSV_EMBED_START__[ \t]*\n[ \t]*// =+[ \t]*\n)"
    r"[ \t]*const CSV_DATA = `[\s\S]*?`;"
    r"(\n[ \t]*// __CSV_EMBED_END__)"
)
# Preserve the indentation captured in group 1; write CSV without leading indent
# (the backtick string content is large and whitespace-insensitive)
replacement = r"\g<1>" + f"const CSV_DATA = `{csv_data}`;" + r"\g<2>"
html_new, count = pattern.subn(replacement, html)
if count == 0:
    sys.exit("ERROR: CSV embed markers not found in source HTML.")
html = html_new
print(f"  CSV re-embedded ({csv_rows} rows).")

# Write refreshed CSV back to source template for local development
open(SRC, "w", encoding="utf-8").write(html)
print(f"  {SRC} updated with fresh CSV.")

# ── 4. Inject about content ──────────────────────────────────────────────────
if "<!-- __ABOUT_CONTENT__ -->" not in html:
    sys.exit("ERROR: <!-- __ABOUT_CONTENT__ --> marker not found in source HTML.")
html = html.replace("<!-- __ABOUT_CONTENT__ -->", about_html)
print("  About content injected.")

# ── 5. Embed GeoJSON ─────────────────────────────────────────────────────────
print(f"Reading {GEOJSON}...")
geojson_str = open(GEOJSON, encoding="utf-8").read()
try:
    json.loads(geojson_str)
except json.JSONDecodeError as e:
    sys.exit(f"ERROR: {GEOJSON} is not valid JSON: {e}")

rr_const = f"const RR_DATA = {geojson_str};"

if "// __RR_DATA_INJECT__" not in html:
    sys.exit("ERROR: // __RR_DATA_INJECT__ marker not found in source HTML.")
html = html.replace("// __RR_DATA_INJECT__", rr_const)
print(f"  GeoJSON embedded ({len(geojson_str) / 1_000_000:.1f} MB).")

# ── 6. Replace fetch() block with data-only assignment ───────────────────────
# Use a regex to handle variations in indentation and arrow function syntax.
fetch_pattern = re.compile(
    r'[ \t]*fetch\("rr_lines\.geojson"\)\s*\n'
    r'(?:[ \t]*\.then\([\s\S]*?\n)*?'
    r'[ \t]*\}\);',
    re.MULTILINE
)
html_new, count = fetch_pattern.subn("rrData = RR_DATA;\nupdateRRLayer();", html)
if count == 0:
    sys.exit("ERROR: fetch() block not found in source HTML — did it change?")
html = html_new
print("  fetch() replaced with direct data assignment.")

# ── 7. Write output ──────────────────────────────────────────────────────────
print(f"Writing {OUT}...")
open(OUT, "w", encoding="utf-8").write(html)
size_mb = len(html.encode("utf-8")) / 1_000_000
print(f"  Done. Output size: {size_mb:.1f} MB")
print(f"\n  {OUT} is ready — open directly in a browser or deploy to GitHub Pages.")
