from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from crypto_trading_system.abtest import run_abtest
from crypto_trading_system.abtest_summary import (
    build_abtest_summary,
    load_abtest_records,
    parse_abtest_report,
    select_non_overlapping_records,
    write_abtest_summary_report,
)
from crypto_trading_system.abtest_walk_forward import parse_period_specs
from crypto_trading_system.backtest.regime_analysis import build_regime_comparison, write_regime_comparison_report
from crypto_trading_system.backtest.universe import build_current_symbol_master, load_symbol_master, save_symbol_master
from crypto_trading_system.backtest.runner import run_backtest
from crypto_trading_system.config import load_settings
from crypto_trading_system.database import database_status, mark_run_failed, tracked_run
from crypto_trading_system.doctor import run_doctor
from crypto_trading_system.paper_trader import add_from_scan, generate_paper_report, update_paper_trades
from crypto_trading_system.paper_db import (
    audit_database_stability,
    build_paper_db_summary,
    export_paper_db,
    load_paper_db_events,
)
from crypto_trading_system.reports import write_scan_reports
from crypto_trading_system.research_tools import (
    build_experiment_index,
    generate_observation_dashboard,
    split_symbol_master_by_cap,
)
from crypto_trading_system.scanner import run_market_scan
from crypto_trading_system.storage import init_db, save_scan_result, update_market_scan_report_path
from crypto_trading_system.verify import verify_symbol


def _prepare_dynamic_symbol_master(settings, args):
    master_file = getattr(args, "symbol_master_file", None)
    write_master = getattr(args, "write_symbol_master", None)
    source_limit = getattr(args, "source_limit", None)
    if master_file and source_limit is not None:
        raise ValueError("--symbol-master-file and --source-limit are mutually exclusive; the file already fixes the master.")
    if master_file:
        master = load_symbol_master(Path(master_file))
        _progress(f"loaded dynamic symbol master from {master_file} ({len(master.symbols)} symbols)")
    else:
        master = build_current_symbol_master(settings, source_limit=source_limit, progress=_progress)
    if write_master:
        save_symbol_master(master, Path(write_master))
        _progress(f"wrote dynamic symbol master to {write_master}")
    return master


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CryptoTradingSystem MVP")
    parser.add_argument(
        "--settings",
        default="config/settings.toml",
        help="Path to TOML settings file.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor", help="Check API connectivity, local paths, and database readiness.")

    db = subparsers.add_parser("db", help="Initialize and inspect the SQLite observation database.")
    db_subparsers = db.add_subparsers(dest="db_command", required=True)
    db_subparsers.add_parser("init", help="Create or migrate the database schema.")
    db_subparsers.add_parser("status", help="Show schema, PRAGMA, run, and open-plan status.")
    db_stability = db_subparsers.add_parser(
        "stability",
        help="Audit the consecutive daily_full gate required before enabling the 4h task.",
    )
    db_stability.add_argument("--days", type=int, default=5, help="Required consecutive successful days.")
    db_mark_failed = db_subparsers.add_parser(
        "mark-run-failed",
        help="Mark one stale running observation run as failed.",
    )
    db_mark_failed.add_argument("--run-id", required=True, help="Run id to mark failed.")
    db_mark_failed.add_argument("--reason", required=True, help="Operational reason recorded in runs.error_message.")

    scan = subparsers.add_parser("scan", help="Scan the market and write reports.")
    scan.add_argument("--top", type=int, default=None, help="Override number of candidates.")
    scan.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    daily = subparsers.add_parser("daily", help="Run daily scan, import candidates, update paper trades, and write reports.")
    daily.add_argument("--top", type=int, default=None, help="Override number of scan candidates.")
    daily.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")
    daily.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    verify = subparsers.add_parser("verify", help="Verify one symbol and write an evidence report.")
    verify.add_argument("--symbol", required=True, help="Symbol to verify, e.g. ZECUSDT or ZEC/USDT.")
    verify.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    backtest = subparsers.add_parser("backtest", help="Replay historical klines and write a backtest report.")
    backtest.add_argument("--symbols", required=True, help="Comma-separated symbols, e.g. BTCUSDT,ETHUSDT.")
    backtest.add_argument("--start", required=True, help="UTC start date, e.g. 2024-01-01.")
    backtest.add_argument("--end", required=True, help="UTC end date, e.g. 2024-12-31.")
    backtest.add_argument("--interval", default=None, help="Primary interval. MVP supports 4h.")
    backtest.add_argument("--intrabar", default=None, choices=["stop_first", "tp_first"], help="Intrabar fill policy.")
    backtest.add_argument("--allow-data-gaps", action="store_true", help="Continue when historical kline gaps are found.")
    backtest.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    backtest_universe = subparsers.add_parser(
        "backtest-universe",
        help="Build a current Binance universe snapshot, replay historical klines, and write a backtest report.",
    )
    backtest_universe.add_argument("--start", required=True, help="UTC start date, e.g. 2024-01-01.")
    backtest_universe.add_argument("--end", required=True, help="UTC end date, e.g. 2024-12-31.")
    backtest_universe.add_argument(
        "--max-symbols",
        type=int,
        default=None,
        help="Override settings.market.max_universe for this universe snapshot.",
    )
    backtest_universe.add_argument("--interval", default=None, help="Primary interval. MVP supports 4h.")
    backtest_universe.add_argument(
        "--intrabar",
        default=None,
        choices=["stop_first", "tp_first"],
        help="Intrabar fill policy.",
    )
    backtest_universe.add_argument(
        "--allow-data-gaps",
        action="store_true",
        help="Continue when historical kline gaps are found.",
    )
    backtest_universe.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    backtest_dynamic = subparsers.add_parser(
        "backtest-dynamic-universe",
        help="Rebuild the historical universe daily from closed klines, replay trades, and write a backtest report.",
    )
    backtest_dynamic.add_argument("--start", required=True, help="UTC start date, e.g. 2024-01-01.")
    backtest_dynamic.add_argument("--end", required=True, help="UTC end date, e.g. 2024-12-31.")
    backtest_dynamic.add_argument(
        "--max-symbols",
        type=int,
        default=None,
        help="Daily dynamic universe size. Defaults to settings.market.max_universe.",
    )
    backtest_dynamic.add_argument(
        "--source-limit",
        type=int,
        default=None,
        help="Debug only: sort master symbols alphabetically and keep the first N before loading history.",
    )
    backtest_dynamic.add_argument(
        "--symbol-master-file",
        default=None,
        help="Load a previously saved dynamic symbol master JSON instead of current exchangeInfo.",
    )
    backtest_dynamic.add_argument(
        "--write-symbol-master",
        default=None,
        help="Write the dynamic symbol master JSON used by this run.",
    )
    backtest_dynamic.add_argument("--interval", default=None, help="Primary interval. MVP supports 4h.")
    backtest_dynamic.add_argument(
        "--intrabar",
        default=None,
        choices=["stop_first", "tp_first"],
        help="Intrabar fill policy.",
    )
    backtest_dynamic.add_argument(
        "--allow-data-gaps",
        action="store_true",
        help="Continue when historical kline gaps are found.",
    )
    backtest_dynamic.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    dynamic_master = subparsers.add_parser(
        "dynamic-symbol-master",
        help="Export the current dynamic universe symbol master JSON without running a backtest.",
    )
    dynamic_master.add_argument("--output", required=True, help="Output JSON path for the symbol master.")
    dynamic_master.add_argument(
        "--source-limit",
        type=int,
        default=None,
        help="Optional debug cap: sort master symbols alphabetically and keep the first N.",
    )
    dynamic_master.add_argument(
        "--fetch-listing-dates",
        action="store_true",
        help="Query Binance for each symbol's first 1d candle date and store in the master JSON.",
    )

    split_master = subparsers.add_parser(
        "split-symbol-master",
        help="Split a dynamic symbol master into large-cap and altcoin JSON files.",
    )
    split_master.add_argument("--input", required=True, help="Input dynamic symbol master JSON.")
    split_master.add_argument("--output-dir", default=None, help="Output directory. Defaults to input file directory.")

    regime_breakdown = subparsers.add_parser(
        "backtest-regime-breakdown",
        help="Group saved backtest trades by BTC/ETH market regime and write a comparison report.",
    )
    regime_breakdown.add_argument("--baseline-run-id", required=True, help="Baseline backtest run_id from an A/B report.")
    regime_breakdown.add_argument("--variant-run-id", required=True, help="Variant backtest run_id from an A/B report.")
    regime_breakdown.add_argument("--reports-date", default=None, help="Reports date directory, default today.")
    regime_breakdown.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    abtest = subparsers.add_parser("abtest", help="Run baseline versus variant backtests for one experiment.")
    abtest.add_argument("--experiment", required=True, help="Experiment id from config/experiments.toml.")
    abtest.add_argument("--experiments", default="config/experiments.toml", help="Path to TOML experiment definitions.")
    abtest.add_argument("--symbols", default=None, help="Comma-separated symbols, e.g. BTCUSDT,ETHUSDT.")
    abtest.add_argument(
        "--dynamic-universe",
        action="store_true",
        help="Run baseline and variant with the same daily dynamic universe master list.",
    )
    abtest.add_argument(
        "--max-symbols",
        type=int,
        default=None,
        help="Daily dynamic universe size when --dynamic-universe is used.",
    )
    abtest.add_argument(
        "--source-limit",
        type=int,
        default=None,
        help="Debug only: limit the dynamic universe master list when --dynamic-universe is used.",
    )
    abtest.add_argument(
        "--symbol-master-file",
        default=None,
        help="Load a previously saved dynamic symbol master JSON for --dynamic-universe.",
    )
    abtest.add_argument(
        "--write-symbol-master",
        default=None,
        help="Write the dynamic symbol master JSON used by --dynamic-universe.",
    )
    abtest.add_argument("--start", required=True, help="UTC start date, e.g. 2024-01-01.")
    abtest.add_argument("--end", required=True, help="UTC end date, e.g. 2024-12-31.")
    abtest.add_argument("--interval", default=None, help="Primary interval. MVP supports 4h.")
    abtest.add_argument("--intrabar", default=None, choices=["stop_first", "tp_first"], help="Intrabar fill policy.")
    abtest.add_argument("--allow-data-gaps", action="store_true", help="Continue when historical kline gaps are found.")
    abtest.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    abtest_summary = subparsers.add_parser("abtest-summary", help="Summarize existing A/B reports across periods.")
    abtest_summary.add_argument("--experiment", required=True, help="Experiment id, e.g. liquidity_50m.")
    abtest_summary.add_argument(
        "--mode",
        default="dynamic_universe",
        choices=["dynamic_universe", "symbols"],
        help="A/B report mode to summarize.",
    )
    abtest_summary.add_argument(
        "--reports-date",
        default=None,
        help="Project reports date directory to read and write, e.g. 2026-06-09. Defaults to today in Beijing time.",
    )
    abtest_summary.add_argument("--start", default=None, help="Optional inclusive start-date filter.")
    abtest_summary.add_argument("--end", default=None, help="Optional inclusive end-date filter.")
    abtest_summary.add_argument(
        "--drop-overlap-periods",
        action="store_true",
        help="Keep the largest earliest-ending set of non-overlapping reports before summarizing.",
    )
    abtest_summary.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    abtest_walk_forward = subparsers.add_parser(
        "abtest-walk-forward",
        help="Run one A/B experiment across multiple periods and write a summary report.",
    )
    abtest_walk_forward.add_argument("--experiment", required=True, help="Experiment id from config/experiments.toml.")
    abtest_walk_forward.add_argument("--experiments", default="config/experiments.toml", help="Path to TOML experiment definitions.")
    abtest_walk_forward.add_argument(
        "--periods",
        required=True,
        help="Comma-separated START:END periods, e.g. 2025-01-01:2025-06-01,2025-06-01:2026-01-01.",
    )
    abtest_walk_forward.add_argument("--symbols", default=None, help="Comma-separated symbols unless --dynamic-universe is used.")
    abtest_walk_forward.add_argument(
        "--dynamic-universe",
        action="store_true",
        help="Run each period with daily dynamic universe reconstruction.",
    )
    abtest_walk_forward.add_argument("--max-symbols", type=int, default=None, help="Daily dynamic universe size.")
    abtest_walk_forward.add_argument("--source-limit", type=int, default=None, help="Debug only: limit dynamic symbol master.")
    abtest_walk_forward.add_argument(
        "--symbol-master-file",
        default=None,
        help="Load a previously saved dynamic symbol master JSON for all dynamic-universe periods.",
    )
    abtest_walk_forward.add_argument(
        "--write-symbol-master",
        default=None,
        help="Write the dynamic symbol master JSON used for all dynamic-universe periods.",
    )
    abtest_walk_forward.add_argument("--interval", default=None, help="Primary interval. MVP supports 4h.")
    abtest_walk_forward.add_argument("--intrabar", default=None, choices=["stop_first", "tp_first"], help="Intrabar fill policy.")
    abtest_walk_forward.add_argument("--allow-data-gaps", action="store_true", help="Continue when historical kline gaps are found.")
    abtest_walk_forward.add_argument(
        "--reports-date",
        default=None,
        help="Summary report date directory, e.g. 2026-06-09. Defaults to today in Beijing time.",
    )
    abtest_walk_forward.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    experiment_index = subparsers.add_parser("experiment-index", help="Build a Markdown index of A/B conclusions.")
    experiment_index.add_argument(
        "--reports-dir",
        default=None,
        help="Reports root or date directory to scan. Defaults to settings.output.reports_dir.",
    )
    experiment_index.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    observation_dashboard = subparsers.add_parser(
        "observation-dashboard",
        help="Write the three-week paper-trading observation dashboard.",
    )
    observation_dashboard.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")
    observation_dashboard.add_argument(
        "--no-obsidian",
        action="store_true",
        help="Write only to the project reports directory.",
    )

    paper = subparsers.add_parser("paper", help="Manage paper trading watchlist and positions.")
    paper_subparsers = paper.add_subparsers(dest="paper_command", required=True)

    add_scan = paper_subparsers.add_parser("add-from-scan", help="Add scan candidates to paper watchlist.")
    add_scan.add_argument("--scan-id", default=None, help="Scan id to import. Defaults to latest market scan.")
    add_scan.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")

    paper_update = paper_subparsers.add_parser("update", help="Update paper trades using current market prices.")
    paper_update.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")
    paper_update.add_argument(
        "--run-type",
        default="manual",
        choices=["manual", "paper_4h_update"],
        help="Run classification stored in SQLite.",
    )

    paper_report = paper_subparsers.add_parser("report", help="Write a paper trading report.")
    paper_report.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")

    paper_summary = paper_subparsers.add_parser("db-summary", help="Summarize runs, plans, events, and snapshots.")
    paper_summary.add_argument("--limit", type=int, default=10, help="Maximum recent and failed runs to show.")

    paper_events = paper_subparsers.add_parser("db-events", help="Show structured paper events.")
    paper_events.add_argument("--plan-id", default=None, help="Optional plan id filter.")
    paper_events.add_argument("--limit", type=int, default=200, help="Maximum events to show.")

    paper_export = paper_subparsers.add_parser("db-export", help="Export plans, events, and snapshots as CSV.")
    paper_export.add_argument("--output-dir", default="exports", help="CSV output directory.")

    paper_cycle = paper_subparsers.add_parser(
        "cycle",
        help="Update existing plans and write report/dashboard without scanning or creating plans.",
    )
    paper_cycle.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")
    paper_cycle.add_argument(
        "--run-type",
        default="paper_4h_update",
        choices=["paper_4h_update", "manual"],
        help="Run classification stored in SQLite.",
    )
    paper_cycle.add_argument("--no-obsidian", action="store_true", help="Write only project reports.")
    return parser


def _progress(message: str) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def _run_scan_and_write(settings, include_obsidian: bool, progress=None, run_id: str | None = None):
    result = run_market_scan(settings, progress=progress)
    if progress is not None:
        progress("saving scan result to SQLite")
    init_db(settings.output.database_path)
    save_scan_result(settings.output.database_path, result, run_id=run_id)
    if progress is not None:
        progress("writing Markdown reports")
    report_paths = write_scan_reports(
        result,
        settings,
        include_obsidian=include_obsidian,
        run_id=run_id,
        run_type="daily_full" if run_id else "manual",
    )
    if run_id is not None and report_paths:
        update_market_scan_report_path(settings.output.database_path, result.scan_id, report_paths[0])
    return result, report_paths


@contextmanager
def _run_step(run_id: str, step: str):
    try:
        yield
    except Exception as exc:
        raise RuntimeError(f"run_id={run_id} step={step}: {type(exc).__name__}: {exc}") from exc


def _run_paper_cycle(settings, *, account_name: str | None, run_type: str, no_obsidian: bool, settings_path: Path):
    init_db(settings.output.database_path)
    with tracked_run(
        settings.output.database_path,
        run_type,
        settings_path=settings_path,
        project_root=PROJECT_ROOT,
        log_path=PROJECT_ROOT / "logs" / "paper_4h_update.log",
    ) as run_id:
        with _run_step(run_id, "paper_update"):
            updated = update_paper_trades(settings, account_name=account_name, run_id=run_id)
        with _run_step(run_id, "paper_report"):
            _, report_paths = generate_paper_report(
                settings,
                account_name=account_name,
                run_id=run_id,
                run_type=run_type,
            )
        original_obsidian = settings.output.obsidian_dir
        try:
            if no_obsidian:
                settings.output.obsidian_dir = None
            with _run_step(run_id, "observation_dashboard"):
                _, dashboard_paths = generate_observation_dashboard(
                    settings,
                    account_name=account_name,
                    run_id=run_id,
                    run_type=run_type,
                )
        finally:
            settings.output.obsidian_dir = original_obsidian
    return run_id, updated, report_paths, dashboard_paths


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    settings = load_settings(Path(args.settings))
    settings_path = Path(args.settings).resolve()

    if args.command == "db":
        init_db(settings.output.database_path)
        if args.db_command == "init":
            print(f"database_initialized={settings.output.database_path.resolve()}")
        if args.db_command == "status":
            status = database_status(settings.output.database_path)
            print(json.dumps(status, ensure_ascii=False, indent=2))
        if args.db_command == "stability":
            audit = audit_database_stability(
                settings.output.database_path,
                settings.output.reports_dir,
                required_days=args.days,
            )
            print(json.dumps(audit, ensure_ascii=False, indent=2))
            if not audit["ready_for_4h_task"]:
                sys.exit(2)
        if args.db_command == "mark-run-failed":
            run = mark_run_failed(settings.output.database_path, args.run_id, reason=args.reason)
            print(json.dumps(run, ensure_ascii=False, indent=2))
        return

    if args.command == "scan" and args.top is not None:
        settings.market.top_n = args.top

    if args.command == "daily" and args.top is not None:
        settings.market.top_n = args.top

    if args.command == "doctor":
        checks = run_doctor(settings)
        print("doctor=completed")
        for check in checks:
            print(f"{check.name}: {check.status} - {check.message}")
        if any(check.status == "FAIL" for check in checks):
            sys.exit(1)

    if args.command == "scan":
        result, report_paths = _run_scan_and_write(settings, include_obsidian=not args.no_obsidian, progress=_progress)
        print(f"scan_id={result.scan_id}")
        print(f"candidates={len(result.candidates)}")
        for path in report_paths:
            print(f"report={path}")

    if args.command == "daily":
        init_db(settings.output.database_path)
        with tracked_run(
            settings.output.database_path,
            "daily_full",
            settings_path=settings_path,
            project_root=PROJECT_ROOT,
            log_path=PROJECT_ROOT / "logs" / "daily_paper_update.log",
        ) as run_id:
            print(f"run_id={run_id}")
            with _run_step(run_id, "scan"):
                result, scan_report_paths = _run_scan_and_write(
                    settings,
                    include_obsidian=not args.no_obsidian,
                    progress=_progress,
                    run_id=run_id,
                )
            _progress("adding latest candidates to paper trading")
            with _run_step(run_id, "add_from_scan"):
                summary = add_from_scan(
                    settings,
                    scan_id=result.scan_id,
                    account_name=args.account,
                    run_id=run_id,
                )
            _progress("updating paper trading positions")
            with _run_step(run_id, "paper_update"):
                updated = update_paper_trades(settings, account_name=args.account, run_id=run_id)
            _progress("writing paper trading report")
            with _run_step(run_id, "paper_report"):
                _, paper_report_paths = generate_paper_report(
                    settings,
                    account_name=args.account,
                    run_id=run_id,
                    run_type="daily_full",
                )
            _progress("writing three-week observation dashboard")
            original_obsidian = settings.output.obsidian_dir
            try:
                if args.no_obsidian:
                    settings.output.obsidian_dir = None
                with _run_step(run_id, "observation_dashboard"):
                    _, observation_paths = generate_observation_dashboard(
                        settings,
                        account_name=args.account,
                        run_id=run_id,
                        run_type="daily_full",
                    )
            finally:
                settings.output.obsidian_dir = original_obsidian

            print("daily=completed")
            print(f"scan_id={result.scan_id}")
            print(f"candidates={len(result.candidates)}")
            print(f"paper_added={summary['added']}")
            print(f"paper_skipped={summary['skipped']}")
            print(f"paper_skipped_action={summary.get('skipped_action', 0)}")
            print(f"paper_archived={summary['archived']}")
            print(f"paper_updated={len(updated)}")
            print("candidate_summary:")
            for candidate in result.candidates:
                print(
                    f"- rank={candidate.rank} symbol={candidate.symbol} verdict={candidate.verdict} "
                    f"entry={candidate.entry_low:.8g}-{candidate.entry_high:.8g} "
                    f"stop={candidate.stop_loss:.8g} tp1={candidate.take_profit_1:.8g}"
                )
            print("paper_status_summary:")
            for trade in updated:
                print(
                    f"- {trade.symbol} status={trade.status} last={trade.last_price} "
                    f"entry={trade.entry_price} pnl={trade.unrealized_pnl + trade.realized_pnl:.2f}"
                )
            for path in scan_report_paths:
                print(f"scan_report={path}")
            for path in paper_report_paths:
                print(f"paper_report={path}")
            for path in observation_paths:
                print(f"observation_dashboard={path}")

    if args.command == "verify":
        result = verify_symbol(settings, args.symbol, progress=_progress)
        _progress("running context market scan for comparison")
        context = run_market_scan(settings, progress=_progress)
        result.context_candidates = context.candidates
        result.limitations.append(
            f"本报告同时附带当前大盘扫描候选，来源 scan_id={context.scan_id}。"
        )
        _progress("saving verification result to SQLite")
        init_db(settings.output.database_path)
        save_scan_result(settings.output.database_path, result)
        _progress("writing verification report")
        report_paths = write_scan_reports(
            result,
            settings,
            include_obsidian=not args.no_obsidian,
        )
        print(f"scan_id={result.scan_id}")
        print(f"symbol={result.candidates[0].symbol}")
        for path in report_paths:
            print(f"report={path}")

    if args.command == "backtest":
        symbols = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]
        if not symbols:
            raise ValueError("--symbols must include at least one symbol")
        _progress(f"starting backtest for {', '.join(symbols)}")
        result, metrics, report_paths = run_backtest(
            settings,
            symbols,
            args.start,
            args.end,
            interval=args.interval,
            intrabar=args.intrabar,
            allow_data_gaps=args.allow_data_gaps,
            include_obsidian=not args.no_obsidian,
            progress=_progress,
        )
        print("backtest=completed")
        print(f"backtest_run_id={result.run_id}")
        print(f"symbols={','.join(result.symbols)}")
        print(f"trades={metrics.trades}")
        print(f"closed_trades={metrics.closed_trades}")
        print(f"net_return_pct={metrics.net_return_pct:.2f}")
        print(f"max_drawdown_pct={metrics.max_drawdown_pct:.2f}")
        for path in report_paths:
            print(f"report={path}")

    if args.command == "backtest-universe":
        _progress("starting universe snapshot backtest")
        result, metrics, report_paths = run_backtest(
            settings,
            [],
            args.start,
            args.end,
            interval=args.interval,
            intrabar=args.intrabar,
            allow_data_gaps=args.allow_data_gaps,
            universe_mode=True,
            max_universe_symbols=args.max_symbols,
            include_obsidian=not args.no_obsidian,
            progress=_progress,
        )
        print("backtest_universe=completed")
        print(f"backtest_run_id={result.run_id}")
        print(f"universe_selected={len(result.symbols)}")
        print(f"symbols={','.join(result.symbols)}")
        print(f"trades={metrics.trades}")
        print(f"closed_trades={metrics.closed_trades}")
        print(f"net_return_pct={metrics.net_return_pct:.2f}")
        print(f"max_drawdown_pct={metrics.max_drawdown_pct:.2f}")
        print(f"sample_sufficient={str(metrics.sample_sufficient).lower()}")
        for path in report_paths:
            print(f"report={path}")

    if args.command == "backtest-dynamic-universe":
        _progress("starting dynamic universe backtest")
        if args.source_limit is not None:
            _progress("source-limit is enabled for smoke/debug; full universe results may differ")
        dynamic_symbol_master = _prepare_dynamic_symbol_master(settings, args)
        result, metrics, report_paths = run_backtest(
            settings,
            [],
            args.start,
            args.end,
            interval=args.interval,
            intrabar=args.intrabar,
            allow_data_gaps=args.allow_data_gaps,
            dynamic_universe_mode=True,
            max_universe_symbols=args.max_symbols,
            source_limit=args.source_limit,
            dynamic_symbol_master=dynamic_symbol_master,
            include_obsidian=not args.no_obsidian,
            progress=_progress,
        )
        summary = result.dynamic_universe_summary or {}
        print("backtest_dynamic_universe=completed")
        print(f"backtest_run_id={result.run_id}")
        print(f"master_symbols={summary.get('master_count', 0)}")
        print(f"universe_refreshes={summary.get('universe_refresh_count', 0)}")
        print(f"symbols={','.join(result.symbols)}")
        print(f"trades={metrics.trades}")
        print(f"closed_trades={metrics.closed_trades}")
        print(f"net_return_pct={metrics.net_return_pct:.2f}")
        print(f"max_drawdown_pct={metrics.max_drawdown_pct:.2f}")
        print(f"sample_sufficient={str(metrics.sample_sufficient).lower()}")
        print("runtime_note=first full dynamic-universe run can be slow; cached klines make later runs faster")
        for path in report_paths:
            print(f"report={path}")

    if args.command == "dynamic-symbol-master":
        if args.source_limit is not None:
            _progress("source-limit is enabled for symbol master export")
        master = build_current_symbol_master(
            settings,
            source_limit=args.source_limit,
            fetch_listing_dates=getattr(args, "fetch_listing_dates", False),
            progress=_progress,
        )
        save_symbol_master(master, Path(args.output))
        print("dynamic_symbol_master=completed")
        print(f"symbols={len(master.symbols)}")
        print(f"source_limit={master.source_limit}")
        print(f"source_limit_applied={str(master.source_limit_applied).lower()}")
        print(f"listing_dates_fetched={str(master.listing_dates is not None).lower()}")
        print(f"output={Path(args.output)}")

    if args.command == "split-symbol-master":
        large_path, alt_path = split_symbol_master_by_cap(
            Path(args.input),
            None if args.output_dir is None else Path(args.output_dir),
        )
        print("split_symbol_master=completed")
        print(f"large_cap={large_path}")
        print(f"altcoin={alt_path}")

    if args.command == "backtest-regime-breakdown":
        _progress("building backtest market regime breakdown")
        comparison = build_regime_comparison(settings, args.baseline_run_id, args.variant_run_id)
        original_obsidian = settings.output.obsidian_dir
        if args.no_obsidian:
            settings.output.obsidian_dir = None
        comparison = write_regime_comparison_report(settings, comparison, report_date=args.reports_date)
        settings.output.obsidian_dir = original_obsidian
        print("backtest_regime_breakdown=completed")
        print(f"baseline_run_id={comparison.baseline.run_id}")
        print(f"variant_run_id={comparison.variant.run_id}")
        for status in sorted(set(comparison.baseline.buckets) | set(comparison.variant.buckets)):
            base = comparison.baseline.buckets.get(status)
            variant = comparison.variant.buckets.get(status)
            print(
                f"regime={status} "
                f"baseline_closed={base.closed_trades if base else 0} "
                f"variant_closed={variant.closed_trades if variant else 0}"
            )
        for path in comparison.report_paths:
            print(f"report={path}")

    if args.command == "abtest":
        if args.dynamic_universe and args.symbols:
            raise ValueError("--symbols and --dynamic-universe are mutually exclusive")
        symbols = []
        if args.symbols:
            symbols = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]
        if not args.dynamic_universe and not symbols:
            raise ValueError("--symbols must include at least one symbol unless --dynamic-universe is used")
        if not args.dynamic_universe and (args.symbol_master_file or args.write_symbol_master):
            raise ValueError("--symbol-master-file and --write-symbol-master require --dynamic-universe")
        dynamic_symbol_master = None
        if args.dynamic_universe:
            _progress(f"starting dynamic-universe A/B test {args.experiment}")
            if args.source_limit is not None:
                _progress("source-limit is enabled for dynamic-universe A/B smoke/debug")
            dynamic_symbol_master = _prepare_dynamic_symbol_master(settings, args)
        else:
            _progress(f"starting A/B test {args.experiment} for {', '.join(symbols)}")
        summary = run_abtest(
            settings,
            args.experiment,
            symbols,
            args.start,
            args.end,
            experiments_path=Path(args.experiments),
            interval=args.interval,
            intrabar=args.intrabar,
            allow_data_gaps=args.allow_data_gaps,
            dynamic_universe=args.dynamic_universe,
            max_universe_symbols=args.max_symbols,
            source_limit=args.source_limit,
            dynamic_symbol_master=dynamic_symbol_master,
            include_obsidian=not args.no_obsidian,
            progress=_progress,
        )
        print("abtest=completed")
        print(f"experiment_id={summary.experiment_id}")
        print(f"baseline_run_id={summary.baseline_run_id}")
        print(f"variant_run_id={summary.variant_run_id}")
        print(f"sample_sufficient={str(summary.sample_sufficient).lower()}")
        print(f"possible_over_filtering={str(summary.possible_over_filtering).lower()}")
        print(f"verdict={summary.verdict}")
        print(f"reason={summary.reason}")
        for path in summary.report_paths:
            print(f"report={path}")

    if args.command == "abtest-summary":
        report_date = args.reports_date or datetime.now().strftime("%Y-%m-%d")
        reports_dir = settings.output.reports_dir / report_date
        _progress(f"loading A/B reports from {reports_dir}")
        records = load_abtest_records(
            reports_dir,
            args.experiment,
            args.mode,
            start=args.start,
            end=args.end,
        )
        if args.drop_overlap_periods:
            before = len(records)
            records = select_non_overlapping_records(records)
            _progress(f"kept {len(records)}/{before} non-overlapping A/B reports")
        summary = build_abtest_summary(records, args.experiment, args.mode)
        summary = write_abtest_summary_report(
            settings,
            summary,
            report_date=report_date,
            include_obsidian=not args.no_obsidian,
        )
        print("abtest_summary=completed")
        print(f"experiment_id={summary.experiment_id}")
        print(f"mode={summary.mode}")
        print(f"periods={len(summary.records)}")
        print(f"sufficient_periods={summary.sufficient_periods}")
        print(f"verdict={summary.verdict}")
        print(f"reason={summary.reason}")
        for path in summary.report_paths:
            print(f"report={path}")

    if args.command == "abtest-walk-forward":
        periods = parse_period_specs(args.periods)
        if args.dynamic_universe and args.symbols:
            raise ValueError("--symbols and --dynamic-universe are mutually exclusive")
        symbols = []
        if args.symbols:
            symbols = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]
        if not args.dynamic_universe and not symbols:
            raise ValueError("--symbols must include at least one symbol unless --dynamic-universe is used")
        if not args.dynamic_universe and (args.symbol_master_file or args.write_symbol_master):
            raise ValueError("--symbol-master-file and --write-symbol-master require --dynamic-universe")
        dynamic_symbol_master = None
        if args.dynamic_universe:
            dynamic_symbol_master = _prepare_dynamic_symbol_master(settings, args)

        mode = "dynamic_universe" if args.dynamic_universe else "symbols"
        records = []
        print("abtest_walk_forward=started")
        print(f"experiment_id={args.experiment}")
        print(f"periods={len(periods)}")
        for index, (start, end) in enumerate(periods, start=1):
            _progress(f"running walk-forward period {index}/{len(periods)} {start} -> {end}")
            period_summary = run_abtest(
                settings,
                args.experiment,
                symbols,
                start,
                end,
                experiments_path=Path(args.experiments),
                interval=args.interval,
                intrabar=args.intrabar,
                allow_data_gaps=args.allow_data_gaps,
                dynamic_universe=args.dynamic_universe,
                max_universe_symbols=args.max_symbols,
                source_limit=args.source_limit,
                dynamic_symbol_master=dynamic_symbol_master,
                include_obsidian=not args.no_obsidian,
                progress=_progress,
            )
            print(
                f"period={start}->{end} verdict={period_summary.verdict} "
                f"sample_sufficient={str(period_summary.sample_sufficient).lower()}"
            )
            for path in period_summary.report_paths:
                print(f"period_report={path}")
            if period_summary.report_paths:
                record = parse_abtest_report(period_summary.report_paths[0], args.experiment, mode)
                if record is not None:
                    records.append(record)

        aggregate = build_abtest_summary(records, args.experiment, mode)
        aggregate = write_abtest_summary_report(
            settings,
            aggregate,
            report_date=args.reports_date,
            include_obsidian=not args.no_obsidian,
        )
        print("abtest_walk_forward=completed")
        print(f"sufficient_periods={aggregate.sufficient_periods}")
        print(f"verdict={aggregate.verdict}")
        print(f"reason={aggregate.reason}")
        for path in aggregate.report_paths:
            print(f"summary_report={path}")

    if args.command == "experiment-index":
        original_obsidian = settings.output.obsidian_dir
        if args.no_obsidian:
            settings.output.obsidian_dir = None
        _, paths = build_experiment_index(
            settings,
            reports_dir=None if args.reports_dir is None else Path(args.reports_dir),
        )
        settings.output.obsidian_dir = original_obsidian
        print("experiment_index=completed")
        for path in paths:
            print(f"report={path}")

    if args.command == "observation-dashboard":
        original_obsidian = settings.output.obsidian_dir
        if args.no_obsidian:
            settings.output.obsidian_dir = None
        init_db(settings.output.database_path)
        _, paths = generate_observation_dashboard(settings, account_name=args.account)
        settings.output.obsidian_dir = original_obsidian
        print("observation_dashboard=completed")
        for path in paths:
            print(f"report={path}")

    if args.command == "paper":
        init_db(settings.output.database_path)

        if args.paper_command == "add-from-scan":
            with tracked_run(
                settings.output.database_path,
                "manual",
                settings_path=settings_path,
                project_root=PROJECT_ROOT,
            ) as run_id:
                summary = add_from_scan(
                    settings,
                    scan_id=args.scan_id,
                    account_name=args.account,
                    run_id=run_id,
                )
            print(f"run_id={run_id}")
            print(f"account={summary['account_name']}")
            print(f"scan_id={summary['scan_id']}")
            print(f"added={summary['added']}")
            print(f"skipped={summary['skipped']}")
            print(f"skipped_action={summary.get('skipped_action', 0)}")
            print(f"import_actions={','.join(summary.get('import_actions', []))}")
            print(f"archived={summary['archived']}")

        if args.paper_command == "update":
            with tracked_run(
                settings.output.database_path,
                args.run_type,
                settings_path=settings_path,
                project_root=PROJECT_ROOT,
            ) as run_id:
                with _run_step(run_id, "paper_update"):
                    updated = update_paper_trades(settings, account_name=args.account, run_id=run_id)
            print(f"run_id={run_id}")
            print(f"updated={len(updated)}")
            for trade in updated:
                print(
                    f"{trade.symbol} status={trade.status} last={trade.last_price} "
                    f"entry={trade.entry_price} pnl={trade.unrealized_pnl + trade.realized_pnl:.2f}"
                )

        if args.paper_command == "report":
            _, report_paths = generate_paper_report(settings, account_name=args.account)
            for path in report_paths:
                print(f"report={path}")

        if args.paper_command == "db-summary":
            print(json.dumps(build_paper_db_summary(settings.output.database_path, args.limit), ensure_ascii=False, indent=2))

        if args.paper_command == "db-events":
            print(
                json.dumps(
                    load_paper_db_events(settings.output.database_path, args.plan_id, args.limit),
                    ensure_ascii=False,
                    indent=2,
                )
            )

        if args.paper_command == "db-export":
            for path in export_paper_db(settings.output.database_path, Path(args.output_dir)):
                print(f"export={path}")

        if args.paper_command == "cycle":
            run_id, updated, report_paths, dashboard_paths = _run_paper_cycle(
                settings,
                account_name=args.account,
                run_type=args.run_type,
                no_obsidian=args.no_obsidian,
                settings_path=settings_path,
            )
            print(f"run_id={run_id}")
            print(f"updated={len(updated)}")
            for path in report_paths:
                print(f"report={path}")
            for path in dashboard_paths:
                print(f"dashboard={path}")


if __name__ == "__main__":
    main()
