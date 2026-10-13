"""Synthetic checks for the preregistered D6 path and density diagnostics."""
from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from research_breakout_d6 import event_density, event_overlap, full_path_quality
from short_horizon_core import COSTS, DAY, H4, HOUR, Market, path


def candle(t, o=100., h=101., low=99., c=100., step=H4):
    return [t, o, h, low, c, 1000., t + step - 1, 100000., 10000., 500., 50000., 0.]


def market(rows, hours=()):
    return Market({"TESTUSDT": {"4h": np.array(rows, dtype=float).reshape(-1, 12),
                                 "1h": np.array(hours, dtype=float).reshape(-1, 12)}})


def test_full_path_quality_keeps_following_after_stop():
    rows = [candle(i * H4) for i in range(13)]
    rows[0] = candle(0, low=96)
    rows[1] = candle(H4, h=106)
    m = market(rows)
    trade = path(m, "TESTUSDT", 0, 13 * H4, COSTS[0], "stop_first")
    quality = full_path_quality(m, trade, 13 * H4, "stop_first")
    assert trade["status"] == "SL"
    assert quality["path_complete_48h"]
    assert quality["sl_then_target_48h"]
    assert not quality["favorable_first"]
    assert quality["mfe_48h_pct"] > 5


def test_full_path_quality_uses_policy_for_unresolved_double_touch():
    hours = [candle(i * HOUR, h=106 if i == 0 else 101,
                    low=96 if i == 0 else 99, step=HOUR) for i in range(4)]
    rows = [candle(0, h=106, low=96)] + [candle(i * H4) for i in range(1, 13)]
    m = market(rows, hours)
    trade = path(m, "TESTUSDT", 0, 13 * H4, COSTS[0], "stop_first")
    stop_first = full_path_quality(m, trade, 13 * H4, "stop_first")
    target_first = full_path_quality(m, trade, 13 * H4, "target_first")
    assert stop_first["sl_then_target_48h"] and not stop_first["favorable_first"]
    assert target_first["favorable_first"] and not target_first["sl_then_target_48h"]


def test_event_density_and_overlap_are_event_key_based():
    d6 = [
        {"symbol": "A", "signal_ms": 0},
        {"symbol": "A", "signal_ms": 2 * H4},
        {"symbol": "B", "signal_ms": DAY},
    ]
    c20 = [{"symbol": "A", "signal_ms": 2 * H4}]
    density = event_density(d6, 0, 30 * DAY)
    overlap = event_overlap({"D6": d6, "C20": c20})
    assert density["events_per_30d"] == pytest.approx(3)
    assert density["median_inter_event_hours_same_symbol"] == 8
    assert overlap == {"same_symbol_time_events": 1, "pct_of_d6": pytest.approx(100 / 3),
                       "pct_of_c20": 100.0}
