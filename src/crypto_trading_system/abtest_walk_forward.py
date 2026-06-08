from __future__ import annotations

from datetime import date


def parse_period_specs(raw_periods: str) -> list[tuple[str, str]]:
    periods: list[tuple[str, str]] = []
    for raw_period in raw_periods.split(","):
        item = raw_period.strip()
        if not item:
            continue
        if ":" in item:
            start, end = item.split(":", 1)
        elif "->" in item:
            start, end = item.split("->", 1)
        else:
            raise ValueError(f"Invalid period '{item}'. Use START:END, for example 2025-01-01:2025-06-01.")
        start = start.strip()
        end = end.strip()
        try:
            start_date = date.fromisoformat(start)
            end_date = date.fromisoformat(end)
        except ValueError as exc:
            raise ValueError(f"Invalid period date in '{item}'. Dates must use YYYY-MM-DD.") from exc
        if end_date <= start_date:
            raise ValueError(f"Invalid period '{item}'. End date must be after start date.")
        periods.append((start, end))
    if not periods:
        raise ValueError("--periods must include at least one START:END pair.")
    return periods
