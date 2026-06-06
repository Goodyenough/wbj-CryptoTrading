from __future__ import annotations

from dataclasses import dataclass
import math

from .replay import BacktestResult, BacktestTrade


@dataclass
class BacktestMetrics:
    trades: int
    closed_trades: int
    open_trades: int
    win_rate: float | None
    profit_factor: float | None
    avg_r: float | None
    net_return_pct: float
    max_drawdown: float
    max_drawdown_pct: float
    intrabar_max_drawdown: float
    intrabar_max_drawdown_pct: float
    tp1_rate: float | None
    tp2_rate: float | None
    stop_rate: float | None
    fee_drag: float
    tail_max_loss: float
    cagr: float | None
    sharpe: float | None
    sortino: float | None
    exposure_pct: float | None
    turnover: float | None
    sample_sufficient: bool
    sample_warning: str


def _closed(trades: list[BacktestTrade]) -> list[BacktestTrade]:
    return [trade for trade in trades if trade.status in {"STOPPED", "CLOSED"}]


def _max_drawdown(values: list[float]) -> tuple[float, float]:
    peak = values[0] if values else 0.0
    max_dd = 0.0
    max_dd_pct = 0.0
    for value in values:
        peak = max(peak, value)
        drawdown = peak - value
        if drawdown > max_dd:
            max_dd = drawdown
            max_dd_pct = drawdown / peak * 100 if peak > 0 else 0.0
    return max_dd, max_dd_pct


def _returns(values: list[float]) -> list[float]:
    output: list[float] = []
    for previous, current in zip(values, values[1:]):
        if previous > 0:
            output.append(current / previous - 1)
    return output


def _mean(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def _std(values: list[float]) -> float | None:
    if len(values) < 2:
        return None
    avg = sum(values) / len(values)
    return math.sqrt(sum((value - avg) ** 2 for value in values) / (len(values) - 1))


def calculate_metrics(result: BacktestResult) -> BacktestMetrics:
    trades = result.trades
    closed = _closed(trades)
    winning = [trade for trade in closed if trade.net_pnl > 0]
    losing = [trade for trade in closed if trade.net_pnl < 0]
    gross_profit = sum(trade.net_pnl for trade in winning)
    gross_loss = abs(sum(trade.net_pnl for trade in losing))
    r_values = [trade.r_multiple_net for trade in closed if trade.r_multiple_net is not None]
    equities = [point.equity for point in result.equity_curve] or [result.initial_equity, result.final_equity]
    intrabar_equities = [point.intrabar_equity_low for point in result.equity_curve] or equities
    max_dd, max_dd_pct = _max_drawdown(equities)
    intra_dd, intra_dd_pct = _max_drawdown(intrabar_equities)
    returns = _returns(equities)
    avg_ret = _mean(returns)
    std_ret = _std(returns)
    downside = [value for value in returns if value < 0]
    std_down = _std(downside)
    bars_per_year = 365 * 6
    sharpe = None
    if avg_ret is not None and std_ret and std_ret > 0:
        sharpe = avg_ret / std_ret * math.sqrt(bars_per_year)
    sortino = None
    if avg_ret is not None and std_down and std_down > 0:
        sortino = avg_ret / std_down * math.sqrt(bars_per_year)
    days = max((len(equities) / 6), 1)
    cagr = ((result.final_equity / result.initial_equity) ** (365 / days) - 1) * 100 if result.initial_equity > 0 else None
    exposure = None
    if result.equity_curve:
        exposure = sum(1 for point in result.equity_curve if point.open_positions > 0) / len(result.equity_curve) * 100
    total_entry_notional = sum((trade.entry_price_filled or 0) * (trade.quantity or 0) for trade in trades)
    turnover = total_entry_notional / result.initial_equity if result.initial_equity > 0 else None
    sample_warning = ""
    if len(closed) < 30:
        sample_warning = "样本不足，Sharpe/Sortino/CAGR 需要谨慎解读。"

    return BacktestMetrics(
        trades=len(trades),
        closed_trades=len(closed),
        open_trades=len([trade for trade in trades if trade.status in {"ENTERED", "TP1_HIT"}]),
        win_rate=(len(winning) / len(closed) * 100) if closed else None,
        profit_factor=(gross_profit / gross_loss) if gross_loss > 0 else (None if gross_profit == 0 else math.inf),
        avg_r=_mean([float(value) for value in r_values]),
        net_return_pct=(result.final_equity / result.initial_equity - 1) * 100 if result.initial_equity > 0 else 0.0,
        max_drawdown=max_dd,
        max_drawdown_pct=max_dd_pct,
        intrabar_max_drawdown=intra_dd,
        intrabar_max_drawdown_pct=intra_dd_pct,
        tp1_rate=(len([trade for trade in trades if trade.tp1_hit_at_utc]) / len(closed) * 100) if closed else None,
        tp2_rate=(len([trade for trade in closed if trade.status == "CLOSED"]) / len(closed) * 100) if closed else None,
        stop_rate=(len([trade for trade in closed if trade.status == "STOPPED"]) / len(closed) * 100) if closed else None,
        fee_drag=sum(trade.entry_fee + trade.exit_fee for trade in trades),
        tail_max_loss=min([trade.net_pnl for trade in closed], default=0.0),
        cagr=cagr,
        sharpe=sharpe,
        sortino=sortino,
        exposure_pct=exposure,
        turnover=turnover,
        sample_sufficient=len(closed) >= 20,
        sample_warning=sample_warning,
    )
