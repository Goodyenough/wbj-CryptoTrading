"""A comparison must reject unmatched, duplicated, or future contexts."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

path=Path(__file__).resolve().parents[1]/"scripts/review_atr_shadow_evidence.py"
spec=importlib.util.spec_from_file_location("atr_evidence_review",path)
review=importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)


def rows():
    context=dict(plan_id="example",kline_time="2026-09-01T03:59:59Z",
        decision_time="2026-09-01T04:10:03Z",current_price=100.0,
        last_4h_close=100.2,entry_high=100.0,atr_4h=2.0,
        capacity_state="capacity_available",controls_paper=0)
    return [dict(context,line_name=line,accepted=int(line=="reference_baseline")) for line in review.LINES]


class PairingTests(unittest.TestCase):
    def test_valid_same_moment_comparison(self):
        self.assertEqual(len(review.pair_rows(rows())),1)

    def test_missing_or_duplicate_line_cannot_inflate_sample(self):
        source=rows()
        with self.assertRaises(ValueError):review.pair_rows(source[:-1])
        with self.assertRaises(ValueError):review.pair_rows(source+[deepcopy(source[0])])

    def test_different_prices_are_not_a_paired_comparison(self):
        source=rows();source[0]["last_4h_close"]=101.0
        with self.assertRaises(ValueError):review.pair_rows(source)

    def test_future_bar_is_rejected(self):
        source=rows()
        for r in source:r["kline_time"]="2026-09-01T07:59:59Z"
        with self.assertRaises(ValueError):review.pair_rows(source)


if __name__=="__main__":unittest.main()
