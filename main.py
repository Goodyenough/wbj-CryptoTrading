from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

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

    if args.command == "paper":
        init_db(settings.output.database_path)

        if args.paper_command == "add-from-scan":
            summary = add_from_scan(settings, scan_id=args.scan_id, account_name=args.account)
            print(f"account={summary['account_name']}")
            print(f"scan_id={summary['scan_id']}")
            print(f"added={summary['added']}")
            print(f"skipped={summary['skipped']}")
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
