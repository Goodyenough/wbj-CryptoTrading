"""Entirely synthetic archive and data-boundary tests; no real data or network."""
import csv
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
from pathlib import Path
import sys
import threading
from urllib.error import HTTPError
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from research.short_trend import data
from research.short_trend.preflight import archive_request

MONTH = "2024-02"
REQUEST = archive_request("BTCUSDT", "klines", MONTH)
START, END = REQUEST["start_ms"], REQUEST["exclusive_end_ms"]


def zip_csv(filename, header, rows):
    text = io.StringIO(newline="")
    writer = csv.writer(text)
    writer.writerow(header)
    writer.writerows(rows)
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(filename.removesuffix(".zip") + ".csv", text.getvalue())
    return stream.getvalue()


def price_row(timestamp, price=100):
    return [timestamp, price, price + 2, price - 2, price + 1, 10,
            timestamp + data.STEP_MS - 1, 1000, 2, 4, 400, 0]


def checksum(payload, filename):
    return f"{hashlib.sha256(payload).hexdigest()}  {filename}\n".encode()


class Response(io.BytesIO):
    def __init__(self, payload, url):
        super().__init__(payload)
        self.url = url

    def geturl(self):
        return self.url


@pytest.fixture(scope="module")
def synthetic_network():
    network = {}
    for symbol in ("BTCUSDT", "ETHUSDT"):
        for kind in sorted(data.KINDS):
            request = archive_request(symbol, kind, MONTH)
            url = request["url"]
            filename = url.rsplit("/", 1)[1]
            if kind == "fundingRate":
                rows = [[stamp + i % 2, 8, .0001]
                        for i, stamp in enumerate(range(START, END, 8 * data.HOUR_MS))]
                header = data._FUNDING_HEADER
            else:
                price = 100 if symbol == "BTCUSDT" else 200
                rows = [price_row(stamp, price) for stamp in range(START, END, data.STEP_MS)]
                header = data._PRICE_HEADER
            payload = zip_csv(filename, header, rows)
            network[url], network[url + ".CHECKSUM"] = payload, checksum(payload, filename)
    return network


@pytest.mark.parametrize("symbol,months,workers", [
    ("BTCUSDT", ["2026-01"], 4), ("BTCUSDT", ["2026-06"], 4),
    ("BTCUSDT", ["2023-11"], 4), ("BTCUSDT", ["2024-13"], 4),
    ("BTCUSDT", [MONTH, "2026-02"], 4), ("BTCUSDT", [MONTH, MONTH], 4),
    ("BTCUSDT", ["2024-01", "2024-03"], 4), ("NOTAPPROVED", [MONTH], 4),
    ("BTCUSDT", [], 4), ("BTCUSDT", [MONTH], True), ("BTCUSDT", [MONTH], 0),
])
def test_request_validation_precedes_all_filesystem_and_network(monkeypatch, symbol, months, workers):
    def forbidden(*args, **kwargs):
        pytest.fail("Filesystem or network accessed before request validation")
    for name in ("resolve", "read_bytes", "exists"):
        monkeypatch.setattr(Path, name, forbidden)
    monkeypatch.setattr(data, "urlopen", forbidden)
    with pytest.raises(ValueError):
        data.load_symbol(symbol, "unused", workers, months=months)


def test_default_requests_are_exact_25_months_and_75_archives():
    requests = data._validated_requests("SOLUSDT", data.MONTHS, 4)
    assert len(requests) == 75
    assert data.MONTHS[0] == "2023-12" and data.MONTHS[-1] == "2025-12"
    assert all(r["exclusive_end_ms"] <= data.EFFECTIVE_END_MS for r in requests)


def test_two_symbols_hash_manifest_and_offline_cache(tmp_path, monkeypatch, synthetic_network):
    calls = []
    def open_mock(request, timeout):
        assert timeout == 30
        calls.append(request.full_url)
        return Response(synthetic_network[request.full_url], request.full_url)
    monkeypatch.setattr(data, "urlopen", open_mock)
    with ThreadPoolExecutor(max_workers=2) as executor:
        btc_job = executor.submit(data.load_symbol, "BTCUSDT", tmp_path, months=[MONTH])
        eth_job = executor.submit(data.load_symbol, "ETHUSDT", tmp_path, months=[MONTH])
        btc, eth = btc_job.result(), eth_job.result()
    assert len(calls) == 12
    assert btc["bars"][0][1] == 100 and eth["bars"][0][1] == 200
    assert btc["manifest"]["symbol"] == "BTCUSDT"
    funding = btc["funding"]
    assert funding[1]["time_ms"] == START + 8 * data.HOUR_MS + 1
    assert funding[1]["mark_proxy_ms"] == START + 8 * data.HOUR_MS
    assert funding[1]["proxy_age_ms"] == 1
    assert funding[1]["interval_hours"] == 8
    assert all(r["mark_proxy_ms"] <= r["time_ms"] < r["mark_proxy_ms"] + data.STEP_MS
               for r in funding)
    for record in btc["manifest"]["archives"]:
        assert record["sha256"] == hashlib.sha256(synthetic_network[record["url"]]).hexdigest()
        assert record["checksum_sha256"] == hashlib.sha256(synthetic_network[record["checksum_url"]]).hexdigest()
    monkeypatch.setattr(data, "urlopen", lambda *_a, **_k: pytest.fail("Offline mode used network"))
    offline = data.load_symbol("BTCUSDT", tmp_path, months=[MONTH], download=False)
    assert offline["bars"] == btc["bars"] and offline["funding"] == btc["funding"]
    assert all(r["origin"] == "cache" for r in offline["manifest"]["archives"])


def test_missing_offline_archive_never_contacts_network(tmp_path, monkeypatch):
    monkeypatch.setattr(data, "urlopen", lambda *_a, **_k: pytest.fail("Missing offline file used network"))
    with pytest.raises(FileNotFoundError):
        data.load_symbol("BTCUSDT", tmp_path, months=[MONTH], download=False)


def test_half_cache_pair_is_failure(tmp_path):
    target = tmp_path / "BTCUSDT" / "klines" / REQUEST["url"].rsplit("/", 1)[1]
    target.parent.mkdir(parents=True)
    target.write_bytes(b"not read")
    with pytest.raises(ValueError, match="cache pair"):
        data._load_archive(tmp_path, REQUEST, False, threading.Event())


def test_checksum_failure_never_writes_cache(tmp_path, monkeypatch, synthetic_network):
    filename = REQUEST["url"].rsplit("/", 1)[1]
    monkeypatch.setattr(data, "_read_url", lambda url, stop: (
        checksum(b"wrong", filename) if url.endswith(".CHECKSUM") else synthetic_network[url]))
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        data._load_archive(tmp_path, REQUEST, True, threading.Event())
    assert not (tmp_path / "BTCUSDT").exists()


@pytest.mark.parametrize("kind", ["price", "funding"])
def test_protected_timestamp_rejected_before_market_conversion(monkeypatch, kind):
    monkeypatch.setattr(data, "_number", lambda *_: pytest.fail("Protected market field converted"))
    if kind == "price":
        name = "BTCUSDT-5m-2024-02.zip"
        payload = zip_csv(name, data._PRICE_HEADER, [price_row(data.EFFECTIVE_END_MS)])
        parser = data._parse_prices
    else:
        name = "BTCUSDT-fundingRate-2024-02.zip"
        payload = zip_csv(name, data._FUNDING_HEADER, [[data.EFFECTIVE_END_MS, 8, "sensitive"]])
        parser = data._parse_funding
    with pytest.raises(ValueError, match="protected"):
        parser(payload, name, START, END)


@pytest.mark.parametrize("issue", ["missing", "duplicate", "ohlc", "nonfinite", "negative_volume", "incomplete"])
def test_price_quality_not_synthesized(issue):
    name = "BTCUSDT-5m-2024-02.zip"
    rows = [price_row(START), price_row(START + data.STEP_MS)]
    if issue == "missing": rows[1][0] += data.STEP_MS; rows[1][6] += data.STEP_MS
    if issue == "duplicate": rows[1] = rows[0]
    if issue == "ohlc": rows[0][3] = 103
    if issue == "nonfinite": rows[0][1] = "nan"
    if issue == "negative_volume": rows[0][5] = -1
    payload = zip_csv(name, data._PRICE_HEADER, rows)
    with pytest.raises(ValueError):
        data._parse_prices(payload, name, START, END)


@pytest.mark.parametrize("rate,hours", [("nan", 8), ("inf", 8), (.0001, 0), (.0001, -4), (.0001, .00001)])
def test_bad_rate_or_reported_interval_rejected(rate, hours):
    name = "BTCUSDT-fundingRate-2024-02.zip"
    payload = zip_csv(name, data._FUNDING_HEADER, [[START, hours, rate]])
    with pytest.raises(ValueError):
        data._parse_funding(payload, name, START, END)


def test_reported_funding_interval_can_change_without_hardcoded_8h():
    name = "BTCUSDT-fundingRate-2024-02.zip"
    # Start with 8h, change to 4h after the first day; each row's interval
    # describes the elapsed preceding settlement schedule interval.
    switch = START + 24 * data.HOUR_MS
    source = [[t + (i % 2), 8, -.0001]
              for i, t in enumerate(range(START, switch + 1, 8 * data.HOUR_MS))]
    source.extend([[t + 2, 4, .0002] for t in range(switch + 4 * data.HOUR_MS, END, 4 * data.HOUR_MS)])
    parsed = data._parse_funding(zip_csv(name, data._FUNDING_HEADER, source), name, START, END)
    assert {r["interval_hours"] for r in parsed} == {4, 8}
    assert [r["time_ms"] for r in parsed] == [r[0] for r in source]
    source.pop(5)
    with pytest.raises(ValueError, match="missing"):
        data._parse_funding(zip_csv(name, data._FUNDING_HEADER, source), name, START, END)


def test_mark_requires_same_bucket_not_future():
    funding = [{"time_ms": START + 1}]
    with pytest.raises(ValueError, match="future"):
        data._attach_marks(funding, {START + data.STEP_MS: 100})
    data._attach_marks(funding, {START: 100})
    assert funding[0]["proxy_age_ms"] == 1


@pytest.mark.parametrize("url", [
    "https://fapi.binance.com/fapi/v1/klines",
    "https://data.binance.vision/data/futures/um/monthly/klines/BTCUSDT/5m/BTCUSDT-5m-2026-01.zip",
    "https://data.binance.vision/data/futures/um/monthly/klines/ETHUSDT/5m/BTCUSDT-5m-2024-02.zip",
])
def test_network_boundary_rejects_arbitrary_urls_before_open(monkeypatch, url):
    monkeypatch.setattr(data, "urlopen", lambda *_a, **_k: pytest.fail("Unapproved network access"))
    with pytest.raises(ValueError):
        data._read_url(url, threading.Event())


def test_redirect_is_rejected_before_destination_access():
    with pytest.raises(ValueError, match="redirects"):
        data._NoRedirect().redirect_request(None, None, 302, "redirect", {}, "https://example.invalid")


def test_response_url_change_is_also_rejected(monkeypatch):
    monkeypatch.setattr(data, "urlopen", lambda *_a, **_k: Response(b"not parsed", "https://example.invalid"))
    with pytest.raises(ValueError, match="redirects"):
        data._read_url(REQUEST["url"], threading.Event())


@pytest.mark.parametrize("status", [403, 451, 429])
def test_denied_or_rate_limited_download_retries_are_bounded(monkeypatch, status):
    calls, sleeps = [], []
    def denied(request, timeout):
        calls.append(request.full_url)
        raise HTTPError(request.full_url, status, "denied", {}, None)
    monkeypatch.setattr(data, "urlopen", denied)
    monkeypatch.setattr(data.time, "sleep", sleeps.append)
    stop = threading.Event()
    with pytest.raises((RuntimeError, HTTPError)):
        data._read_url(REQUEST["url"], stop)
    assert len(calls) == (3 if status == 429 else 1)
    assert sleeps == ([.5, 1.] if status == 429 else [])
    assert stop.is_set()


def test_modified_request_metadata_rejected_before_cache_access(tmp_path, monkeypatch):
    request = {**REQUEST, "exclusive_end_ms": data.EFFECTIVE_END_MS + 1}
    monkeypatch.setattr(Path, "exists", lambda *_: pytest.fail("Modified request accessed cache"))
    with pytest.raises(ValueError, match="metadata"):
        data._load_archive(tmp_path, request, False, threading.Event())


def test_wrong_zip_members_and_header_are_not_accepted():
    name = "BTCUSDT-5m-2024-02.zip"
    wrong_member = zip_csv("OTHER.zip", data._PRICE_HEADER, [price_row(START)])
    with pytest.raises(ValueError, match="matching CSV"):
        data._parse_prices(wrong_member, name, START, END)
    wrong_header = zip_csv(name, ["unknown"], [["unparsed"]])
    with pytest.raises(ValueError, match="header"):
        data._parse_prices(wrong_header, name, START, END)
