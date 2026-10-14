"""Synthetic checks for CRYPTOTRADIN-133 ATR-adaptive exits."""
from __future__ import annotations

from types import SimpleNamespace
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from research_atr_adaptive_short_exit import (  # noqa: E402
    H4,
    causal_atr20,
    compare,
    decide,
    exit_levels,
    risk_metrics,
    simulate_exit,
)
from short_horizon_core import Market  # noqa: E402


def bars(count: int = 30, *, start: int = 0, close: float = 100.0) -> np.ndarray:
    rows = []
    for index in range(count):
        opened = start + index * H4
        rows.append([opened, close, close + 1, close - 1, close, 1, 1, 1, 1])
    return np.asarray(rows, dtype=float)


def costs():
    return SimpleNamespace(
        name="zero",
        entry_fee=0.0,
        entry_slip=0.0,
        tp_fee=0.0,
        tp_slip=0.0,
        exit_fee=0.0,
        exit_slip=0.0,
    )


def trade(net_r: float, net_pct: float, status: str = "TP") -> dict:
    return {
        "symbol": "XUSDT",
        "signal_ms": H4,
        "entry_ms": 2 * H4,
        "exit_ms": 3 * H4,
        "status": status,
        "closed": True,
        "net_return_pct": net_pct,
        "raw_return_pct": net_pct,
        "fee_pct": 0.0,
        "slippage_pct": 0.0,
        "duration_hours": 4.0,
        "ambiguous": 0,
        "fallback": {},
        "net_r": net_r,
        "cost_r": 0.0,
        "planned_risk_pct": 3.0,
        "stop_distance_pct": 3.0,
        "target_distance_pct": 5.0,
    }


def test_causal_atr_ignores_future_bars() -> None:
    rows = bars()
    signal = 25 * H4
    before = causal_atr20(rows, signal)
    rows[25:, 2] = 999
    rows[25:, 3] = 1
    after = causal_atr20(rows, signal)
    assert before == after == (2.0, 100.0)


def test_atr_exit_levels_scale_with_volatility_and_keep_ratio() -> None:
    stop, target = exit_levels(100.0, 4.0, "atr")
    assert stop == 96.0
    assert np.isclose(target, 106.66666666666667)
    assert np.isclose((target - 100) / (100 - stop), 5 / 3)


def test_planned_stop_is_minus_one_r_without_costs() -> None:
    rows = bars(40)
    entered = 25 * H4
    rows[25] = [entered, 100, 101, 95, 96, 1, 1, 1, 1]
    market = Market({"XUSDT": {"4h": rows, "1h": np.empty((0, 9))}})
    result = simulate_exit(market, "XUSDT", entered, 40 * H4, costs(), "stop_first", 4.0, "atr")
    assert result["status"] == "SL"
    assert np.isclose(result["net_r"], -1.0)


def test_fixed_simple_target_path() -> None:
    rows = bars(40)
    entered = 25 * H4
    rows[25] = [entered, 100, 106, 99, 105, 1, 1, 1, 1]
    market = Market({"XUSDT": {"4h": rows, "1h": np.empty((0, 9))}})
    result = simulate_exit(market, "XUSDT", entered, 40 * H4, costs(), "stop_first", 4.0, "fixed")
    assert result["status"] == "TP"
    assert result["raw_exit"] == 105.0
    assert np.isclose(result["net_return_pct"], 5.0)


def test_risk_metrics_and_compare_use_equal_risk_units() -> None:
    fixed = [trade(1.0, 5.0), trade(-1.0, -3.0, "SL")]
    adaptive = [trade(1.5, 7.5), trade(-1.0, -5.0, "SL")]
    fixed[1]["symbol"] = "YUSDT"
    adaptive[1]["symbol"] = "YUSDT"
    metrics = risk_metrics(adaptive)
    assert np.isclose(metrics["mean_net_r"], 0.25)
    result = compare(fixed, adaptive)
    assert np.isclose(result["mean_net_r_delta"], 0.25)
    assert result["mean_net_pct_delta_pp"] == 0.25


def test_decision_rejects_failed_near_window() -> None:
    def item(delta, atr_mean, atr_pf, pf_delta, p05_delta=0.0, mdd_delta=0.0):
        return {
            "mean_net_r_delta": delta,
            "r_pf_delta": pf_delta,
            "p05_r_delta": p05_delta,
            "risk_mdd_delta_pp": mdd_delta,
            "atr": {"mean_net_r": atr_mean, "r_profit_factor": atr_pf},
        }

    robustness = {
        "bootstrap": {"delta_mean_net_r_ci": [-0.2, 0.1]},
        "leave_one_symbol": {"min_delta": -0.1},
        "leave_one_week": {"min_delta": -0.1},
    }
    summary = {
        "windows": {
            "early": {
                "primary": item(0.1, 0.05, 1.1, 0.1),
                "robustness": robustness,
                "branches": {
                    "stress_stop_first": item(0.0, 0.0, 1.0, 0.0),
                    "taker_target_first": item(0.0, 0.0, 1.0, 0.0),
                },
            },
            "near": {
                "primary": item(-0.1, -0.05, 0.9, -0.1),
                "robustness": robustness,
                "branches": {
                    "stress_stop_first": item(-0.1, -0.1, 0.8, -0.1),
                    "taker_target_first": item(-0.1, -0.1, 0.8, -0.1),
                },
            },
        }
    }
    decision, _ = decide(summary)
    assert decision == "reject_preregistered_atr_exit"
