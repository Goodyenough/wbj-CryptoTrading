"""Synthetic checks for the preregistered baseline post-exit diagnostic."""
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from diagnose_baseline_post_exit_recovery import (
    BAR_MS,
    choose_cutoff,
    contiguous_prefix,
    horizon_metrics,
    wilson_interval,
)


def bar(index: int, *, high: float = 100.0, low: float = 99.0):
    timestamp = index * BAR_MS
    return (timestamp, 100.0, high, low, 100.0)


def test_contiguous_prefix_starts_strictly_after_exit_and_stops_at_gap():
    exit_ms = 5 * BAR_MS
    rows = [bar(6), bar(7), bar(9)]
    assert [row[0] for row in contiguous_prefix(rows, exit_ms)] == [6 * BAR_MS, 7 * BAR_MS]


def test_horizon_recovery_excludes_censored_trade_from_primary_boolean():
    rows = [bar(index, high=111.0 if index == 4 else 100.0) for index in range(1, 11)]
    metric = horizon_metrics(rows, entry=100.0, stop=90.0, horizon=20)
    assert not metric["eligible"]
    assert metric["observed_recover_1r"]
    assert metric["recover_1r"] is None
    assert metric["time_to_recover_1r_bars"] == 4


def test_horizon_recovery_uses_original_entry_risk():
    rows = [bar(index, high=109.9) for index in range(1, 21)]
    rows[9] = bar(10, high=110.0)
    metric = horizon_metrics(rows, entry=100.0, stop=90.0, horizon=20)
    assert metric["eligible"]
    assert metric["recover_1r"]
    assert metric["time_to_recover_1r_bars"] == 10
    assert metric["max_favorable_r"] == pytest.approx(1.0)


def test_cutoff_uses_next_entry_before_window_and_horizon():
    exit_ms = 100 * BAR_MS
    cutoff, reason = choose_cutoff(
        exit_ms,
        window_end_ms=exit_ms + 100 * BAR_MS,
        next_entry_ms=exit_ms + 15 * BAR_MS,
    )
    assert cutoff == exit_ms + 15 * BAR_MS
    assert reason == "next_same_symbol_entry"


def test_wilson_interval_contains_observed_rate():
    low, high = wilson_interval(4, 10)
    assert low < 40 < high
    assert wilson_interval(0, 0) == (None, None)
