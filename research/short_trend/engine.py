"""Frozen, causal short-trend event study. Pure functions; no I/O or orders.

The continuous mirror pairs are independent shadow events, not an executable
account. Slippage is embedded once in fills; its reported cost is diagnostic.
Unknown intrabar exits use the candle's last millisecond as a time upper bound.
"""
from __future__ import annotations

from bisect import bisect_right
from collections import Counter, deque
from datetime import datetime, timezone
import math
from typing import Sequence

FIVE = 300_000
HOUR = 12 * FIVE
HOLD = 4 * HOUR
WARMUP_MS = 1_701_388_800_000  # 2023-12-01T00:00:00Z
EXCLUSIVE_END_MS = 1_767_225_600_000
EQUITY = 110.0
RISK = 1.65
TARGET = 1.1
RESERVE = 0.0005
SYMBOLS = frozenset({"BTCUSDT", "ETHUSDT", "SOLUSDT", "ZECUSDT"})


class DataQualityError(ValueError):
    """Do not publish a complete study from incomplete price data."""


def _integer_time(value, label: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"Invalid {label} timestamp")
    try:
        when = int(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError(f"Invalid {label} timestamp") from exc
    if str(value) != str(when) and value != when:
        raise ValueError(f"Noninteger {label} timestamp")
    if not WARMUP_MS <= when < EXCLUSIVE_END_MS:
        raise ValueError(f"Excluded timestamp in {label}; validate time before market values")
    return when


def _bars(raw_rows: Sequence[Sequence]) -> list[list]:
    rows = []
    previous = None
    for raw in raw_rows:
        if len(raw) < 7:
            raise DataQualityError("Expected [open_ms,open,high,low,close,volume,close_ms]")
        opened = _integer_time(raw[0], "bar open")
        closed = _integer_time(raw[6], "bar close")
        if opened % FIVE or closed != opened + FIVE - 1:
            raise DataQualityError("Incomplete or misaligned 5m candle")
        if previous is not None and opened <= previous:
            raise DataQualityError("Duplicate or unsorted 5m timestamps")
        values = [float(value) for value in raw[1:6]]
        if not all(math.isfinite(value) for value in values):
            raise DataQualityError("Nonfinite OHLCV")
        o, h, lo, c, volume = values
        if min(o, h, lo, c) <= 0 or h < max(o, c) or lo > min(o, c) or lo > h or volume < 0:
            raise DataQualityError("Invalid OHLCV geometry")
        rows.append([opened, o, h, lo, c, volume, closed])
        previous = opened
    return rows


def _hours(rows: list[list]) -> list[list]:
    result = []
    group = []
    for row in rows:
        opened = row[0] // HOUR * HOUR
        if group and group[0][0] // HOUR * HOUR != opened:
            if len(group) == 12 and all(r[0] == group[0][0] + i * FIVE for i, r in enumerate(group)) and group[0][0] % HOUR == 0:
                result.append([group[0][0], group[0][1], max(r[2] for r in group), min(r[3] for r in group), group[-1][4]])
            group = []
        group.append(row)
    if len(group) == 12 and group[0][0] % HOUR == 0 and all(r[0] == group[0][0] + i * FIVE for i, r in enumerate(group)):
        result.append([group[0][0], group[0][1], max(r[2] for r in group), min(r[3] for r in group), group[-1][4]])
    return result


def _signals(rows: list[list]) -> list[dict]:
    history: deque = deque(maxlen=50)
    prior_hour = None
    previous_close = None
    true_ranges = []
    volatility = None
    result = []
    for row in _hours(rows):
        if prior_hour is None or row[0] != prior_hour + HOUR:
            history.clear()
            previous_close = None
            true_ranges = []
            volatility = None
        if previous_close is not None:
            tr = max(row[2] - row[3], abs(row[2] - previous_close), abs(row[3] - previous_close))
            if volatility is None:
                true_ranges.append(tr)
                if len(true_ranges) == 14:
                    volatility = sum(true_ranges) / 14
            else:
                volatility = (13 * volatility + tr) / 14
        history.append(row)
        if len(history) == 50 and volatility is not None:
            window = list(history)
            high = max(r[2] for r in window[1:49])
            low = min(r[3] for r in window[1:49])
            old_high = max(r[2] for r in window[:48])
            old_low = min(r[3] for r in window[:48])
            previous = window[48][4]
            direction = (1 if row[4] > high and previous <= old_high else
                         -1 if row[4] < low and previous >= old_low else 0)
            decision = row[0] + HOUR
            if direction and decision < EXCLUSIVE_END_MS:
                level = high if direction == 1 else low
                result.append({"decision_ms": decision, "side": "long" if direction == 1 else "short",
                               "direction": direction, "decision_close": row[4], "atr": volatility,
                               "breakout_level": level, "signal_stop": level - direction * volatility})
        previous_close = row[4]
        prior_hour = row[0]
    return result


def signals(bars5: Sequence[Sequence]) -> list[dict]:
    """First close crossing of prior 48 completed hours, Wilder ATR(14).

    Missing/incomplete hours reset all history; this diagnostic does not imply
    the symbol/year passes data-quality acceptance (event_pairs fails closed).
    Prefixes produce the same already-completed decisions as longer inputs.
    """
    return _signals(_bars(bars5))


def _funding(raw_events: Sequence[dict]) -> list[dict]:
    result = []
    previous = None
    for raw in raw_events:
        when = _integer_time(raw["time_ms"], "funding")
        if previous is not None and when <= previous:
            raise DataQualityError("Duplicate or unsorted funding timestamps")
        proxy = _integer_time(raw.get("mark_proxy_ms", when // FIVE * FIVE), "funding mark proxy")
        if proxy % FIVE or not proxy <= when < proxy + FIVE:
            raise DataQualityError("Funding mark proxy must be same-bucket open, not future")
        rate, mark = float(raw["rate"]), float(raw["mark_price"])
        if not math.isfinite(rate) or not math.isfinite(mark) or mark <= 0:
            raise DataQualityError("Invalid funding rate/mark")
        interval = raw.get("interval_hours", raw.get("funding_interval_hours"))
        if interval is not None and (isinstance(interval, bool) or not math.isfinite(float(interval)) or float(interval) <= 0):
            raise DataQualityError("Invalid documented funding interval")
        result.append({"time_ms": when, "rate": rate, "mark_price": mark,
                       "mark_proxy_ms": proxy, "proxy_age_ms": when - proxy,
                       "interval_hours": interval})
        previous = when
    return result


def _geometry(p: float, direction: int, stop: float, fee: float, slip: float) -> dict:
    entry_s = p * (1 + direction * slip)
    entry_m = p * (1 - direction * slip)
    distance = direction * (entry_s - stop)
    mirror_stop = entry_m + direction * distance
    if distance <= 0 or direction * (p - stop) <= 0:
        raise ValueError("gap_invalid")
    if -direction * (p - mirror_stop) <= 0 or mirror_stop <= 0:
        raise ValueError("mirror_geometry_invalid")
    entries = (entry_s, entry_m)
    stops = (stop, mirror_stop)
    directions = (direction, -direction)
    risks = []
    for e, st, d in zip(entries, stops, directions):
        exit_fill = st * (1 - d * slip)
        risk = d * (e - exit_fill) + fee * (e + exit_fill) + RESERVE * e
        if not math.isfinite(risk) or min(e, st, exit_fill, risk) <= 0:
            raise ValueError("invalid_unit_risk")
        risks.append(risk)
    cap_risk = RISK / max(risks)
    cap_notional = 2 * EQUITY / max(entries)
    return {"entries": entries, "stops": stops, "risks": risks,
            "cap": min(cap_risk, cap_notional), "notional_cap": cap_notional,
            "distance": distance}


def _target(entry: float, direction: int, quantity: float, funding: float, fee: float, slip: float) -> float:
    actual_fill = ((TARGET + funding) / quantity + (direction + fee) * entry) / (direction - fee)
    return actual_fill / (1 - direction * slip)


def _arm(rows: list[list], by_time: dict[int, int], funds: list[dict], fund_times: list[int],
         entry_ms: int, quantity: float, direction: int, entry: float, stop: float,
         unit_risk: float, fee: float, slip: float, order: str) -> dict:
    deadline = entry_ms + HOLD
    entry_raw = rows[by_time[entry_ms]][1]
    cursor = bisect_right(fund_times, entry_ms)  # A new position does not pay exact-entry funding.
    paid = 0.0
    ledger = []
    clamped = False
    gap_stop = False
    gap_target = False
    cashflow_target_at_open = False
    pending_target_before_funding = None
    simultaneous = False
    both_touched = False
    funding_order_ambiguous = []

    def apply_funding(items: list[dict]) -> None:
        nonlocal paid
        for item in items:
            amount = direction * quantity * item["mark_price"] * item["rate"]
            paid += amount
            ledger.append(dict(item, amount_usdt=amount, funding_usdt=amount,
                               paid_usdt=amount, pnl_usdt=-amount))

    def finalize(raw_exit: float, when: int, reason: str, upper: bool) -> dict:
        exit_fill = raw_exit * (1 - direction * slip)
        gross = direction * quantity * (exit_fill - entry)
        fees = fee * quantity * (entry + exit_fill)
        slip_cost = quantity * (abs(entry - entry_raw) + abs(exit_fill - raw_exit))
        pnl = gross - fees - paid
        return {"side": "long" if direction == 1 else "short", "direction": direction,
                "entry_ms": entry_ms, "entry_raw": entry_raw, "entry_price": entry,
                "stop_price": stop, "exit_ms": when, "exit_time_upper_bound": upper,
                "exit_raw": raw_exit, "exit_price": exit_fill, "exit_reason": reason,
                "deadline_ms": deadline, "quantity": quantity, "unit_risk_usdt": unit_risk,
                "planned_risk_usdt": quantity * unit_risk, "gross_pnl_usdt": gross,
                "price_pnl_usdt": gross,
                "raw_price_pnl_usdt": direction * quantity * (raw_exit - entry_raw),
                "fees_usdt": fees, "fee_usdt": fees, "slippage_usdt": slip_cost, "funding_usdt": paid,
                "net_pnl_usdt": pnl, "net_R": pnl / RISK,
                "funding_events": ledger, "gap_stop": gap_stop, "target_clamped": clamped,
                "gap_target": gap_target,
                "cashflow_target_at_open": cashflow_target_at_open,
                "funding_touch_same_bucket": simultaneous, "both_sl_tp_touched": both_touched,
                "funding_order_ambiguous_events": funding_order_ambiguous,
                "slippage_included_in_fills": True}

    def touches(row: list, target: float) -> tuple[bool, bool]:
        if direction == 1:
            return row[3] <= stop, row[2] >= target
        return row[2] >= stop, row[3] <= target

    for index in range(by_time[entry_ms], by_time[deadline] + 1):
        row = rows[index]
        opened, o, hi, lo, _, _, closed = row
        # Alternative ordering may have changed TP after the preceding bar's
        # last price check. Keep that previously observable TP to distinguish
        # a cashflow-induced exit from an ordinary gap across an existing TP.
        old_target = (pending_target_before_funding if pending_target_before_funding is not None
                      else _target(entry, direction, quantity, paid, fee, slip))
        pending_target_before_funding = None
        exact = []
        while cursor < len(funds) and funds[cursor]["time_ms"] <= opened:
            exact.append(funds[cursor]); cursor += 1
        apply_funding(exact)  # Includes exact deadline; precedes any existing-position exit.
        target = _target(entry, direction, quantity, paid, fee, slip)
        if direction * (o - stop) <= 0:
            gap_stop = o != stop
            return finalize(o, opened, "SL", False)
        if direction * (o - target) >= 0:
            if target != old_target and direction * (o - old_target) < 0:
                # New funding made the cash target immediately attainable.
                # The first observable price is this open; back-filling the
                # newly calculated threshold would invent a past execution.
                cashflow_target_at_open = True
                return finalize(o, opened, "TP", False)
            # Existing TP obtains no favorable opening-gap improvement.
            gap_target = o != target
            if target <= 0:
                target = o
                clamped = True
            return finalize(target, opened, "TP", False)
        if opened == deadline:
            return finalize(o, opened, "TIME", False)
        intrabar = []
        while cursor < len(funds) and funds[cursor]["time_ms"] <= closed:
            intrabar.append(funds[cursor]); cursor += 1
        if order == "funding_first":
            apply_funding(intrabar)
            target = _target(entry, direction, quantity, paid, fee, slip)
        hit_stop, hit_target = touches(row, target)
        if intrabar and (hit_stop or hit_target):
            simultaneous = True
            funding_order_ambiguous.extend(dict(item) for item in intrabar)
        if hit_stop:
            both_touched = both_touched or hit_target
            return finalize(stop, closed, "SL", True)
        if hit_target:
            raw_exit = max(target, lo) if direction == 1 else min(target, hi)
            clamped = clamped or raw_exit != target
            return finalize(raw_exit, closed, "TP", True)
        if order == "price_first":
            if intrabar:
                pending_target_before_funding = target
            apply_funding(intrabar)
            # Do not revisit this candle's extremes using the newly funded TP.
    raise DataQualityError("Missing complete four-hour event path")


def event_pairs(symbol: str, bars5: Sequence[Sequence], funding: Sequence[dict],
                start_ms: int, end_ms: int, fee_bps: float, slippage_bps: float,
                order: str = "funding_first") -> dict:
    """Replay independent signal/mirror events at fixed E=110, r=1.65, G=1.1.

    This deliberately does not implement an account from unknown historical
    lot/tick/margin rules. Complete input coverage is required, with no gaps.
    """
    if symbol not in SYMBOLS or order not in {"funding_first", "price_first"}:
        raise ValueError("Unsupported symbol or execution order")
    if type(start_ms) is not int or type(end_ms) is not int or not WARMUP_MS <= start_ms < end_ms <= EXCLUSIVE_END_MS or start_ms % FIVE or end_ms % FIVE:
        raise ValueError("Invalid or excluded evaluation segment")
    if any(isinstance(v, bool) or not math.isfinite(v) or not 0 <= v < 10000 for v in (fee_bps, slippage_bps)):
        raise ValueError("Invalid fee/slippage assumption")
    fee, slip = fee_bps / 10000, slippage_bps / 10000
    rows = _bars(bars5)
    funds = _funding(funding)
    if not rows or rows[0][0] != WARMUP_MS:
        raise DataQualityError("Fixed Wilder history must start at 2023-12-01T00:00:00Z")
    if rows[0][0] > start_ms or rows[-1][0] + FIVE < end_ms:
        raise DataQualityError("5m price coverage does not include complete evaluation segment")
    if any(b[0] != a[0] + FIVE for a, b in zip(rows, rows[1:])):
        raise DataQualityError("Missing 5m candle: symbol/year is data-quality ineligible")
    by_time = {row[0]: index for index, row in enumerate(rows)}
    fund_times = [item["time_ms"] for item in funds]
    candidates = [item for item in _signals(rows) if start_ms <= item["decision_ms"] < end_ms]
    events = []
    skipped = Counter()
    skip_records = []
    cost_regime = "normal" if (fee_bps, slippage_bps) == (5, 3) else "stress" if (fee_bps, slippage_bps) == (10, 10) else "custom"
    for item in candidates:
        decision = item["decision_ms"]
        entry_ms = decision + FIVE
        reason = None
        if entry_ms + HOLD >= end_ms:
            reason = "incomplete_horizon_before_segment_end"
        elif entry_ms not in by_time:
            reason = "missing_arrival_bar"
        if reason is None:
            try:
                dec = _geometry(item["decision_close"], item["direction"], item["signal_stop"], fee, slip)
                arrival = _geometry(rows[by_time[entry_ms]][1], item["direction"], item["signal_stop"], fee, slip)
                quantity = min(dec["cap"], arrival["cap"])
                if quantity <= 0 or not math.isfinite(quantity):
                    raise ValueError("invalid_quantity")
                for direction, entry in zip((item["direction"], -item["direction"]), arrival["entries"]):
                    target = _target(entry, direction, quantity, 0, fee, slip)
                    if target <= 0 or direction * (target - rows[by_time[entry_ms]][1]) <= 0:
                        raise ValueError("invalid_entry_target")
            except ValueError as exc:
                reason = str(exc)
        if reason is not None:
            skipped[reason] += 1
            skip_records.append({"decision_ms": decision, "side": item["side"], "reason": reason})
            continue
        d = item["direction"]
        arms = [_arm(rows, by_time, funds, fund_times, entry_ms, quantity, direction,
                     entry, stop, risk, fee, slip, order)
                for direction, entry, stop, risk in zip((d, -d), arrival["entries"], arrival["stops"], arrival["risks"])]
        event = dict(item, symbol=symbol, entry_ms=entry_ms, deadline_ms=entry_ms + HOLD,
                     year=datetime.fromtimestamp(entry_ms / 1000, timezone.utc).year,
                     cost_regime=cost_regime, funding_order="primary" if order == "funding_first" else "alternative",
                     q_dec=dec["cap"], quantity=quantity, arrival_reduced=quantity < dec["cap"],
                     risk_budget_usdt=RISK, target_net_usdt=TARGET, event_equity_usdt=EQUITY,
                     stop_distance=arrival["distance"],
                     notional_cap_hit=quantity == arrival["notional_cap"] or quantity == dec["notional_cap"],
                     planned_risk_signal=quantity * arrival["risks"][0], planned_risk_mirror=quantity * arrival["risks"][1],
                     signal=arms[0], mirror=arms[1], delta_R=0.5 * (arms[0]["net_R"] - arms[1]["net_R"]))
        raw_entry = rows[by_time[entry_ms]][1]
        for horizon in (1, 2, 4):
            # Fixed close immediately before entry+h; never an exit-dependent mark.
            close = rows[by_time[entry_ms + horizon * HOUR - FIVE]][4]
            directional_return = d * (close / raw_entry - 1)
            event[f"direction_return_{horizon}h"] = directional_return
            event[f"direction_hit_{horizon}h"] = directional_return > 0
            event[f"direction_tie_{horizon}h"] = directional_return == 0
        events.append(event)
    return {"events": events, "skips": dict(skipped), "skip_records": skip_records,
            "signal_count": len(candidates), "valid_event_count": len(events),
            "data_quality": {"valid": True, "bar_count": len(rows), "funding_count": len(funds),
                             "continuous_5m": True, "account_status": "NOT_EVALUATED_UNKNOWN_METADATA"}}
