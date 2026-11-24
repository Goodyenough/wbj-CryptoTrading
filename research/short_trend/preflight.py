"""Metadata-only guards. This module cannot download or replay market data.

Protocol fields are frozen in Git; no command-line strategy overrides exist.
Archive requests are validated before a future caller may touch cache/network.
Historical account acceptance fails closed on missing dated rule evidence.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re

EFFECTIVE_END_MS = 1_767_225_600_000
HARD_SEAL_MS = 1_782_144_000_000
EARLIEST_MONTH = "2023-12"
LATEST_MONTH = "2025-12"
SYMBOLS = frozenset({"BTCUSDT", "ETHUSDT", "SOLUSDT", "ZECUSDT"})
KINDS = frozenset({"klines", "markPriceKlines", "fundingRate"})
BASE = "https://data.binance.vision/data/futures/um/monthly"
REQUIRED_FILTER_FIELDS = frozenset({
    "tickSize", "stepSize", "minQty", "maxQty", "marketStepSize",
    "marketMinQty", "marketMaxQty", "minNotional", "contractStatus",
})


def utc_ms(value: str) -> int:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ValueError("Expected explicit UTC timestamp ending in Z")
    when = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return int(when.timestamp() * 1000)


def _month_bounds(month: str) -> tuple[int, int]:
    if not isinstance(month, str) or not re.fullmatch(r"\d{4}-\d{2}", month):
        raise ValueError("Explicit YYYY-MM month required")
    if not EARLIEST_MONTH <= month <= LATEST_MONTH:
        raise ValueError("Month is outside frozen historical allowlist")
    start = datetime.strptime(month, "%Y-%m").replace(tzinfo=timezone.utc)
    end = datetime(start.year + (start.month == 12), start.month % 12 + 1, 1, tzinfo=timezone.utc)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)


def archive_request(symbol: str, kind: str, month: str) -> dict:
    """Return an approved URL; no filesystem/network access takes place."""
    if symbol not in SYMBOLS or kind not in KINDS:
        raise ValueError("Unapproved symbol or archive kind")
    start, end = _month_bounds(month)
    if end > EFFECTIVE_END_MS or end > HARD_SEAL_MS:
        raise ValueError("Archive crosses a protected boundary")
    if kind == "fundingRate":
        url = f"{BASE}/{kind}/{symbol}/{symbol}-fundingRate-{month}.zip"
    else:
        url = f"{BASE}/{kind}/{symbol}/5m/{symbol}-5m-{month}.zip"
    return {"symbol": symbol, "kind": kind, "month": month,
            "start_ms": start, "exclusive_end_ms": end, "url": url,
            "checksum_url": url + ".CHECKSUM"}


def validate_protocol(config: dict) -> None:
    data = config["data"]
    # A later cutoff in a hand-edited JSON cannot relax the code-level seal.
    if (type(data["effective_exclusive_end_ms"]) is not int
            or data["effective_exclusive_end_ms"] != EFFECTIVE_END_MS
            or data["hard_seal_start_ms"] != HARD_SEAL_MS):
        raise ValueError("Frozen cutoffs cannot be overridden")
    if (data["archive_first_month"] != EARLIEST_MONTH
            or data["archive_last_month"] != LATEST_MONTH
            or utc_ms(data["exclusive_end_utc"]) != EFFECTIVE_END_MS
            or data["archive_base"] != BASE):
        raise ValueError("Archive bounds or origin differ from frozen protocol")
    for field in ("production_database_allowed", "live_endpoints_allowed",
                  "archive_discovery_allowed", "redirects_allowed"):
        if data[field] is not False:
            raise ValueError(f"Forbidden data access: {field}")
    if data["checksum_required"] is not True:
        raise ValueError("Archive checksums cannot be disabled")
    if (config["primary_symbols"] != ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
            or config["exploratory_symbols"] != ["ZECUSDT"]):
        raise ValueError("Universe differs from frozen research specification")
    if set(data["archive_kinds"]) != KINDS or data["base_interval"] != "5m":
        raise ValueError("Archive types differ from frozen specification")
    if utc_ms(data["warmup_start_utc"]) != _month_bounds(EARLIEST_MONTH)[0]:
        raise ValueError("Warmup start differs from frozen boundary")
    if set(config["execution_coverage"]["required_fields"]) != REQUIRED_FILTER_FIELDS:
        raise ValueError("Historical filter requirements cannot be weakened")
    expected_segments = [("2024-01-01T00:00:00Z", "2025-01-01T00:00:00Z"),
                         ("2025-01-01T00:00:00Z", "2026-01-01T00:00:00Z")]
    actual = [(s["start_utc"], s["end_utc"]) for s in config["segments"]]
    if actual != expected_segments:
        raise ValueError("Evaluation years differ from frozen specification")
    for start, end in actual:
        if not utc_ms(start) < utc_ms(end) <= EFFECTIVE_END_MS:
            raise ValueError("Segment reaches excluded data")


def validate_record_times(open_ms: int, close_ms: int, *, interval_ms: int = 300_000) -> None:
    """Future loaders call this before parsing or returning market values."""
    if type(open_ms) is not int or type(close_ms) is not int:
        raise ValueError("Integer millisecond timestamps required")
    if (interval_ms != 300_000 or open_ms % interval_ms
            or close_ms != open_ms + interval_ms - 1
            or open_ms < _month_bounds(EARLIEST_MONTH)[0]
            or close_ms >= EFFECTIVE_END_MS):
        raise ValueError("Misaligned, cross-boundary or unapproved historical record")


def validate_funding_time(time_ms: int, month: str) -> None:
    """Keep raw funding milliseconds; reject before converting its rate/mark."""
    start, end = _month_bounds(month)
    if type(time_ms) is not int or not start <= time_ms < end or time_ms >= EFFECTIVE_END_MS:
        raise ValueError("Cross-month or excluded funding timestamp")


def historical_order_filter_gate(config: dict, evidence: dict) -> dict:
    """Require contiguous, sourced, complete historical rule coverage.

    A single known change announcement or a current snapshot is insufficient.
    This is only the dated-rule gate, not a claim about depth or fill quality.
    """
    required = REQUIRED_FILTER_FIELDS
    if set(config["execution_coverage"]["required_fields"]) != required:
        raise ValueError("Historical filter requirements cannot be weakened")
    start = utc_ms(config["segments"][0]["start_utc"])
    end = utc_ms(config["segments"][-1]["end_utc"])
    issues = []
    for symbol in config["primary_symbols"]:
        cursor = start
        intervals = sorted(evidence.get("historical_rule_intervals", {}).get(symbol, []),
                           key=lambda row: row.get("start_utc", ""))
        for row in intervals:
            left, right = utc_ms(row["start_utc"]), utc_ms(row["end_utc"])
            if not left < right:
                raise ValueError("Historical-rule interval must have positive duration")
            if right <= start or left >= end:
                continue
            if left > cursor:
                break
            values = row.get("filters", {})
            numeric = required - {"contractStatus"}
            valid_numeric = all(
                key in values and not isinstance(values[key], bool)
                and isinstance(values[key], (int, float))
                and math.isfinite(values[key]) and values[key] > 0
                for key in numeric
            )
            valid_ranges = (valid_numeric and values["minQty"] <= values["maxQty"]
                            and values["marketMinQty"] <= values["marketMaxQty"])
            if (row.get("status") != "verified_historical_interval"
                    or row.get("basis") != "source_backed_historical_interval"
                    or not row.get("source_refs") or not valid_ranges
                    or values.get("contractStatus") != "TRADING"):
                break
            cursor = max(cursor, min(right, end))
        if cursor < end:
            issues.append({"symbol": symbol, "reason": "incomplete_dated_historical_rules",
                           "verified_contiguous_through_ms": cursor})
    return {"dated_order_filter_coverage_pass": not issues,
            "historical_account_acceptance_allowed": False,
            "account_acceptance_status": (
                "BLOCKED_MISSING_ORDER_FILTERS" if issues
                else "NOT_EVALUATED_MARGIN_TRIGGER_LIQUIDATION_AND_REPLAY"),
            "issues": issues}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=Path(__file__).with_name("protocol.json"))
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, help="Optional metadata-only JSON receipt")
    args = parser.parse_args()
    raw = args.protocol.read_bytes()
    config = json.loads(raw)
    validate_protocol(config)
    evidence = json.loads(args.evidence.read_bytes())
    result = {"strategy_id": config["strategy_id"],
              "scope": "metadata_preflight_process_only_not_whole_audit",
              "protocol_sha256": hashlib.sha256(json.dumps(
                  config, ensure_ascii=False, sort_keys=True,
                  separators=(",", ":")).encode("utf-8")).hexdigest(),
              "protocol_hash_mode": "canonical_json_utf8_sorted_compact",
              "data_boundary_check": "PASS", "market_data_read": False,
              "network_used": False, "backtest_run": False,
              **historical_order_filter_gate(config, evidence)}
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output is not None:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
