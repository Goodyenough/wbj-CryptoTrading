"""Synthetic checks for CRYPTOTRADIN-132 volatility-fit diagnostics."""
from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from diagnose_fixed_exit_volatility_fit import (
    apply_cuts,
    bucket,
    choose_selector,
    early_cuts,
    early_qualifies,
    select_rows,
)
from research_breakout_d6 import natr20
from short_horizon_core import H4


def trade(natr, net, *, status="TP", symbol="TEST", day=0):
    return {
        "closed": True,
        "natr20_pct": natr,
        "net_return_pct": net,
        "raw_return_pct": net + 0.3,
        "fee_pct": 0.2,
        "slippage_pct": 0.1,
        "duration_hours": 4,
        "status": status,
        "ambiguous": 0,
        "fallback": {},
        "entry_ms": day * 24 * 3_600_000,
        "signal_ms": day * 24 * 3_600_000,
        "symbol": symbol,
        "regime": "NEUTRAL",
        "signal_week": f"W{day // 7}",
        "net_pnl": net * 10,
        "tp_atr": 5 / natr,
        "sl_atr": 3 / natr,
        "path_complete_48h": False,
    }


def test_natr20_uses_only_latest_twenty_closed_bars():
    rows = []
    for index in range(25):
        close = 100 + index
        rows.append([index * H4, close, close + 2, close - 1, close, 1, 0, 1, 1, 1, 1, 0])
    rows = np.asarray(rows, dtype=float)
    before = natr20(rows, 21)
    rows[21:, 2:5] = 10_000
    assert natr20(rows, 21) == before


def test_early_cuts_are_frozen_and_reused():
    rows = [trade(value, 1) for value in range(1, 10)]
    cuts = early_cuts(rows)
    near = [trade(0.5, 1), trade(5, 1), trade(20, 1)]
    apply_cuts(near, cuts)
    assert [row["natr_bucket"] for row in near] == ["low", "mid", "high"]
    assert bucket(cuts[0], cuts) == "low"
    assert bucket(cuts[1], cuts) == "mid"


def test_selector_chooses_qualified_best_net_contiguous_group():
    rows = []
    for label, natr, values in (
        ("low", 1, [-3] * 6 + [5] * 4),
        ("mid", 2, [-3] * 3 + [5] * 7),
        ("high", 3, [-3] * 7 + [5] * 3),
    ):
        for index, value in enumerate(values):
            row = trade(natr, value, status="TP" if value > 0 else "SL", day=index)
            row["natr_bucket"] = label
            rows.append(row)
    selector, candidates = choose_selector(rows)
    assert selector == ("mid",)
    assert next(item for item in candidates if item["selector"] == "mid")["early_qualifies"]


def test_win_rate_gain_does_not_qualify_when_expectancy_worsens():
    baseline = [trade(1, value) for value in (1, 1, 1, 1, 1, -10)]
    baseline += [trade(3, value) for value in (10, 10, -1, -1)]
    for row in baseline[:6]:
        row["natr_bucket"] = "low"
    for row in baseline[6:]:
        row["natr_bucket"] = "high"
    selector, candidates = choose_selector(baseline)
    assert selector is None
    result = next(item for item in candidates if item["selector"] == "low")
    assert result["win_rate_delta_pp"] > 5
    assert result["mean_net_delta_pp"] < 0
    assert not early_qualifies(result)


def test_select_rows_never_changes_fixed_bucket_labels():
    rows = [trade(1, 1), trade(2, -1), trade(3, 1)]
    for row, label in zip(rows, ("low", "mid", "high")):
        row["natr_bucket"] = label
    assert [row["natr_bucket"] for row in select_rows(rows, ("low", "mid"))] == ["low", "mid"]
