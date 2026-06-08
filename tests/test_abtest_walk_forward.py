from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.abtest_walk_forward import parse_period_specs


def test_parse_period_specs_accepts_colon_and_arrow() -> None:
    periods = parse_period_specs("2025-01-01:2025-06-01, 2025-06-01 -> 2026-01-01")
    assert periods == [
        ("2025-01-01", "2025-06-01"),
        ("2025-06-01", "2026-01-01"),
    ]


def test_parse_period_specs_rejects_empty_input() -> None:
    try:
        parse_period_specs(" , ")
    except ValueError as exc:
        assert "at least one" in str(exc)
    else:
        raise AssertionError("Expected empty periods to raise ValueError")


def test_parse_period_specs_rejects_non_increasing_period() -> None:
    try:
        parse_period_specs("2025-06-01:2025-06-01")
    except ValueError as exc:
        assert "End date must be after start date" in str(exc)
    else:
        raise AssertionError("Expected non-increasing period to raise ValueError")


if __name__ == "__main__":
    test_parse_period_specs_accepts_colon_and_arrow()
    test_parse_period_specs_rejects_empty_input()
    test_parse_period_specs_rejects_non_increasing_period()
    print("test_abtest_walk_forward=passed")
