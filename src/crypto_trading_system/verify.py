from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from collections.abc import Callable
import uuid

from .config import Settings
from .data_validation import cross_validate_candidates
from .data_quality import tradable_spot_symbols
from .market_data import BinanceClient
from .models import RawTicker, ScanResult
from .scanner import _analyze_ticker


def verify_symbol(settings: Settings, symbol: str, progress: Callable[[str], None] | None = None) -> ScanResult:
    normalized = symbol.upper().replace("/", "").replace("-", "").replace("_", "")
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )

    if progress is not None:
        progress(f"loading Binance metadata for {normalized}")
    exchange_info = client.exchange_info()
    symbol_meta = tradable_spot_symbols(exchange_info, settings.market.quote_asset)
    if normalized not in symbol_meta:
        raise ValueError(f"{normalized} is not a tradable Binance {settings.market.quote_asset} spot symbol")

    if progress is not None:
        progress(f"loading Binance 24h ticker for {normalized}")
    ticker_map = {item["symbol"]: item for item in client.ticker_24hr()}
    ticker = ticker_map.get(normalized)
    if ticker is None:
        raise ValueError(f"No 24h ticker found for {normalized}")

    meta = symbol_meta[normalized]
    high = float(ticker["highPrice"])
    low = float(ticker["lowPrice"])
    raw = RawTicker(
        symbol=normalized,
        base_asset=str(meta["baseAsset"]).upper(),
        price=float(ticker["lastPrice"]),
        pct_24h=float(ticker["priceChangePercent"]),
        quote_volume_24h=float(ticker["quoteVolume"]),
        trades_24h=int(ticker["count"]),
        high_low_range_24h=(high / low - 1) * 100 if low else 0,
    )

    if progress is not None:
        progress(f"loading 1h/4h/1d klines for {normalized}")
    k1h = client.klines(normalized, "1h", 168)
    k4h = client.klines(normalized, "4h", 120)
    k1d = client.klines(normalized, "1d", 100)
    if progress is not None:
        progress(f"building trade plan for {normalized}")
    candidate = _analyze_ticker(
        raw,
        k1h,
        k4h,
        k1d,
        settings.analysis.risk_reward_min,
        pump_chase_24h_pct=settings.analysis.pump_chase_24h_pct,
        pump_chase_distance_pct=settings.analysis.pump_chase_distance_pct,
        pump_chase_penalty=settings.analysis.pump_chase_penalty,
        high_volatility_range_pct=settings.analysis.high_volatility_range_pct,
        high_volatility_penalty=settings.analysis.high_volatility_penalty,
    )
    if candidate is None:
        raise ValueError(f"{normalized} did not produce a valid trade plan under current rules")

    candidate = replace(candidate, rank=1)
    candidates, validation_notes = cross_validate_candidates(settings, [candidate], progress=progress)
    now = datetime.now(timezone.utc)
    return ScanResult(
        scan_id=f"verify_{uuid.uuid4().hex[:8]}",
        timestamp_utc=now.isoformat(timespec="seconds"),
        source="Binance public spot API + CoinGecko/CoinMarketCap cross-check",
        filters=f"single-symbol verification for {normalized}; analyze 1h/4h/1d klines",
        limitations=[
            "单币复核报告用于人工核对数据、指标和交易计划推导。",
            "交易信号仍以 Binance 公开现货 K 线为主源；外部数据源用于一致性复核。",
            *validation_notes,
        ],
        candidates=candidates,
    )
