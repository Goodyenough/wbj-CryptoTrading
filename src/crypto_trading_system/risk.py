from __future__ import annotations


def reward_to_risk(entry: float, stop_loss: float, target: float) -> float | None:
    risk = entry - stop_loss
    if risk <= 0:
        return None
    return (target - entry) / risk


def position_size(
    account_equity: float,
    risk_per_trade_pct: float,
    entry: float,
    stop_loss: float,
) -> float | None:
    per_unit_risk = entry - stop_loss
    if account_equity <= 0 or risk_per_trade_pct <= 0 or per_unit_risk <= 0:
        return None
    cash_risk = account_equity * risk_per_trade_pct
    return cash_risk / per_unit_risk

