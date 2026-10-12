"""Synthetic causal/ledger checks for the isolated research contract."""
from pathlib import Path
import sys

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from short_horizon_core import (COSTS, DAY, H4, HOLD, HOUR, Market, bootstrap,
                                new_breakout, path, plan_decision, replay, size_for_account)
from research_short_horizon_entries import Series


def candle(t, o=100., h=101., low=99., c=100., step=H4):
    return [t, o, h, low, c, 1000., t + step - 1, 100000., 10000., 500., 50000., 0.]


def market(rows, hours=(), symbol="TESTUSDT"):
    return Market({symbol: {"4h": np.array(rows, dtype=float).reshape(-1, 12),
                           "1h": np.array(hours, dtype=float).reshape(-1, 12)}})


def feature(candidate=None, qv=50e6):
    return dict(qv=qv, regime="NEUTRAL", crash=False, candidate=candidate, breakout=True)


def test_breakout_excludes_current_high_and_requires_new_event():
    rows = [candle(i * H4, h=100, low=98, c=99) for i in range(22)]
    rows[-1] = candle(21 * H4, h=110, c=101)
    assert new_breakout(rows)
    rows[-2] = candle(20 * H4, h=102, c=101)
    rows[-1] = candle(21 * H4, h=110, c=103)
    assert not new_breakout(rows)


def test_breakout_equality_is_not_breakout_and_previous_uses_own_channel():
    rows = [candle(i * H4, h=101, c=100) for i in range(22)]
    rows[-1][4] = 101
    assert not new_breakout(rows)
    rows[0][2] = 105
    rows[-2] = candle(20 * H4, h=103, c=102)
    rows[-1] = candle(21 * H4, h=107, c=104)
    assert new_breakout(rows)  # previous close did not exceed its own 105 channel


def test_watching_activation_touch_reclaim_invalidation_and_expiry():
    plan = dict(created_ms=H4, entry_low=99, entry_high=101, original_stop=95)
    assert plan_decision(plan, candle(0, h=103, low=98, c=102), H4, True) == "waiting"
    assert plan_decision(plan, candle(H4, h=103, low=98, c=102), 2 * H4, True) == "signal"
    assert plan_decision(plan, candle(H4, h=103, low=98, c=100), 2 * H4, True) == "waiting"
    assert plan_decision(plan, candle(H4, h=103, low=98, c=102), 2 * H4, False) == "waiting"
    assert plan_decision(plan, candle(H4, o=94, h=98, low=93, c=94), 2 * H4, False) == "invalidated"
    assert plan_decision(plan, None, 20 * H4, True) == "expired"


def test_next_open_not_signal_bar_and_targets_use_filled_price():
    m = market([candle(0, h=200, low=1), candle(H4, o=110, h=117, low=109, c=115)])
    r = path(m, "TESTUSDT", H4, 2 * H4, COSTS[0], "stop_first")
    assert r["entry_price"] == pytest.approx(110 * 1.0005)
    assert r["target"] == pytest.approx(110 * 1.0005 * 1.05)
    assert r["status"] == "TP"
    assert r["exit_ms"] == 2 * H4


def test_same_entry_bar_can_stop_and_missing_next_open_cancels():
    m = market([candle(H4, low=96)])
    assert path(m, "TESTUSDT", H4, 2 * H4, COSTS[0], "stop_first")["status"] == "SL"
    assert path(m, "TESTUSDT", 2 * H4, 3 * H4, COSTS[0], "stop_first")["status"] == "NO_ENTRY"


def test_stop_gap_fills_at_worse_open_and_costs_reconcile():
    m = market([candle(0), candle(H4, o=90, h=92, low=89, c=91)])
    r = path(m, "TESTUSDT", 0, 2 * H4, COSTS[0], "stop_first")
    assert r["status"] == "SL"
    assert r["raw_exit"] == 90
    assert r["exit_price"] == pytest.approx(90 * .999)
    assert r["exit_ms"] == H4 and r["exit_time_exact"]
    assert r["raw_return_pct"] - r["fee_pct"] - r["slippage_pct"] == pytest.approx(r["net_return_pct"])


def test_fine_bars_resolve_parent_double_touch():
    hours = [candle(i * HOUR, h=106 if i == 0 else 101, low=95 if i == 1 else 99, step=HOUR) for i in range(4)]
    m = market([candle(0, h=106, low=95)], hours)
    for policy in ("stop_first", "target_first"):
        r = path(m, "TESTUSDT", 0, H4, COSTS[0], policy)
        assert r["status"] == "TP" and r["ambiguous"] == 0
        assert r["exit_ms"] == HOUR


def test_unresolved_fine_double_touch_keeps_two_bounds():
    hours = [candle(i * HOUR, h=106 if i == 0 else 101, low=95 if i == 0 else 99, step=HOUR) for i in range(4)]
    m = market([candle(0, h=106, low=95)], hours)
    low = path(m, "TESTUSDT", 0, H4, COSTS[0], "stop_first")
    high = path(m, "TESTUSDT", 0, H4, COSTS[0], "target_first")
    assert low["status"] == "SL" and high["status"] == "TP"
    assert low["ambiguous"] == high["ambiguous"] == 1


def test_fine_mismatch_falls_back_instead_of_inventing_order():
    m = market([candle(0, h=106, low=95)], [candle(i * HOUR, step=HOUR) for i in range(4)])
    r = path(m, "TESTUSDT", 0, H4, COSTS[0], "stop_first")
    assert r["status"] == "SL" and r["fallback"] == {"4h_mismatch": 1}


def test_time_exit_at_48h_does_not_use_later_high_low():
    m = market([candle(i * H4) for i in range(12)] + [candle(HOLD, h=200, low=1)])
    r = path(m, "TESTUSDT", 0, HOLD, COSTS[0], "stop_first")
    assert r["status"] == "TIME" and r["raw_exit"] == 100
    assert r["duration_hours"] == 48


def test_protective_gap_precedes_time_exit_at_deadline():
    m = market([candle(i * H4) for i in range(12)] + [candle(HOLD, o=90, h=92, low=89, c=91)])
    r = path(m, "TESTUSDT", 0, HOLD, COSTS[0], "stop_first")
    assert r["status"] == "SL" and r["raw_exit"] == 90


def test_missing_path_and_end_censor_are_explicit():
    gap = path(market([candle(0)]), "TESTUSDT", 0, 3 * H4, COSTS[0], "stop_first")
    end = path(market([candle(0)]), "TESTUSDT", 0, H4, COSTS[0], "stop_first")
    assert gap["status"] == "GAP_CENSORED" and gap["gap_at"] == H4
    assert end["status"] == "END_CENSORED"
    assert not gap["closed"] and not end["closed"]


def test_sizing_includes_fees_cash_and_expected_stop_slippage():
    qty, unit_risk = size_for_account(10000, 10000, 0, 100, COSTS[0])
    assert qty * unit_risk == pytest.approx(100)
    qty, unit_risk = size_for_account(10000, 12, 499, 100, COSTS[0])
    assert qty * 100 * 1.001 <= 12 + 1e-9
    assert qty * unit_risk <= 1 + 1e-9


def test_portfolio_routing_does_not_use_future_cash_and_blocks_cash_capacity():
    arrays = {f"S{i}USDT": {"4h": np.array([candle(t * H4) for t in range(1, 5)]),
                           "1h": np.empty((0, 12))} for i in range(8)}
    frames = {H4: {s: feature(qv=(20 - i) * 1e6) for i, s in enumerate(arrays)}}
    r = replay(Market(arrays), frames, 0, 5 * H4, "C", "portfolio", COSTS[0], "stop_first")
    assert r["counts"]["new_candidate_budget"] == 3
    assert r["counts"]["cash_or_risk"] >= 1
    assert sum(t["cash_invested"] for t in r["trades"]) <= 10000 + 1e-8
    assert r["max_cash_reconciliation_error"] < 1e-7
    assert r["curve"][-1]["equity"] == pytest.approx(10000 + sum(t["net_pnl"] for t in r["trades"]))


def test_same_symbol_lock_does_not_suppress_all_event_diagnostics():
    m = market([candle(t * H4) for t in range(1, 5)])
    frames = {t * H4: {"TESTUSDT": feature()} for t in (1, 2, 3)}
    all_r = replay(m, frames, 0, 5 * H4, "C", "all_events", COSTS[0], "stop_first")
    sym_r = replay(m, frames, 0, 5 * H4, "C", "symbol_only", COSTS[0], "stop_first")
    assert len(all_r["trades"]) == 3 and len(sym_r["trades"]) == 1
    assert sym_r["counts"]["same_symbol"] == 2


@pytest.mark.parametrize("price", [1e-8, 1e-6, 1e-4, 1., 10000.])
def test_cash_tolerance_is_denomination_invariant(price):
    arrays = {}
    for i in range(8):
        rows = np.array([candle(t * H4) for t in range(1, 5)])
        rows[:, 1:5] *= price / 100
        arrays[f"S{i}USDT"] = {"4h": rows, "1h": np.empty((0, 12))}
    frames = {H4: {s: feature(qv=(20 - i) * 1e6) for i, s in enumerate(arrays)}}
    r = replay(Market(arrays), frames, 0, 5 * H4, "C", "portfolio", COSTS[0], "stop_first")
    assert all(t["cash_invested"] > 1e-8 for t in r["trades"])
    assert len(r["trades"]) == 4


def test_quality_is_closed_prefix_only_and_detects_gap():
    rows = np.array([candle(t * H4) for t in range(150)])
    before = Series(rows.copy(), H4)
    rows[120:, 4] = 10_000  # future corruption cannot change earlier eligibility/EMA
    after = Series(rows, H4)
    assert before.quality(120, 120, 120 * H4) is None
    assert after.quality(120, 120, 120 * H4) is None
    assert before.ema[20][119] == after.ema[20][119]
    gaps = Series(np.delete(rows[:120], 50, axis=0), H4)
    assert gaps.quality(119, 100, 120 * H4) == "history_gap"


def test_paired_block_bootstrap_preserves_same_day_difference():
    b = [dict(closed=True, entry_ms=i * DAY, net_return_pct=1.) for i in range(42)]
    c = [dict(closed=True, entry_ms=i * DAY, net_return_pct=2.) for i in range(42)]
    r = bootstrap(b, c, 0, 42 * DAY, repetitions=50)
    assert r["delta_ci"] == [1., 1.]
