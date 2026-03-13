"""
find_outliers.py

Detect potential transcription errors in transit-times-merged.csv by comparing
each route's value across years. Flags values that deviate significantly from the
median of other years, then checks whether a 3<->8 digit substitution explains
the discrepancy (a common OCR error in 19th-century railroad tables).

Outputs:
  outliers.csv       - machine-readable flagged values with suggested corrections
  outliers-report.md - human-readable report grouped by confidence
"""

import pandas as pd
import numpy as np
from itertools import product

THRESHOLD = 15.0  # hours: minimum deviation to flag as potential outlier
CANDIDATE_WINDOW = 10.0  # hours: max distance from median for a candidate to qualify


def decimal_to_hhmm(hours: float) -> str:
    """Convert decimal hours to HH:MM string."""
    h = int(hours)
    m = round((hours - h) * 60)
    if m == 60:
        h += 1
        m = 0
    return f"{h}:{m:02d}"


def hhmm_to_decimal(h: int, m: int) -> float:
    """Convert hours + minutes to decimal hours."""
    return h + m / 60.0


def substitution_candidates(hours: float) -> list[dict]:
    """
    Generate all candidates from 3<->8 digit substitutions applied to the
    integer hours and minutes components of a decimal hours value.
    Returns list of dicts with keys: h, m, hours, hhmm, substitution.
    """
    h = int(hours)
    m = round((hours - h) * 60)
    candidates = []

    def swap_digits(s: str) -> list[str]:
        """Return all strings produced by swapping one or more 3s and 8s."""
        positions = [i for i, c in enumerate(s) if c in "38"]
        if not positions:
            return []
        results = set()
        for r in range(1, len(positions) + 1):
            from itertools import combinations
            for combo in combinations(positions, r):
                chars = list(s)
                for pos in combo:
                    chars[pos] = "8" if chars[pos] == "3" else "3"
                candidate = "".join(chars)
                if candidate != s:
                    results.add(candidate)
        return list(results)

    h_str = str(h)
    m_str = f"{m:02d}"

    # Try substitutions in hours component only
    for new_h_str in swap_digits(h_str):
        new_h = int(new_h_str)
        if new_h >= 0:
            candidates.append({
                "h": new_h, "m": m,
                "hours": hhmm_to_decimal(new_h, m),
                "hhmm": f"{new_h}:{m:02d}",
                "substitution": f"H: {h_str}->{new_h_str}"
            })

    # Try substitutions in minutes component only
    for new_m_str in swap_digits(m_str):
        new_m = int(new_m_str)
        if 0 <= new_m <= 59:
            candidates.append({
                "h": h, "m": new_m,
                "hours": hhmm_to_decimal(h, new_m),
                "hhmm": f"{h}:{new_m:02d}",
                "substitution": f"M: {m_str}->{new_m_str}"
            })

    # Try substitutions in both
    for new_h_str in swap_digits(h_str):
        for new_m_str in swap_digits(m_str):
            new_h = int(new_h_str)
            new_m = int(new_m_str)
            if new_h >= 0 and 0 <= new_m <= 59:
                candidates.append({
                    "h": new_h, "m": new_m,
                    "hours": hhmm_to_decimal(new_h, new_m),
                    "hhmm": f"{new_h}:{new_m:02d}",
                    "substitution": f"H: {h_str}->{new_h_str}, M: {m_str}->{new_m_str}"
                })

    return candidates


def missing_digit_candidates(hours: float) -> list[dict]:
    """
    Check if prepending a digit (1, 2) to the hours integer explains the outlier
    (e.g., 5:35 that should be 65:35, or 24:04 that should be 124:04).
    """
    h = int(hours)
    m = round((hours - h) * 60)
    candidates = []
    for prefix in ["1", "2"]:
        new_h = int(prefix + str(h))
        candidates.append({
            "h": new_h, "m": m,
            "hours": hhmm_to_decimal(new_h, m),
            "hhmm": f"{new_h}:{m:02d}",
            "substitution": f"prepend '{prefix}' to H: {h}->{new_h}"
        })
    return candidates


def classify_candidate(substitution: str) -> str:
    """Classify the error type from the substitution description."""
    if "prepend" in substitution:
        return "missing_digit"
    if "->" in substitution:
        parts = substitution.replace("H: ", "").replace("M: ", "")
        for part in parts.split(","):
            part = part.strip()
            if "->" in part:
                before, after = part.split("->")
                before, after = before.strip(), after.strip()
                for b, a in zip(before, after):
                    if b != a:
                        if b == "3" and a == "8":
                            return "3to8"
                        if b == "8" and a == "3":
                            return "8to3"
    return "unknown"


def main():
    df = pd.read_csv("data/transit-times-merged.csv")
    route_cols = ["origin_city", "origin_state", "destination_city", "destination_state"]
    years = sorted(df["year"].unique())

    records = []

    for route_key, group in df.groupby(route_cols):
        if len(group) < 2:
            continue  # need at least 2 years to compare

        year_to_hours = dict(zip(group["year"], group["hours"]))

        for year, value in year_to_hours.items():
            other_values = [v for y, v in year_to_hours.items() if y != year]
            if not other_values:
                continue
            other_median = float(np.median(other_values))
            deviation = abs(value - other_median)

            if deviation < THRESHOLD:
                continue

            # This value is flagged — try to find a correction
            all_candidates = (
                substitution_candidates(value) +
                missing_digit_candidates(value)
            )

            # Find the best candidate (closest to other_median, within CANDIDATE_WINDOW)
            best = None
            best_dev = float("inf")
            for cand in all_candidates:
                cand_dev = abs(cand["hours"] - other_median)
                if cand_dev < best_dev and cand_dev <= CANDIDATE_WINDOW:
                    best_dev = cand_dev
                    best = cand

            if best is not None:
                if best_dev <= 5:
                    confidence = "HIGH"
                elif best_dev <= 10:
                    confidence = "MEDIUM"
                else:
                    confidence = "LOW"
                error_type = classify_candidate(best["substitution"])
                candidate_hhmm = best["hhmm"]
                candidate_hours = best["hours"]
                candidate_dev = best_dev
                substitution = best["substitution"]
            else:
                confidence = "LOW"
                error_type = "unknown"
                candidate_hhmm = ""
                candidate_hours = None
                candidate_dev = None
                substitution = ""

            # Label likely-historical cases: 1882/1883 value is higher than other years
            # (consistent with genuine improvement in rail travel over time;
            #  both early years may be legitimately slower than 1892+ routes)
            is_likely_historical = (
                year in (1882, 1883)
                and value > other_median
                and confidence == "LOW"
            )
            if is_likely_historical:
                confidence = "HISTORICAL"

            origin_city, origin_state, dest_city, dest_state = route_key
            records.append({
                "origin_city": origin_city,
                "origin_state": origin_state,
                "destination_city": dest_city,
                "destination_state": dest_state,
                "year": year,
                "current_hours": round(value, 4),
                "current_hhmm": decimal_to_hhmm(value),
                "other_years_median": round(other_median, 4),
                "deviation": round(deviation, 4),
                "best_candidate_hhmm": candidate_hhmm,
                "best_candidate_hours": round(candidate_hours, 4) if candidate_hours is not None else "",
                "candidate_deviation": round(candidate_dev, 4) if candidate_dev is not None else "",
                "substitution": substitution,
                "error_type": error_type,
                "confidence": confidence,
                # Store year context for report
                "_year_values": {y: v for y, v in year_to_hours.items()},
            })

    out_df = pd.DataFrame(records)
    if out_df.empty:
        print("No outliers found at current threshold.")
        return

    # Drop internal column before saving CSV
    csv_df = out_df.drop(columns=["_year_values"])
    csv_df = csv_df.sort_values(["confidence", "deviation"], ascending=[True, False])
    csv_df.to_csv("data/outliers.csv", index=False)
    print(f"Wrote {len(csv_df)} flagged values to data/outliers.csv")

    # Summary counts
    conf_counts = out_df["confidence"].value_counts()
    n_high = conf_counts.get("HIGH", 0)
    n_medium = conf_counts.get("MEDIUM", 0)
    n_low = conf_counts.get("LOW", 0)
    n_hist = conf_counts.get("HISTORICAL", 0)

    # Generate markdown report
    lines = [
        "# Transit Times Outlier Report",
        "",
        "Flags values where a year's transit time deviates ≥15 hours from the median",
        "of other years for the same route. Checks whether a 3↔8 digit substitution",
        "(common OCR confusion in 19th-century typefaces) explains the discrepancy.",
        "",
        "**Years compared:** 1882, 1883, 1892, 1902, 1908  ",
        "*(1883 data loaded from `1883-transit-times-google.csv` and merged into `transit-times-merged.csv`)*",
        "",
        "## Summary",
        "",
        f"| Category | Count | Description |",
        f"|----------|-------|-------------|",
        f"| HIGH | {n_high} | 3↔8 substitution resolves the outlier (within 5h of median) — likely errors |",
        f"| MEDIUM | {n_medium} | 3↔8 substitution partially explains the outlier (within 10h) — probably errors |",
        f"| LOW | {n_low} | Outlier unexplained by 3↔8 — may be other error types or route changes |",
        f"| HISTORICAL | {n_hist} | 1882 value higher than later years — likely genuine historical variation, not an error |",
        "",
    ]

    def format_section(conf: str, desc: str):
        subset = out_df[out_df["confidence"] == conf]
        if subset.empty:
            return
        lines.append(f"## {conf} ({len(subset)} cases)")
        lines.append(f"*{desc}*")
        lines.append("")
        for _, row in subset.sort_values("deviation", ascending=False).iterrows():
            route = f"{row['origin_city']}, {row['origin_state']} → {row['destination_city']}, {row['destination_state']}"
            year_vals = row["_year_values"]
            year_str = " | ".join(
                f"**{y}: {decimal_to_hhmm(v)}{'*' if y == row['year'] else ''}**"
                for y, v in sorted(year_vals.items())
            )
            lines.append(f"### {route} ({row['year']})")
            lines.append(f"- Values by year: {year_str}  *(asterisk = flagged)*")
            lines.append(f"- Flagged value: **{row['current_hhmm']}**, deviation {row['deviation']:.1f} h from other-years median ({row['other_years_median']:.2f} h)")
            if row["best_candidate_hhmm"]:
                lines.append(f"- Suggested correction: **{row['best_candidate_hhmm']}** via `{row['substitution']}`, within {row['candidate_deviation']:.1f} h of median")
            else:
                lines.append("- No 3↔8 substitution found — manual review needed")
            lines.append(f"- Error type: `{row['error_type']}`")
            lines.append("")

    format_section("HIGH", "Strong evidence of 3↔8 transcription error — recommend correcting these")
    format_section("MEDIUM", "Probable 3↔8 error — verify against source PDF before correcting")
    format_section("LOW", "Outlier with no clear digit-substitution explanation — could be route change, data entry error, or other cause")
    format_section("HISTORICAL", "1882 value is plausibly higher due to slower pre-transcontinental-railroad travel — likely not an error")

    with open("docs/outliers-report.md", "w") as f:
        f.write("\n".join(lines))
    print("Wrote docs/outliers-report.md")


if __name__ == "__main__":
    import os
    from pathlib import Path
    os.chdir(Path(__file__).parent)
    main()
