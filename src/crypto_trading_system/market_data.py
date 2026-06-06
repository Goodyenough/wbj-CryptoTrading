from __future__ import annotations

import json
import http.client
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


class BinanceClient:
    def __init__(
        self,
        base_url: str,
        timeout_seconds: int = 30,
        pause_seconds: float = 0.04,
        retries: int = 3,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.pause_seconds = pause_seconds
        self.retries = retries

    def _get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        query = ""
        if params:
            query = "?" + urllib.parse.urlencode(params)
        url = f"{self.base_url}{path}{query}"
        last_error: Exception | None = None

        for attempt in range(self.retries):
            try:
                request = urllib.request.Request(
                    url,
                    headers={"User-Agent": "CryptoTradingSystem/0.1"},
                )
                with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                    payload = response.read().decode("utf-8")
                if self.pause_seconds:
                    time.sleep(self.pause_seconds)
                return json.loads(payload)
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code in {418, 429}:
                    time.sleep(2**attempt + 1)
                    continue
                raise
            except (urllib.error.URLError, http.client.IncompleteRead) as exc:
                last_error = exc
                time.sleep(2**attempt + 1)

        if last_error:
            raise last_error
        raise RuntimeError(f"Failed to fetch {url}")

    def exchange_info(self) -> dict[str, Any]:
        return self._get_json("/api/v3/exchangeInfo")

    def ticker_24hr(self) -> list[dict[str, Any]]:
        return self._get_json("/api/v3/ticker/24hr")

    def klines(
        self,
        symbol: str,
        interval: str,
        limit: int = 1000,
        start_time_ms: int | None = None,
        end_time_ms: int | None = None,
    ) -> list[list[Any]]:
        params: dict[str, Any] = {"symbol": symbol, "interval": interval, "limit": limit}
        if start_time_ms is not None:
            params["startTime"] = start_time_ms
        if end_time_ms is not None:
            params["endTime"] = end_time_ms
        return self._get_json("/api/v3/klines", params)
