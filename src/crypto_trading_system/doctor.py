from __future__ import annotations

from dataclasses import dataclass
import sqlite3

from .config import Settings
from .data_validation import ProviderError, _get_json
from .market_data import BinanceClient
from .storage import init_db


@dataclass
class DoctorCheck:
    name: str
    status: str
    message: str


def _ok(name: str, message: str) -> DoctorCheck:
    return DoctorCheck(name=name, status="OK", message=message)


def _skip(name: str, message: str) -> DoctorCheck:
    return DoctorCheck(name=name, status="SKIP", message=message)


def _warn(name: str, message: str) -> DoctorCheck:
    return DoctorCheck(name=name, status="WARN", message=message)


def _fail(name: str, message: str) -> DoctorCheck:
    return DoctorCheck(name=name, status="FAIL", message=message)


def _check_binance(settings: Settings) -> DoctorCheck:
    try:
        client = BinanceClient(
            settings.market.base_url,
            timeout_seconds=settings.market.request_timeout_seconds,
            pause_seconds=settings.market.request_pause_seconds,
        )
        tickers = client.ticker_24hr()
        return _ok("Binance", f"24h ticker endpoint returned {len(tickers)} symbols.")
    except Exception as exc:
        return _fail("Binance", str(exc))


def _check_coingecko(settings: Settings) -> DoctorCheck:
    try:
        payload = _get_json(
            settings.data_validation.coingecko_base_url,
            "/simple/price",
            {"ids": "bitcoin", "vs_currencies": "usd"},
            headers=None,
            timeout_seconds=settings.data_validation.request_timeout_seconds,
            pause_seconds=settings.data_validation.request_pause_seconds,
        )
        price = payload.get("bitcoin", {}).get("usd") if isinstance(payload, dict) else None
        if price is None:
            return _warn("CoinGecko", "Endpoint responded, but BTC/USD price was missing.")
        return _ok("CoinGecko", f"BTC/USD price endpoint responded: {price}.")
    except ProviderError as exc:
        return _fail("CoinGecko", str(exc))


def _check_coinmarketcap(settings: Settings) -> DoctorCheck:
    if not settings.data_validation.coinmarketcap_api_key:
        return _skip("CoinMarketCap", "API key not detected. Set CMC_API_KEY or COINMARKETCAP_API_KEY.")

    try:
        payload = _get_json(
            settings.data_validation.coinmarketcap_base_url,
            "/v2/cryptocurrency/quotes/latest",
            {"symbol": "BTC", "convert": "USD"},
            headers={"X-CMC_PRO_API_KEY": settings.data_validation.coinmarketcap_api_key},
            timeout_seconds=settings.data_validation.request_timeout_seconds,
            pause_seconds=settings.data_validation.request_pause_seconds,
        )
        rows = payload.get("data", {}).get("BTC", []) if isinstance(payload, dict) else []
        if isinstance(rows, dict):
            rows = [rows]
        if not rows:
            return _warn("CoinMarketCap", "API key detected, but BTC quote was missing from response.")
        return _ok("CoinMarketCap", "API key detected and BTC quote endpoint responded.")
    except ProviderError as exc:
        return _fail("CoinMarketCap", str(exc))


def _check_database(settings: Settings) -> DoctorCheck:
    try:
        init_db(settings.output.database_path)
        with sqlite3.connect(settings.output.database_path) as connection:
            rows = connection.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
        table_names = {str(row[0]) for row in rows}
        required = {"scan_runs", "scan_candidates", "paper_trades", "paper_trade_events", "data_cross_checks"}
        missing = sorted(required - table_names)
        if missing:
            return _warn("Database", f"Database exists but missing tables: {', '.join(missing)}.")
        return _ok("Database", f"SQLite database ready at {settings.output.database_path}.")
    except Exception as exc:
        return _fail("Database", str(exc))


def _check_reports_dir(settings: Settings) -> DoctorCheck:
    reports_dir = settings.output.reports_dir
    if reports_dir.exists() and reports_dir.is_dir():
        return _ok("Reports", f"Reports directory exists: {reports_dir}.")
    if reports_dir.parent.exists():
        return _warn("Reports", f"Reports directory does not exist yet, but parent exists: {reports_dir.parent}.")
    return _fail("Reports", f"Reports parent directory does not exist: {reports_dir.parent}.")


def _check_obsidian_dir(settings: Settings) -> DoctorCheck:
    obsidian_dir = settings.output.obsidian_dir
    if obsidian_dir is None:
        return _skip("Obsidian", "No Obsidian directory configured.")
    if obsidian_dir.exists() and obsidian_dir.is_dir():
        return _ok("Obsidian", f"Obsidian directory exists: {obsidian_dir}.")
    return _warn("Obsidian", f"Configured Obsidian directory not found: {obsidian_dir}.")


def run_doctor(settings: Settings) -> list[DoctorCheck]:
    return [
        _check_binance(settings),
        _check_coingecko(settings),
        _check_coinmarketcap(settings),
        _check_database(settings),
        _check_reports_dir(settings),
        _check_obsidian_dir(settings),
    ]
