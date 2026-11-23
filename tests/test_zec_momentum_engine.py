"""Only synthetic candles: no network, database, or research result inputs."""
from __future__ import annotations

import pytest

from research.zec_momentum.engine import FIVE, FIFTEEN, HOUR, run_replay, signals


def bar(opened, opening=100.0, high=100.2, low=99.8, close=100.0):
    return [opened, opening, high, low, close, 10.0, opened + FIVE - 1, 1000.0, 20, 5.0, 500.0, 0]


def candles(hours=6):
    return [bar(index * FIVE) for index in range(hours * 12)]


def event(decision=FIFTEEN, side="long", stop=None):
    return dict(decision_ms=decision, side=side,
                stop_price=(98.0 if side == "long" else 102.0) if stop is None else stop)


def replay(rows=None, events=None, funding=(), **kwargs):
    options = dict(start_ms=0, end_ms=6 * HOUR, target_pct=0.01, hold_hours=2,
                   fee_bps=5, slippage_bps=3)
    options.update(kwargs)
    return run_replay(candles() if rows is None else rows, funding,
                      precomputed_signals=[event()] if events is None else events, **options)


@pytest.mark.parametrize("side", ["long", "short"])
@pytest.mark.parametrize("target", [0.01, 0.02])
@pytest.mark.parametrize("fee,slip", [(5, 3), (10, 10)])
def test_two_sided_net_target_after_all_execution_costs(side, target, fee, slip):
    rows = candles()
    fill_time = FIFTEEN + FIVE
    rows[fill_time // FIVE] = bar(fill_time, high=110 if side == "long" else 100.2,
                                low=90 if side == "short" else 99.8)
    result = replay(rows, [event(side=side)], target_pct=target, fee_bps=fee, slippage_bps=slip)
    trade = result["trades"][0]
    assert trade["exit_reason"] == "TP"
    assert trade["net_pnl_usdt"] == pytest.approx(110 * target)
    assert result["final_equity"] == pytest.approx(110 * (1 + target))
    assert trade["quantity"] * trade["entry_price"] <= 110 + 1e-9
    assert trade["initial_risk_usdt"] <= 5 + 1e-9
    assert trade["fees_usdt"] > 0
    assert trade["entry_ms"] == fill_time
    assert trade["exit_ms"] == fill_time + FIVE - 1
    assert trade["exit_time_exact"] is False


def test_strict_next_open_delay_does_not_trade_signal_or_decision_bar():
    rows = candles()
    rows[2] = bar(2 * FIVE, high=150, low=50)
    rows[3] = bar(3 * FIVE, high=150, low=50)
    rows[4] = bar(4 * FIVE, opening=101, high=101.2, low=100.8, close=101)
    result = replay(rows)
    trade = result["trades"][0]
    assert trade["entry_ms"] == FIFTEEN + FIVE
    assert trade["raw_entry"] == 101
    assert trade["exit_reason"] == "TIME"


@pytest.mark.parametrize("side", ["long", "short"])
def test_entry_bar_stop_and_stop_first_for_double_touch(side):
    rows = candles()
    fill_time = FIFTEEN + FIVE
    rows[4] = bar(fill_time, high=110, low=90)
    trade = replay(rows, [event(side=side)])["trades"][0]
    assert trade["exit_reason"] == "SL"
    assert trade["ambiguous"]
    assert trade["net_pnl_usdt"] < 0
    assert trade["exit_ms"] == fill_time + FIVE - 1


@pytest.mark.parametrize("side,opening", [("long", 95), ("short", 105)])
def test_stop_gap_uses_worse_open_and_adverse_exit_slippage(side, opening):
    rows = candles()
    rows[5] = bar(5 * FIVE, opening=opening, high=opening + 0.2,
                  low=opening - 0.2, close=opening)
    trade = replay(rows, [event(side=side)])["trades"][0]
    sign = 1 if side == "long" else -1
    assert trade["exit_reason"] == "SL_GAP"
    assert trade["exit_ms"] == 5 * FIVE
    assert trade["raw_exit"] == opening
    assert trade["exit_price"] == pytest.approx(opening * (1 - sign * 0.0003))
    assert trade["exit_time_exact"]


def test_structure_risk_shrinks_quantity_without_moving_stop():
    trade = replay(events=[event(stop=90)])["trades"][0]
    assert trade["stop_price"] == 90
    assert trade["initial_risk_usdt"] == pytest.approx(5)
    assert trade["notional_usdt"] < trade["entry_equity"]
    assert trade["reference_margin_usdt"] == pytest.approx(trade["notional_usdt"] / 2)


@pytest.mark.parametrize("side", ["long", "short"])
def test_funding_sign_entry_boundary_and_net_target_recalculation(side):
    rows = candles()
    rows[6] = bar(6 * FIVE, high=110 if side == "long" else 100.2,
                  low=90 if side == "short" else 99.8)
    funding = [dict(time_ms=4 * FIVE, rate=0.5, mark_price=100),
               dict(time_ms=5 * FIVE, rate=0.001, mark_price=101)]
    trade = replay(rows, [event(side=side)], funding)["trades"][0]
    assert len(trade["funding_events"]) == 1  # Entry-time funding is excluded.
    assert trade["funding_cost_usdt"] > 0 if side == "long" else trade["funding_cost_usdt"] < 0
    assert trade["funding_cost_usdt"] == pytest.approx((1 if side == "long" else -1) * trade["quantity"] * 101 * 0.001)
    assert trade["net_pnl_usdt"] == pytest.approx(1.1)
    assert trade["exit_reason"] == "TP"


def test_funding_at_exact_time_exit_is_charged_first_and_future_funding_ignored():
    deadline = 4 * FIVE + 2 * HOUR
    funding = [dict(time_ms=deadline, rate=0.001, mark_price=102),
               dict(time_ms=deadline + FIVE, rate=0.5, mark_price=100)]
    trade = replay(funding=funding)["trades"][0]
    assert trade["exit_reason"] == "TIME"
    assert trade["exit_ms"] == deadline
    assert len(trade["funding_events"]) == 1
    assert trade["funding_cost_usdt"] == pytest.approx(trade["quantity"] * 102 * 0.001)
    assert trade["net_pnl_usdt"] == pytest.approx(trade["gross_pnl_usdt"] - trade["fees_usdt"] - trade["funding_cost_usdt"])


def test_one_position_and_only_a_later_signal_can_reenter():
    events = [event(), event(30 * 60_000, "short"), event(135 * 60_000), event(150 * 60_000, "short")]
    result = replay(events=events)
    assert [trade["side"] for trade in result["trades"]] == ["long", "short"]
    assert result["skip_counts"]["position_or_pending"] == 2
    assert result["trades"][0]["exit_ms"] < result["trades"][1]["decision_ms"]


def test_exit_at_signal_timestamp_waits_for_next_signal():
    # A custom 10m decision gives a 15m fill and a 135m time exit.
    events = [event(2 * FIVE), event(135 * 60_000), event(150 * 60_000)]
    result = replay(events=events)
    assert len(result["trades"]) == 2
    assert result["skip_counts"]["wait_next_signal_after_exit"] == 1


def test_segment_end_gate_does_not_read_next_segment_open():
    result = replay(events=[event(4 * HOUR)])
    assert not result["trades"]
    assert result["skip_counts"]["insufficient_full_horizon"] == 1


def test_cutoff_bar_funding_signal_and_segment_are_rejected():
    cutoff = 6 * HOUR
    with pytest.raises(ValueError, match="Sealed cutoff"):
        replay(candles() + [bar(cutoff)], cutoff_ms=cutoff)
    with pytest.raises(ValueError, match="Sealed cutoff"):
        replay(funding=[dict(time_ms=cutoff, rate=0.001, mark_price=100)], cutoff_ms=cutoff)
    with pytest.raises(ValueError, match="Sealed cutoff"):
        replay(events=[event(cutoff)], cutoff_ms=cutoff)
    with pytest.raises(ValueError, match="segment"):
        replay(end_ms=cutoff + FIVE, cutoff_ms=cutoff)


def test_missing_execution_bar_and_non_grid_funding_are_rejected():
    rows = candles()
    del rows[7]
    with pytest.raises(ValueError, match="missing"):
        replay(rows)
    with pytest.raises(ValueError, match="align"):
        replay(funding=[dict(time_ms=5 * FIVE + 1, rate=0.001, mark_price=100)])


def trending(hours=26, side="long"):
    sign = 1 if side == "long" else -1
    rows = []
    for index in range(hours * 12):
        opening = 100 + sign * index * 0.005
        closing = opening + sign * 0.005
        rows.append(bar(index * FIVE, opening, max(opening, closing) + 0.001,
                        min(opening, closing) - 0.001, closing))
    return rows


@pytest.mark.parametrize("side", ["long", "short"])
def test_actual_signal_direction_structure_and_no_unclosed_hour_leak(side):
    rows = trending(side=side)
    decision = 23 * HOUR + FIFTEEN
    prefix = [row for row in rows if row[0] < decision]
    before = signals(prefix)
    after = signals(rows)
    assert before
    assert before == [row for row in after if row["decision_ms"] <= decision]
    assert all(row["side"] == side for row in before)
    assert before[-1]["decision_ms"] == decision
    # Change future candles within the same still-uncompleted hour dramatically.
    changed = [row[:] for row in rows]
    for index in range(decision // FIVE, 24 * 12):
        changed[index] = bar(index * FIVE, 50, 200, 1, 50)
    assert before == [row for row in signals(changed) if row["decision_ms"] <= decision]
    signal = before[-1]
    structure = [row for row in prefix if decision - 4 * FIFTEEN <= row[0] < decision]
    expected = min(row[3] for row in structure) - 0.1 * signal["atr"] if side == "long" else max(row[2] for row in structure) + 0.1 * signal["atr"]
    assert signal["stop_price"] == pytest.approx(expected)


def test_precomputed_and_regenerated_signals_produce_identical_replay():
    rows = trending(hours=30)
    options = dict(start_ms=23 * HOUR, end_ms=30 * HOUR, target_pct=0.01,
                   hold_hours=2, fee_bps=5, slippage_bps=3)
    assert run_replay(rows, [], **options) == run_replay(rows, [], precomputed_signals=signals(rows), **options)
def test_sealed_cutoff_cannot_be_moved_later():
    import pytest
    from research.zec_momentum.engine import DEFAULT_CUTOFF_MS, signals
    with pytest.raises(ValueError, match="cannot be moved later"):
        signals([], cutoff_ms=DEFAULT_CUTOFF_MS + 300000)

