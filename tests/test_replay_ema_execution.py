"""Causal OHLC replay execution and cash-ledger regression cases (no network)."""
from copy import deepcopy
from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from crypto_trading_system.backtest import replay
from crypto_trading_system.backtest.costs import entry_fill, stop_exit_fill, target_exit_fill
from crypto_trading_system.backtest.history import KlineFetchResult, interval_ms
from crypto_trading_system.config import load_settings
from test_replay import _make_sim_trade, make_kline, ms, ROOT


@pytest.fixture
def settings():
    value = load_settings(ROOT / "config/settings.toml")
    value.analysis.tp1_ema_trailing_stop_enabled = True
    value.analysis.tp1_move_stop_to_breakeven_enabled = False
    return value


def bar(o, h, l, c):
    return [0, o, h, l, c, 1, interval_ms("4h") - 1]


def trailing():
    item = _make_sim_trade(entry_price=100, stop_loss=101)
    item.paper.status = "TP1_HIT"
    item.paper.tp1_trailing_ema_stop_active = True
    return item


def step(item, candle, settings, ema, entry=None):
    return replay._step_replay_bar(item, candle, settings,
                                  bar_time="2026-01-01T08:00:00+00:00",
                                  intrabar="stop_first", closing_ema=ema, entry=entry)


def test_new_ema_cannot_stop_earlier_low_and_next_bar_uses_new_fill(settings):
    item = trailing()
    # Prior bug: raised trigger 112 but booked old-stop fill 100.899 here.
    assert step(item, bar(114, 115, 110, 114), settings, 112) == 0
    assert item.paper.status == "TP1_HIT"
    assert item.paper.stop_loss == 112
    assert [e["event_type"] for e in item.record.events] == ["TP1_EMA_TRAILING_RAISED"]
    cash_delta = step(item, bar(114, 115, 110, 111), settings, 120)
    fill = stop_exit_fill(112, item.paper.quantity, settings.backtest)
    assert item.paper.status == "STOPPED"
    assert item.paper.stop_loss == 112  # no closing update after exit
    assert item.paper.exit_price == fill.filled_price
    assert item.record.exit_price_raw == 112
    assert item.record.exit_fee == fill.fee
    assert item.record.slippage_cost == fill.slippage_cost
    assert cash_delta == pytest.approx(item.paper.quantity * fill.filled_price - fill.fee)
    assert item.paper.realized_pnl == pytest.approx((fill.filled_price - 100) * item.paper.quantity - fill.fee - item.record.entry_fee)
    assert "EMA20" in item.record.events[-1]["message"]
    assert step(item, bar(114, 115, 110, 111), settings, 120) == 0  # terminal ledger is idempotent


@pytest.mark.parametrize("closing_ema", [80, 100, 112, 130])
def test_exit_on_existing_stop_is_independent_of_current_close_ema(settings, closing_ema):
    item = trailing()
    step(item, bar(114, 115, 100, 114), settings, closing_ema)
    assert item.paper.exit_price == pytest.approx(101 * .999)
    assert item.paper.stop_loss == 101
    assert [e["event_type"] for e in item.record.events] == ["STOPPED"]


@pytest.mark.parametrize("opening,raw_exit", [(108, 108), (112, 112), (114, 112)])
def test_active_stop_gaps_use_open_and_consistent_costs(settings, opening, raw_exit):
    item = trailing()
    item.paper.stop_loss = 112
    delta = step(item, bar(opening, 116, 105, 115), settings, 120)
    fill = stop_exit_fill(raw_exit, item.paper.quantity, settings.backtest)
    assert item.record.exit_price_raw == raw_exit
    assert item.paper.exit_price == fill.filled_price
    assert delta == pytest.approx(fill.filled_price * item.paper.quantity - fill.fee)


def test_tp1_activation_is_after_range_evaluation_and_stop_never_decreases(settings):
    item = _make_sim_trade(entry_price=100)
    step(item, bar(115, 125, 105, 122), settings, 112)
    assert item.paper.status == "TP1_HIT"
    assert item.paper.stop_loss == 112
    assert [e["event_type"] for e in item.record.events] == ["TP1_HIT", "TP1_EMA_TRAILING_ACTIVATED"]
    step(item, bar(120, 124, 114, 121), settings, 95)
    assert item.paper.stop_loss == 112
    assert item.paper.status == "TP1_HIT"


@pytest.mark.parametrize("ema_enabled,breakeven,ema_value,expected_stop", [
    (True, False, None, 90), (False, False, 112, 90), (True, True, 112, 100),
])
def test_optional_tp1_modes_preserved(settings, ema_enabled, breakeven, ema_value, expected_stop):
    settings.analysis.tp1_ema_trailing_stop_enabled = ema_enabled
    settings.analysis.tp1_move_stop_to_breakeven_enabled = breakeven
    item = _make_sim_trade(entry_price=100)
    step(item, bar(115, 125, 105, 122), settings, ema_value)
    assert item.paper.status == "TP1_HIT"
    assert item.paper.stop_loss == expected_stop
    assert not item.paper.tp1_trailing_ema_stop_active


@pytest.mark.parametrize("exit_kind", ["stop", "target"])
def test_entry_bar_exit_books_both_fills_once(settings, exit_kind):
    item = _make_sim_trade()
    item.paper.status, item.paper.quantity, item.paper.entry_price = "WATCHING", None, None
    item.record.entry_fee = 0
    fill = entry_fill(105, 4, settings.backtest)
    item.paper.cash_risk = (fill.filled_price - 90) * 4
    candle = bar(104, 140 if exit_kind == "target" else 110, 100 if exit_kind == "target" else 89, 106)
    delta = step(item, candle, settings, 112, entry=fill)
    qty = item.paper.quantity
    exit_fill = target_exit_fill(135, qty, settings.backtest) if exit_kind == "target" else stop_exit_fill(90, qty, settings.backtest)
    assert item.record.exit_fee == exit_fill.fee
    assert item.record.exit_price_raw == exit_fill.raw_price
    assert delta == pytest.approx(qty * (exit_fill.filled_price - fill.filled_price) - fill.fee - exit_fill.fee)
    assert item.paper.realized_pnl == pytest.approx(delta)
    assert not item.paper.tp1_trailing_ema_stop_active


@pytest.mark.parametrize("same_bar_target", [False, True])
def test_run_backtest_replay_wires_causal_ema_and_cash(monkeypatch, settings, same_bar_target):
    """Exercise real replay plan/entry/exit loops; stub only market/scanner inputs."""
    start = ms("2026-01-01T00:00:00")
    duration = interval_ms("4h")
    data = {}
    for iv, count in [("1h", 200), ("4h", 90), ("1d", 250)]:
        step_ms = interval_ms(iv)
        data[iv] = [make_kline(start - i * step_ms, 114, step_ms) for i in range(count, 0, -1)]
    ranges = [(104, 106, 102, 105), (104, 140 if same_bar_target else 125, 100, 122),
              (120, 125, 115, 122), (116, 119, 110, 116)]
    for index, (o, h, l, c) in enumerate(ranges):
        data["4h"].append([start + index * duration, o, h, l, c, 100, start + (index + 1) * duration - 1])
    settings.analysis.market_regime_filter_enabled = False
    settings.backtest.max_holding_bars_without_tp1 = 0
    candidate = SimpleNamespace(symbol="TESTUSDT", base_asset="TEST", rank=1, score=80, action="BUY_CANDIDATE",
                                setup="fixture", verdict="fixture", entry_low=100, entry_high=105, stop_loss=90,
                                take_profit_1=120, take_profit_2=135, risk_reward_1=1, risk_reward_2=2, price=105)
    calls = []
    def analyze(*args, **kwargs):
        calls.append(True)
        return deepcopy(candidate) if len(calls) == 1 else None
    monkeypatch.setattr(replay, "_analyze_ticker", analyze)
    monkeypatch.setattr(replay, "reconstruct_ticker", lambda *args, **kwargs: None)
    monkeypatch.setattr(replay, "fetch_klines_cached", lambda settings, symbol, interval, *args, **kwargs:
                        KlineFetchResult(symbol=symbol, interval=interval, klines=data[interval], issues=[], fetched_from_api=0))
    monkeypatch.setattr(replay, "batch_load_klines_cached", lambda *args, **kwargs: {"TESTUSDT": data})
    result = replay.run_backtest_replay(settings, ["TESTUSDT"], "2026-01-01", "2026-01-01T16:00:00+00:00")
    assert len(result.trades) == 1
    trade = result.trades[0]
    assert trade.status == ("CLOSED" if same_bar_target else "STOPPED")
    assert trade.exit_fee > 0 and trade.entry_fee > 0
    assert result.cash == pytest.approx(result.initial_equity + trade.net_pnl)
    assert result.final_equity == pytest.approx(result.cash)
    assert trade.net_pnl == pytest.approx(trade.gross_pnl - trade.entry_fee - trade.exit_fee)
    if same_bar_target:
        assert trade.exit_price_raw == 135
    else:
        # TP1 on bar 1 survives its earlier low, raised stop from bar 2 is used on bar 3.
        assert trade.closed_at_utc == "2026-01-01T16:00:00+00:00"
        raised = [e for e in trade.events if e["event_type"] == "TP1_EMA_TRAILING_RAISED"]
        assert raised
        assert trade.exit_price_raw == pytest.approx(raised[-1]["price"])
