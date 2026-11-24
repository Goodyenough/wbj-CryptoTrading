"""Synthetic cross-module and unit-invariance checks; no market/cache IO.

These properties are independent of any observed strategy result: changing
the quote-price unit cannot change dollar outcomes, and a flat post-entry
path cannot create a directional edge merely from fees or slippage.
"""
import copy
import json
import unittest

from research.short_trend import engine
from research.short_trend.audit import audit_event_batch
from research.short_trend.preflight import utc_ms
from research.short_trend.run import (
    flat_event, locked_protocol, monthly_events, render_report, validate_event_bounds,
)
from research.short_trend.stats import describe_events, summarize_events


START = utc_ms("2024-01-01T00:00:00Z")
END = utc_ms("2024-01-02T00:00:00Z")
SIGNAL_HOUR = START + engine.HOUR
ARRIVAL = SIGNAL_HOUR + engine.HOUR + engine.FIVE


def artificial_bars(*, scale=1.0, reflected=False):
    """Constant range, one explicit break, then a constant post-arrival path."""
    result = []
    for timestamp in range(engine.WARMUP_MS, END, engine.FIVE):
        if timestamp < SIGNAL_HOUR:
            o, high, low, close = 100.0, 100.2, 99.8, 100.0
        elif timestamp < SIGNAL_HOUR + engine.HOUR:
            o, high, low, close = 100.0, 101.2, 99.8, 101.0
        else:
            o, high, low, close = 101.0, 101.1, 100.9, 101.0
        if reflected:
            o, high, low, close = 200 - o, 200 - low, 200 - high, 200 - close
        result.append([timestamp, o * scale, high * scale, low * scale, close * scale,
                       1.0, timestamp + engine.FIVE - 1])
    return result


def replay(*, scale=1.0, reflected=False, fee=5, slip=3,
           order="funding_first", with_funding=False, symbol="BTCUSDT"):
    funding = []
    if with_funding:
        funding = [{"time_ms": ARRIVAL + engine.HOUR + 1,
                    "mark_proxy_ms": ARRIVAL + engine.HOUR,
                    "mark_price": (99.0 if reflected else 101.0) * scale,
                    "rate": 0.0001, "funding_interval_hours": 8}]
    return engine.event_pairs(symbol, artificial_bars(scale=scale, reflected=reflected),
                              funding, START, END, fee, slip, order=order)


class FinancialMetamorphicTests(unittest.TestCase):
    def test_quote_unit_scaling_preserves_signals_risk_and_dollar_outcomes(self):
        baseline = replay(with_funding=True)
        self.assertGreater(len(baseline["events"]), 0)
        self.assertEqual(baseline["events"][0]["entry_ms"], ARRIVAL)
        for scale in (0.01, 7.0, 10000.0):
            result = replay(scale=scale, with_funding=True)
            self.assertEqual(result["signal_count"], baseline["signal_count"])
            self.assertEqual(result["skips"], baseline["skips"])
            self.assertEqual(len(result["events"]), len(baseline["events"]))
            for original, scaled in zip(baseline["events"], result["events"]):
                with self.subTest(scale=scale, entry=original["entry_ms"]):
                    self.assertEqual(scaled["decision_ms"], original["decision_ms"])
                    self.assertEqual(scaled["entry_ms"], original["entry_ms"])
                    self.assertEqual(scaled["direction"], original["direction"])
                    self.assertAlmostEqual(scaled["quantity"] * scale, original["quantity"], places=9)
                    self.assertAlmostEqual(scaled["delta_R"], original["delta_R"], places=9)
                    for arm in ("signal", "mirror"):
                        self.assertEqual(scaled[arm]["exit_ms"], original[arm]["exit_ms"])
                        self.assertEqual(scaled[arm]["exit_reason"], original[arm]["exit_reason"])
                        for key in ("net_pnl_usdt", "net_R", "fee_usdt", "slippage_usdt", "funding_usdt"):
                            self.assertAlmostEqual(scaled[arm][key], original[arm][key], places=9)

    def test_no_drift_has_zero_costless_edge_and_exact_roundtrip_cost_drag(self):
        free = replay(fee=0, slip=0)["events"][0]
        charged = replay()["events"][0]
        for name in ("signal", "mirror"):
            self.assertEqual(free[name]["exit_reason"], "TIME")
            self.assertAlmostEqual(free[name]["net_pnl_usdt"], 0, places=12)
            self.assertEqual(charged[name]["exit_reason"], "TIME")
            self.assertLess(charged[name]["net_pnl_usdt"], 0)
        self.assertAlmostEqual(free["delta_R"], 0, places=12)
        self.assertAlmostEqual(charged["delta_R"], 0, places=12)
        # Each arm buys/sells the same flat raw price twice. Fees and adverse
        # slippage each enter twice, rather than charging slippage a second time.
        expected_pair_loss = -4 * charged["quantity"] * 101.0 * (0.0005 + 0.0003)
        actual_pair_pnl = charged["signal"]["net_pnl_usdt"] + charged["mirror"]["net_pnl_usdt"]
        self.assertAlmostEqual(actual_pair_pnl, expected_pair_loss, places=10)

    def test_price_reflection_reverses_first_break_without_changing_its_time(self):
        upward = replay()["events"]
        downward = replay(reflected=True)["events"]
        self.assertEqual(len(upward), len(downward))
        self.assertGreater(len(upward), 0)
        for long_event, short_event in zip(upward, downward):
            self.assertEqual(long_event["decision_ms"], short_event["decision_ms"])
            self.assertEqual(long_event["direction"], -short_event["direction"])
            self.assertAlmostEqual(long_event["atr"], short_event["atr"], places=10)
            for event in (long_event, short_event):
                self.assertAlmostEqual(event["delta_R"], 0, places=10)
                self.assertLess(event["signal"]["net_pnl_usdt"], 0)

    def test_swapping_pair_labels_negates_relative_direction_statistic(self):
        original = replay(with_funding=True)["events"][0]
        swapped = copy.deepcopy(original)
        swapped["signal"], swapped["mirror"] = swapped["mirror"], swapped["signal"]
        swapped["direction"] *= -1
        swapped["delta_R"] *= -1
        normal = describe_events([original])
        reverse = describe_events([swapped])
        self.assertAlmostEqual(normal["mean_delta_R"], -reverse["mean_delta_R"], places=12)
        self.assertAlmostEqual(normal["mean_net_R"], reverse["mirror"]["mean_net_R"], places=12)


class SyntheticPipelineTests(unittest.TestCase):
    def test_engine_runner_statistics_and_report_share_one_result_schema(self):
        config = locked_protocol()  # Only the fixed metadata JSON is opened.
        events = []
        for cost, assumptions in config["cost_regimes"].items():
            for order_label, order in (("primary", "funding_first"), ("alternative", "price_first")):
                for symbol in config["primary_symbols"]:
                    result = replay(fee=assumptions["fee_bps_per_side"],
                                    slip=assumptions["slippage_bps_per_side"],
                                    order=order, symbol=symbol)
                    self.assertTrue(result["data_quality"]["valid"])
                    audit = audit_event_batch(result["events"], artificial_bars(), config)
                    self.assertEqual(audit["events_audited"], len(result["events"]))
                    self.assertEqual(audit["violations"], 0)
                    self.assertGreater(audit["arithmetic_and_path_assertions"], 0)
                    self.assertFalse(audit["account_execution_proven"])
                    for event in result["events"]:
                        self.assertEqual(event["cost_regime"], cost)
                        self.assertEqual(event["funding_order"], order_label)
                        validate_event_bounds(event, START, END)
                        row = flat_event(event)
                        self.assertTrue(all(not isinstance(v, (dict, list, tuple)) for v in row.values()))
                        self.assertEqual(row["signal_net_R"], event["signal"]["net_R"])
                        self.assertEqual(row["direction_hit_4h"], event["direction_hit_4h"])
                        self.assertIn("signal_cashflow_target_at_open", row)
                        events.append(event)
        self.assertGreater(len(events), 0)
        monthly = monthly_events(events)
        self.assertEqual(sum(row["events"] for row in monthly), len(events))
        self.assertAlmostEqual(sum(row["fee_usdt_sum_diagnostic_not_account_pnl"] for row in monthly),
                               sum(event["signal"]["fee_usdt"] for event in events), places=10)
        summary = summarize_events(events, config, bootstrap_replicates=50)
        self.assertFalse(summary["account_acceptance_allowed"])
        self.assertFalse(summary["account_65_percent_goal_evaluated"])
        report = render_report(events, summary, {"primary_symbols": config["primary_symbols"]})
        self.assertIn(summary["event_verdict"], report)
        self.assertIn(summary["overall_verdict"], report)
        self.assertIn("账户层未评估", report)
        json.dumps({"summary": summary, "events": events, "monthly": monthly}, allow_nan=False)

    def test_independent_raw_path_audit_accepts_funding_and_scaled_quote_units(self):
        config = locked_protocol()
        for scale in (0.01, 1.0, 10000.0):
            events = replay(scale=scale, with_funding=True)["events"]
            audit = audit_event_batch(events, artificial_bars(scale=scale), config)
            self.assertEqual(audit["violations"], 0)
            self.assertGreater(audit["arithmetic_and_path_assertions"], 0)


if __name__ == "__main__":
    unittest.main()
