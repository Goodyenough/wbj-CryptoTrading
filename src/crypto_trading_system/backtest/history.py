from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import sqlite3
from typing import Callable

from ..config import Settings
from ..market_data import BinanceClient
from ..storage import init_db


INTERVAL_MS = {
    "1m": 60_000,
    "5m": 5 * 60_000,
    "15m": 15 * 60_000,
    "1h": 60 * 60_000,
    "4h": 4 * 60 * 60_000,
    "1d": 24 * 60 * 60_000,
}


@dataclass
class KlineQualityIssue:
    symbol: str
    interval: str
    severity: str
    message: str
    open_time: int | None = None


@dataclass
class KlineFetchResult:
    symbol: str
    interval: str
    klines: list[list]
    issues: list[KlineQualityIssue]
    fetched_from_api: int


def interval_ms(interval: str) -> int:
    try:
        return INTERVAL_MS[interval]
    except KeyError as exc:
        raise ValueError(f"Unsupported interval: {interval}") from exc


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _normalise_kline(row: sqlite3.Row) -> list:
    return [
        int(row["open_time"]),
        str(row["open"]),
        str(row["high"]),
        str(row["low"]),
        str(row["close"]),
        str(row["volume"]),
        int(row["close_time"]),
        str(row["quote_volume"]),
        int(row["trades"]),
        str(row["taker_buy_base_volume"]),
        str(row["taker_buy_quote_volume"]),
        "0",
    ]


def _load_cached_klines(
    connection: sqlite3.Connection,
    symbol: str,
    interval: str,
    start_time_ms: int,
    end_time_ms: int,
    source: str = "Binance",
) -> list[list]:
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT *
        FROM kline_cache
        WHERE source = ?
          AND symbol = ?
          AND interval = ?
          AND open_time >= ?
          AND open_time < ?
          AND is_closed = 1
        ORDER BY open_time
        """,
        (source, symbol, interval, start_time_ms, end_time_ms),
    ).fetchall()
    return [_normalise_kline(row) for row in rows]


def _insert_klines(
    connection: sqlite3.Connection,
    symbol: str,
    interval: str,
    klines: list[list],
    source: str = "Binance",
) -> int:
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    fetched_at = _utc_now()
    inserted = 0
    for kline in klines:
        close_time = int(kline[6])
        is_closed = close_time < now_ms
        if not is_closed:
            continue
        connection.execute(
            """
            INSERT OR REPLACE INTO kline_cache (
                source, symbol, interval, open_time, open, high, low, close,
                volume, close_time, quote_volume, trades,
                taker_buy_base_volume, taker_buy_quote_volume, is_closed, fetched_at_utc
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                source,
                symbol,
                interval,
                int(kline[0]),
                float(kline[1]),
                float(kline[2]),
                float(kline[3]),
                float(kline[4]),
                float(kline[5]),
                close_time,
                float(kline[7]),
                int(kline[8]),
                float(kline[9]),
                float(kline[10]),
                1,
                fetched_at,
            ),
        )
        inserted += 1
    return inserted


def _quality_issues(symbol: str, interval: str, klines: list[list]) -> list[KlineQualityIssue]:
    issues: list[KlineQualityIssue] = []
    if not klines:
        return [KlineQualityIssue(symbol, interval, "ERROR", "No klines available for requested range.")]

    step = interval_ms(interval)
    seen: set[int] = set()
    last_open: int | None = None
    for kline in klines:
        open_time = int(kline[0])
        high = float(kline[2])
        low = float(kline[3])
        close = float(kline[4])
        volume = float(kline[5])
        if open_time in seen:
            issues.append(KlineQualityIssue(symbol, interval, "ERROR", "Duplicate candle.", open_time))
        seen.add(open_time)
        if last_open is not None and open_time - last_open != step:
            issues.append(
                KlineQualityIssue(
                    symbol,
                    interval,
                    "ERROR",
                    f"Missing candle gap between {last_open} and {open_time}.",
                    open_time,
                )
            )
        if volume == 0:
            issues.append(KlineQualityIssue(symbol, interval, "WARNING", "Zero volume candle.", open_time))
        if low > 0 and close > 0 and (high / low - 1) * 100 > 40:
            issues.append(KlineQualityIssue(symbol, interval, "WARNING", "Large wick/range candle.", open_time))
        last_open = open_time
    return issues


def fetch_klines_cached(
    settings: Settings,
    symbol: str,
    interval: str,
    start_time_ms: int,
    end_time_ms: int,
    *,
    allow_data_gaps: bool = False,
    progress: Callable[[str], None] | None = None,
) -> KlineFetchResult:
    init_db(settings.output.database_path)
    step = interval_ms(interval)
    with sqlite3.connect(settings.output.database_path) as connection:
        cached = _load_cached_klines(connection, symbol, interval, start_time_ms, end_time_ms)
        expected = max(0, (end_time_ms - start_time_ms + step - 1) // step)
        fetched_from_api = 0
        if len(cached) < expected:
            if progress is not None:
                progress(f"fetching {symbol} {interval} klines from Binance")
            client = BinanceClient(
                settings.market.base_url,
                timeout_seconds=settings.market.request_timeout_seconds,
                pause_seconds=settings.market.request_pause_seconds,
            )
            cursor = start_time_ms
            while cursor < end_time_ms:
                batch = client.klines(
                    symbol,
                    interval,
                    limit=1000,
                    start_time_ms=cursor,
                    end_time_ms=end_time_ms - 1,
                )
                if not batch:
                    break
                fetched_from_api += _insert_klines(connection, symbol, interval, batch)
                last_open = int(batch[-1][0])
                next_cursor = last_open + step
                if next_cursor <= cursor:
                    break
                cursor = next_cursor
                if len(batch) < 1000:
                    break
            cached = _load_cached_klines(connection, symbol, interval, start_time_ms, end_time_ms)

    issues = _quality_issues(symbol, interval, cached)
    severe = [issue for issue in issues if issue.severity == "ERROR"]
    if severe and not allow_data_gaps:
        messages = "; ".join(issue.message for issue in severe[:3])
        raise ValueError(f"{symbol} {interval} data quality failed: {messages}")
    return KlineFetchResult(
        symbol=symbol,
        interval=interval,
        klines=cached,
        issues=issues,
        fetched_from_api=fetched_from_api,
    )
