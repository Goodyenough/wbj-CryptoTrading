from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from diagnose_breakout_lateness import event_features
from short_horizon_core import H4


def candle(t, o=100., h=101., low=99., c=100.):
    return [t, o, h, low, c, 1000., t + H4 - 1, 100000., 10000., 500., 50000., 0.]


def fixture(post_high=104., status="SL"):
    rows = [candle(i * H4) for i in range(34)]
    for i in range(20):
        rows[i] = candle(i * H4, low=94 if i == 5 else 99, h=101, c=100)
    rows[20] = candle(20 * H4, o=100, h=107, low=99, c=102)
    rows[21] = candle(21 * H4, o=102, h=post_high, low=98, c=100)
    for i in range(22, 33):
        rows[i] = candle(i * H4, h=post_high)
    trade = {"symbol": "TESTUSDT", "entry_ms": 21 * H4, "status": status,
             "regime": "NEUTRAL", "raw_entry": 102., "entry_price": 102.051,
             "target": 107.15355}
    return np.array(rows, dtype=float), trade


def test_feature_uses_prior_twenty_low_and_closed_breakout_bar():
    rows, trade = fixture()
    r = event_features(rows, trade)
    assert r["breakout_close"] == 102
    assert r["pre_advance_20bar_pct"] == pytest.approx(100 * (102 / 94 - 1))
    assert r["pre_move_5"]


def test_actual_slipped_entry_target_defines_future_space():
    rows, trade = fixture(post_high=107.15)
    assert not event_features(rows, trade)["post_target_available"]
    # Only future bars gain the high; the frozen breakout channel is unchanged.
    rows[21:, 2] = np.maximum(rows[21:, 2], 107.16)
    assert event_features(rows, trade)["post_target_available"]


def test_late_exhausted_and_stopped_then_target_are_mutually_explanatory():
    rows, trade = fixture(post_high=104.)
    r = event_features(rows, trade)
    assert r["late_exhausted"] and not r["stopped_then_target_available"]
    rows[25, 2] = 108
    r = event_features(rows, trade)
    assert not r["late_exhausted"] and r["stopped_then_target_available"]


def test_pre_features_ignore_all_future_mutations():
    rows, trade = fixture()
    before = event_features(rows, trade)
    rows[21:, 1:5] *= 3
    after = event_features(rows, trade)
    for key in ("pre_advance_20bar_pct", "pre_return_12h_pct", "pre_return_24h_pct", "pre_return_48h_pct"):
        assert before[key] == after[key]


def test_deadline_open_is_included_but_deadline_high_is_not():
    rows, trade = fixture(post_high=104.)
    rows[33, 1] = 108
    rows[33, 2] = 200
    r = event_features(rows, trade)
    assert r["post_target_available"]
    assert r["post_mfe_48h_pct"] == pytest.approx(100 * (108 / trade["entry_price"] - 1))


def test_missing_entry_bar_fails_closed():
    rows, trade = fixture()
    rows = np.delete(rows, 21, axis=0)
    with pytest.raises(ValueError, match="missing entry bar"):
        event_features(rows, trade)
