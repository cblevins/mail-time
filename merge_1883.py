"""
merge_1883.py

Merges 1883-transit-times-google.csv into transit-times-merged.csv.
The 1883 file uses hyphenated column names and has no year column;
this script normalizes it and appends it as year=1883.
"""

import os
from pathlib import Path
import pandas as pd

os.chdir(Path(__file__).parent)

# --- Load existing merged CSV ---
merged = pd.read_csv("data/transit-times-merged.csv")
print(f"Existing rows in transit-times-merged.csv: {len(merged)}")
print(f"  Years present: {sorted(merged['year'].unique())}")

# --- Load and normalize 1883 CSV ---
df_1883 = pd.read_csv("data/1883-transit-times-google.csv")
print(f"\n1883 raw rows: {len(df_1883)}")
print(f"  Columns: {list(df_1883.columns)}")

# Rename hyphenated columns to underscores
df_1883 = df_1883.rename(columns={
    "origin-city":       "origin_city",
    "origin-state":      "origin_state",
    "destination-city":  "destination_city",
    "destination-state": "destination_state",
})

# Add year column
df_1883["year"] = 1883

# Reorder columns to match merged schema
df_1883 = df_1883[["year", "origin_city", "origin_state",
                    "destination_city", "destination_state", "hours"]]

# --- Guard: don't double-add if 1883 already present ---
if 1883 in merged["year"].values:
    print("\nYear 1883 already present in merged file — aborting to avoid duplicates.")
else:
    combined = pd.concat([merged, df_1883], ignore_index=True)
    combined = combined.sort_values(
        ["year", "origin_state", "origin_city", "destination_city"]
    ).reset_index(drop=True)

    combined.to_csv("data/transit-times-merged.csv", index=False)
    print(f"\nWrote data/transit-times-merged.csv")
    print(f"  Total rows: {len(combined)}  (was {len(merged)}, added {len(df_1883)})")
    print(f"  Years present: {sorted(combined['year'].unique())}")

    # Spot-check
    spot = combined[
        (combined["year"] == 1883) &
        (combined["origin_city"] == "Decatur") &
        (combined["destination_city"] == "Boston")
    ]
    print(f"\nSpot-check (Decatur → Boston, 1883):")
    print(spot.to_string(index=False))
