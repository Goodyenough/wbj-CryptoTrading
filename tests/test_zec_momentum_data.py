"""Synthetic archive tests; never contact Binance or open shared market data."""
import csv
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
from research.zec_momentum import data


MONTH = "2024-02"
START, END = data._month_bounds(MONTH)


def zip_csv(filename, header, rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream)
    writer.writerow(header)
    writer.writerows(rows)
    result = io.BytesIO()
    with zipfile.ZipFile(result, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(filename.removesuffix(".zip") + ".csv", stream.getvalue())
    return result.getvalue()


def price_row(timestamp, price=100):
    return [timestamp, price, price + 2, price - 2, price + 1, 10,
            timestamp + data.STEP_MS - 1, 1000, 2, 4, 400, 0]


def checksum(payload, filename):
    return f"{hashlib.sha256(payload).hexdigest()}  {filename}\n".encode()


@pytest.fixture(scope="module")
def archives():
    result = {}
    for kind in data.KINDS:
        url = data._archive_url(kind, MONTH)
        filename = url.rsplit("/", 1)[1]
        if kind == "fundingRate":
            rows = [[time_ms, 8, "0.0001"] for time_ms in range(START, END, 8 * 3_600_000)]
            header = data._FUNDING_HEADER
        else:
            rows = [price_row(time_ms, 100 + index / 1000 if kind == "markPriceKlines" else 90)
                    for index, time_ms in enumerate(range(START, END, data.STEP_MS))]
            header = data._PRICE_HEADER
        payload = zip_csv(filename, header, rows)
        result[url] = payload
        result[url + ".CHECKSUM"] = checksum(payload, filename)
    return result


class Response(io.BytesIO):
    def __init__(self, content, url):
        super().__init__(content)
        self.url = url

    def geturl(self):
        return self.url


@pytest.mark.parametrize("months,cutoff", [
    (["2026-01"], data.CUTOFF_MS),
    (["2026-06"], data.CUTOFF_MS),
    (["2023-11"], data.CUTOFF_MS),
    (["2024-13"], data.CUTOFF_MS),
    ([MONTH, "2026-07"], data.CUTOFF_MS),
    ([MONTH, MONTH], data.CUTOFF_MS),
    (["2024-01", "2024-03"], data.CUTOFF_MS),
    ([MONTH], END - 1),
    ([MONTH], data.CUTOFF_MS + 1),
])
def test_protected_or_invalid_request_rejected_before_cache_or_network(monkeypatch, months, cutoff):
    def forbidden(*args, **kwargs):
        raise AssertionError("Filesystem/network operation preceded request validation")
    monkeypatch.setattr(data, "urlopen", forbidden)
    monkeypatch.setattr(Path, "read_bytes", forbidden)
    monkeypatch.setattr(Path, "resolve", forbidden)
    monkeypatch.setattr(Path, "exists", forbidden)
    with pytest.raises(ValueError):
        data.load_dataset("unused-isolated-cache", months=months, cutoff_ms=cutoff)


def test_mock_download_hash_manifest_mark_alignment_and_offline_cache(tmp_path, monkeypatch, archives):
    calls = []
    def fake_open(request, timeout):
        assert timeout == 30
        calls.append(request.full_url)
        return Response(archives[request.full_url], request.full_url)
    monkeypatch.setattr(data, "urlopen", fake_open)
    bars, funding, manifest = data.load_dataset(tmp_path / "isolated", months=[MONTH])
    assert len(calls) == 6
    assert set(calls) == set(archives)
    assert len(bars) == (END - START) // data.STEP_MS
    assert len(bars[0]) == 12
    assert funding[0]["mark_price"] == 100
    assert funding[1]["time_ms"] == START + 8 * 3_600_000
    assert funding[1]["mark_price"] == pytest.approx(100.096)
    assert funding[1]["rate"] == 0.0001
    assert manifest["funding"]["min_time_ms"] == START
    assert manifest["bars"]["max_close_time_ms"] == END - 1
    assert all(record["sha256"] == hashlib.sha256(archives[record["url"]]).hexdigest()
               for record in manifest["archives"])
    assert "exactly funding time" in manifest["funding_mark_proxy"]
    def no_network(*args, **kwargs):
        pytest.fail("download=False reached the network")
    monkeypatch.setattr(data, "urlopen", no_network)
    cached_bars, cached_funding, cached_manifest = data.load_dataset(
        tmp_path / "isolated", months=[MONTH], download=False)
    assert cached_bars == bars
    assert cached_funding == funding
    assert all(record["origin"] == "cache" for record in cached_manifest["archives"])


@pytest.mark.parametrize("timestamp,cutoff", [(END, data.CUTOFF_MS), (START, START + data.STEP_MS - 1)])
def test_cross_month_or_cutoff_candle_is_rejected(timestamp, cutoff):
    filename = f"ZECUSDT-5m-{MONTH}.zip"
    payload = zip_csv(filename, data._PRICE_HEADER, [price_row(timestamp)])
    with pytest.raises(ValueError, match="protected kline"):
        data._parse_prices(payload, filename, START, END, cutoff)


def test_checksum_corruption_rejected_without_caching(tmp_path, monkeypatch, archives):
    url = data._archive_url("klines", MONTH)
    def fake_read(requested, stop):
        if requested.endswith(".CHECKSUM"):
            return checksum(b"different bytes", url.rsplit("/", 1)[1])
        return archives[url]
    monkeypatch.setattr(data, "_read_url", fake_read)
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        data._load_archive(tmp_path, "klines", MONTH, START, END, data.CUTOFF_MS, True, threading.Event())
    assert not (tmp_path / "klines").exists()


def test_wrong_header_rejected_after_valid_mock_network_checksum(tmp_path, monkeypatch):
    url = data._archive_url("klines", MONTH)
    filename = url.rsplit("/", 1)[1]
    payload = zip_csv(filename, ("unexpected",), [["not market data"]])
    network = {url: payload, url + ".CHECKSUM": checksum(payload, filename)}
    monkeypatch.setattr(data, "urlopen", lambda request, timeout: Response(network[request.full_url], request.full_url))
    with pytest.raises(ValueError, match="CSV header"):
        data._load_archive(tmp_path, "klines", MONTH, START, END, data.CUTOFF_MS, True, threading.Event())
    assert not (tmp_path / "klines").exists()


@pytest.mark.parametrize("issue", ["missing", "duplicate", "ohlc"])
def test_price_quality_errors_are_not_synthesized(issue):
    filename = f"ZECUSDT-5m-{MONTH}.zip"
    rows = [price_row(START), price_row(START + data.STEP_MS)]
    if issue == "missing":
        rows[1] = price_row(START + 2 * data.STEP_MS)
    elif issue == "duplicate":
        rows[1] = rows[0]
    else:
        rows[0][3] = 103
    payload = zip_csv(filename, data._PRICE_HEADER, rows)
    with pytest.raises(ValueError, match="missing kline|OHLC"):
        data._parse_prices(payload, filename, START, END, data.CUTOFF_MS)


def test_funding_requires_exact_mark_instead_of_future_proxy(monkeypatch, tmp_path):
    def fake_load(cache, kind, month, start, end, cutoff, download, stop):
        if kind == "fundingRate":
            rows = [{"time_ms": start, "rate": .0001, "funding_interval_hours": 8}]
        else:
            rows = [price_row(start + data.STEP_MS)]
        return rows, {"kind": kind}
    monkeypatch.setattr(data, "_load_archive", fake_load)
    with pytest.raises(ValueError, match="exactly aligned"):
        data.load_dataset(tmp_path, months=[MONTH])


def test_funding_off_grid_and_missing_event_rejected():
    filename = f"ZECUSDT-fundingRate-{MONTH}.zip"
    offgrid = zip_csv(filename, data._FUNDING_HEADER, [[START + 1, 8, .0001]])
    with pytest.raises(ValueError, match="funding timestamp"):
        data._parse_funding(offgrid, filename, START, END, data.CUTOFF_MS)
    missing = zip_csv(filename, data._FUNDING_HEADER,
                      [[START, 8, .0001], [START + 16 * 3_600_000, 8, .0001]])
    with pytest.raises(ValueError, match="missing funding"):
        data._parse_funding(missing, filename, START, END, data.CUTOFF_MS)


@pytest.mark.parametrize("status", [403, 451])
def test_access_denied_stops_immediately(monkeypatch, status):
    calls = []
    def denied(request, timeout):
        calls.append(request.full_url)
        raise HTTPError(request.full_url, status, "denied", {}, None)
    monkeypatch.setattr(data, "urlopen", denied)
    stop = threading.Event()
    with pytest.raises(RuntimeError, match="downloads stopped"):
        data._read_url(data._archive_url("klines", MONTH), stop)
    assert len(calls) == 1
    assert stop.is_set()


def test_rate_limit_retry_is_finite(monkeypatch):
    calls, sleeps = [], []
    def limited(request, timeout):
        calls.append(request.full_url)
        raise HTTPError(request.full_url, 429, "limited", {}, None)
    monkeypatch.setattr(data, "urlopen", limited)
    monkeypatch.setattr(data.time, "sleep", sleeps.append)
    with pytest.raises(HTTPError):
        data._read_url(data._archive_url("klines", MONTH), threading.Event())
    assert len(calls) == 3
    assert sleeps == [.5, 1.0]


def test_redirect_handler_rejects_before_requesting_another_url():
    with pytest.raises(ValueError, match="redirects"):
        data._NoRedirect().redirect_request(None, None, 302, "redirect", {},
                                           "https://example.invalid/protected")
