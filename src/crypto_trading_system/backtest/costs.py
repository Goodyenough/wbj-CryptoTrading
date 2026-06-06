from __future__ import annotations

from dataclasses import dataclass

from ..config import BacktestSettings


@dataclass(frozen=True)
class CostBreakdown:
    raw_price: float
    filled_price: float
    fee: float
    slippage_cost: float


def _bps(value: float) -> float:
    return value / 10_000


def entry_fill(raw_price: float, quantity: float, settings: BacktestSettings) -> CostBreakdown:
    filled = raw_price * (1 + _bps(settings.entry_slippage_bps))
    fee = filled * quantity * _bps(settings.maker_fee_bps)
    slippage_cost = max(filled - raw_price, 0) * quantity
    return CostBreakdown(raw_price=raw_price, filled_price=filled, fee=fee, slippage_cost=slippage_cost)


def stop_exit_fill(raw_price: float, quantity: float, settings: BacktestSettings) -> CostBreakdown:
    filled = raw_price * (1 - _bps(settings.stop_slippage_bps))
    fee = filled * quantity * _bps(settings.taker_fee_bps)
    slippage_cost = max(raw_price - filled, 0) * quantity
    return CostBreakdown(raw_price=raw_price, filled_price=filled, fee=fee, slippage_cost=slippage_cost)


def target_exit_fill(raw_price: float, quantity: float, settings: BacktestSettings) -> CostBreakdown:
    fee = raw_price * quantity * _bps(settings.maker_fee_bps)
    return CostBreakdown(raw_price=raw_price, filled_price=raw_price, fee=fee, slippage_cost=0.0)
