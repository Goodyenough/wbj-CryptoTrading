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
from crypto_trading_system.report_versions import next_report_version, versioned_markdown_filename  # noqa: E402


BLOCKING_TYPES = {
    "standard_spot_missing_from_current_master",
    "standard_spot_rename_or_migration_candidate",
}

EXCLUDABLE_TYPES = {
    "leveraged_token",
    "stable_or_fiat_or_excluded_base",
    "nonstandard_wrapped_or_staked_asset",
}


def _status_for(row: dict) -> tuple[str, str, str, str]:
    if row["present_in_current_master"]:
        return (
            "active_current_master",
            "eligible_for_dynamic_universe_if_data_and_liquidity_pass",
            "high",
            "current exchangeInfo-derived master and Binance public-data kline existence",
        )
    if row["symbol_type"] in EXCLUDABLE_TYPES:
        return (
            "excluded_by_strategy_universe_rule",
            "exclude_from_historical_master",
            "high",
            f"existing or equivalent exclusion rule: {row['exclusion_reason']}",
        )
    if row["symbol_type"] == "standard_spot_rename_or_migration_candidate":
        return (
            "historical_standard_gap_requires_mapping",
            "manual_review_rename_or_migration_before_validation",
            "medium",
            f"public-data kline existence; migration hint: {row['exclusion_reason']}",
        )
    return (
        "historical_standard_gap_requires_mapping",
        "manual_review_delisting_or_exclusion_before_validation",
        "medium",
        "public-data kline existence; absent from current exchangeInfo-derived master",
    )


def build_master(args: argparse.Namespace) -> dict:
    rows = json.loads(Path(args.n3_dataset_json).read_text(encoding="utf-8"))
    master_rows = []
    review_queue = []
    for row in sorted(rows, key=lambda item: item["symbol"]):
        status, action, confidence, evidence = _status_for(row)
        master_row = {
            "symbol": row["symbol"],
            "base_asset": row["base_asset"],
            "quote_asset": row["quote_asset"],
            "listing_time": None,
            "delisting_time": None,
            "first_kline_time": row["first_kline_time"],
            "last_kline_time": row["last_kline_time"],
            "tradable_from": row["tradable_from"],
            "tradable_to": row["tradable_to"],
            "first_kline_month": row["first_kline_month"],
            "last_kline_month": row["last_kline_month"],
            "months_in_window_count": row["months_in_window_count"],
            "present_in_current_master": row["present_in_current_master"],
            "symbol_type": row["symbol_type"],
            "membership_status": status,
            "operational_action": action,
            "source": row["source"],
            "source_evidence": evidence,
            "confidence": confidence,
            "limitations": (
                "listing_time and delisting_time require official announcement or exchangeInfo archive; "
                "public-data kline months are used only as observed availability bounds."
            ),
        }
        master_rows.append(master_row)
        if row["symbol_type"] in BLOCKING_TYPES and not row["present_in_current_master"]:
            review_queue.append(
                {
                    "symbol": row["symbol"],
                    "base_asset": row["base_asset"],
                    "symbol_type": row["symbol_type"],
                    "first_kline_month": row["first_kline_month"],
                    "last_kline_month": row["last_kline_month"],
                    "months_in_window_count": row["months_in_window_count"],
                    "review_question": (
                        "Was this a normal spot asset that should be included in the historical universe, "
                        "or should it be mapped/excluded because of delisting, migration, or strategy eligibility rules?"
                    ),
                    "minimum_sources_needed": [
                        "Binance listing or delisting announcement when available",
                        "Binance public-data kline availability",
                        "Current or archived symbol mapping if renamed/migrated",
                    ],
                }
            )

    status_counts = Counter(row["membership_status"] for row in master_rows)
    action_counts = Counter(row["operational_action"] for row in master_rows)
    blocking_count = len(review_queue)
    if blocking_count:
        verdict = "historical_master_mvp_built_validation_blocked"
        reason = f"{blocking_count} standard-like historical symbols still require source-backed mapping before validation."
    else:
        verdict = "historical_master_mvp_validation_ready_with_limitations"
        reason = "No blocking standard-like missing symbols remain after rule-based exclusions."
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "start": args.start,
        "end": args.end,
        "n3_dataset_json": str(Path(args.n3_dataset_json)),
        "total_rows": len(master_rows),
        "membership_status_counts": dict(sorted(status_counts.items())),
        "operational_action_counts": dict(sorted(action_counts.items())),
        "blocking_review_count": blocking_count,
        "review_queue_examples": review_queue[:80],
        "verdict": verdict,
        "reason": reason,
        "master_rows": master_rows,
        "review_queue": review_queue,
    }


def render_report(audit: dict, artifacts: dict[str, str]) -> str:
    lines = [
        "---",
        f"created: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - historical-master",
        "experiment: atr_reclaim_stage_n4_historical_master_mvp",
        f"verdict: {audit['verdict']}",
        "---",
        "",
        "# Stage N4 Historical Master MVP",
        "",
        "## Plain-language conclusion",
        "",
        (
            "A first historical master dataset now exists, but it is not validation-ready because standard-like missing symbols still need source-backed mapping."
            if audit["blocking_review_count"]
            else "A first historical master dataset exists and has no blocking standard-like missing symbols after rule-based exclusions."
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
            f"- Historical master rows: `{audit['total_rows']}`",
            f"- Blocking review queue: `{audit['blocking_review_count']}`",
            "",
            "## Membership Status Counts",
            "",
            "| Status | Count |",
            "|---|---:|",
        ]
    )
    for key, value in audit["membership_status_counts"].items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Operational Action Counts",
            "",
            "| Action | Count |",
            "|---|---:|",
        ]
    )
    for key, value in audit["operational_action_counts"].items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## Review Queue Examples",
            "",
            "| Symbol | Type | First Month | Last Month | Window Months |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for row in audit["review_queue_examples"][:50]:
        lines.append(
            f"| `{row['symbol']}` | `{row['symbol_type']}` | `{row['first_kline_month']}` | `{row['last_kline_month']}` | {row['months_in_window_count']} |"
        )
    lines.extend(
        [
            "",
            "## Verdict",
            "",
            f"`{audit['verdict']}`",
            "",
            audit["reason"],
            "",
            "## Decision",
            "",
            "Do not connect this MVP historical master to A/B execution yet. It is a data-engineering artifact until the blocking review queue is resolved or quantified as immaterial.",
            "",
            "## Raw Summary",
            "",
            "```json",
            json.dumps(
                {
                    "total_rows": audit["total_rows"],
                    "membership_status_counts": audit["membership_status_counts"],
                    "operational_action_counts": audit["operational_action_counts"],
                    "blocking_review_count": audit["blocking_review_count"],
                    "verdict": audit["verdict"],
                    "reason": audit["reason"],
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
    parser = argparse.ArgumentParser(description="Build a source-backed historical master MVP from N3 dataset.")
    parser.add_argument("--settings", default="config/settings.toml")
    parser.add_argument("--n3-dataset-json", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--reports-date", required=True)
    args = parser.parse_args()

    settings = load_settings(Path(args.settings))
    audit = build_master(args)
    report_dir = settings.output.reports_dir / args.reports_date
    report_dir.mkdir(parents=True, exist_ok=True)
    prefix = f"atr_reclaim_stage_n4_historical_master_mvp_{args.reports_date}"
    version = next_report_version([report_dir], prefix)
    master_path = report_dir / versioned_markdown_filename(prefix + "_master", version).replace(".md", ".json")
    queue_path = report_dir / versioned_markdown_filename(prefix + "_review_queue", version).replace(".md", ".json")
    raw_path = report_dir / versioned_markdown_filename(prefix + "_raw", version).replace(".md", ".json")
    report_path = report_dir / versioned_markdown_filename(prefix, version)
    master_path.write_text(json.dumps(audit["master_rows"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    queue_path.write_text(json.dumps(audit["review_queue"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raw_copy = {key: value for key, value in audit.items() if key not in {"master_rows", "review_queue"}}
    raw_path.write_text(json.dumps(raw_copy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    artifacts = {
        "historical_master_mvp_json": str(master_path),
        "blocking_review_queue_json": str(queue_path),
        "raw_summary_json": str(raw_path),
    }
    report_path.write_text(render_report(audit, artifacts), encoding="utf-8")
    print("n4_historical_master_mvp=completed")
    print(f"verdict={audit['verdict']}")
    print(f"total_rows={audit['total_rows']}")
    print(f"blocking_review_count={audit['blocking_review_count']}")
    print(f"report={report_path}")
    print(f"historical_master={master_path}")
    print(f"review_queue={queue_path}")


if __name__ == "__main__":
    main()
