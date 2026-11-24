"""Strictly bounded, checksummed Binance USD-M monthly historical archives.

Only named symbols and explicit months through December 2025 are accepted.
Request validation precedes cache and network access, and timestamps precede
market-value conversion. This module never discovers dates or live symbols.
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

from .preflight import (BASE, EFFECTIVE_END_MS, HARD_SEAL_MS, KINDS, SYMBOLS,
                        archive_request)

STEP_MS = 300_000
HOUR_MS = 3_600_000
MONTHS = tuple(["2023-12"] + [f"{year}-{month:02d}"
               for year in (2024, 2025) for month in range(1, 13)])
PRODUCTION_ROOT = Path(r"D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects")
_PRICE_HEADER = ("open_time", "open", "high", "low", "close", "volume",
                 "close_time", "quote_volume", "count", "taker_buy_volume",
                 "taker_buy_quote_volume", "ignore")
_FUNDING_HEADER = ("calc_time", "funding_interval_hours", "last_funding_rate")


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        raise ValueError("Archive redirects are forbidden before destination access")


def urlopen(request, timeout):
    """Replaceable network boundary for synthetic tests."""
    return build_opener(_NoRedirect()).open(request, timeout=timeout)


def _validated_requests(symbol: str, months: tuple[str, ...] | list[str], workers: int) -> list[dict]:
    # Do not perform filesystem operations before this function returns.
    if not isinstance(symbol, str) or symbol not in SYMBOLS:
        raise ValueError("Unapproved explicit symbol")
    if type(workers) is not int or not 1 <= workers <= 8:
        raise ValueError("workers must be an integer in [1, 8]")
    if not isinstance(months, (list, tuple)) or not months:
        raise ValueError("A nonempty explicit month sequence is required")
    requests = [archive_request(symbol, kind, month)
                for month in months for kind in sorted(KINDS)]
    if len(set(months)) != len(months):
        raise ValueError("Duplicate requested month")
    boundaries = sorted((r["month"], r["start_ms"], r["exclusive_end_ms"])
                        for r in requests if r["kind"] == "klines")
    if any(a[2] != b[1] for a, b in zip(boundaries, boundaries[1:])):
        raise ValueError("Requested months must be continuous")
    return sorted(requests, key=lambda r: (r["month"], r["kind"]))


def _approved_url(url: str) -> None:
    """Even internal network calls cannot fetch arbitrary or protected URLs."""
    pattern = (re.escape(BASE) + r"/(klines|markPriceKlines|fundingRate)/"
               r"(BTCUSDT|ETHUSDT|SOLUSDT|ZECUSDT)/(?:5m/)?"
               r"[^/?#]+\.zip(?:\.CHECKSUM)?")
    if not isinstance(url, str) or re.fullmatch(pattern, url) is None:
        raise ValueError("Unapproved archive URL")
    suffix = ".CHECKSUM" if url.endswith(".CHECKSUM") else ""
    bare = url.removesuffix(suffix) if suffix else url
    month = bare[-11:-4]
    match = re.fullmatch(pattern, url)
    expected = archive_request(match.group(2), match.group(1), month)["url"] + suffix
    if url != expected:
        raise ValueError("Archive URL is not the exact approved historical path")


def _read_url(url: str, stop: threading.Event) -> bytes:
    _approved_url(url)
    for attempt in range(3):
        if stop.is_set():
            raise RuntimeError("Historical download stopped after another task failed")
        try:
            request = Request(url, headers={"User-Agent": "bounded-short-trend-research/1.0"})
            with urlopen(request, timeout=30) as response:
                if response.geturl() != url:
                    raise ValueError("Archive redirects are forbidden")
                return response.read()
        except HTTPError as exc:
            if exc.code in {403, 451}:
                stop.set()
                raise RuntimeError(f"Archive access denied ({exc.code}); downloads stopped") from exc
            if (exc.code != 429 and not 500 <= exc.code < 600) or attempt == 2:
                stop.set()
                raise
        except (TimeoutError, URLError):
            if attempt == 2:
                stop.set()
                raise
        if attempt < 2:
            time.sleep(.5 * 2 ** attempt)
    raise AssertionError("Unreachable retry state")


def _verify_checksum(payload: bytes, checksum: bytes, filename: str) -> str:
    try:
        entry = checksum.decode("ascii").strip()
    except UnicodeDecodeError as exc:
        raise ValueError("Checksum is not ASCII") from exc
    match = re.fullmatch(r"([0-9a-fA-F]{64})[ \t]+\*?([^\r\n]+)", entry)
    if match is None or match.group(2) != filename:
        raise ValueError("Malformed checksum or filename mismatch")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != match.group(1).lower():
        raise ValueError(f"SHA256 mismatch for {filename}")
    return digest


def _csv_rows(payload: bytes, filename: str, header: tuple[str, ...]):
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        if archive.namelist() != [filename.removesuffix(".zip") + ".csv"]:
            raise ValueError("ZIP must contain exactly its matching CSV")
        with archive.open(archive.namelist()[0]) as source:
            with io.TextIOWrapper(source, encoding="utf-8-sig", newline="") as stream:
                reader = csv.reader(stream)
                if tuple(next(reader, [])) != header:
                    raise ValueError("Unexpected CSV header")
                yield from reader


def _number(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("Non-finite historical value")
    return number


def _parse_prices(payload: bytes, filename: str, start: int, end: int) -> list[list]:
    rows = []
    for source in _csv_rows(payload, filename, _PRICE_HEADER):
        if len(source) != 12:
            raise ValueError("Price row requires twelve fields")
        opened, closed = int(source[0]), int(source[6])
        # No price, volume or other market field is converted before these guards.
        if (not start <= opened < end or closed >= end
                or closed >= EFFECTIVE_END_MS or opened < 1_701_388_800_000):
            raise ValueError("Cross-month or protected price row rejected")
        if opened % STEP_MS or closed != opened + STEP_MS - 1:
            raise ValueError("Misaligned 5m candle")
        row = [opened, *(_number(value) for value in source[1:6]), closed,
               _number(source[7]), int(source[8]), _number(source[9]),
               _number(source[10]), _number(source[11])]
        opening, high, low, close = row[1:5]
        if low <= 0 or low > min(opening, close) or high < max(opening, close):
            raise ValueError("Invalid OHLC geometry")
        if any(row[index] < 0 for index in (5, 7, 8, 9, 10)):
            raise ValueError("Negative historical volume or trade count")
        if rows and opened != rows[-1][0] + STEP_MS:
            raise ValueError("Duplicate, unordered or missing 5m candle")
        rows.append(row)
    if (len(rows) != (end - start) // STEP_MS or not rows
            or rows[0][0] != start or rows[-1][0] != end - STEP_MS):
        raise ValueError("Incomplete monthly price coverage")
    return rows


def _validate_funding_continuity(rows: list[dict]) -> None:
    for previous, current in zip(rows, rows[1:]):
        if current["time_ms"] <= previous["time_ms"]:
            raise ValueError("Duplicate or unordered raw funding timestamp")
        reported = round(current["funding_interval_hours"] * HOUR_MS)
        if current["scheduled_ms"] - previous["scheduled_ms"] != reported:
            raise ValueError("Duplicate, missing or interval-inconsistent funding event")


def _parse_funding(payload: bytes, filename: str, start: int, end: int) -> list[dict]:
    rows = []
    for source in _csv_rows(payload, filename, _FUNDING_HEADER):
        if len(source) != 3:
            raise ValueError("Funding row requires three fields")
        timestamp = int(source[0])
        if not start <= timestamp < end or timestamp >= EFFECTIVE_END_MS:
            raise ValueError("Cross-month or protected funding row rejected")
        hours, rate = _number(source[1]), _number(source[2])
        interval = hours * HOUR_MS
        if hours <= 0 or interval != int(interval) or int(interval) % STEP_MS:
            raise ValueError("Invalid funding interval")
        rows.append({"time_ms": timestamp, "scheduled_ms": timestamp // STEP_MS * STEP_MS,
                     "funding_interval_hours": hours, "interval_hours": hours, "rate": rate})
    _validate_funding_continuity(rows)
    if not rows or rows[0]["scheduled_ms"] != start:
        raise ValueError("Incomplete beginning of monthly funding coverage")
    # Monthly terminal coverage follows the final reported cadence; a change
    # across a month boundary is additionally checked against the next row's
    # own reported interval when months are joined. Never synthesize an event.
    if rows[-1]["scheduled_ms"] + round(rows[-1]["funding_interval_hours"] * HOUR_MS) != end:
        raise ValueError("Incomplete end of monthly funding coverage")
    return rows


def _load_archive(cache: Path, request: dict, download: bool,
                  stop: threading.Event) -> tuple[list, dict]:
    # Revalidate the full request before even checking its cache path.
    approved = archive_request(request["symbol"], request["kind"], request["month"])
    if request != approved:
        raise ValueError("Archive request metadata differs from approved bounds")
    url = request["url"]
    filename = url.rsplit("/", 1)[1]
    target = cache / request["symbol"] / request["kind"] / filename
    checksum_target = target.with_suffix(".zip.CHECKSUM")
    exists, checksum_exists = target.exists(), checksum_target.exists()
    if exists != checksum_exists:
        raise ValueError("Incomplete archive/checksum cache pair")
    if exists:
        payload, checksum = target.read_bytes(), checksum_target.read_bytes()
        origin = "cache"
    else:
        if not download:
            raise FileNotFoundError(f"Explicit old archive absent: {request['kind']}/{filename}")
        checksum = _read_url(request["checksum_url"], stop)
        payload = _read_url(url, stop)
        origin = "download"
    digest = _verify_checksum(payload, checksum, filename)
    parser = _parse_funding if request["kind"] == "fundingRate" else _parse_prices
    rows = parser(payload, filename, request["start_ms"], request["exclusive_end_ms"])
    if not exists:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        checksum_target.write_bytes(checksum)
    record = {**request, "sha256": digest, "checksum_sha256": hashlib.sha256(checksum).hexdigest(), "origin": origin,
              "rows": len(rows), "filename": filename}
    if request["kind"] == "fundingRate":
        record.update(min_time_ms=rows[0]["time_ms"], max_time_ms=rows[-1]["time_ms"],
                      reported_interval_hours=sorted({r["funding_interval_hours"] for r in rows}))
    else:
        record.update(min_time_ms=rows[0][0], max_time_ms=rows[-1][0],
                      max_close_time_ms=rows[-1][6])
    return rows, record


def _attach_marks(funding: list[dict], marks: dict[int, float]) -> None:
    for row in funding:
        mark_open = row["time_ms"] // STEP_MS * STEP_MS
        if mark_open not in marks or mark_open > row["time_ms"]:
            raise ValueError("Missing same-bucket mark; future proxy is forbidden")
        row["mark_price"] = marks[mark_open]
        row["mark_open_ms"] = mark_open
        row["mark_proxy_age_ms"] = row["time_ms"] - mark_open
        row["mark_proxy_ms"] = mark_open
        row["proxy_age_ms"] = row["mark_proxy_age_ms"]
        if not 0 <= row["mark_proxy_age_ms"] < STEP_MS:
            raise ValueError("Invalid mark proxy age")


def load_symbol(symbol: str, cache_root: str | Path, workers: int = 4, *,
                months: tuple[str, ...] | list[str] = MONTHS,
                download: bool = True) -> dict:
    """Return 5m bars, raw-ms funding with prior mark proxy, and SHA manifest.

    Each call owns its symbol; no module-global symbol mutation exists. The
    default is the frozen 25 months. Explicit shorter contiguous approved month
    sequences are available for isolated synthetic tests and diagnostics only.
    """
    requests = _validated_requests(symbol, months, workers)
    if cache_root is None or not str(cache_root).strip():
        raise ValueError("An explicit isolated cache root is required")
    if type(download) is not bool:
        raise ValueError("download must be boolean")
    cache = Path(cache_root).resolve()
    production = PRODUCTION_ROOT.resolve()
    if cache == production or production in cache.parents:
        raise ValueError("Production workspace cannot be a research cache")
    stop = threading.Event()
    loaded, records = {}, []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [(request, executor.submit(_load_archive, cache, request, download, stop))
                   for request in requests]
        try:
            for request, future in futures:
                rows, record = future.result()
                loaded[(request["kind"], request["month"])] = rows
                records.append(record)
        except BaseException:
            stop.set()
            for _, future in futures:
                future.cancel()
            raise
    ordered_months = sorted(months)
    bars = [bar for month in ordered_months for bar in loaded[("klines", month)]]
    marks = {bar[0]: bar[1] for month in ordered_months
             for bar in loaded[("markPriceKlines", month)]}
    funding = [dict(row) for month in ordered_months for row in loaded[("fundingRate", month)]]
    _validate_funding_continuity(funding)
    _attach_marks(funding, marks)
    manifest = {
        "symbol": symbol, "market": "Binance_USDM", "interval": "5m",
        "months": ordered_months, "archives": records,
        "effective_exclusive_end_ms": EFFECTIVE_END_MS, "hard_seal_start_ms": HARD_SEAL_MS,
        "bars": {"rows": len(bars), "min_time_ms": bars[0][0],
                 "max_time_ms": bars[-1][0], "max_close_time_ms": bars[-1][6]},
        "funding": {"rows": len(funding), "min_time_ms": funding[0]["time_ms"],
                    "max_time_ms": funding[-1]["time_ms"],
                    "reported_interval_hours": sorted({r["funding_interval_hours"] for r in funding}),
                    "max_mark_proxy_age_ms": max(r["mark_proxy_age_ms"] for r in funding)},
        "funding_time_basis": "time_ms preserves raw calc_time; scheduled_ms is its 5m bucket for coverage checks only. Each current row's interval describes the preceding interval; never assumes 8h.",
        "funding_mark_proxy": "Same-bucket markPriceKlines open, mark_open_ms <= time_ms; not exact settlement mark and never a future open.",
        "terminal_funding_coverage": "Final monthly reported cadence must reach exclusive month end; changes at joins are additionally checked against the next event's reported interval.",
    }
    return {"bars": bars, "funding": funding, "manifest": manifest}
