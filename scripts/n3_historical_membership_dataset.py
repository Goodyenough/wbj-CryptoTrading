from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.config import load_settings  # noqa: E402
from crypto_trading_system.data_quality import EXCLUDED_SUFFIXES  # noqa: E402
from crypto_trading_system.report_versions import next_report_version, versioned_markdown_filename  # noqa: E402


KNOWN_STABLE_OR_FIAT_BASES = {
    "USDT",
    "USDC",
    "FDUSD",
    "TUSD",
    "DAI",
    "USDP",
    "USDE",
    "BUSD",
    "USTC",
    "EUR",
    "EURI",
    "AEUR",
    "GBP",
    "PAXG",
}

KNOWN_NONSTANDARD_BASES = {
    "BETH",
}

KNOWN_RENAME_OR_MIGRATION_HINTS = {
    "AGIX": "ASI/FET ecosystem migration candidate",
    "FTM": "Sonic S migration candidate",
    "GAL": "G migration candidate",
    "MATIC": "POL migration candidate",
    "OCEAN": "ASI/FET ecosystem migration candidate",
    "RNDR": "RENDER migration candidate",
    "TOMO": "VIC migration candidate",
}


def _base(symbol: str, quote_asset: str) -> str:
    if symbol.endswith(quote_asset):
        return symbol[: -len(quote_asset)]
    return symbol


def _month_to_time(month: str, *, end: bool = False) -> str:
    year, month_num = (int(part) for part in month.split("-"))
    if end:
        month_num += 1
        if month_num == 13:
            year += 1
            month_num = 1
    return f"{year:04d}-{month_num:02d}-01T00:00:00+00:00"


def _classify_symbol(symbol: str, base: str, in_current_master: bool, excluded_bases: set[str]) -> tuple[str, str, str, str]:
    if in_current_master:
        return "current_master_present", "included_current_master", "high", ""
    if symbol.endswith(EXCLUDED_SUFFIXES):
        return "leveraged_token", "exclude_nonstandard_suffix", "high", "leveraged token suffix"
    if base in excluded_bases or base in KNOWN_STABLE_OR_FIAT_BASES:
        return "stable_or_fiat_or_excluded_base", "exclude_existing_or_equivalent_base_filter", "high", "stable/fiat/excluded base"
    if base in KNOWN_NONSTANDARD_BASES:
        return "nonstandard_wrapped_or_staked_asset", "exclude_manual_nonstandard_asset", "medium", "wrapped/staked/nonstandard asset"
    if base in KNOWN_RENAME_OR_MIGRATION_HINTS:
        return "standard_spot_rename_or_migration_candidate", "historical_standard_gap_manual_mapping_needed", "medium", KNOWN_RENAME_OR_MIGRATION_HINTS[base]
    return "standard_spot_missing_from_current_master", "historical_standard_gap", "medium", "not in current exchangeInfo-derived master"


def build_dataset(args: argparse.Namespace) -> dict:
    settings = load_settings(Path(args.settings))
    quote_asset = settings.market.quote_asset
    excluded_bases = {item.upper() for item in settings.market.exclude_bases}
    historical_rows = json.loads(Path(args.historical_membership_json).read_text(encoding="utf-8"))
    current_rows = json.loads(Path(args.current_master_json).read_text(encoding="utf-8"))
    current_lookup = {row["symbol"]: row for row in current_rows}

    rows = []
    for row in sorted(historical_rows, key=lambda item: item["symbol"]):
        symbol = row["symbol"]
        base = _base(symbol, quote_asset)
        in_current_master = bool(row.get("in_current_master"))
        symbol_type, eligibility_class, confidence, exclusion_reason = _classify_symbol(
            symbol,
            base,
            in_current_master,
            excluded_bases,
        )
        first_month = row["first_month"]
        last_month = row["last_month"]
        current_row = current_lookup.get(symbol, {})
        rows.append(
            {
                "symbol": symbol,
                "base_asset": base,
                "quote_asset": quote_asset,
                "first_kline_month": first_month,
                "last_kline_month": last_month,
                "first_kline_time": _month_to_time(first_month),
                "last_kline_time": _month_to_time(last_month, end=True),
                "tradable_from": _month_to_time(first_month),
                "tradable_to": _month_to_time(last_month, end=True),
                "months_in_window": row["months_in_window"],
                "months_in_window_count": row["months_in_window_count"],
                "present_in_current_master": in_current_master,
                "current_master_listing_date": current_row.get("listing_date"),
                "current_master_classification": current_row.get("classification"),
                "symbol_type": symbol_type,
                "eligibility_class": eligibility_class,
                "source": "Binance public-data spot monthly 1d kline object listing",
                "confidence": confidence,
                "exclusion_reason": exclusion_reason,
            }
        )

    type_counts = Counter(row["symbol_type"] for row in rows)
    missing_rows = [row for row in rows if not row["present_in_current_master"]]
    missing_type_counts = Counter(row["symbol_type"] for row in missing_rows)
    recoverable_exclusions = {
        "leveraged_token",
        "stable_or_fiat_or_excluded_base",
        "nonstandard_wrapped_or_staked_asset",
    }
    excludable_missing = [row for row in missing_rows if row["symbol_type"] in recoverable_exclusions]
    standard_gap_rows = [row for row in missing_rows if row["symbol_type"] not in recoverable_exclusions]
    standard_universe_rows = [row for row in rows if row["symbol_type"] not in recoverable_exclusions]
    standard_gap_ratio = (len(standard_gap_rows) / len(standard_universe_rows) * 100) if standard_universe_rows else 0.0
    if len(standard_gap_rows) > max(10, int(len(standard_universe_rows) * 0.05)):
        verdict = "third_window_not_recoverable_without_historical_master"
        reason = "Standard-like historical symbol gap remains material after excluding leveraged, stable/fiat, and nonstandard assets."
    else:
        verdict = "third_window_potentially_recoverable_with_documented_limitations"
        reason = "Most missing historical symbols are explainable by existing or equivalent exclusion rules."

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "start": args.start,
        "end": args.end,
        "historical_membership_json": str(Path(args.historical_membership_json)),
        "current_master_json": str(Path(args.current_master_json)),
        "total_historical_symbols": len(rows),
        "present_in_current_master": sum(1 for row in rows if row["present_in_current_master"]),
        "missing_from_current_master": len(missing_rows),
        "excludable_missing_count": len(excludable_missing),
        "standard_gap_count": len(standard_gap_rows),
        "standard_universe_count": len(standard_universe_rows),
        "standard_gap_ratio_pct": standard_gap_ratio,
        "symbol_type_counts": dict(sorted(type_counts.items())),
        "missing_symbol_type_counts": dict(sorted(missing_type_counts.items())),
        "standard_gap_examples": [row["symbol"] for row in standard_gap_rows[:80]],
        "excludable_missing_examples": [row["symbol"] for row in excludable_missing[:80]],
        "verdict": verdict,
        "reason": reason,
        "rows": rows,
    }


def render_report(audit: dict, artifacts: dict[str, str]) -> str:
    lines = [
        "---",
        f"created: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - historical-membership",
        "experiment: atr_reclaim_stage_n3_historical_membership_dataset",
        f"verdict: {audit['verdict']}",
        "---",
        "",
        "# Stage N3 Historical Membership Dataset MVP",
        "",
        "## Plain-language conclusion",
        "",
        (
            "The third window still should not be rescued for validation. After excluding obvious leveraged tokens, "
            "stable/fiat pairs, and known nonstandard assets, the missing historical standard-like spot gap remains material."
            if audit["verdict"] == "third_window_not_recoverable_without_historical_master"
            else "The third window may be recoverable, but only with documented universe limitations and a reconstructed historical master."
        ),
        "",
        "## Artifacts",
        "",
        "| Artifact | Path |",
        "|---|---|",
    ]
    for key, value in artifacts.items():
        lines.append(f"| {key} | `{value}` |")
    lines.extend(
        [
            "",
            "## Scope",
            "",
            f"- Window: `{audit['start']} -> {audit['end']}`",
            f"- Historical symbols: `{audit['total_historical_symbols']}`",
            f"- Present in current master: `{audit['present_in_current_master']}`",
            f"- Missing from current master: `{audit['missing_from_current_master']}`",
            "",
            "## Missing Symbol Classification",
            "",
            "| Metric | Value |",
            "|---|---:|",
            f"| excludable_missing_count | {audit['excludable_missing_count']} |",
            f"| standard_gap_count | {audit['standard_gap_count']} |",
            f"| standard_universe_count | {audit['standard_universe_count']} |",
            f"| standard_gap_ratio_pct | {audit['standard_gap_ratio_pct']:.2f} |",
            "",
            "### Missing Type Counts",
            "",
            "| Type | Count |",
            "|---|---:|",
        ]
    )
    for key, value in audit["missing_symbol_type_counts"].items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "### Standard-like missing examples",
            "",
            "`" + "`, `".join(audit["standard_gap_examples"][:80]) + "`",
            "",
            "### Excludable missing examples",
            "",
            "`" + "`, `".join(audit["excludable_missing_examples"][:80]) + "`",
            "",
            "## Verdict",
            "",
            f"`{audit['verdict']}`",
            "",
            audit["reason"],
            "",
            "## Decision",
            "",
            "Do not rerun corrected N1 on the third window until a historical master can add or explicitly exclude the standard-like missing symbols with source-backed rules.",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(
                {
                    "total_historical_symbols": audit["total_historical_symbols"],
                    "present_in_current_master": audit["present_in_current_master"],
                    "missing_from_current_master": audit["missing_from_current_master"],
                    "excludable_missing_count": audit["excludable_missing_count"],
                    "standard_gap_count": audit["standard_gap_count"],
                    "standard_universe_count": audit["standard_universe_count"],
                    "standard_gap_ratio_pct": audit["standard_gap_ratio_pct"],
                    "missing_symbol_type_counts": audit["missing_symbol_type_counts"],
                    "standard_gap_examples": audit["standard_gap_examples"][:80],
                    "verdict": audit["verdict"],
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
    parser = argparse.ArgumentParser(description="Build Stage N3 historical membership dataset MVP.")
    parser.add_argument("--settings", default="config/settings.toml")
    parser.add_argument("--historical-membership-json", required=True)
    parser.add_argument("--current-master-json", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--reports-date", required=True)
    args = parser.parse_args()

    settings = load_settings(Path(args.settings))
    audit = build_dataset(args)
    report_dir = settings.output.reports_dir / args.reports_date
    report_dir.mkdir(parents=True, exist_ok=True)
    prefix = f"atr_reclaim_stage_n3_historical_membership_dataset_{args.reports_date}"
    version = next_report_version([report_dir], prefix)
    dataset_path = report_dir / versioned_markdown_filename(prefix + "_dataset", version).replace(".md", ".json")
    raw_path = report_dir / versioned_markdown_filename(prefix + "_raw", version).replace(".md", ".json")
    report_path = report_dir / versioned_markdown_filename(prefix, version)
    dataset_path.write_text(json.dumps(audit["rows"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raw_copy = {key: value for key, value in audit.items() if key != "rows"}
    raw_path.write_text(json.dumps(raw_copy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    artifacts = {
        "dataset_json": str(dataset_path),
        "raw_summary_json": str(raw_path),
    }
    report_path.write_text(render_report(audit, artifacts), encoding="utf-8")
    print("n3_historical_membership_dataset=completed")
    print(f"verdict={audit['verdict']}")
    print(f"missing_from_current_master={audit['missing_from_current_master']}")
    print(f"excludable_missing_count={audit['excludable_missing_count']}")
    print(f"standard_gap_count={audit['standard_gap_count']}")
    print(f"standard_gap_ratio_pct={audit['standard_gap_ratio_pct']:.2f}")
    print(f"report={report_path}")
    print(f"dataset={dataset_path}")


if __name__ == "__main__":
    main()
