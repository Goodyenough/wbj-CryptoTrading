"""Synthetic-only tests of frozen calendar statistics and conclusion gates."""
import copy
import json
from pathlib import Path
import unittest

import numpy as np

from research.short_trend.preflight import EFFECTIVE_END_MS, utc_ms
from research.short_trend.stats import (
    ACCOUNT_NOT_EVALUATED, EVENT_REJECT, EVENT_SUPPORT, INSUFFICIENT,
    WEEK_MS, _block_indices, _bootstrap, _method_verdict, _normalise, _week_floor,
    describe_events, summarize_events,
)


CONFIG = json.loads((Path(__file__).parents[1] / "research/short_trend/protocol.json").read_bytes())
START = utc_ms("2024-01-01T00:00:00Z")
END = utc_ms("2025-01-01T00:00:00Z")
RISK = 1.65


def event(timestamp=START, *, symbol="BTCUSDT", net_r=0.5, mirror_r=-0.5,
          order="primary", regime="normal", direction=1, reason="TP"):
    def arm(value):
        pnl = value * RISK
        return {"net_pnl_usdt": pnl, "net_R": value, "exit_reason": reason,
                "price_pnl_usdt": pnl + 0.03 + 0.02, "fee_usdt": 0.03,
                "funding_usdt": 0.02, "slippage_usdt": 0.01}
    return {"symbol": symbol, "entry_ms": timestamp, "direction": direction,
            "risk_budget_usdt": RISK, "target_net_usdt": 1.1,
            "cost_regime": regime, "funding_order": order,
            "signal": arm(net_r), "mirror": arm(mirror_r),
            "delta_R": 0.5 * (net_r - mirror_r),
            "direction_hits": {"1h": True, "2h": None, "4h": False}}


def complete_positive_events():
    rows = []
    for order in ("primary", "alternative"):
        for regime in ("normal", "stress"):
            for year in (2024, 2025):
                start = utc_ms(f"{year}-01-01T00:00:00Z")
                for week in range(45):
                    for number, symbol in enumerate(CONFIG["primary_symbols"]):
                        rows.append(event(start + week * WEEK_MS + number * 300_000,
                                          symbol=symbol, order=order, regime=regime,
                                          net_r=0.8, mirror_r=-0.4))
    return rows


class CalendarBootstrapTests(unittest.TestCase):
    def test_week_floor_uses_utc_monday(self):
        self.assertEqual(_week_floor(utc_ms("2025-01-01T00:00:00Z")),
                         utc_ms("2024-12-30T00:00:00Z"))
        self.assertEqual(_week_floor(utc_ms("2024-01-07T23:59:59Z")), START)

    def test_zero_event_weeks_are_retained(self):
        rows = _normalise([event(START)])
        result = _bootstrap(rows, START, START + 10 * WEEK_MS,
                            replicates=500, seed=20261124, block_weeks=1)
        self.assertEqual(result["calendar_week_count"], 10)
        self.assertEqual(result["occupied_week_count"], 1)
        self.assertEqual(result["zero_event_week_count"], 9)
        self.assertGreater(result["zero_event_replica_fraction"], 0.1)
        self.assertTrue(result["intervals_conditioned_on_nonempty_replicas"])

    def test_event_weighting_does_not_average_week_means(self):
        rows = [event(START, net_r=1, mirror_r=-1)]
        rows += [event(START + WEEK_MS + index * 300_000, net_r=-1, mirror_r=1)
                 for index in range(9)]
        result = _bootstrap(_normalise(rows), START, START + 2 * WEEK_MS,
                            replicates=100, seed=20261124, block_weeks=1)
        self.assertAlmostEqual(result["net_R"]["point"], -0.8)
        self.assertAlmostEqual(result["delta_R"]["point"], -0.8)
        self.assertNotEqual(result["net_R"]["point"], 0)

    def test_cross_symbol_covariance_preserved_and_joint_delta_same_samples(self):
        rows = []
        for week in range(8):
            for symbol in CONFIG["primary_symbols"]:
                value = 1 if week % 2 == 0 else -1
                # mirror=0 => delta is exactly half of signal R, in every replica.
                rows.append(event(START + week * WEEK_MS, symbol=symbol,
                                  net_r=value, mirror_r=0))
        result = _bootstrap(_normalise(rows), START, START + 8 * WEEK_MS,
                            replicates=1000, seed=20261124, block_weeks=1)
        self.assertTrue(result["all_symbols_sampled_together"])
        self.assertTrue(result["joint_net_R_delta_resampling"])
        np.testing.assert_allclose(result["delta_R"]["ci95"],
                                   np.array(result["net_R"]["ci95"]) / 2)
        single = _bootstrap(_normalise([row for row in rows if row["symbol"] == "BTCUSDT"]),
                            START, START + 8 * WEEK_MS, replicates=1000,
                            seed=20261124, block_weeks=1)
        np.testing.assert_allclose(result["net_R"]["ci95"], single["net_R"]["ci95"])

    def test_seed_is_reproducible_and_fixed_four_week_blocks_wrap_and_truncate(self):
        first = _block_indices(7, 8, 4, 20261124)
        second = _block_indices(7, 8, 4, 20261124)
        np.testing.assert_array_equal(first, second)
        self.assertEqual(first.shape, (8, 7))
        for block in (first[:, :4], first[:, 4:]):
            np.testing.assert_array_equal(np.diff(block, axis=1) % 7,
                                          np.ones((8, block.shape[1] - 1), dtype=int))
        self.assertTrue(np.any(np.diff(first[:, :4], axis=1) < 0))

    def test_empty_bootstrap_has_no_fabricated_zero_return_or_win_rate(self):
        result = _bootstrap([], START, END, replicates=20, seed=20261124, block_weeks=4)
        self.assertIsNone(result["net_R"]["point"])
        self.assertIsNone(result["net_R"]["ci95"])
        self.assertIsNone(result["net_win_rate"]["point"])
        self.assertEqual(result["zero_event_replica_fraction"], 1)


class ResultDescriptionsTests(unittest.TestCase):
    def test_costs_are_not_double_deducted_and_wins_are_distinct_from_target(self):
        rows = [event(net_r=0.1, reason="TIME"),
                event(START + 300_000, net_r=-0.5, reason="SL")]
        result = describe_events(rows)
        self.assertEqual(result["net_win_rate"], 0.5)
        self.assertEqual(result["target_achieved_rate"], 0)
        self.assertEqual(result["tp_exit_rate"], 0)
        self.assertEqual(result["time_exit_rate"], 0.5)
        self.assertAlmostEqual(result["net_pnl_usdt"], -0.4 * RISK)
        self.assertAlmostEqual(result["costs"]["fee_usdt"]["total"], 0.06)
        self.assertAlmostEqual(result["costs"]["slippage_diagnostic_usdt"]["total"], 0.02)
        self.assertAlmostEqual(result["profit_factor"], 0.2)
        self.assertAlmostEqual(result["breakeven_net_win_rate"], 5 / 6)
        self.assertFalse(result["account_winning_fraction_evaluated"])
        self.assertEqual(result["direction_hit_rates"]["1h"]["hit_rate"], 1)
        self.assertEqual(result["direction_hit_rates"]["2h"]["count"], 0)

    def test_reject_protected_timestamp_before_consuming_pnl(self):
        row = {"entry_ms": EFFECTIVE_END_MS, "symbol": "BTCUSDT"}
        with self.assertRaisesRegex(ValueError, "timestamp"):
            describe_events([row])

    def test_horizon_and_exit_cannot_borrow_next_year(self):
        row = event(END - 4 * 60 * 60 * 1000)
        with self.assertRaisesRegex(ValueError, "horizon"):
            describe_events([row])
        row = event(END - 5 * 60 * 60 * 1000)
        row["signal"]["exit_ms"] = END
        with self.assertRaisesRegex(ValueError, "Exit timestamp"):
            describe_events([row])

    def test_inconsistent_R_delta_risk_or_costs_fail_closed(self):
        for key, value in (("risk_budget_usdt", 5), ("delta_R", 9), ("year", 2025)):
            row = event()
            row[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                describe_events([row])
        row = event()
        row["signal"]["net_R"] = 2
        with self.assertRaises(ValueError):
            describe_events([row])
        row = event()
        row["signal"]["price_pnl_usdt"] += 1
        with self.assertRaises(ValueError):
            describe_events([row])

    def test_duplicate_pair_in_same_scenario_is_rejected(self):
        row = event()
        with self.assertRaises(ValueError):
            describe_events([row, row])

    def test_engine_sign_schema_and_fee_alias_are_supported(self):
        row = event(direction=-1)
        del row["direction"]
        row["signal"]["sign"] = -1
        row["signal"]["fees_usdt"] = row["signal"].pop("fee_usdt")
        row["signal"]["gross_pnl_usdt"] = row["signal"].pop("price_pnl_usdt")
        result = describe_events([row])
        self.assertAlmostEqual(result["mean_net_R"], 0.5)


class FrozenDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = complete_positive_events()
        cls.positive = summarize_events(cls.rows, CONFIG, bootstrap_replicates=100)

    def test_positive_event_cannot_satisfy_unknown_account_or_65_percent_goal(self):
        result = self.positive
        self.assertEqual(result["event_verdict"], EVENT_SUPPORT)
        self.assertEqual(result["account_status"], ACCOUNT_NOT_EVALUATED)
        self.assertEqual(result["overall_verdict"], "INSUFFICIENT_EXECUTION_EVIDENCE")
        self.assertFalse(result["account_65_percent_goal_evaluated"])
        self.assertFalse(result["account_acceptance_allowed"])

    def test_calendar_pooled_has_one_cross_year_week_not_two_strata(self):
        result = self.positive["scenarios"]["primary"]["normal"]
        pooled = result["pooled"]["bootstrap"]["one_week"]
        years = result["by_year"]
        annual_count = sum(year["bootstrap"]["one_week"]["calendar_week_count"]
                           for year in years.values())
        self.assertEqual(pooled["calendar_week_count"], 105)
        self.assertEqual(annual_count, 106)
        self.assertEqual(pooled["seed"], 20261124)
        self.assertEqual(result["pooled"]["bootstrap"]["four_week"]["block_weeks"], 4)

    def test_zec_is_exploratory_and_cannot_rescue_main_result(self):
        rows = copy.deepcopy(self.rows)
        for row in rows:
            for arm in ("signal", "mirror"):
                value = -0.5 if arm == "signal" else 0.5
                row[arm]["net_R"] = value
                row[arm]["net_pnl_usdt"] = value * RISK
                row[arm]["price_pnl_usdt"] = value * RISK + 0.05
            row["delta_R"] = -0.5
        zec = []
        for order in ("primary", "alternative"):
            for regime in ("normal", "stress"):
                for index in range(100):
                    zec.append(event(START + index * 300_000, symbol="ZECUSDT",
                                     net_r=100, mirror_r=-100, order=order, regime=regime))
        result = summarize_events(rows + zec, CONFIG, bootstrap_replicates=100)
        self.assertEqual(result["event_verdict"], EVENT_REJECT)
        self.assertEqual(result["exploratory_events_excluded_from_main"], 400)
        self.assertLess(result["scenarios"]["primary"]["normal"]["pooled"]["metrics"]["mean_net_R"], 0)
        self.assertGreater(result["exploratory_only"]["primary"]["normal"]["mean_net_R"], 0)

    def test_missing_data_blocks_support_instead_of_dropping_bad_coin(self):
        result = summarize_events(self.rows, CONFIG, data_quality_ok=False, bootstrap_replicates=50)
        self.assertEqual(result["event_verdict"], INSUFFICIENT)

    def test_missing_funding_scenario_is_insufficient(self):
        rows = [row for row in self.rows if row["funding_order"] == "primary"]
        result = summarize_events(rows, CONFIG, bootstrap_replicates=50)
        self.assertEqual(result["event_verdict"], INSUFFICIENT)
        self.assertTrue(result["execution_order_verdict_sensitive"])

    def test_zero_delta_rejects_even_with_all_winning_signal_arms(self):
        rows = copy.deepcopy(self.rows)
        for row in rows:
            row["mirror"] = copy.deepcopy(row["signal"])
            row["delta_R"] = 0
        result = summarize_events(rows, CONFIG, bootstrap_replicates=50)
        self.assertEqual(result["event_verdict"], EVENT_REJECT)

    def test_negative_stress_prevents_support_without_extra_subgroup_stress_gates(self):
        rows = copy.deepcopy(self.rows)
        for row in rows:
            if row["cost_regime"] == "stress":
                row["signal"]["net_R"] = -0.1
                row["signal"]["net_pnl_usdt"] = -0.1 * RISK
                row["signal"]["price_pnl_usdt"] = -0.1 * RISK + 0.05
                row["delta_R"] = 0.15
        result = summarize_events(rows, CONFIG, bootstrap_replicates=50)
        self.assertEqual(result["event_verdict"], INSUFFICIENT)
        self.assertFalse(result["scenario_decisions"]["primary"]["checks"]["stress_pooled_mean_net_R_nonnegative"])

    def test_output_is_strict_json_without_nan_or_infinity(self):
        json.dumps(self.positive, allow_nan=False)

    def test_frozen_interval_boundaries_and_empty_replica_threshold(self):
        def result(net, delta, empty=0):
            return {"zero_event_replica_fraction": empty,
                    "net_R": {"ci95": net}, "delta_R": {"ci95": delta}}
        self.assertEqual(_method_verdict(result([0, 1], [0.1, 1]), 0.01), INSUFFICIENT)
        self.assertEqual(_method_verdict(result([-1, 0], [0.1, 1]), 0.01), INSUFFICIENT)
        self.assertEqual(_method_verdict(result([0.1, 1], [-1, 0]), 0.01), EVENT_REJECT)
        self.assertEqual(_method_verdict(result([0.1, 1], [0.1, 1], 0.01), 0.01), EVENT_SUPPORT)
        self.assertEqual(_method_verdict(result([0.1, 1], [0.1, 1], 0.011), 0.01), INSUFFICIENT)

    def test_annual_and_leave_one_symbol_out_gates_are_not_skipped(self):
        result = copy.deepcopy(self.positive)
        from research.short_trend.stats import _order_decision
        normal = result["scenarios"]["primary"]["normal"]
        normal["by_year"]["2024"]["metrics"]["mean_net_R"] = 0
        decision = _order_decision(result["scenarios"]["primary"], True, 0.01)
        self.assertEqual(decision["event_verdict"], INSUFFICIENT)
        self.assertFalse(decision["checks"]["normal_each_year_positive_net_R_and_delta"])
        normal["by_year"]["2024"]["metrics"]["mean_net_R"] = 0.8
        normal["leave_one_symbol_out"]["BTCUSDT"]["mean_delta_R"] = 0
        decision = _order_decision(result["scenarios"]["primary"], True, 0.01)
        self.assertEqual(decision["event_verdict"], INSUFFICIENT)
        self.assertFalse(decision["checks"]["normal_leave_any_primary_symbol_out_positive_net_R_and_delta"])


if __name__ == "__main__":
    unittest.main()
