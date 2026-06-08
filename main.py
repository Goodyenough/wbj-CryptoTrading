from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from crypto_trading_system.abtest import run_abtest
from crypto_trading_system.abtest_summary import (
    build_abtest_summary,
    load_abtest_records,
    write_abtest_summary_report,
)
from crypto_trading_system.backtest.runner import run_backtest
from crypto_trading_system.config import load_settings
from crypto_trading_system.doctor import run_doctor
from crypto_trading_system.paper_trader import add_from_scan, generate_paper_report, update_paper_trades
from crypto_trading_system.reports import write_scan_reports
from crypto_trading_system.scanner import run_market_scan
from crypto_trading_system.storage import init_db, save_scan_result
from crypto_trading_system.verify import verify_symbol


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CryptoTradingSystem MVP")
    parser.add_argument(
        "--settings",
        default="config/settings.toml",
        help="Path to TOML settings file.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor", help="Check API connectivity, local paths, and database readiness.")

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

    paper_report = paper_subparsers.add_parser("report", help="Write a paper trading report.")
    paper_report.add_argument("--account", default=None, help="Paper account name. Defaults to settings.")
    return parser


def _progress(message: str) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def _run_scan_and_write(settings, include_obsidian: bool, progress=None):
    result = run_market_scan(settings, progress=progress)
    if progress is not None:
        progress("saving scan result to SQLite")
    init_db(settings.output.database_path)
    save_scan_result(settings.output.database_path, result)
    if progress is not None:
        progress("writing Markdown reports")
    report_paths = write_scan_reports(
        result,
        settings,
        include_obsidian=include_obsidian,
    )
    return result, report_paths


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    settings = load_settings(Path(args.settings))

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
        result, scan_report_paths = _run_scan_and_write(settings, include_obsidian=not args.no_obsidian, progress=_progress)
        _progress("adding latest candidates to paper trading")
        summary = add_from_scan(settings, scan_id=result.scan_id, account_name=args.account)
        _progress("updating paper trading positions")
        updated = update_paper_trades(settings, account_name=args.account)
        _progress("writing paper trading report")
        _, paper_report_paths = generate_paper_report(settings, account_name=args.account)

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

    if args.command == "abtest":
        if args.dynamic_universe and args.symbols:
            raise ValueError("--symbols and --dynamic-universe are mutually exclusive")
        symbols = []
        if args.symbols:
            symbols = [symbol.strip().upper() for symbol in args.symbols.split(",") if symbol.strip()]
        if not args.dynamic_universe and not symbols:
            raise ValueError("--symbols must include at least one symbol unless --dynamic-universe is used")
        if args.dynamic_universe:
            _progress(f"starting dynamic-universe A/B test {args.experiment}")
            if args.source_limit is not None:
                _progress("source-limit is enabled for dynamic-universe A/B smoke/debug")
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

    if args.command == "paper":
        init_db(settings.output.database_path)

        if args.paper_command == "add-from-scan":
            summary = add_from_scan(settings, scan_id=args.scan_id, account_name=args.account)
            print(f"account={summary['account_name']}")
            print(f"scan_id={summary['scan_id']}")
            print(f"added={summary['added']}")
            print(f"skipped={summary['skipped']}")
            print(f"skipped_action={summary.get('skipped_action', 0)}")
            print(f"import_actions={','.join(summary.get('import_actions', []))}")
            print(f"archived={summary['archived']}")

        if args.paper_command == "update":
            updated = update_paper_trades(settings, account_name=args.account)
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


if __name__ == "__main__":
    main()
