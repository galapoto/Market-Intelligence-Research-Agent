"""Recompute historical charger growth from curated course evidence (not raw IEA)."""
import csv
from pathlib import Path


def load_indicators(path):
    with Path(path).open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("Empty data")
    for row in rows:
        for year in ("2020", "2021", "2022", "2023"):
            row[year] = int(row[year])
    return rows


def annual_growth_pct(previous, current):
    if previous <= 0:
        raise ValueError("Previous year must be positive")
    return round(100 * (current - previous) / previous, 2)


def calculate_growth(rows):
    return [
        {
            "country": row["country"],
            "charger_type": row["charger_type"],
            "2022": row["2022"],
            "2023": row["2023"],
            "growth_pct": annual_growth_pct(row["2022"], row["2023"]),
        }
        for row in rows
    ]


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    args = parser.parse_args()
    print(json.dumps(calculate_growth(load_indicators(args.csv_path)), indent=2))
