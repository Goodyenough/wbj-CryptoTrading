"""Independent arithmetic, raw-path and boundary reconciliation of event output."""
from __future__ import annotations

import math

FIVE = 300_000
HOUR = 3_600_000
END = 1_767_225_600_000


def audit_event_batch(events: list[dict], bars: list[list], protocol: dict) -> dict:
    raw = {row[0]: row for row in bars}
    checks = 0

    def require(condition: bool, message: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    def equal(actual: float, expected: float, message: str) -> None:
        require(math.isfinite(actual) and math.isfinite(expected)
                and math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-8), message)

    for event in events:
        costs = protocol["cost_regimes"][event["cost_regime"]]
        fee, slip = costs["fee_bps_per_side"] / 10000, costs["slippage_bps_per_side"] / 10000
        q, budget, direction = event["quantity"], event["risk_budget_usdt"], event["direction"]
        entry_ms, deadline = event["entry_ms"], event["deadline_ms"]
        require(event["decision_ms"] + FIVE == entry_ms, "Execution latency mismatch")
        require(deadline == entry_ms + 4 * HOUR and deadline < END, "Invalid horizon")
        equal(budget, 1.65, "Wrong fixed budget")
        equal(event["target_net_usdt"], 1.1, "Wrong fixed net goal")
        require(0 < q <= event["q_dec"] + 1e-10, "Arrival increased quantity")
        stop = event["breakout_level"] - direction * event["atr"]
        equal(event["signal"]["stop_price"], stop, "Structure stop moved")
        raw_entry = raw[entry_ms][1]
        risks = []
        fills = []
        for name, sign in (("signal", direction), ("mirror", -direction)):
            trade = event[name]
            entry, exit_fill, exit_raw = trade["entry_price"], trade["exit_price"], trade["exit_raw"]
            equal(trade["quantity"], q, "Arms have unequal quantities")
            require(trade["direction"] == sign, "Wrong arm sign")
            equal(entry, raw_entry * (1 + sign * slip), "Wrong entry slippage")
            equal(exit_fill, exit_raw * (1 - sign * slip), "Wrong exit slippage")
            equal(trade["gross_pnl_usdt"], sign * q * (exit_fill - entry), "Fill PnL mismatch")
            equal(trade["fees_usdt"], fee * q * (entry + exit_fill), "Fee mismatch")
            equal(trade["raw_price_pnl_usdt"] - trade["gross_pnl_usdt"],
                  trade["slippage_usdt"], "Slippage counted incorrectly")
            funding_sum = 0.0
            for funding in trade["funding_events"]:
                require(entry_ms < funding["time_ms"] <= trade["exit_ms"] < END,
                        "Funding outside held interval")
                require(funding["mark_proxy_ms"] <= funding["time_ms"]
                        < funding["mark_proxy_ms"] + FIVE, "Future/stale mark proxy")
                amount = sign * q * funding["mark_price"] * funding["rate"]
                equal(funding["amount_usdt"], amount, "Funding sign or amount mismatch")
                funding_sum += amount
            equal(trade["funding_usdt"], funding_sum, "Funding ledger mismatch")
            equal(trade["net_pnl_usdt"], trade["gross_pnl_usdt"] - trade["fees_usdt"] - funding_sum,
                  "Net PnL mismatch")
            equal(trade["net_R"], trade["net_pnl_usdt"] / budget, "R denominator mismatch")
            require(entry_ms <= trade["exit_ms"] <= deadline, "Exit outside horizon")
            require(q * entry <= 220 + 1e-8, "Notional cap exceeded")
            stop_fill = trade["stop_price"] * (1 - sign * slip)
            unit_risk = sign * (entry - stop_fill) + fee * (entry + stop_fill) + .0005 * entry
            risks.append(unit_risk)
            fills.append(entry)
            equal(trade["unit_risk_usdt"], unit_risk, "Unit risk mismatch")
            equal(trade["planned_risk_usdt"], q * unit_risk, "Planned risk mismatch")
            require(q * unit_risk <= budget + 1e-8, "Planned risk cap exceeded")
            exit_bucket = trade["exit_ms"] // FIVE * FIVE
            candle = raw[exit_bucket]
            if trade["exit_time_upper_bound"]:
                require(trade["exit_ms"] == candle[6], "Intrabar exit timestamp not upper bound")
                require(candle[3] - 1e-8 <= exit_raw <= candle[2] + 1e-8,
                        "Invented intrabar raw fill outside OHLC")
            elif trade["exit_reason"] == "TIME":
                require(trade["exit_ms"] == deadline, "Time exit at wrong time")
                equal(exit_raw, candle[1], "Time exit not at observed open")
            elif trade["exit_reason"] == "SL":
                equal(exit_raw, candle[1], "Gap stop not at observed open")
            elif trade.get("cashflow_target_at_open"):
                equal(exit_raw, candle[1], "Cashflow-induced target not at first observed open")
            if trade["exit_reason"] == "TP":
                require(trade["net_pnl_usdt"] >= 1.1 - 1e-7, "TP did not achieve net target")
        equal(direction * (fills[0] - event["signal"]["stop_price"]),
              -direction * (fills[1] - event["mirror"]["stop_price"]), "Unmatched mirror distance")
        expected_q = min(event["q_dec"], budget / max(risks), 220 / max(fills))
        equal(q, expected_q, "Arrival quantity differs from shared cap")
        equal(event["delta_R"], (event["signal"]["net_R"] - event["mirror"]["net_R"]) / 2,
              "Paired delta mismatch")
        for horizon in (1, 2, 4):
            close = raw[entry_ms + horizon * HOUR - FIVE][4]
            expected_return = direction * (close / raw_entry - 1)
            equal(event[f"direction_return_{horizon}h"], expected_return, "Direction mark mismatch")
            require(event[f"direction_hit_{horizon}h"] == (expected_return > 0), "Wrong direction hit")
    return {"events_audited": len(events), "arithmetic_and_path_assertions": checks,
            "violations": 0, "account_execution_proven": False}
