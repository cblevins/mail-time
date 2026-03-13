"""
convert_rr.py
Converts RR1826-1911Modified103123 shapefile to a web-ready GeoJSON.

- Reprojects from Albers Equal Area Conic to WGS84 (EPSG:4326)
- Keeps only: RRname, InOpBy
- Drops records with missing/zero InOpBy year
- Dissolves ALL segments by InOpBy year (preserves null-RRname records which
  represent ~82% of the data; geopandas dissolve silently drops null-key rows
  when grouping includes a null column)
- Simplifies geometry to reduce file size
- Exports rr_lines.geojson

Requirements: pip install geopandas shapely
"""

import geopandas as gpd
import os

SHP = "data/RR1826-1911Modified103123/RR1826-1911Modified103123.shp"
OUT = "data/rr_lines.geojson"
SIMPLIFY_TOLERANCE = 0.02  # degrees (~2km)

print(f"Reading shapefile: {SHP}")
gdf = gpd.read_file(SHP)
print(f"  {len(gdf)} records, CRS: {gdf.crs}")

# Reproject to WGS84
print("Reprojecting to WGS84...")
gdf = gdf.to_crs(epsg=4326)

# Keep only needed columns
gdf = gdf[["RRname", "InOpBy", "geometry"]]

# Drop records with missing or zero InOpBy
before = len(gdf)
gdf = gdf[gdf["InOpBy"] > 0]
print(f"  Dropped {before - len(gdf)} records with missing InOpBy; {len(gdf)} remain")

# Dissolve by InOpBy only — this preserves ALL records including those with
# null RRname, which make up ~82% of the data.
# One feature per year; tooltip on the map will show the year.
print("Dissolving segments by InOpBy year...")
gdf = gdf.dissolve(by="InOpBy", as_index=False)
print(f"  Dissolved to {len(gdf)} features (one per year)")

# Simplify geometry
print(f"Simplifying geometry (tolerance={SIMPLIFY_TOLERANCE})...")
gdf["geometry"] = gdf["geometry"].simplify(tolerance=SIMPLIFY_TOLERANCE, preserve_topology=True)

# Export only the columns needed by the browser
gdf = gdf[["InOpBy", "geometry"]]

print(f"Writing {OUT}...")
gdf.to_file(OUT, driver="GeoJSON")
size_mb = os.path.getsize(OUT) / 1_000_000
print(f"  Done. File size: {size_mb:.1f} MB")
