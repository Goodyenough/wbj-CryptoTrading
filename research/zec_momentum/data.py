"""Bounded public Binance USDM archives for the preregistered ZEC study.

This module never opens the production database and never discovers available
months. Every requested month is validated before any cache or network access.
"""
from __future__ import annotations

import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import io
import math
from pathlib import Path
import re
import threading
import time
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener
import zipfile


SYMBOL = "ZECUSDT"
STEP_MS = 300_000
CUTOFF_MS = 1_782_144_000_000
RESERVED_2026_START_MS = 1_767_225_600_000
BASE_URL = "https://data.binance.vision/data/futures/um/monthly"
KINDS = ("klines", "markPriceKlines", "fundingRate")
PRODUCTION_ROOT = Path(r"D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects")
_PRICE_HEADER = (
    "open_time", "open", "high", "low", "close", "volume", "close_time",
    "quote_volume", "count", "taker_buy_volume", "taker_buy_quote_volume", "ignore",
)
_FUNDING_HEADER = ("calc_time", "funding_interval_hours", "last_funding_rate")


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        # Checking response.geturl alone would detect a redirect too late: an
        # unapproved URL would already have been requested by urllib.
        raise ValueError("Archive redirects are not permitted.")


def urlopen(request, timeout):
    """Module-local entry point remains replaceable by network-free tests."""
    return build_opener(_NoRedirect()).open(request, timeout=timeout)


def _month_bounds(month: str) -> tuple[int, int]:
    if not isinstance(month, str) or not re.fullmatch(r"\d{4}-\d{2}", month):
        raise ValueError("Month must be an explicit YYYY-MM string.")
    if not "2023-12" <= month <= "2025-12":
        raise ValueError(f"Protected or unapproved month: {month}")
    try:
        start = datetime.strptime(month, "%Y-%m").replace(tzinfo=timezone.utc)
    except ValueError as exc:
        raise ValueError(f"Invalid calendar month: {month}") from exc
    end = datetime(start.year + (start.month == 12), start.month % 12 + 1, 1, tzinfo=timezone.utc)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)


def _validate_request(months: list[str], cutoff_ms: int) -> list[tuple[str, int, int]]:
    # Keep every check here free of filesystem and network operations.
    if isinstance(cutoff_ms, bool) or not isinstance(cutoff_ms, int) or cutoff_ms > CUTOFF_MS:
        raise ValueError("cutoff_ms must be an integer no later than the sealed cutoff.")
    if not isinstance(months, list) or not months:
        raise ValueError("Supply a nonempty explicit list of months.")
    bounds = [(month, *_month_bounds(month)) for month in months]
    if len({month for month, _, _ in bounds}) != len(bounds):
        raise ValueError("Duplicate requested month.")
    bounds.sort()
    for _, _, end in bounds:
        if end > cutoff_ms or end > RESERVED_2026_START_MS:
            raise ValueError("A complete requested month extends into reserved data.")
    if any(left[2] != right[1] for left, right in zip(bounds, bounds[1:])):
        raise ValueError("Requested months must be contiguous; missing months cannot be synthesized.")
    return bounds


def _archive_url(kind: str, month: str) -> str:
    if kind not in KINDS:
        raise ValueError("Unsupported archive kind.")
    _month_bounds(month)
    if kind == "fundingRate":
        return f"{BASE_URL}/{kind}/{SYMBOL}/{SYMBOL}-fundingRate-{month}.zip"
    return f"{BASE_URL}/{kind}/{SYMBOL}/5m/{SYMBOL}-5m-{month}.zip"


def _read_url(url: str, stop: threading.Event) -> bytes:
    for attempt in range(3):  # Initial attempt plus at most two retries.
        if stop.is_set():
            raise RuntimeError("Archive loading stopped after another download failed.")
        try:
            request = Request(url, headers={"User-Agent": "ZEC-historical-research/1.0"})
            with urlopen(request, timeout=30) as response:
                final_url = response.geturl()
                if final_url != url:
                    raise ValueError("Archive redirects are not permitted.")
                return response.read()
        except HTTPError as exc:
            if exc.code in {403, 451}:
                stop.set()
                raise RuntimeError(f"Archive access denied ({exc.code}); downloads stopped.") from exc
            if exc.code != 429 and not 500 <= exc.code < 600:
                stop.set()
                raise
            if attempt == 2:
                stop.set()
                raise
        except (TimeoutError, URLError):
            if attempt == 2:
                stop.set()
                raise
        time.sleep(0.5 * (2 ** attempt))
    raise AssertionError("Unreachable retry state")


def _verify_checksum(payload: bytes, checksum: bytes, filename: str) -> str:
    try:
        entry = checksum.decode("ascii").strip()
    except UnicodeDecodeError as exc:
        raise ValueError("Checksum must be ASCII.") from exc
    match = re.fullmatch(r"([0-9a-fA-F]{64})[ \t]+\*?([^\r\n]+)", entry)
    if match is None or match.group(2) != filename:
        raise ValueError("Malformed checksum or checksum filename mismatch.")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != match.group(1).lower():
        raise ValueError(f"SHA256 mismatch: {filename}")
    return digest


def _number(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("Non-finite archive value.")
    return number


def _csv_rows(payload: bytes, filename: str, expected_header: tuple[str, ...]):
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        members = archive.namelist()
        if members != [filename.removesuffix(".zip") + ".csv"]:
            raise ValueError("ZIP must contain exactly its matching CSV file.")
        with archive.open(members[0]) as source:
            with io.TextIOWrapper(source, encoding="utf-8-sig", newline="") as stream:
                reader = csv.reader(stream)
                header = tuple(next(reader, []))
                if header != expected_header:
                    raise ValueError(f"Unexpected CSV header in {filename}: {header}")
                yield from reader


def _parse_prices(payload: bytes, filename: str, start: int, end: int, cutoff: int) -> list[list]:
    rows: list[list] = []
    for source in _csv_rows(payload, filename, _PRICE_HEADER):
        if len(source) != 12:
            raise ValueError("Kline row must contain twelve fields.")
        opened, closed = int(source[0]), int(source[6])
        # Reject a row before converting or returning any of its market values.
        if not start <= opened < end or closed >= cutoff or closed >= end:
            raise ValueError("Cross-month or protected kline row rejected.")
        if opened % STEP_MS or closed != opened + STEP_MS - 1:
            raise ValueError("Misaligned or incorrectly bounded 5m candle.")
        row = [opened, *(_number(value) for value in source[1:6]), closed,
               _number(source[7]), int(source[8]), _number(source[9]),
               _number(source[10]), _number(source[11])]
        opening, high, low, close = row[1:5]
        if low <= 0 or low > min(opening, close) or high < max(opening, close):
            raise ValueError("Invalid OHLC geometry.")
        if any(row[index] < 0 for index in (5, 7, 8, 9, 10)):
            raise ValueError("Negative volume or trade count.")
        if rows and opened != rows[-1][0] + STEP_MS:
            raise ValueError("Duplicate, overlapping, out-of-order or missing kline.")
        rows.append(row)
    expected = (end - start) // STEP_MS
    if len(rows) != expected or not rows or rows[0][0] != start or rows[-1][0] != end - STEP_MS:
        raise ValueError("Incomplete monthly 5m archive; no candles are synthesized.")
    return rows


def _validate_funding_continuity(rows: list[dict]) -> None:
    for previous, current in zip(rows, rows[1:]):
        if current["time_ms"] <= previous["time_ms"]:
            raise ValueError("Duplicate or out-of-order raw funding timestamp.")
        interval = int(current["funding_interval_hours"] * 3_600_000)
        if current["scheduled_ms"] - previous["scheduled_ms"] != interval:
            raise ValueError("Duplicate, overlapping or missing funding event.")


def _parse_funding(payload: bytes, filename: str, start: int, end: int, cutoff: int) -> list[dict]:
    rows: list[dict] = []
    for source in _csv_rows(payload, filename, _FUNDING_HEADER):
        if len(source) != 3:
            raise ValueError("Funding row must contain three fields.")
        timestamp = int(source[0])
        if not start <= timestamp < end or timestamp >= cutoff:
            raise ValueError("Cross-month or protected funding row rejected.")
        hours, rate = _number(source[1]), _number(source[2])
        interval = hours * 3_600_000
        if hours <= 0 or interval != int(interval):
            raise ValueError("Invalid funding interval.")
        rows.append({"time_ms": timestamp, "scheduled_ms": timestamp // STEP_MS * STEP_MS,
                     "rate": rate, "funding_interval_hours": hours})
    _validate_funding_continuity(rows)
    if not rows or rows[0]["scheduled_ms"] != start:
        raise ValueError("Funding archive does not cover the beginning of the month.")
    if rows[-1]["scheduled_ms"] + int(rows[-1]["funding_interval_hours"] * 3_600_000) != end:
        raise ValueError("Funding archive does not cover the end of the month.")
    return rows


def _load_archive(cache: Path, kind: str, month: str, start: int, end: int,
                  cutoff: int, download: bool, stop: threading.Event) -> tuple[list, dict]:
    url = _archive_url(kind, month)
    # Mark and trade archives share a basename, so keep kind-specific folders.
    filename = url.rsplit("/", 1)[1]
    target = cache / kind / filename
    checksum_target = target.with_suffix(".zip.CHECKSUM")
    exists, checksum_exists = target.exists(), checksum_target.exists()
    if exists != checksum_exists:
        raise ValueError(f"Incomplete archive/checksum cache pair: {kind}/{filename}")
    if exists:
        payload, checksum = target.read_bytes(), checksum_target.read_bytes()
        origin = "cache"
    else:
        if not download:
            raise FileNotFoundError(f"Explicit archive absent from cache: {kind}/{filename}")
        checksum = _read_url(url + ".CHECKSUM", stop)
        payload = _read_url(url, stop)
        origin = "download"
    digest = _verify_checksum(payload, checksum, filename)
    parser = _parse_funding if kind == "fundingRate" else _parse_prices
    rows = parser(payload, filename, start, end, cutoff)
    if not exists:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        checksum_target.write_bytes(checksum)
    timestamps = [row["time_ms"] if isinstance(row, dict) else row[0] for row in rows]
    record = {"kind": kind, "month": month, "url": url, "checksum_url": url + ".CHECKSUM",
              "sha256": digest, "rows": len(rows), "min_time_ms": min(timestamps),
              "max_time_ms": max(timestamps), "origin": origin}
    if kind != "fundingRate":
        record["max_close_time_ms"] = rows[-1][6]
    else:
        record["min_scheduled_ms"] = rows[0]["scheduled_ms"]
        record["max_scheduled_ms"] = rows[-1]["scheduled_ms"]
    return rows, record


def load_dataset(cache_dir: str | Path, *, months: list[str], cutoff_ms: int = CUTOFF_MS,
                 download: bool = True) -> tuple[list[list], list[dict], dict]:
    """Read only named approved months, with SHA256 and full coverage validation."""
    bounds = _validate_request(months, cutoff_ms)  # Must remain the first operation.
    if cache_dir is None or not str(cache_dir).strip():
        raise ValueError("An explicit isolated cache_dir is required.")
    cache = Path(cache_dir).resolve()
    production = PRODUCTION_ROOT.resolve()
    if cache == production or production in cache.parents:
        raise ValueError("The production workspace cannot be used as a research cache.")
    tasks = [(kind, month, start, end) for month, start, end in bounds for kind in KINDS]
    stop = threading.Event()
    loaded: dict[tuple[str, str], list] = {}
    records: list[dict] = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [(kind, month, executor.submit(_load_archive, cache, kind, month, start, end,
                                               cutoff_ms, download, stop))
                   for kind, month, start, end in tasks]
        try:
            for kind, month, future in futures:
                rows, record = future.result()
                loaded[(kind, month)] = rows
                records.append(record)
        except BaseException:
            stop.set()
            for _, _, future in futures:
                future.cancel()
            raise
    bars = [bar for month, _, _ in bounds for bar in loaded[("klines", month)]]
    marks = {bar[0]: bar[1] for month, _, _ in bounds for bar in loaded[("markPriceKlines", month)]}
    funding = [dict(row) for month, _, _ in bounds for row in loaded[("fundingRate", month)]]
    # Check across month boundaries as well as within each archive. Raw exchange
    # timestamps remain untouched; only schedule validation uses their 5m bucket.
    _validate_funding_continuity(funding)
    for row in funding:
        mark_open = row["scheduled_ms"]
        if mark_open not in marks or mark_open > row["time_ms"]:
            raise ValueError("Funding has no same-bucket historical mark-price candle; future marks are forbidden.")
        row["mark_price"] = marks[mark_open]
        row["mark_open_ms"] = mark_open
        row["mark_proxy_age_ms"] = row["time_ms"] - mark_open
    manifest = {"symbol": SYMBOL, "market": "Binance_USDM", "interval": "5m",
                "months": [month for month, _, _ in bounds], "cutoff_ms": cutoff_ms,
                "reserved_2026_start_ms": RESERVED_2026_START_MS, "archives": records,
                "bars": {"rows": len(bars), "min_time_ms": bars[0][0],
                         "max_time_ms": bars[-1][0], "max_close_time_ms": bars[-1][6]},
                "funding": {"rows": len(funding), "min_time_ms": funding[0]["time_ms"],
                            "max_time_ms": funding[-1]["time_ms"],
                            "min_scheduled_ms": funding[0]["scheduled_ms"],
                            "max_scheduled_ms": funding[-1]["scheduled_ms"],
                            "max_mark_proxy_age_ms": max(row["mark_proxy_age_ms"] for row in funding)},
                "funding_time_basis": "time_ms preserves raw calc_time; scheduled_ms floors it to its 5m bucket solely for coverage and continuity checks.",
                "funding_mark_proxy": "Open of the markPriceKlines 5m candle containing raw funding time (mark_open_ms <= time_ms); mark_proxy_age_ms records the age. Not an exact settlement mark; never uses a future open."}
    return bars, funding, manifest
