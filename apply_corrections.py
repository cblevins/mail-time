"""
apply_corrections.py

Reads the user-annotated outliers.csv (change == "yes") and applies
the approved corrections to transit-times-merged.csv.
"""

import os
from pathlib import Path
import pandas as pd

os.chdir(Path(__file__).parent)

KEY_COLS = ["origin_city", "origin_state", "destination_city", "destination_state", "year"]

# --- Load approved corrections ---
outliers = pd.read_csv("data/outliers.csv")
approved = outliers[outliers["change"].str.strip().str.lower() == "yes"].copy()
print(f"Approved corrections to apply: {len(approved)}")
print()

# --- Load main data ---
df = pd.read_csv("data/transit-times-merged.csv")
print(f"Rows in data/transit-times-merged.csv before corrections: {len(df)}")
print()

# --- Apply each correction ---
applied = 0
for _, row in approved.iterrows():
    mask = (
        (df["origin_city"]      == row["origin_city"])      &
        (df["origin_state"]     == row["origin_state"])     &
        (df["destination_city"] == row["destination_city"]) &
        (df["destination_state"]== row["destination_state"])&
        (df["year"]             == row["year"])
    )
    matches = mask.sum()
    if matches == 0:
        print(f"  WARNING: No match found for "
              f"{row['origin_city']}, {row['origin_state']} → "
              f"{row['destination_city']} ({row['year']}) — skipping")
        continue
    if matches > 1:
        print(f"  WARNING: {matches} matches found for "
              f"{row['origin_city']}, {row['origin_state']} → "
              f"{row['destination_city']} ({row['year']}) — skipping to be safe")
        continue

    old_val = df.loc[mask, "hours"].values[0]
    new_val = row["best_candidate_hours"]
    df.loc[mask, "hours"] = new_val
    print(f"  APPLIED: {row['origin_city']}, {row['origin_state']} → "
          f"{row['destination_city']}, {row['destination_state']} ({row['year']}): "
          f"{old_val} → {new_val}")
    applied += 1

print()
print(f"Corrections applied: {applied} / {len(approved)}")

# --- Write back ---
df.to_csv("data/transit-times-merged.csv", index=False)
print(f"Wrote data/transit-times-merged.csv ({len(df)} rows)")
