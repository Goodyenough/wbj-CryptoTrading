"""Protection and fail-closed metadata checks; no prices, network or database."""
import copy
import json
from pathlib import Path
import unittest

from research.short_trend.preflight import (
    EFFECTIVE_END_MS, archive_request, historical_order_filter_gate,
    validate_protocol, validate_record_times, validate_funding_time,
)


CONFIG = json.loads((Path(__file__).parents[1] / "research/short_trend/protocol.json").read_bytes())


class ProtectedArchiveTests(unittest.TestCase):
    def test_excluded_months_rejected_before_any_io(self):
        for month in ("2026-01", "2026-06", "2026-11", "2027-01", "2023-11", "latest"):
            with self.subTest(month=month), self.assertRaises(ValueError):
                archive_request("BTCUSDT", "klines", month)

    def test_url_cannot_be_redirected_or_injected_via_symbol_kind(self):
        for symbol, kind in (("../BTCUSDT", "klines"), ("BTCUSDT", "ticker"),
                             ("ETHUSDT", "../../spot"), ("DOGEUSDT", "klines")):
            with self.subTest(symbol=symbol, kind=kind), self.assertRaises(ValueError):
                archive_request(symbol, kind, "2025-12")

    def test_last_approved_month_is_complete_and_checksum_bound(self):
        row = archive_request("SOLUSDT", "fundingRate", "2025-12")
        self.assertEqual(row["exclusive_end_ms"], EFFECTIVE_END_MS)
        self.assertTrue(row["url"].endswith("/SOLUSDT/SOLUSDT-fundingRate-2025-12.zip"))
        self.assertEqual(row["checksum_url"], row["url"] + ".CHECKSUM")

    def test_forged_later_cutoff_cannot_relax_guard(self):
        config = copy.deepcopy(CONFIG)
        config["data"]["effective_exclusive_end_ms"] += 365 * 86_400_000
        with self.assertRaises(ValueError):
            validate_protocol(config)

    def test_disabling_security_control_rejected(self):
        for field in ("live_endpoints_allowed", "production_database_allowed",
                      "redirects_allowed", "archive_discovery_allowed"):
            config = copy.deepcopy(CONFIG)
            config["data"][field] = True
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_protocol(config)

    def test_evaluation_segment_cannot_extend_into_2026(self):
        config = copy.deepcopy(CONFIG)
        config["segments"][-1]["end_utc"] = "2026-01-02T00:00:00Z"
        with self.assertRaises(ValueError):
            validate_protocol(config)

    def test_row_crossing_exclusive_boundary_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_record_times(EFFECTIVE_END_MS, EFFECTIVE_END_MS + 299_999)
        validate_record_times(EFFECTIVE_END_MS - 300_000, EFFECTIVE_END_MS - 1)
        with self.assertRaises(ValueError):
            validate_record_times(EFFECTIVE_END_MS - 300_000, EFFECTIVE_END_MS)

    def test_millisecond_alignment_and_types_are_not_silently_coerced(self):
        for opened, closed in ((True, 299_999), (1.5, 299_999),
                               (EFFECTIVE_END_MS - 299_999, EFFECTIVE_END_MS - 1)):
            with self.subTest(opened=opened), self.assertRaises(ValueError):
                validate_record_times(opened, closed)

    def test_funding_milliseconds_preserved_but_protected_time_rejected(self):
        validate_funding_time(EFFECTIVE_END_MS - 3_600_000 + 1, "2025-12")
        with self.assertRaises(ValueError):
            validate_funding_time(EFFECTIVE_END_MS, "2025-12")

    def test_funding_cross_month_and_boolean_rejected(self):
        for timestamp in (True, 1735689600000, EFFECTIVE_END_MS - 1.5):
            with self.subTest(timestamp=timestamp), self.assertRaises(ValueError):
                validate_funding_time(timestamp, "2025-12")


def verified_evidence():
    # Synthetic attestations only: no actual contract rules are invented here.
    filters = {key: 1.0 for key in CONFIG["execution_coverage"]["required_fields"]}
    filters["contractStatus"] = "TRADING"
    row = {"start_utc": "2024-01-01T00:00:00Z", "end_utc": "2026-01-01T00:00:00Z",
           "status": "verified_historical_interval", "basis": "source_backed_historical_interval",
           "source_refs": ["synthetic-test-evidence"], "filters": filters}
    return {"historical_rule_intervals": {s: [copy.deepcopy(row)] for s in CONFIG["primary_symbols"]}}


class HistoricalRuleGateTests(unittest.TestCase):
    def test_missing_rules_block_every_primary_symbol(self):
        gate = historical_order_filter_gate(CONFIG, {})
        self.assertFalse(gate["historical_account_acceptance_allowed"])
        self.assertEqual(len(gate["issues"]), 3)

    def test_change_announcement_does_not_establish_all_period_coverage(self):
        evidence = verified_evidence()
        evidence["historical_rule_intervals"]["SOLUSDT"][0]["start_utc"] = "2024-10-14T06:30:00Z"
        self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])

    def test_current_snapshot_cannot_be_relabelled_as_history(self):
        evidence = verified_evidence()
        evidence["historical_rule_intervals"]["BTCUSDT"][0]["basis"] = "current_snapshot"
        self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])

    def test_unknown_field_and_missing_provenance_block(self):
        for modification in ("field", "source"):
            evidence = verified_evidence()
            row = evidence["historical_rule_intervals"]["ETHUSDT"][0]
            if modification == "field":
                del row["filters"]["marketStepSize"]
            else:
                row["source_refs"] = []
            with self.subTest(modification=modification):
                self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])

    def test_valid_contiguous_intervals_required_not_only_endpoints(self):
        evidence = verified_evidence()
        row = evidence["historical_rule_intervals"]["SOLUSDT"][0]
        second = copy.deepcopy(row)
        row["end_utc"] = "2025-01-01T00:00:00Z"
        second["start_utc"] = "2025-01-01T00:00:00Z"
        evidence["historical_rule_intervals"]["SOLUSDT"].append(second)
        complete = historical_order_filter_gate(CONFIG, evidence)
        self.assertTrue(complete["dated_order_filter_coverage_pass"])
        self.assertFalse(complete["historical_account_acceptance_allowed"])
        second["start_utc"] = "2025-01-02T00:00:00Z"
        self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])

    def test_nonfinite_or_boolean_filter_value_is_not_evidence(self):
        for value in (float("nan"), float("inf"), True, 0, -1):
            evidence = verified_evidence()
            evidence["historical_rule_intervals"]["BTCUSDT"][0]["filters"]["stepSize"] = value
            with self.subTest(value=value):
                self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])

    def test_required_fields_cannot_be_deleted_to_bypass_evidence(self):
        config = copy.deepcopy(CONFIG)
        config["execution_coverage"]["required_fields"] = []
        with self.assertRaises(ValueError):
            validate_protocol(config)
        with self.assertRaises(ValueError):
            historical_order_filter_gate(config, verified_evidence())

    def test_inconsistent_quantity_ranges_fail_closed(self):
        evidence = verified_evidence()
        evidence["historical_rule_intervals"]["ETHUSDT"][0]["filters"]["minQty"] = 2.0
        self.assertFalse(historical_order_filter_gate(CONFIG, evidence)["dated_order_filter_coverage_pass"])


if __name__ == "__main__":
    unittest.main()
