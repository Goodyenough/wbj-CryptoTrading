from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest import universe as universe_module
from crypto_trading_system.config import load_settings


class FakeBinanceClient:
    def __init__(self, *args, **kwargs) -> None:
        pass

    def exchange_info(self) -> dict:
        return {
            "symbols": [
                _symbol("BTCUSDT", "BTC"),
                _symbol("ETHUSDT", "ETH"),
                _symbol("LOWUSDT", "LOW"),
                _symbol("USDCUSDT", "USDC"),
                _symbol("BADUSDT", "BAD", status="BREAK"),
            ]
        }

    def ticker_24hr(self) -> list[dict]:
        return [
            _ticker("BTCUSDT", 100.0, 1.0, 100_000_000, 100_000, 110.0, 90.0),
            _ticker("ETHUSDT", 10.0, 0.0, 90_000_000, 90_000, 11.0, 9.0),
            _ticker("LOWUSDT", 1.0, 10.0, 1_000, 10, 1.1, 1.0),
            _ticker("USDCUSDT", 1.0, 0.1, 200_000_000, 200_000, 1.001, 0.999),
            _ticker("BADUSDT", 1.0, 100.0, 200_000_000, 200_000, 2.0, 1.0),
        ]


def _symbol(symbol: str, base_asset: str, status: str = "TRADING") -> dict:
    return {
        "symbol": symbol,
        "status": status,
        "baseAsset": base_asset,
        "quoteAsset": "USDT",
        "isSpotTradingAllowed": True,
    }


def _ticker(
    symbol: str,
    price: float,
    pct_24h: float,
    quote_volume: float,
    trades: int,
    high: float,
    low: float,
) -> dict:
    return {
        "symbol": symbol,
        "lastPrice": str(price),
        "priceChangePercent": str(pct_24h),
        "quoteVolume": str(quote_volume),
        "count": str(trades),
        "highPrice": str(high),
        "lowPrice": str(low),
    }


def test_fetch_universe_snapshot_filters_and_sorts() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    original = universe_module.BinanceClient
    universe_module.BinanceClient = FakeBinanceClient
    try:
        snapshot = universe_module.fetch_universe_snapshot(settings, max_symbols=2)
    finally:
        universe_module.BinanceClient = original

    assert snapshot.mode == "universe_snapshot"
    assert snapshot.candidate_count == 2
    assert snapshot.selected_count == 2
    assert snapshot.selected_symbols == ["BTCUSDT", "ETHUSDT"]
    assert "24h quote volume" in snapshot.filters


if __name__ == "__main__":
    test_fetch_universe_snapshot_filters_and_sorts()
    print("test_universe=passed")
