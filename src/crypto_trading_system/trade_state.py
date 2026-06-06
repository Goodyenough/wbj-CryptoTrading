from __future__ import annotations

from datetime import datetime, timezone

from .models import PaperTrade, StepEvent


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _entry_price_for_bar(trade: PaperTrade, high: float, low: float, fallback: float) -> float | None:
    if high < trade.entry_low or low > trade.entry_high:
        return None
    return fallback


def step_trade(
    trade: PaperTrade,
    high: float,
    low: float,
    close: float,
    *,
    open_price: float | None = None,
    event_time_utc: str | None = None,
    intrabar: str = "stop_first",
    entry_price_override: float | None = None,
    stop_exit_price_override: float | None = None,
    tp2_exit_price_override: float | None = None,
) -> list[StepEvent]:
    if intrabar not in {"stop_first", "tp_first"}:
        raise ValueError("intrabar must be stop_first or tp_first")
    event_time = event_time_utc or _utc_now()
    old_status = trade.status
    events: list[StepEvent] = []
    trade.last_price = close
    trade.updated_at_utc = event_time

    if trade.status == "WATCHING":
        if high < trade.entry_low and low <= trade.stop_loss:
            trade.status = "INVALIDATED"
            trade.closed_at_utc = event_time
            trade.exit_price = close if open_price is None else min(open_price, close)
            trade.notes = "Plan invalidated before entry: current price is below stop loss."
            events.append(
                StepEvent(
                    event_type="INVALIDATED",
                    message="Plan invalidated before entry: current price is below stop loss.",
                    event_time_utc=event_time,
                    price=trade.exit_price,
                )
            )
        else:
            entry_price = _entry_price_for_bar(
                trade,
                high,
                low,
                entry_price_override if entry_price_override is not None else close,
            )
            if entry_price is not None:
                trade.status = "ENTERED"
                trade.entry_price = entry_price
                per_unit_risk = entry_price - trade.stop_loss
                if per_unit_risk > 0:
                    trade.quantity = trade.cash_risk / per_unit_risk
                trade.entered_at_utc = event_time
                trade.notes = "Paper entry triggered inside entry zone."
                qty_text = "n/a" if trade.quantity is None else f"{trade.quantity:.8g}"
                events.append(
                    StepEvent(
                        event_type="ENTERED",
                        message=f"Paper entry triggered at {entry_price:.8g}; quantity {qty_text}.",
                        event_time_utc=event_time,
                        price=entry_price,
                    )
                )
            elif close > trade.entry_high:
                trade.notes = "Watching: price is above entry zone; waiting for pullback."
            else:
                trade.notes = "Watching: price is below entry zone but above stop; waiting for recovery."

    if trade.status in {"ENTERED", "TP1_HIT"} and trade.entry_price is not None and trade.quantity:
        trade.unrealized_pnl = (close - trade.entry_price) * trade.quantity
        stop_hit = low <= trade.stop_loss
        tp2_hit = high >= trade.take_profit_2
        tp1_hit = high >= trade.take_profit_1 and trade.status == "ENTERED"
        if intrabar == "stop_first":
            order = ("stop", "tp2", "tp1")
        else:
            order = ("tp2", "tp1", "stop")

        for trigger in order:
            if trigger == "stop" and stop_hit:
                exit_price = stop_exit_price_override if stop_exit_price_override is not None else trade.stop_loss
                trade.status = "STOPPED"
                trade.closed_at_utc = event_time
                trade.exit_price = exit_price
                trade.realized_pnl = (exit_price - trade.entry_price) * trade.quantity
                trade.unrealized_pnl = 0
                trade.notes = "Stop loss hit."
                if old_status != "STOPPED":
                    events.append(
                        StepEvent(
                            event_type="STOPPED",
                            message=f"Stop loss hit at {exit_price:.8g}.",
                            event_time_utc=event_time,
                            price=exit_price,
                        )
                    )
                break
            if trigger == "tp2" and tp2_hit:
                exit_price = tp2_exit_price_override if tp2_exit_price_override is not None else trade.take_profit_2
                trade.status = "CLOSED"
                trade.closed_at_utc = event_time
                trade.exit_price = exit_price
                trade.realized_pnl = (exit_price - trade.entry_price) * trade.quantity
                trade.unrealized_pnl = 0
                trade.notes = "TP2 hit; paper trade closed."
                if old_status != "CLOSED":
                    events.append(
                        StepEvent(
                            event_type="CLOSED",
                            message=f"TP2 hit at {exit_price:.8g}; trade closed.",
                            event_time_utc=event_time,
                            price=exit_price,
                        )
                    )
                break
            if trigger == "tp1" and tp1_hit:
                trade.status = "TP1_HIT"
                trade.tp1_hit_at_utc = event_time
                trade.notes = "TP1 hit; trade remains open for TP2 tracking."
                events.append(
                    StepEvent(
                        event_type="TP1_HIT",
                        message=f"TP1 hit at {trade.take_profit_1:.8g}; trade remains open.",
                        event_time_utc=event_time,
                        price=trade.take_profit_1,
                    )
                )
                break

    return events
