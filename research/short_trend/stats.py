"""Pure, pre-specified event statistics; no market IO or account simulation.

The shadow events have fixed equity and may overlap.  Their winning fraction
is never substituted for the user's executable-account 65% requirement.
Calendar bootstrap samples all symbols together, including empty weeks.  A
pooled sample uses the complete two-year calendar, not separate year strata.
Before any strategy replay, rejection is conservatively interpreted as
requiring agreement of both fixed block lengths and both funding orders.
Conflicting method/order verdicts remain insufficient; the better scenario
cannot be selected.  Even event support cannot pass unknown account gates.
"""
from __future__ import annotations

from datetime import datetime, timezone
import math
from typing import Iterable, Mapping

import numpy as np

from research.short_trend.preflight import EFFECTIVE_END_MS, utc_ms, validate_protocol

WEEK_MS = 7 * 24 * 60 * 60 * 1000
DAY_MS = 24 * 60 * 60 * 1000
SEED = 20261124
REPLICATES = 10000
ACCOUNT_NOT_EVALUATED = "NOT_EVALUATED_UNKNOWN_METADATA"
EVENT_SUPPORT = "SUPPORT_EVENT_RESEARCH_ONLY"
EVENT_REJECT = "REJECT_FIXED_EVENT_SPEC"
INSUFFICIENT = "INSUFFICIENT_EVIDENCE"
ORDERS = ("primary", "alternative")
REGIMES = ("normal", "stress")
_DEFAULT_PRIMARY = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
_START_MS = utc_ms("2024-01-01T00:00:00Z")


def _finite(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{label} must be a finite number")
    return result


def _direction(event: Mapping) -> int:
    arm = event["signal"]
    value = event.get("direction", event.get("sign", event.get("side")))
    if value is None:
        value = arm.get("direction", arm.get("sign", arm.get("side")))
    if isinstance(value, str):
        value = {"LONG": 1, "SHORT": -1, "BUY": 1, "SELL": -1}.get(value.upper())
    if isinstance(value, bool) or value not in (-1, 1):
        raise ValueError("Event must identify its signal direction as +/-1")
    return int(value)


def _normalise(events: Iterable[Mapping], protocol: Mapping | None = None) -> list[dict]:
    """Copy only result fields; reject timestamps before consuming PnL fields."""
    primary = tuple(protocol["primary_symbols"]) if protocol else _DEFAULT_PRIMARY
    exploratory = tuple(protocol["exploratory_symbols"]) if protocol else ("ZECUSDT",)
    risk_config = protocol["risk"] if protocol else {
        "initial_equity_usdt": 110.0, "planned_risk_fraction": 0.015,
        "planned_risk_cap_usdt": 5.0, "target_fraction": 0.01,
    }
    equity = float(risk_config["initial_equity_usdt"])
    expected_risk = min(equity * risk_config["planned_risk_fraction"],
                        risk_config["planned_risk_cap_usdt"])
    expected_target = equity * risk_config["target_fraction"]
    rows = []
    keys = set()
    for event in events:
        timestamp = event.get("entry_ms")
        if type(timestamp) is not int or not _START_MS <= timestamp < EFFECTIVE_END_MS:
            raise ValueError("Event timestamp is outside frozen evaluation years")
        symbol = event.get("symbol")
        if symbol not in primary + exploratory:
            raise ValueError("Unapproved event symbol")
        year = datetime.fromtimestamp(timestamp / 1000, timezone.utc).year
        if "year" in event and (type(event["year"]) is not int or event["year"] != year):
            raise ValueError("Event year does not match UTC entry timestamp")
        year_end = int(datetime(year + 1, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
        holding_minutes = protocol["signal"]["holding_minutes"] if protocol else 240
        if timestamp + holding_minutes * 60_000 >= year_end:
            raise ValueError("Event lacks its complete strictly pre-year-end horizon")
        order = event.get("funding_order", "primary")
        order = {
            "funding_first": "primary", "price_first": "alternative",
            "funding_before_unknown_stop_then_target": "primary",
            "unknown_stop_then_target_before_intrabar_funding": "alternative",
        }.get(order, order)
        regime = event.get("cost_regime", "normal")
        if order not in ORDERS or regime not in REGIMES:
            raise ValueError("Unknown funding order or cost regime")
        identity = (symbol, timestamp, order, regime)
        if identity in keys:
            raise ValueError("Duplicate paired event within one execution scenario")
        keys.add(identity)
        risk = _finite(event.get("risk_budget_usdt", expected_risk), "risk_budget_usdt")
        if risk <= 0 or not math.isclose(risk, expected_risk, rel_tol=1e-10, abs_tol=1e-10):
            raise ValueError("Shadow-event R must use the frozen fixed common risk budget")
        arms = {}
        for name in ("signal", "mirror"):
            arm = event[name]
            if "exit_ms" in arm and (type(arm["exit_ms"]) is not int
                                     or not timestamp <= arm["exit_ms"] < year_end):
                raise ValueError("Exit timestamp crosses its event evaluation year")
            pnl = _finite(arm["net_pnl_usdt"], f"{name}.net_pnl_usdt")
            net_r = _finite(arm["net_R"], f"{name}.net_R")
            if not math.isclose(pnl / risk, net_r, rel_tol=1e-8, abs_tol=1e-8):
                raise ValueError("net_R must equal net PnL divided by the common budget")
            costs = {}
            for dest, alternatives in (
                ("fill_price_pnl_usdt", ("price_pnl_usdt", "gross_pnl_usdt")),
                ("fee_usdt", ("fee_usdt", "fees_usdt")),
                ("funding_usdt", ("funding_usdt",)),
                ("slippage_diagnostic_usdt", ("slippage_usdt",)),
            ):
                value = next((arm[key] for key in alternatives if key in arm), None)
                costs[dest] = None if value is None else _finite(value, f"{name}.{dest}")
            if all(costs[key] is not None for key in (
                    "fill_price_pnl_usdt", "fee_usdt", "funding_usdt")):
                reconciled = (costs["fill_price_pnl_usdt"] - costs["fee_usdt"]
                              - costs["funding_usdt"])
                if not math.isclose(pnl, reconciled, rel_tol=1e-8, abs_tol=1e-8):
                    raise ValueError("PnL does not reconcile; do not deduct slippage twice")
            arms[name] = {"net_pnl_usdt": pnl, "net_R": net_r,
                          "exit_reason": str(arm.get("exit_reason", "UNKNOWN")).upper(),
                          **costs}
        delta = 0.5 * (arms["signal"]["net_R"] - arms["mirror"]["net_R"])
        if "delta_R" in event and not math.isclose(
                _finite(event["delta_R"], "delta_R"), delta, rel_tol=1e-8, abs_tol=1e-8):
            raise ValueError("Paired delta_R differs from its frozen half-difference")
        hits = {}
        provided = event.get("direction_hits", {})
        for horizon in ("1h", "2h", "4h"):
            hit = provided.get(horizon, event.get(f"direction_hit_{horizon}"))
            if hit is not None and type(hit) is not bool:
                raise ValueError("Direction hit values must be boolean or None")
            hits[horizon] = hit
        rows.append({"symbol": symbol, "entry_ms": timestamp, "year": year,
                     "direction": _direction(event), "cost_regime": regime,
                     "funding_order": order, "risk_budget_usdt": risk,
                     "target_net_usdt": _finite(event.get("target_net_usdt", expected_target),
                                                "target_net_usdt"),
                     "signal": arms["signal"], "mirror": arms["mirror"],
                     "delta_R": delta, "direction_hits": hits})
    return rows


def _ratio(num: float, den: float) -> float | None:
    return float(num / den) if den else None


def _arm_description(rows: list[dict], arm: str) -> dict:
    pnls = [row[arm]["net_pnl_usdt"] for row in rows]
    wins = [pnl for pnl in pnls if pnl > 0]
    losses = [pnl for pnl in pnls if pnl < 0]
    reasons = {}
    for row in rows:
        reason = row[arm]["exit_reason"]
        reasons[reason] = reasons.get(reason, 0) + 1
    time_pnls = [row[arm]["net_pnl_usdt"] for row in rows
                 if row[arm]["exit_reason"] == "TIME"]
    count = len(rows)
    risk_sum = sum(row["risk_budget_usdt"] for row in rows)
    average_win = _ratio(sum(wins), len(wins))
    average_loss = _ratio(sum(losses), len(losses))
    if average_win is not None and average_loss is not None:
        breakeven = -average_loss / (average_win - average_loss)
    else:
        breakeven = None
    costs = {}
    for key in ("fill_price_pnl_usdt", "fee_usdt", "funding_usdt", "slippage_diagnostic_usdt"):
        known = [row[arm][key] for row in rows if row[arm][key] is not None]
        costs[key] = {"total": sum(known) if known else None, "available_count": len(known)}
    return {
        "count": count, "net_pnl_usdt": sum(pnls), "common_risk_budget_sum_usdt": risk_sum,
        "mean_net_R": _ratio(sum(pnls), risk_sum), "net_win_rate": _ratio(len(wins), count),
        "win_count": len(wins), "loss_count": len(losses),
        "zero_pnl_count": count - len(wins) - len(losses),
        "profit_factor": _ratio(sum(wins), -sum(losses)),
        "profit_factor_no_losses": bool(wins) and not losses,
        "avg_win_usdt": average_win, "avg_loss_usdt": average_loss,
        "breakeven_net_win_rate": breakeven,
        "tp_exit_rate": _ratio(reasons.get("TP", 0), count),
        "target_achieved_rate": _ratio(sum(
            row[arm]["net_pnl_usdt"] >= row["target_net_usdt"] - 1e-8 for row in rows), count),
        "time_exit_rate": _ratio(reasons.get("TIME", 0), count),
        "time_mean_net_pnl_usdt": _ratio(sum(time_pnls), len(time_pnls)),
        "exit_reasons": reasons, "costs": costs,
        "slippage_is_embedded_in_fill_price_pnl": True,
    }


def _describe(rows: list[dict]) -> dict:
    signal = _arm_description(rows, "signal")
    risk_sum = signal["common_risk_budget_sum_usdt"]
    delta_num = sum(row["delta_R"] * row["risk_budget_usdt"] for row in rows)
    directions = {}
    for horizon in ("1h", "2h", "4h"):
        values = [row["direction_hits"][horizon] for row in rows
                  if row["direction_hits"][horizon] is not None]
        directions[horizon] = {"count": len(values), "hit_rate": _ratio(sum(values), len(values))}
    return {**signal, "mean_delta_R": _ratio(delta_num, risk_sum),
            "mirror": _arm_description(rows, "mirror"), "direction_hit_rates": directions,
            "account_winning_fraction_evaluated": False,
            "scope": "overlapping_fixed_equity_shadow_events_not_executable_account"}


def describe_events(events: Iterable[Mapping], protocol: Mapping | None = None) -> dict:
    """Describe one event collection; shadow win rates do not pass account gates."""
    return _describe(_normalise(events, protocol))


def _week_floor(timestamp: int) -> int:
    day = timestamp // DAY_MS
    # Unix epoch was Thursday; Monday index is (day + 3) % 7.
    return (day - (day + 3) % 7) * DAY_MS


def _block_indices(week_count: int, replicates: int, block_weeks: int, seed: int) -> np.ndarray:
    """One shared index array supplies both R and paired-delta estimates."""
    generator = np.random.default_rng(seed)
    if block_weeks == 1:
        return generator.integers(0, week_count, size=(replicates, week_count))
    block_count = (week_count + block_weeks - 1) // block_weeks
    starts = generator.integers(0, week_count, size=(replicates, block_count))
    offsets = np.arange(block_weeks)
    indices = (starts[:, :, None] + offsets[None, None, :]) % week_count
    return indices.reshape(replicates, -1)[:, :week_count]


def _interval(values: np.ndarray) -> list[float] | None:
    finite = values[np.isfinite(values)]
    if not finite.size:
        return None
    low, high = np.percentile(finite, [2.5, 97.5])
    return [float(low), float(high)]


def _bootstrap(rows: list[dict], start_ms: int, end_ms: int, *, replicates: int,
               seed: int, block_weeks: int) -> dict:
    first_week = _week_floor(start_ms)
    week_count = (_week_floor(end_ms - 1) - first_week) // WEEK_MS + 1
    # Columns are sums, never per-week means. Empty calendar weeks remain zeros.
    totals = np.zeros((week_count, 6), dtype=float)
    for row in rows:
        if not start_ms <= row["entry_ms"] < end_ms:
            raise ValueError("Bootstrap row is outside its declared period")
        index = (_week_floor(row["entry_ms"]) - first_week) // WEEK_MS
        risk = row["risk_budget_usdt"]
        totals[index] += (row["signal"]["net_pnl_usdt"], row["delta_R"] * risk,
                          risk, row["signal"]["net_pnl_usdt"] > 0, 1,
                          row["signal"]["net_pnl_usdt"] >= row["target_net_usdt"] - 1e-8)
    indices = _block_indices(week_count, replicates, block_weeks, seed)
    sampled = totals[indices].sum(axis=1)
    nonempty = sampled[:, 4] > 0
    risk_positive = sampled[:, 2] > 0
    net_r = np.full(replicates, np.nan)
    delta = np.full(replicates, np.nan)
    win = np.full(replicates, np.nan)
    target = np.full(replicates, np.nan)
    np.divide(sampled[:, 0], sampled[:, 2], out=net_r, where=risk_positive)
    np.divide(sampled[:, 1], sampled[:, 2], out=delta, where=risk_positive)
    np.divide(sampled[:, 3], sampled[:, 4], out=win, where=nonempty)
    np.divide(sampled[:, 5], sampled[:, 4], out=target, where=nonempty)
    metrics = _describe(rows)
    return {
        "replicates": replicates, "seed": seed, "block_weeks": block_weeks,
        "calendar_week_count": int(week_count),
        "occupied_week_count": int(np.count_nonzero(totals[:, 4])),
        "zero_event_week_count": int(np.count_nonzero(totals[:, 4] == 0)),
        "calendar_first_week_start_ms": first_week,
        "calendar_last_week_start_ms": first_week + (week_count - 1) * WEEK_MS,
        "zero_event_replica_fraction": float(1.0 - np.mean(nonempty)),
        "intervals_conditioned_on_nonempty_replicas": bool(np.any(~nonempty)),
        "net_R": {"point": metrics["mean_net_R"], "ci95": _interval(net_r)},
        "delta_R": {"point": metrics["mean_delta_R"], "ci95": _interval(delta)},
        "net_win_rate": {"point": metrics["net_win_rate"], "ci95": _interval(win)},
        "target_achieved_rate": {"point": metrics["target_achieved_rate"], "ci95": _interval(target)},
        "joint_net_R_delta_resampling": True,
        "estimator": "sum_sampled_net_pnl_or_delta_pnl_divided_by_sum_sampled_common_risk",
        "all_symbols_sampled_together": True,
    }


def _period(rows: list[dict], start_ms: int, end_ms: int, reps: int, seed: int) -> dict:
    return {"metrics": _describe(rows), "bootstrap": {
        "one_week": _bootstrap(rows, start_ms, end_ms, replicates=reps, seed=seed, block_weeks=1),
        "four_week": _bootstrap(rows, start_ms, end_ms, replicates=reps, seed=seed, block_weeks=4),
    }}


def _positive(value) -> bool:
    return value is not None and value > 0


def _method_verdict(result: dict, max_empty: float) -> str:
    if result["zero_event_replica_fraction"] > max_empty:
        return INSUFFICIENT
    net = result["net_R"]["ci95"]
    delta = result["delta_R"]["ci95"]
    if net is None or delta is None:
        return INSUFFICIENT
    if net[1] < 0 or delta[1] <= 0:
        return EVENT_REJECT
    if net[0] > 0 and delta[0] > 0:
        return EVENT_SUPPORT
    return INSUFFICIENT


def _order_decision(costs: dict, data_quality_ok: bool, max_empty: float) -> dict:
    normal = costs["normal"]
    stress = costs["stress"]
    methods = {name: _method_verdict(result, max_empty)
               for name, result in normal["pooled"]["bootstrap"].items()}
    annual = all(_positive(period["metrics"]["mean_net_R"])
                 and _positive(period["metrics"]["mean_delta_R"])
                 for period in normal["by_year"].values())
    leave_out = all(_positive(metrics["mean_net_R"]) and _positive(metrics["mean_delta_R"])
                    for metrics in normal["leave_one_symbol_out"].values())
    pressure = stress["pooled"]["metrics"]["mean_net_R"]
    stress_pass = pressure is not None and pressure >= 0
    checks = {"data_quality_complete": data_quality_ok,
              "both_normal_block_methods_positive_intervals": all(
                  verdict == EVENT_SUPPORT for verdict in methods.values()),
              "normal_each_year_positive_net_R_and_delta": annual,
              "normal_leave_any_primary_symbol_out_positive_net_R_and_delta": leave_out,
              "stress_pooled_mean_net_R_nonnegative": stress_pass}
    if not data_quality_ok:
        verdict = INSUFFICIENT
    elif all(value == EVENT_REJECT for value in methods.values()):
        verdict = EVENT_REJECT
    elif all(checks.values()):
        verdict = EVENT_SUPPORT
    else:
        verdict = INSUFFICIENT
    return {"event_verdict": verdict, "checks": checks, "block_method_verdicts": methods,
            "block_method_verdicts_differ": len(set(methods.values())) != 1,
            "reasons": [key for key, passed in checks.items() if not passed],
            "annual_and_leave_out_gates_cost_regime": "normal"}


def summarize_events(events: Iterable[Mapping], protocol: Mapping, *,
                     data_quality_ok: bool = True,
                     account_status: str = ACCOUNT_NOT_EVALUATED,
                     bootstrap_replicates: int | None = None) -> dict:
    """Return event evidence and its frozen gates without fabricating an account.

    ``bootstrap_replicates`` exists for inexpensive synthetic tests. Production
    callers use the frozen default 10000; an override is prominently marked.
    """
    validate_protocol(protocol)
    if type(data_quality_ok) is not bool:
        raise ValueError("Data-quality gate must be an explicit bool")
    stats = protocol["statistics"]
    if (stats["bootstrap_replicates"] != REPLICATES or stats["bootstrap_seed"] != SEED):
        raise ValueError("Frozen bootstrap seed or replicate count changed")
    reps = REPLICATES if bootstrap_replicates is None else bootstrap_replicates
    if type(reps) is not int or reps <= 0:
        raise ValueError("Positive integer bootstrap replicate count required")
    rows = _normalise(events, protocol)
    primary = tuple(protocol["primary_symbols"])
    main = [row for row in rows if row["symbol"] in primary]
    exploration = [row for row in rows if row["symbol"] not in primary]
    periods = [(str(datetime.fromisoformat(item["start_utc"].replace("Z", "+00:00")).year),
                utc_ms(item["start_utc"]), utc_ms(item["end_utc"]))
               for item in protocol["segments"]]
    scenarios = {}
    exploration_summaries = {}
    decisions = {}
    for order in ORDERS:
        scenarios[order] = {}
        exploration_summaries[order] = {}
        for regime in REGIMES:
            selected = [row for row in main
                        if row["funding_order"] == order and row["cost_regime"] == regime]
            result = {
                "pooled": _period(selected, periods[0][1], periods[-1][2], reps, SEED),
                "by_year": {
                    year: _period([row for row in selected if start <= row["entry_ms"] < end],
                                  start, end, reps, SEED)
                    for year, start, end in periods},
                "by_symbol": {symbol: _describe([row for row in selected if row["symbol"] == symbol])
                              for symbol in primary},
                "by_direction": {name: _describe([row for row in selected if row["direction"] == side])
                                 for name, side in (("long", 1), ("short", -1))},
                "leave_one_symbol_out": {
                    symbol: _describe([row for row in selected if row["symbol"] != symbol])
                    for symbol in primary},
            }
            scenarios[order][regime] = result
            exploration_summaries[order][regime] = _describe([
                row for row in exploration
                if row["funding_order"] == order and row["cost_regime"] == regime])
        decisions[order] = _order_decision(
            scenarios[order], data_quality_ok, stats["maximum_zero_trade_bootstrap_fraction"])
    order_verdicts = [decisions[order]["event_verdict"] for order in ORDERS]
    if all(value == EVENT_REJECT for value in order_verdicts):
        event_verdict = EVENT_REJECT
    elif all(value == EVENT_SUPPORT for value in order_verdicts):
        event_verdict = EVENT_SUPPORT
    else:
        event_verdict = INSUFFICIENT
    if event_verdict == EVENT_REJECT:
        overall = EVENT_REJECT
    else:
        overall = "INSUFFICIENT_EXECUTION_EVIDENCE"
    return {
        "strategy_id": protocol["strategy_id"],
        "scope": "known_years_shadow_event_recheck_not_independent_validation",
        "event_verdict": event_verdict, "account_status": account_status,
        "overall_verdict": overall,
        "account_65_percent_goal_evaluated": False,
        "account_acceptance_allowed": False,
        "primary_symbols": list(primary), "exploratory_events_excluded_from_main": len(exploration),
        "event_count_including_scenario_repetitions": len(rows),
        "bootstrap_replicates": reps, "bootstrap_seed": SEED,
        "bootstrap_test_override": bootstrap_replicates is not None,
        "pooled_calendar": "single_complete_calendar_no_year_stratification",
        "scenarios": scenarios, "scenario_decisions": decisions,
        "execution_order_verdict_sensitive": len(set(order_verdicts)) != 1,
        "exploratory_only": exploration_summaries,
        "limitations": [
            "Event winning fractions are not executable-account winning fractions.",
            "Overlapping events are correlated; both pre-specified calendar-block methods are reported.",
            "Unknown historical execution metadata prevents account acceptance.",
            "Both funding-order scenarios are approximations, not strict pathwise bounds.",
            "Known years are historical rechecks, not pristine independent validation.",
        ],
    }
