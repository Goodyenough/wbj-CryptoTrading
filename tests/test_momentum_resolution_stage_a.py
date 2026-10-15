"""Synthetic checks for CRYPTOTRADIN-129 Stage A."""
from __future__ import annotations

from types import SimpleNamespace
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from diagnose_momentum_resolution_stage_a import (  # noqa: E402
    HOUR,
    decide,
    earliest_price_reclaim,
    simulate_hourly_exit,
)


def costs():
    return SimpleNamespace(entry_fee=0.0, entry_slip=0.0, tp_fee=0.0, tp_slip=0.0, exit_fee=0.0, exit_slip=0.0)


def hourly_rows(count: int = 60, price: float = 100.0) -> np.ndarray:
    return np.asarray([[i * HOUR, price, price + 1, price - 1, price, 1, i * HOUR + HOUR - 1, 1, 1] for i in range(count)], dtype=float)


def test_earliest_reclaim_uses_only_completed_hourly_bars() -> None:
    plan = {"signal_ms": 4 * HOUR, "entry_low": 99.0, "entry_high": 101.0}
    hours = np.asarray([
        [0, 100, 101, 98, 100, 1, HOUR - 1, 1, 1],
        [HOUR, 100, 103, 99, 102, 1, 2 * HOUR - 1, 1, 1],
        [2 * HOUR, 102, 103, 101, 102, 1, 3 * HOUR - 1, 1, 1],
        [3 * HOUR, 102, 104, 101, 103, 1, 4 * HOUR - 1, 1, 1],
    ], dtype=float)
    result = earliest_price_reclaim(plan, hours)
    assert result["earlier_reclaim"]
    assert result["oracle_entry_ms"] == 2 * HOUR
    assert result["lead_hours"] == 2
    assert result["oracle_raw_entry"] == 102


def test_fourth_hour_close_is_not_counted_as_earlier() -> None:
    plan = {"signal_ms": 4 * HOUR, "entry_low": 99.0, "entry_high": 101.0}
    hours = hourly_rows(4)
    hours[:3, 4] = 100
    hours[3, 4] = 102
    result = earliest_price_reclaim(plan, hours)
    assert not result["earlier_reclaim"]
    assert result["oracle_entry_ms"] == 4 * HOUR


def test_hourly_exit_handles_target_stop_and_time() -> None:
    rows = hourly_rows()
    rows[0] = [0, 100, 106, 99, 105, 1, HOUR - 1, 1, 1]
    target = simulate_hourly_exit(rows, "XUSDT", 0, 60 * HOUR, costs(), "stop_first")
    assert target["status"] == "TP"
    assert target["net_return_pct"] == 5.0

    rows = hourly_rows()
    rows[0] = [0, 100, 101, 96, 97, 1, HOUR - 1, 1, 1]
    stop = simulate_hourly_exit(rows, "XUSDT", 0, 60 * HOUR, costs(), "stop_first")
    assert stop["status"] == "SL"
    assert stop["net_return_pct"] == -3.0

    rows = hourly_rows()
    timed = simulate_hourly_exit(rows, "XUSDT", 0, 60 * HOUR, costs(), "stop_first")
    assert timed["status"] == "TIME"
    assert timed["exit_ms"] == 48 * HOUR


def summary(positive=True, ci=True, stress=True, measurement=True, flip=False):
    def branch(mean, delta, lower=0.1):
        return {"measurement": {"passed": measurement}, "comparison": {
            "oracle": {"mean_net_pct": mean},
            "mean_net_pct_delta": delta,
            "bootstrap": {"delta_mean_net_pct_ci": [lower, 0.5]},
        }}
    main = branch(0.2 if positive else -0.1, 0.2, 0.1 if ci else -0.1)
    stressed = branch(0.1 if stress else -0.2, 0.1)
    target = branch(-0.1 if flip else main["comparison"]["oracle"]["mean_net_pct"], -0.1 if flip else 0.2)
    return {"windows": {name: {"branches": {
        "taker_stop_first": main,
        "stress_stop_first": stressed,
        "taker_target_first": target,
    }} for name in ("early", "near")}}


def test_decision_requires_measurement_profit_cost_and_ci() -> None:
    assert decide(summary())[0] == "stage_b_eligible"
    assert decide(summary(positive=False))[0] == "stop_lower_timeframe_timing_route"
    assert decide(summary(ci=False))[0] == "stop_lower_timeframe_timing_route"
    assert decide(summary(stress=False))[0] == "stop_lower_timeframe_timing_route"
    assert decide(summary(measurement=False))[0] == "measurement_insufficient"
    assert decide(summary(flip=True))[0] == "measurement_insufficient"
