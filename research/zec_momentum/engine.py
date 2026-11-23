"""Causal, single-position, linear USDT contract replay. This module performs no I/O.

All cutoffs are exclusive. OHLC bars include a close timestamp at index 6.
Decisions occur at a completed 15m bar's right boundary; execution is delayed
another 5m. Unknown intrabar ordering uses stop-first and the bar's final
millisecond as an upper-bound exit timestamp. Funding aligns to 5m opens.
Fees and slippage are assumptions supplied by the caller, not exchange facts.
"""
from __future__ import annotations

from bisect import bisect_right
from collections import Counter
import math
from typing import Sequence

from crypto_trading_system.indicators import atr, ema_series

FIVE = 300_000
FIFTEEN = 3 * FIVE
HOUR = 12 * FIVE
DEFAULT_CUTOFF_MS = 1_782_144_000_000
FUNDING_RESERVE = 0.0005


def _validate_bars(bars: Sequence[Sequence], cutoff_ms: int) -> list[list[float]]:
    if isinstance(cutoff_ms, bool) or not isinstance(cutoff_ms, int) or not 0 < cutoff_ms <= DEFAULT_CUTOFF_MS:
        raise ValueError("Sealed cutoff cannot be moved later")
    result = []
    previous = None
    for raw in bars:
        if len(raw) < 7:
            raise ValueError("Expected OHLCV with close timestamp at index 6")
        row = [float(value) for value in raw]
        if not all(math.isfinite(value) for value in row):
            raise ValueError("Nonfinite bar")
        opened, closed = int(row[0]), int(row[6])
        if opened != row[0] or opened % FIVE or closed != opened + FIVE - 1:
            raise ValueError("Bars must be complete aligned 5m candles")
        if opened >= cutoff_ms or closed >= cutoff_ms:
            raise ValueError("Sealed cutoff: bar reaches reserved data")
        if previous is not None and opened <= previous:
            raise ValueError("Bars must have strictly increasing unique timestamps")
        if min(row[1:5]) <= 0 or row[2] < max(row[1], row[4]) or row[3] > min(row[1], row[4]):
            raise ValueError("Invalid OHLC")
        if row[5] < 0:
            raise ValueError("Negative volume")
        result.append(row)
        previous = opened
    return result


def _aggregate(bars: list[list[float]], step: int) -> list[list[float]]:
    """Return only complete aligned groups; never synthesize missing candles."""
    groups: dict[int, list[list[float]]] = {}
    for row in bars:
        groups.setdefault(int(row[0]) // step * step, []).append(row)
    result = []
    expected = step // FIVE
    for opened, group in groups.items():
        if len(group) != expected or any(int(row[0]) != opened + index * FIVE for index, row in enumerate(group)):
            continue
        result.append([opened, group[0][1], max(row[2] for row in group),
                       min(row[3] for row in group), group[-1][4],
                       sum(row[5] for row in group), opened + step - 1])
    return result


def signals(bars5: Sequence[Sequence], *, cutoff_ms: int = DEFAULT_CUTOFF_MS) -> list[dict]:
    """Generate frozen two-sided momentum signals from completed bars only.

    Gaps reset hourly EMA history, and every ATR/structure window must be
    contiguous. Returned records contain only information known at decision_ms.
    """
    bars = _validate_bars(bars5, cutoff_ms)
    hours = _aggregate(bars, HOUR)
    quarters = _aggregate(bars, FIFTEEN)
    hour_ends = [int(row[0]) + HOUR for row in hours]
    directions: list[dict | None] = [None] * len(hours)
    start = 0
    while start < len(hours):
        end = start + 1
        while end < len(hours) and hours[end][0] == hours[end - 1][0] + HOUR:
            end += 1
        values = ema_series([row[4] for row in hours[start:end]], 20)
        for offset in range(22, end - start):
            current, before = values[offset - 19], values[offset - 22]
            close = hours[start + offset][4]
            side = "long" if close > current > before else "short" if close < current < before else None
            if side:
                directions[start + offset] = {"side": side, "direction_close": close,
                                              "ema20": current, "ema20_3h_ago": before}
        start = end
    result = []
    for index in range(14, len(quarters)):
        row = quarters[index]
        decision = int(row[0]) + FIFTEEN
        if decision >= cutoff_ms:
            continue
        window = quarters[index - 14:index + 1]
        if any(after[0] != before[0] + FIFTEEN for before, after in zip(window, window[1:])):
            continue
        hourly = bisect_right(hour_ends, decision) - 1
        if hourly < 0 or hour_ends[hourly] < decision // HOUR * HOUR:
            continue
        direction = directions[hourly]
        if direction is None:
            continue
        previous = quarters[index - 4:index]
        side = direction["side"]
        breakout = row[4] > max(item[2] for item in previous) if side == "long" else row[4] < min(item[3] for item in previous)
        if not breakout:
            continue
        volatility = atr(window, 14)
        assert volatility is not None
        structure = quarters[index - 3:index + 1]
        stop = min(item[3] for item in structure) - 0.1 * volatility if side == "long" else max(item[2] for item in structure) + 0.1 * volatility
        result.append(dict(decision_ms=decision, stop_price=stop, atr=volatility, **direction))
    return result


def _target_raw(position: dict, fee: float, slip: float) -> float:
    side = position["sign"]
    target_fill = ((position["target_net_usdt"] + position["funding_usdt"]) / position["quantity"]
                   + (side + fee) * position["entry_price"]) / (side - fee)
    return target_fill / (1 - side * slip)


def run_replay(
    bars5: Sequence[Sequence], funding: Sequence[dict], start_ms: int, end_ms: int,
    target_pct: float, hold_hours: int, fee_bps: float, slippage_bps: float,
    cutoff_ms: int = DEFAULT_CUTOFF_MS, initial_equity: float = 110.0,
    *, precomputed_signals: Sequence[dict] | None = None,
) -> dict:
    """Replay one prespecified branch; percentages are fractions (0.01 = 1%).

    The 5 USDT cap is planned stop loss with assumed friction and funding
    reserve. Gaps or funding above the reserve can produce a larger realized
    loss. Nominal exposure is at most 1x entry equity; 2x margin is informational.
    Missing execution bars abort instead of fabricating an exit or sequence.
    """
    if not (start_ms < end_ms <= cutoff_ms) or start_ms % FIVE or end_ms % FIVE:
        raise ValueError("Invalid segment or sealed cutoff")
    if hold_hours not in {2, 4} or target_pct not in {0.01, 0.02}:
        raise ValueError("Only frozen 2h/4h and net 1%/2% branches are supported")
    if not (0 <= fee_bps < 10000 and 0 <= slippage_bps < 10000 and initial_equity > 0 and math.isfinite(initial_equity)):
        raise ValueError("Invalid costs or initial equity")
    bars = _validate_bars(bars5, cutoff_ms)
    bars = [row for row in bars if row[6] < end_ms]
    funding_rows = []
    previous_funding = None
    for event in funding:
        when = int(event["time_ms"])
        rate, mark = float(event["rate"]), float(event["mark_price"])
        if when != event["time_ms"] or when % FIVE:
            raise ValueError("Funding events must align to 5m opens")
        if when >= cutoff_ms:
            raise ValueError("Sealed cutoff: funding reaches reserved data")
        if not math.isfinite(rate) or not math.isfinite(mark) or mark <= 0:
            raise ValueError("Invalid historical funding")
        if previous_funding is not None and when <= previous_funding:
            raise ValueError("Funding events must be sorted and unique")
        previous_funding = when
        if when < end_ms:
            funding_rows.append(dict(time_ms=when, rate=rate, mark_price=mark))
    generated = signals(bars, cutoff_ms=cutoff_ms) if precomputed_signals is None else precomputed_signals
    if any(event["decision_ms"] >= cutoff_ms for event in generated):
        raise ValueError("Sealed cutoff: precomputed signal reaches reserved data")
    events = {event["decision_ms"]: event for event in generated
              if start_ms <= event["decision_ms"] < end_ms}
    execution = [row for row in bars if row[0] >= start_ms]
    if any(after[0] != before[0] + FIVE for before, after in zip(execution, execution[1:])):
        raise ValueError("Execution segment has missing 5m candles")
    by_open = {int(row[0]): row for row in execution}
    fee, slip = fee_bps / 10_000, slippage_bps / 10_000
    balance = float(initial_equity)
    position = None
    pending = None
    trades, curve = [], [dict(time_ms=start_ms, equity=balance)]
    skips = Counter()
    last_exit = -1
    funding_index = 0

    def close(raw_price: float, when: int, reason: str, ambiguous: bool = False) -> None:
        nonlocal balance, position, last_exit
        assert position is not None and when < min(end_ms, cutoff_ms)
        p = position
        fill = raw_price * (1 - p["sign"] * slip)
        gross = p["sign"] * p["quantity"] * (fill - p["entry_price"])
        exit_fee = p["quantity"] * fill * fee
        balance += gross - exit_fee
        net = gross - p["entry_fee_usdt"] - exit_fee - p["funding_usdt"]
        trade = dict(p, exit_ms=when, raw_exit=raw_price, exit_price=fill,
                     exit_fee_usdt=exit_fee, gross_pnl_usdt=gross, net_pnl_usdt=net,
                     initial_risk_usdt=p["planned_risk_usdt"],
                     fees_usdt=p["entry_fee_usdt"] + exit_fee,
                     funding_cost_usdt=p["funding_usdt"], exit_reason=reason,
                     exit_time_exact=reason in {"SL_GAP", "TP_GAP", "TIME"},
                     account_return_pct=100 * net / p["entry_equity"], status=reason,
                     ambiguous=ambiguous, equity_after=balance,
                     duration_hours=(when - p["entry_ms"]) / HOUR)
        if abs(balance - p["entry_equity"] - net) > 1e-8:
            raise AssertionError("Account PnL does not reconcile")
        trades.append(trade)
        last_exit, position = when, None

    for row in execution:
        now, opening, high, low = int(row[0]), row[1], row[2], row[3]
        while funding_index < len(funding_rows) and funding_rows[funding_index]["time_ms"] <= now:
            event = funding_rows[funding_index]
            if position is not None and event["time_ms"] > position["entry_ms"]:
                cost = position["sign"] * position["quantity"] * event["mark_price"] * event["rate"]
                balance -= cost
                position["funding_usdt"] += cost
                position["funding_events"].append(dict(event, paid_usdt=cost))
            funding_index += 1
        # Opening gaps and funding at the same instant precede time exits.
        if position is not None:
            stop, sign = position["stop_price"], position["sign"]
            target = _target_raw(position, fee, slip)
            position["target_raw"] = target
            if sign * (opening - stop) <= 0:
                close(opening, now, "SL_GAP")
            elif sign * (opening - target) >= 0:
                close(opening, now, "TP_GAP")
            elif now >= position["deadline_ms"]:
                close(opening, now, "TIME")
        event = events.get(now)
        if event is not None:
            if position is not None or pending is not None:
                skips["position_or_pending"] += 1
            elif now <= last_exit:
                skips["wait_next_signal_after_exit"] += 1
            else:
                fill_time = now + FIVE
                deadline = fill_time + hold_hours * HOUR
                if fill_time not in by_open or deadline not in by_open or deadline >= min(end_ms, cutoff_ms):
                    skips["insufficient_full_horizon"] += 1
                else:
                    pending = dict(event, fill_ms=fill_time, deadline_ms=deadline)
        if pending is not None and pending["fill_ms"] == now:
            sign = 1 if pending["side"] == "long" else -1
            fill = opening * (1 + sign * slip)
            stop_fill = pending["stop_price"] * (1 - sign * slip)
            unit_risk = -sign * (stop_fill - fill) + fee * (fill + stop_fill) + FUNDING_RESERVE * fill
            if balance <= 0 or pending["stop_price"] <= 0 or sign * (opening - pending["stop_price"]) <= 0 or unit_risk <= 0:
                skips["invalid_entry_or_stop"] += 1
            else:
                quantity = min(balance / fill, 5.0 / unit_risk)
                position = dict(pending, sign=sign, entry_ms=now, raw_entry=opening,
                                entry_price=fill, quantity=quantity, entry_equity=balance,
                                entry_fee_usdt=quantity * fill * fee, funding_usdt=0.0,
                                funding_events=[], target_net_usdt=balance * target_pct,
                                planned_risk_usdt=quantity * unit_risk,
                                notional_usdt=quantity * fill, reference_margin_usdt=quantity * fill / 2)
                target = _target_raw(position, fee, slip)
                position["target_raw"] = target
                if target <= 0 or sign * (target - opening) <= 0:
                    skips["unreachable_target"] += 1
                    position = None
                else:
                    balance -= position["entry_fee_usdt"]
            pending = None
        if position is not None:
            stop, target, sign = position["stop_price"], _target_raw(position, fee, slip), position["sign"]
            sl_hit = low <= stop if sign == 1 else high >= stop
            tp_hit = high >= target if sign == 1 else low <= target
            if sl_hit:
                close(stop, int(row[6]), "SL", ambiguous=bool(tp_hit))
            elif tp_hit:
                close(target, int(row[6]), "TP")
        value = balance
        if position is not None:
            exit_mark = row[4] * (1 - position["sign"] * slip)
            value += position["sign"] * position["quantity"] * (exit_mark - position["entry_price"]) - position["quantity"] * exit_mark * fee
        curve.append(dict(time_ms=int(row[6]), equity=value))
    if position is not None or pending is not None:
        raise AssertionError("Full-horizon entry gate left an unresolved position")
    pnl = [trade["net_pnl_usdt"] for trade in trades]
    profit = sum(max(value, 0) for value in pnl)
    loss = -sum(min(value, 0) for value in pnl)
    peak = initial_equity
    drawdown = 0.0
    for point in curve:
        peak = max(peak, point["equity"])
        drawdown = max(drawdown, (peak - point["equity"]) / peak)
    metrics = dict(trades=len(trades), win_rate_pct=100 * sum(value > 0 for value in pnl) / len(pnl) if pnl else None,
                   profit_factor=profit / loss if loss else None,
                   mean_net_usdt=sum(pnl) / len(pnl) if pnl else None,
                   net_return_pct=100 * (balance / initial_equity - 1), max_drawdown_pct=100 * drawdown,
                   ambiguous_trades=sum(trade["ambiguous"] for trade in trades),
                   fees_usdt=sum(trade["entry_fee_usdt"] + trade["exit_fee_usdt"] for trade in trades),
                   funding_usdt=sum(trade["funding_usdt"] for trade in trades),
                   long_trades=sum(trade["side"] == "long" for trade in trades),
                   short_trades=sum(trade["side"] == "short" for trade in trades))
    return dict(trades=trades, equity_curve=curve, equity=balance, final_equity=balance,
                signal_count=len(events), skip_counts=dict(skips), metrics=metrics)
