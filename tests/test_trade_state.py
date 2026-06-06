from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.models import PaperTrade
from crypto_trading_system.trade_state import step_trade


def make_trade(status: str = "WATCHING") -> PaperTrade:
    return PaperTrade(
        paper_trade_id="test",
        account_name="demo",
        source_scan_id="scan",
        source_rank=1,
        symbol="TESTUSDT",
        base_asset="TEST",
        status=status,
        created_at_utc="2026-01-01T00:00:00+00:00",
        updated_at_utc="2026-01-01T00:00:00+00:00",
        setup="test",
        verdict="test",
        entry_low=100.0,
        entry_high=105.0,
        planned_entry_mid=102.5,
        stop_loss=90.0,
        take_profit_1=120.0,
        take_profit_2=135.0,
        risk_reward_1=2.0,
        risk_reward_2=3.0,
        account_equity=10_000.0,
        risk_per_trade_pct=0.01,
        cash_risk=100.0,
    )


def test_watching_to_entered() -> None:
    trade = make_trade()
    events = step_trade(trade, high=103.0, low=103.0, close=103.0, event_time_utc="2026-01-01T04:00:00+00:00")
    assert trade.status == "ENTERED"
    assert trade.entry_price == 103.0
    assert round(trade.quantity or 0, 8) == round(100 / 13, 8)
    assert [event.event_type for event in events] == ["ENTERED"]


def test_watching_invalidated_before_entry() -> None:
    trade = make_trade()
    events = step_trade(trade, high=95.0, low=89.0, close=89.0, event_time_utc="2026-01-01T04:00:00+00:00")
    assert trade.status == "INVALIDATED"
    assert trade.closed_at_utc == "2026-01-01T04:00:00+00:00"
    assert [event.event_type for event in events] == ["INVALIDATED"]


def test_entered_to_stopped() -> None:
    trade = make_trade("ENTERED")
    trade.entry_price = 103.0
    trade.quantity = 100 / 13
    events = step_trade(trade, high=110.0, low=88.0, close=91.0, event_time_utc="2026-01-01T08:00:00+00:00")
    assert trade.status == "STOPPED"
    assert trade.exit_price == 90.0
    assert round(trade.realized_pnl, 8) == round((90 - 103) * (100 / 13), 8)
    assert [event.event_type for event in events] == ["STOPPED"]


def test_entered_to_closed() -> None:
    trade = make_trade("ENTERED")
    trade.entry_price = 103.0
    trade.quantity = 100 / 13
    events = step_trade(trade, high=140.0, low=110.0, close=136.0, event_time_utc="2026-01-01T08:00:00+00:00")
    assert trade.status == "CLOSED"
    assert trade.exit_price == 135.0
    assert [event.event_type for event in events] == ["CLOSED"]


def test_watching_same_bar_entry_then_stop() -> None:
    trade = make_trade()
    events = step_trade(
        trade,
        high=104.0,
        low=88.0,
        close=92.0,
        event_time_utc="2026-01-01T04:00:00+00:00",
        entry_price_override=105.0,
    )
    assert trade.status == "STOPPED"
    assert trade.entry_price == 105.0
    assert trade.exit_price == 90.0
    assert [event.event_type for event in events] == ["ENTERED", "STOPPED"]


if __name__ == "__main__":
    test_watching_to_entered()
    test_watching_invalidated_before_entry()
    test_entered_to_stopped()
    test_entered_to_closed()
    test_watching_same_bar_entry_then_stop()
    print("test_trade_state=passed")
