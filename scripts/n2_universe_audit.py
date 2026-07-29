from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest.history import interval_ms  # noqa: E402
from crypto_trading_system.backtest.universe import SymbolMaster, fetch_symbol_listing_dates, load_symbol_master, save_symbol_master  # noqa: E402
from crypto_trading_system.config import load_settings  # noqa: E402
from crypto_trading_system.database import connect_db  # noqa: E402
from crypto_trading_system.report_versions import next_report_version, versioned_markdown_filename  # noqa: E402


S3_ENDPOINT = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
S3_NS = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
MONTH_RE = re.compile(r"-1d-(\d{4})-(\d{2})\.zip$")


def _utc_ms(date_text: str) -> int:
    return int(datetime.fromisoformat(date_text + "T00:00:00+00:00").timestamp() * 1000)


def _iso_from_ms(ms: int | None) -> str | None:
    if ms is None:
        return None
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat(timespec="seconds")


def _date_from_ms(ms: int | None) -> str | None:
    if ms is None:
        return None
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).date().isoformat()


def _expected_bars(start_ms: int, end_ms: int, interval: str) -> int:
    return max(0, (end_ms - start_ms) // interval_ms(interval))


def _db_interval_summary(connection: sqlite3.Connection, symbol: str, interval: str, start_ms: int, end_ms: int) -> dict:
    row = connection.execute(
        """
        SELECT MIN(open_time) AS first_open, MAX(open_time) AS last_open, COUNT(*) AS total_bars
        FROM kline_cache
        WHERE source = 'Binance'
          AND symbol = ?
          AND interval = ?
          AND is_closed = 1
        """,
        (symbol, interval),
    ).fetchone()
    window = connection.execute(
        """
        SELECT COUNT(*) AS window_bars
        FROM kline_cache
        WHERE source = 'Binance'
          AND symbol = ?
          AND interval = ?
          AND open_time >= ?
          AND open_time < ?
          AND is_closed = 1
        """,
        (symbol, interval, start_ms, end_ms),
    ).fetchone()
    unavailable = connection.execute(
        """
        SELECT reason
        FROM kline_unavailable_ranges
        WHERE source = 'Binance'
          AND symbol = ?
          AND interval = ?
          AND start_time <= ?
          AND end_time >= ?
        ORDER BY fetched_at_utc DESC
        LIMIT 1
        """,
        (symbol, interval, start_ms, end_ms),
    ).fetchone()
    expected = _expected_bars(start_ms, end_ms, interval)
    window_bars = int(window["window_bars"] or 0)
    return {
        "first_open_utc": _iso_from_ms(row["first_open"]),
        "last_open_utc": _iso_from_ms(row["last_open"]),
        "total_bars": int(row["total_bars"] or 0),
        "window_bars": window_bars,
        "expected_window_bars": expected,
        "window_coverage_pct": (window_bars / expected * 100.0) if expected else 0.0,
        "unavailable_reason": None if unavailable is None else str(unavailable["reason"]),
    }


def _request_xml(params: dict[str, str], pause: float = 0.04) -> ET.Element:
    url = S3_ENDPOINT + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "CryptoTradingSystem/0.1"})
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = response.read()
            if pause:
                time.sleep(pause)
            return ET.fromstring(payload)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last_error = exc
            time.sleep(2**attempt)
    if last_error is not None:
        raise last_error
    raise RuntimeError(f"Failed to fetch S3 XML: {url}")


def _s3_common_prefixes(prefix: str) -> list[str]:
    prefixes: list[str] = []
    marker: str | None = None
    while True:
        params = {"delimiter": "/", "prefix": prefix}
        if marker:
            params["marker"] = marker
        root = _request_xml(params)
        for item in root.findall("s3:CommonPrefixes/s3:Prefix", S3_NS):
            if item.text:
                prefixes.append(item.text)
        truncated = (root.findtext("s3:IsTruncated", default="false", namespaces=S3_NS) or "false").lower() == "true"
        next_marker = root.findtext("s3:NextMarker", default="", namespaces=S3_NS)
        if not truncated:
            break
        marker = next_marker or (prefixes[-1] if prefixes else None)
        if not marker:
            break
    return prefixes


def _s3_keys(prefix: str) -> list[str]:
    keys: list[str] = []
    marker: str | None = None
    while True:
        params = {"prefix": prefix}
        if marker:
            params["marker"] = marker
        root = _request_xml(params)
        for item in root.findall("s3:Contents/s3:Key", S3_NS):
            if item.text:
                keys.append(item.text)
        truncated = (root.findtext("s3:IsTruncated", default="false", namespaces=S3_NS) or "false").lower() == "true"
        if not truncated:
            break
        marker = keys[-1] if keys else None
        if not marker:
            break
    return keys


def _month_range(start: str, end: str) -> set[str]:
    start_dt = datetime.fromisoformat(start + "T00:00:00+00:00")
    end_dt = datetime.fromisoformat(end + "T00:00:00+00:00")
    months: set[str] = set()
    year, month = start_dt.year, start_dt.month
    while True:
        month_start = datetime(year, month, 1, tzinfo=timezone.utc)
        if month_start >= end_dt:
            break
        months.add(f"{year:04d}-{month:02d}")
        month += 1
        if month == 13:
            month = 1
            year += 1
    return months


def _symbol_months_from_s3(symbol: str) -> list[str]:
    keys = _s3_keys(f"data/spot/monthly/klines/{symbol}/1d/")
    months = []
    for key in keys:
        match = MONTH_RE.search(key)
        if match:
            months.append(f"{match.group(1)}-{match.group(2)}")
    return sorted(set(months))


def _load_json_dict(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save_json_dict(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_n2_audit(args: argparse.Namespace) -> tuple[dict, SymbolMaster]:
    settings = load_settings(Path(args.settings))
    master_path = Path(args.symbol_master_file)
    master = load_symbol_master(master_path)
    start_ms = _utc_ms(args.start)
    end_ms = _utc_ms(args.end)
    warmup_start_ms = min(
        start_ms - settings.backtest.warmup_1h_bars * interval_ms("1h"),
        start_ms - settings.backtest.warmup_4h_bars * interval_ms("4h"),
        start_ms - settings.backtest.warmup_1d_bars * interval_ms("1d"),
    )
    cache_dir = settings.output.reports_dir / args.reports_date / ".n2_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    listing_cache_path = cache_dir / "listing_dates.json"
    months_cache_path = cache_dir / "historical_symbol_months.json"
    listing_dates = dict(master.listing_dates or {})
    listing_dates.update({str(k): str(v) for k, v in _load_json_dict(listing_cache_path).items()})
    if args.fetch_listing_dates:
        missing_listing_symbols = [symbol for symbol in master.symbols if symbol not in listing_dates]
        if missing_listing_symbols:
            fetched = fetch_symbol_listing_dates(
                settings,
                missing_listing_symbols,
                progress=lambda message: print(f"[n2] {message}"),
            )
            listing_dates.update(fetched)
            _save_json_dict(listing_cache_path, listing_dates)

    current_rows = []
    with connect_db(settings.output.database_path) as connection:
        for symbol in master.symbols:
            intervals = {
                interval: _db_interval_summary(connection, symbol, interval, warmup_start_ms, end_ms)
                for interval in ["1h", "4h", "1d"]
            }
            earliest_local_date = _date_from_ms(
                min(
                    (
                        int(datetime.fromisoformat(item["first_open_utc"]).timestamp() * 1000)
                        for item in intervals.values()
                        if item["first_open_utc"]
                    ),
                    default=None,
                )
            )
            listing_date = listing_dates.get(symbol)
            classification = "unknown"
            if listing_date and listing_date >= args.end:
                classification = "listed_after_window"
            elif listing_date and listing_date > args.start:
                classification = "listed_inside_window"
            elif listing_date and listing_date <= args.start and intervals["4h"]["window_bars"] == 0:
                classification = "should_have_data_but_window_empty"
            elif intervals["4h"]["window_coverage_pct"] >= 99.0 and intervals["1d"]["window_coverage_pct"] >= 99.0:
                classification = "full_window_coverage"
            elif intervals["4h"]["window_bars"] > 0:
                classification = "partial_window_coverage"
            elif not listing_date and earliest_local_date and earliest_local_date >= args.end:
                classification = "local_first_kline_after_window"
            elif not listing_date and intervals["4h"]["window_bars"] == 0:
                classification = "no_listing_or_window_data"
            current_rows.append(
                {
                    "symbol": symbol,
                    "listing_date": listing_date,
                    "earliest_local_kline_date": earliest_local_date,
                    "first_valid_strategy_warmup_date": None
                    if listing_date is None
                    else datetime.fromtimestamp(
                        (int(datetime.fromisoformat(listing_date + "T00:00:00+00:00").timestamp()) + settings.analysis.min_history_days * 86_400),
                        tz=timezone.utc,
                    ).date().isoformat(),
                    "classification": classification,
                    "intervals": intervals,
                }
            )

    print("[n2] listing Binance public-data spot monthly symbol directories")
    prefixes = _s3_common_prefixes("data/spot/monthly/klines/")
    historical_symbols = sorted({prefix.rstrip("/").split("/")[-1] for prefix in prefixes if prefix.rstrip("/").split("/")[-1].endswith("USDT")})
    target_months = _month_range(args.start, args.end)
    historical_rows = []
    months_cache = _load_json_dict(months_cache_path)
    for i, symbol in enumerate(historical_symbols, start=1):
        if i == 1 or i % 50 == 0:
            print(f"[n2] checking historical monthly files {i}/{len(historical_symbols)}")
        if symbol in months_cache and isinstance(months_cache[symbol], list):
            months = [str(item) for item in months_cache[symbol]]
        else:
            months = _symbol_months_from_s3(symbol)
            months_cache[symbol] = months
            if i % 25 == 0:
                _save_json_dict(months_cache_path, months_cache)
        months_in_window = sorted(set(months) & target_months)
        if not months_in_window:
            continue
        historical_rows.append(
            {
                "symbol": symbol,
                "first_month": months[0] if months else None,
                "last_month": months[-1] if months else None,
                "months_in_window": months_in_window,
                "months_in_window_count": len(months_in_window),
                "in_current_master": symbol in set(master.symbols),
            }
        )
    _save_json_dict(months_cache_path, months_cache)

    current_set = set(master.symbols)
    historical_set = {row["symbol"] for row in historical_rows}
    missing_from_current = sorted(historical_set - current_set)
    enriched_master = SymbolMaster(
        source=master.source + " + Binance first available 1d kline listing_dates",
        created_at_utc=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        symbols=master.symbols,
        source_limit=master.source_limit,
        source_limit_applied=master.source_limit_applied,
        filters=master.filters,
        listing_dates=listing_dates,
    )
    current_counts = Counter(row["classification"] for row in current_rows)
    historical_counts = {
        "historical_usdt_symbols_with_1d_monthly_data_in_window": len(historical_rows),
        "missing_from_current_master": len(missing_from_current),
        "present_in_current_master": len(historical_set & current_set),
    }
    current_future_or_partial = (
        current_counts["listed_after_window"]
        + current_counts["listed_inside_window"]
        + current_counts["should_have_data_but_window_empty"]
        + current_counts["no_listing_or_window_data"]
    )
    if len(missing_from_current) > max(10, len(historical_set) * 0.05):
        window_qualification = "diagnostic_only_historical_membership_gap"
    elif current_counts["should_have_data_but_window_empty"] > 0:
        window_qualification = "invalid_until_missing_current_data_repaired"
    elif current_future_or_partial > len(master.symbols) * 0.10:
        window_qualification = "diagnostic_only_current_master_temporal_gap"
    else:
        window_qualification = "validation_with_documented_universe_limitations"

    audit = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "start": args.start,
        "end": args.end,
        "symbol_master_file": str(master_path),
        "symbol_master_count": len(master.symbols),
        "listing_dates_count": len(listing_dates),
        "current_master_classification_counts": dict(current_counts),
        "historical_membership_counts": historical_counts,
        "missing_from_current_master_examples": missing_from_current[:50],
        "window_qualification": window_qualification,
        "current_master_rows": current_rows,
        "historical_membership_rows": historical_rows,
    }
    return audit, enriched_master


def render_report(audit: dict, artifacts: dict[str, str]) -> str:
    counts = audit["current_master_classification_counts"]
    h = audit["historical_membership_counts"]
    lines = [
        "---",
        f"created: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - universe-audit",
        "experiment: atr_reclaim_stage_n2_universe_audit",
        f"verdict: {audit['window_qualification']}",
        "---",
        "",
        "# Stage N2 Universe And Data Substrate Audit",
        "",
        "## Plain-language conclusion",
        "",
    ]
    if audit["window_qualification"] == "diagnostic_only_historical_membership_gap":
        lines.append(
            "The third window should remain diagnostic only. Current-master listing dates reduce future-symbol ambiguity, but Binance public-data membership shows many USDT symbols with 1d monthly files inside the window that are missing from the current master."
        )
    elif audit["window_qualification"] == "invalid_until_missing_current_data_repaired":
        lines.append("The third window is invalid until current-master symbols that should have data but have empty window coverage are repaired or excluded.")
    else:
        lines.append("The third window may be used with documented universe limitations, subject to N0 rerun and mechanism-alignment caveats.")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            "| Artifact | Path |",
            "|---|---|",
        ]
    )
    for key, path in artifacts.items():
        lines.append(f"| {key} | `{path}` |")
    lines.extend(
        [
            "",
            "## N2-A Current Master Audit",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| symbol_master_count | {audit['symbol_master_count']} |",
            f"| listing_dates_count | {audit['listing_dates_count']} |",
        ]
    )
    for key in sorted(counts):
        lines.append(f"| {key} | {counts[key]} |")
    lines.extend(
        [
            "",
            "## N2-B Historical Membership Audit",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| historical_usdt_symbols_with_1d_monthly_data_in_window | {h['historical_usdt_symbols_with_1d_monthly_data_in_window']} |",
            f"| present_in_current_master | {h['present_in_current_master']} |",
            f"| missing_from_current_master | {h['missing_from_current_master']} |",
            "",
            "### Missing-from-current examples",
            "",
        ]
    )
    lines.append("`" + "`, `".join(audit["missing_from_current_master_examples"][:50]) + "`")
    lines.extend(
        [
            "",
            "## Window Qualification",
            "",
            f"`{audit['window_qualification']}`",
            "",
            "## Decision",
            "",
            "Do not treat the third window as a clean confirmatory validation unless historical membership is reconstructed or the missing-current-master bias is proven immaterial. If N0 is rerun with listing dates, its result must be interpreted together with this N2-B membership gap.",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(
                {
                    "generated_at_utc": audit["generated_at_utc"],
                    "start": audit["start"],
                    "end": audit["end"],
                    "symbol_master_count": audit["symbol_master_count"],
                    "listing_dates_count": audit["listing_dates_count"],
                    "current_master_classification_counts": audit["current_master_classification_counts"],
                    "historical_membership_counts": audit["historical_membership_counts"],
                    "missing_from_current_master_examples": audit["missing_from_current_master_examples"][:100],
                    "window_qualification": audit["window_qualification"],
                },
                ensure_ascii=False,
                indent=2,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage N2 universe/data substrate audit.")
    parser.add_argument("--settings", default="config/settings.toml")
    parser.add_argument("--symbol-master-file", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--reports-date", required=True)
    parser.add_argument("--fetch-listing-dates", action="store_true")
    args = parser.parse_args()

    settings = load_settings(Path(args.settings))
    audit, enriched_master = build_n2_audit(args)
    report_dir = settings.output.reports_dir / args.reports_date
    report_dir.mkdir(parents=True, exist_ok=True)
    prefix = f"atr_reclaim_stage_n2_universe_audit_{args.reports_date}"
    version = next_report_version([report_dir], prefix)
    json_path = report_dir / versioned_markdown_filename(prefix + "_raw", version).replace(".md", ".json")
    current_csv_path = report_dir / versioned_markdown_filename(prefix + "_current_master", version).replace(".md", ".json")
    historical_json_path = report_dir / versioned_markdown_filename(prefix + "_historical_membership", version).replace(".md", ".json")
    enriched_master_path = report_dir / f"dynamic_master_full_listing_enriched_{args.reports_date}_v{version}.json"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    current_csv_path.write_text(json.dumps(audit["current_master_rows"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    historical_json_path.write_text(json.dumps(audit["historical_membership_rows"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save_symbol_master(enriched_master, enriched_master_path)
    artifacts = {
        "raw_audit_json": str(json_path),
        "current_master_json": str(current_csv_path),
        "historical_membership_json": str(historical_json_path),
        "listing_enriched_master": str(enriched_master_path),
    }
    report_path = report_dir / versioned_markdown_filename(prefix, version)
    report_path.write_text(render_report(audit, artifacts), encoding="utf-8")
    print("n2_universe_audit=completed")
    print(f"verdict={audit['window_qualification']}")
    print(f"listing_dates_count={audit['listing_dates_count']}")
    print(f"historical_missing_from_current={audit['historical_membership_counts']['missing_from_current_master']}")
    print(f"report={report_path}")
    print(f"enriched_master={enriched_master_path}")


if __name__ == "__main__":
    main()
