"""Synthetic-only frozen event-study checks; never reads market data."""
import math
import unittest
from unittest.mock import patch

from research.short_trend import engine as e


def candles(hours=12, price=100.0):
    return [[e.WARMUP_MS + i * e.FIVE, price, price, price, price, 1,
             e.WARMUP_MS + (i + 1) * e.FIVE - 1] for i in range(hours * 12)]


def hourly(ohlc):
    result = []
    for hour, (high, low, close) in enumerate(ohlc):
        for i in range(12):
            opened = e.WARMUP_MS + hour * e.HOUR + i * e.FIVE
            result.append([opened, close, high, low, close, 1, opened + e.FIVE - 1])
    return result


class SignalsTests(unittest.TestCase):
    def history(self):
        hours = [(101, 99, 100)] * 49
        hours[20] = (104, 96, 100)
        hours += [(107, 99, 106), (109, 105, 108), (101, 99, 100), (112, 99, 111)]
        return hours

    def test_first_cross_uses_own_prior_boundary_and_rearms(self):
        records = e.signals(hourly(self.history()))
        self.assertEqual([item["decision_ms"] for item in records],
                         [e.WARMUP_MS + 50 * e.HOUR, e.WARMUP_MS + 53 * e.HOUR])
        self.assertEqual(records[0]["breakout_level"], 104)

    def test_wilder_is_seeded_then_recursive_not_rolling_mean(self):
        hours = self.history()[:50]
        tr = [max(h - lo, abs(h - hours[i - 1][2]), abs(lo - hours[i - 1][2]))
              for i, (h, lo, _) in enumerate(hours) if i]
        expected = sum(tr[:14]) / 14
        for value in tr[14:]:
            expected = (13 * expected + value) / 14
        actual = e.signals(hourly(hours))[0]["atr"]
        self.assertAlmostEqual(actual, expected)
        self.assertFalse(math.isclose(actual, sum(tr[-14:]) / 14))

    def test_completed_prefix_and_future_mutation_do_not_change_signal(self):
        rows = hourly(self.history())
        first = e.signals(rows[:50 * 12])
        self.assertEqual(e.signals(rows)[:1], first)
        future = [list(row) for row in rows]
        for row in future[50 * 12:]:
            row[1:5] = [1, 1000, 1, 900]
        self.assertEqual(e.signals(future)[:1], first)
        self.assertEqual(e.signals(rows[:50 * 12 - 1]), [])

    def test_missing_five_minute_resets_history(self):
        rows = hourly(self.history())
        del rows[10 * 12 + 3]
        self.assertEqual(e.signals(rows), [])

    def test_symmetric_short_first_cross(self):
        mirrored = [(200 - lo, 200 - h, 200 - c) for h, lo, c in self.history()]
        self.assertEqual([r["direction"] for r in e.signals(hourly(mirrored))], [-1, -1])


class EventTests(unittest.TestCase):
    def setUp(self):
        self.rows = candles()
        self.decision = e.WARMUP_MS + e.HOUR
        self.entry = self.decision + e.FIVE
        self.start = self.decision
        self.end = e.WARMUP_MS + 12 * e.HOUR
        self.item = {"decision_ms": self.decision, "side": "long", "direction": 1,
                     "decision_close": 100.0, "atr": 1.0,
                     "breakout_level": 100.0, "signal_stop": 99.0}

    def replay(self, *, funding=(), fee=5, slip=3, order="funding_first", items=None):
        with patch.object(e, "_signals", return_value=[self.item] if items is None else items):
            return e.event_pairs("BTCUSDT", self.rows, funding, self.start, self.end, fee, slip, order)

    def setbar(self, when, o=None, h=None, lo=None, c=None):
        row = self.rows[(when - e.WARMUP_MS) // e.FIVE]
        for index, value in ((1, o), (2, h), (3, lo), (4, c)):
            if value is not None:
                row[index] = value

    def test_common_quantity_cap_and_exact_mirror_distance(self):
        event = self.replay()["events"][0]
        sig, mir = event["signal"], event["mirror"]
        self.assertEqual(sig["quantity"], mir["quantity"])
        self.assertLessEqual(max(sig["planned_risk_usdt"], mir["planned_risk_usdt"]), e.RISK + 1e-12)
        self.assertLessEqual(event["quantity"] * max(sig["entry_price"], mir["entry_price"]), 220 + 1e-12)
        self.assertAlmostEqual(sig["entry_price"] - sig["stop_price"], mir["stop_price"] - mir["entry_price"])
        self.assertEqual(sig["stop_price"], 99)
        self.assertEqual(event["delta_R"], (sig["net_R"] - mir["net_R"]) / 2)

    def test_arrival_can_only_reduce_and_stop_remains_fixed(self):
        baseline = self.replay()["events"][0]
        self.setbar(self.entry, o=102, h=102, lo=102, c=102)
        later = self.replay()["events"][0]
        self.assertTrue(later["arrival_reduced"])
        self.assertLess(later["quantity"], baseline["quantity"])
        self.assertEqual(later["signal"]["stop_price"], 99)
        self.assertEqual(later["q_dec"], baseline["q_dec"])

    def test_invalid_gap_excludes_both_arms(self):
        self.setbar(self.entry, o=98, h=98, lo=98, c=98)
        result = self.replay()
        self.assertEqual(result["events"], [])
        self.assertEqual(result["skips"], {"gap_invalid": 1})

    def test_net_target_exact_both_sides_with_fees_slip_and_signed_funding(self):
        initial = self.replay()["events"][0]
        q = initial["quantity"]
        fundtime = self.entry + 1
        funds = [{"time_ms": fundtime, "rate": 0.0001, "mark_price": 100}]
        for sign, arm in ((1, "signal"), (-1, "mirror")):
            with self.subTest(sign=sign):
                rows = self.rows
                self.rows = candles()
                paid = sign * q * 100 * .0001
                entry = initial[arm]["entry_price"]
                target = e._target(entry, sign, q, paid, .0005, .0003)
                if sign == 1:
                    self.setbar(self.entry, h=target + .01)
                else:
                    self.setbar(self.entry, lo=target - .01)
                result = self.replay(funding=funds)["events"][0][arm]
                self.assertEqual(result["exit_reason"], "TP")
                self.assertAlmostEqual(result["net_pnl_usdt"], 1.1)
                self.assertAlmostEqual(result["funding_usdt"], paid)
                self.assertAlmostEqual(result["net_pnl_usdt"], result["gross_pnl_usdt"] - result["fees_usdt"] - result["funding_usdt"])
                self.assertAlmostEqual(result["raw_price_pnl_usdt"] - result["gross_pnl_usdt"], result["slippage_usdt"])
                self.rows = rows

    def test_stop_first_same_bar_double_touch_uses_upper_timestamp(self):
        self.setbar(self.entry, h=105, lo=95)
        result = self.replay()["events"][0]["signal"]
        self.assertEqual(result["exit_reason"], "SL")
        self.assertEqual(result["exit_raw"], 99)
        self.assertTrue(result["both_sl_tp_touched"])
        self.assertTrue(result["exit_time_upper_bound"])
        self.assertEqual(result["exit_ms"], self.entry + e.FIVE - 1)

    def test_stop_gap_worse_open_and_target_gap_no_improvement(self):
        self.setbar(self.entry + e.FIVE, o=97, h=97, lo=97, c=97)
        stopped = self.replay()["events"][0]["signal"]
        self.assertEqual(stopped["exit_raw"], 97)
        self.assertTrue(stopped["gap_stop"])
        self.assertFalse(stopped["exit_time_upper_bound"])
        self.rows = candles()
        base = self.replay()["events"][0]["signal"]
        target = e._target(base["entry_price"], 1, base["quantity"], 0, .0005, .0003)
        self.setbar(self.entry + e.FIVE, o=110, h=110, lo=110, c=110)
        tp = self.replay()["events"][0]["signal"]
        self.assertEqual(tp["exit_raw"], target)
        self.assertLess(tp["exit_raw"], 110)
        self.assertTrue(tp["gap_target"])

    def test_exact_entry_funding_excluded_exact_deadline_funding_before_time_exit(self):
        deadline = self.entry + e.HOLD
        funds = [{"time_ms": self.entry, "rate": .001, "mark_price": 100},
                 {"time_ms": deadline, "rate": .0001, "mark_price": 100}]
        for order in ("funding_first", "price_first"):
            event = self.replay(funding=funds, order=order)["events"][0]
            self.assertEqual(event["signal"]["exit_reason"], "TIME")
            self.assertEqual(event["signal"]["exit_ms"], deadline)
            self.assertEqual(len(event["signal"]["funding_events"]), 1)
            self.assertEqual(event["signal"]["funding_events"][0]["time_ms"], deadline)
            self.assertGreater(event["signal"]["funding_usdt"], 0)
            self.assertLess(event["mirror"]["funding_usdt"], 0)

    def test_unknown_funding_order_changes_accounting_not_events(self):
        self.setbar(self.entry, h=103)
        funds = [{"time_ms": self.entry + 1, "rate": .0002, "mark_price": 100}]
        first = self.replay(funding=funds)["events"][0]
        alternative = self.replay(funding=funds, order="price_first")["events"][0]
        self.assertEqual(first["signal"]["exit_reason"], "TP")
        self.assertEqual(alternative["signal"]["exit_reason"], "TP")
        self.assertGreater(first["signal"]["funding_usdt"], 0)
        self.assertEqual(alternative["signal"]["funding_usdt"], 0)
        self.assertTrue(alternative["signal"]["funding_touch_same_bucket"])
        self.assertAlmostEqual(first["signal"]["net_pnl_usdt"], 1.1)
        self.assertAlmostEqual(alternative["signal"]["net_pnl_usdt"], 1.1)

    def test_funding_change_target_clamps_to_visible_bar_and_no_retroactive_alt_fill(self):
        funds = [{"time_ms": self.entry + 1, "rate": -.02, "mark_price": 100}]
        primary = self.replay(funding=funds)["events"][0]["signal"]
        alternative = self.replay(funding=funds, order="price_first")["events"][0]["signal"]
        self.assertTrue(primary["target_clamped"])
        self.assertEqual(primary["exit_raw"], 100)
        self.assertEqual(primary["exit_ms"], self.entry + e.FIVE - 1)
        self.assertEqual(alternative["exit_ms"], self.entry + e.FIVE)
        self.assertEqual(alternative["exit_raw"], 100)
        self.assertTrue(alternative["cashflow_target_at_open"])

    def test_exact_open_funding_cannot_backfill_newly_satisfied_target(self):
        funds = [{"time_ms": self.entry + e.FIVE, "rate": -.02, "mark_price": 100}]
        for order in ("funding_first", "price_first"):
            arm = self.replay(funding=funds, order=order)["events"][0]["signal"]
            self.assertEqual(arm["exit_reason"], "TP")
            self.assertEqual(arm["exit_ms"], self.entry + e.FIVE)
            self.assertEqual(arm["exit_raw"], 100)
            self.assertTrue(arm["cashflow_target_at_open"])
            self.assertFalse(arm["gap_target"])
            self.assertGreater(arm["net_pnl_usdt"], e.TARGET)

    def test_cashflow_open_fix_is_symmetric_for_short_arm(self):
        funds = [{"time_ms": self.entry + 1, "rate": .02, "mark_price": 100}]
        arm = self.replay(funding=funds, order="price_first")["events"][0]["mirror"]
        self.assertEqual(arm["exit_raw"], 100)
        self.assertEqual(arm["exit_ms"], self.entry + e.FIVE)
        self.assertTrue(arm["cashflow_target_at_open"])

    def test_funding_does_not_turn_ordinary_existing_target_gap_into_open_improvement(self):
        baseline = self.replay()["events"][0]["signal"]
        funds = [{"time_ms": self.entry + e.FIVE, "rate": -.0001, "mark_price": 100}]
        self.setbar(self.entry + e.FIVE, o=103, h=103, lo=103, c=103)
        arm = self.replay(funding=funds)["events"][0]["signal"]
        target = e._target(baseline["entry_price"], 1, baseline["quantity"], arm["funding_usdt"], .0005, .0003)
        self.assertAlmostEqual(arm["exit_raw"], target)
        self.assertFalse(arm["cashflow_target_at_open"])
        self.assertTrue(arm["gap_target"])

    def test_overlap_fixed_equity_no_compounding_and_direction_marks(self):
        second = dict(self.item, decision_ms=self.decision + e.HOUR)
        result = self.replay(items=[self.item, second])
        self.assertEqual(len(result["events"]), 2)
        self.assertEqual(result["events"][0]["quantity"], result["events"][1]["quantity"])
        for event in result["events"]:
            self.assertEqual(event["event_equity_usdt"], 110)
            self.assertTrue(event["direction_tie_4h"])
            self.assertFalse(event["direction_hit_4h"])

    def test_horizon_must_be_strictly_inside_segment(self):
        self.end = self.entry + e.HOLD
        self.assertEqual(self.replay()["skips"], {"incomplete_horizon_before_segment_end": 1})

    def test_missing_bars_fail_full_result_instead_of_dropping_trade(self):
        del self.rows[30]
        with self.assertRaises(e.DataQualityError):
            self.replay()

    def test_wilder_warmup_origin_and_complete_segment_are_required(self):
        self.rows = self.rows[1:]
        with self.assertRaisesRegex(e.DataQualityError, "Fixed Wilder history"):
            self.replay()
        self.rows = candles()[:-1]
        with self.assertRaisesRegex(e.DataQualityError, "complete evaluation segment"):
            self.replay()

    def test_deadline_stop_and_target_precede_time_exit(self):
        deadline = self.entry + e.HOLD
        self.setbar(deadline, o=98, h=98, lo=98, c=98)
        stop = self.replay()["events"][0]["signal"]
        self.assertEqual((stop["exit_ms"], stop["exit_reason"]), (deadline, "SL"))
        self.rows = candles()
        self.setbar(deadline, o=103, h=103, lo=103, c=103)
        target = self.replay()["events"][0]["signal"]
        self.assertEqual((target["exit_ms"], target["exit_reason"]), (deadline, "TP"))

    def test_future_timestamp_rejected_before_price_conversion(self):
        class Poison:
            def __float__(self):
                raise AssertionError("A protected market value was converted")
        self.rows.append([e.EXCLUSIVE_END_MS, Poison(), Poison(), Poison(), Poison(), Poison(), e.EXCLUSIVE_END_MS + e.FIVE - 1])
        with self.assertRaisesRegex(ValueError, "Excluded timestamp"):
            self.replay()
        self.rows = candles()
        with self.assertRaisesRegex(ValueError, "Excluded timestamp"):
            self.replay(funding=[{"time_ms": e.EXCLUSIVE_END_MS, "rate": Poison(), "mark_price": Poison()}])

    def test_funding_proxy_future_duplicate_and_bad_geometry_rejected(self):
        bad = {"time_ms": self.entry + 1, "rate": .0001, "mark_price": 100, "mark_proxy_ms": self.entry + e.FIVE}
        with self.assertRaises(e.DataQualityError):
            self.replay(funding=[bad])
        bad["mark_proxy_ms"] = self.entry + 1
        with self.assertRaises(e.DataQualityError):
            self.replay(funding=[bad])
        good = {"time_ms": self.entry + 1, "rate": .0001, "mark_price": 100}
        with self.assertRaises(e.DataQualityError):
            self.replay(funding=[good, good])
        self.setbar(self.entry, lo=101)
        with self.assertRaises(e.DataQualityError):
            self.replay()

    def test_arrival_uses_five_minute_open_not_decision_bar_or_future_high(self):
        self.setbar(self.decision, o=90, h=90, lo=90, c=90)
        self.setbar(self.entry, o=101, h=101, lo=101, c=101)
        event = self.replay()["events"][0]
        self.assertEqual(event["signal"]["entry_raw"], 101)
        self.assertAlmostEqual(event["signal"]["entry_price"], 101 * 1.0003)

    def test_funding_millisecond_after_entry_is_paid_and_exact_open_exit_pays(self):
        next_open = self.entry + e.FIVE
        funds = [{"time_ms": self.entry + 1, "rate": .0001, "mark_price": 100},
                 {"time_ms": next_open, "rate": .0002, "mark_price": 100}]
        self.setbar(next_open, o=98, h=98, lo=98, c=98)
        for order in ("funding_first", "price_first"):
            trade = self.replay(funding=funds, order=order)["events"][0]["signal"]
            self.assertEqual(trade["exit_reason"], "SL")
            self.assertEqual([row["time_ms"] for row in trade["funding_events"]], [self.entry + 1, next_open])
            self.assertEqual(trade["funding_events"][0]["proxy_age_ms"], 1)

    def test_risk_and_notional_caps_for_stress_and_short_signal(self):
        self.item.update(side="short", direction=-1, signal_stop=101, breakout_level=100)
        for fee, slip in ((5, 3), (10, 10)):
            event = self.replay(fee=fee, slip=slip)["events"][0]
            self.assertEqual(event["signal"]["direction"], -1)
            self.assertLessEqual(max(event["planned_risk_signal"], event["planned_risk_mirror"]), e.RISK + 1e-12)
            self.assertLessEqual(event["quantity"] * max(event["signal"]["entry_price"], event["mirror"]["entry_price"]), 220 + 1e-12)


if __name__ == "__main__":
    unittest.main()
