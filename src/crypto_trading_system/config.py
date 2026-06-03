from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import tomllib


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class MarketSettings:
    base_url: str
    quote_asset: str
    min_quote_volume: float
    min_trades: int
    max_universe: int
    top_n: int
    request_timeout_seconds: int
    request_pause_seconds: float
    exclude_bases: tuple[str, ...]


@dataclass
class AnalysisSettings:
    risk_reward_min: float
    risk_per_trade_pct: float


@dataclass
class PaperSettings:
    account_name: str
    account_equity: float
    risk_per_trade_pct: float


@dataclass
class DataValidationSettings:
    enabled: bool
    coingecko_base_url: str
    coinmarketcap_base_url: str
    coinmarketcap_api_key: str | None
    price_warning_pct: float
    price_error_pct: float
    pct_24h_warning_points: float
    request_timeout_seconds: int
    request_pause_seconds: float
    coin_id_overrides: dict[str, str]
    cmc_id_overrides: dict[str, int]


@dataclass
class OutputSettings:
    database_path: Path
    reports_dir: Path
    obsidian_dir: Path | None


@dataclass
class Settings:
    market: MarketSettings
    analysis: AnalysisSettings
    paper: PaperSettings
    data_validation: DataValidationSettings
    output: OutputSettings


def _resolve_path(raw: str | None, root: Path) -> Path | None:
    if not raw:
        return None
    path = Path(raw)
    if path.is_absolute():
        return path
    return root / path


def load_settings(path: Path) -> Settings:
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    data = tomllib.loads(path.read_text(encoding="utf-8"))

    market = data["market"]
    analysis = data["analysis"]
    paper = data.get("paper", {})
    data_validation = data.get("data_validation", {})
    output = data["output"]

    coinmarketcap_api_key = data_validation.get("coinmarketcap_api_key")
    if not coinmarketcap_api_key:
        coinmarketcap_api_key = os.environ.get("CMC_API_KEY") or os.environ.get("COINMARKETCAP_API_KEY")

    return Settings(
        market=MarketSettings(
            base_url=str(market["base_url"]).rstrip("/"),
            quote_asset=str(market.get("quote_asset", "USDT")),
            min_quote_volume=float(market.get("min_quote_volume", 30_000_000)),
            min_trades=int(market.get("min_trades", 30_000)),
            max_universe=int(market.get("max_universe", 50)),
            top_n=int(market.get("top_n", 5)),
            request_timeout_seconds=int(market.get("request_timeout_seconds", 30)),
            request_pause_seconds=float(market.get("request_pause_seconds", 0.04)),
            exclude_bases=tuple(str(x).upper() for x in market.get("exclude_bases", [])),
        ),
        analysis=AnalysisSettings(
            risk_reward_min=float(analysis.get("risk_reward_min", 2.0)),
            risk_per_trade_pct=float(analysis.get("risk_per_trade_pct", 0.01)),
        ),
        paper=PaperSettings(
            account_name=str(paper.get("account_name", "demo")),
            account_equity=float(paper.get("account_equity", 10_000)),
            risk_per_trade_pct=float(paper.get("risk_per_trade_pct", analysis.get("risk_per_trade_pct", 0.01))),
        ),
        data_validation=DataValidationSettings(
            enabled=bool(data_validation.get("enabled", True)),
            coingecko_base_url=str(data_validation.get("coingecko_base_url", "https://api.coingecko.com/api/v3")).rstrip("/"),
            coinmarketcap_base_url=str(data_validation.get("coinmarketcap_base_url", "https://pro-api.coinmarketcap.com")).rstrip("/"),
            coinmarketcap_api_key=None if not coinmarketcap_api_key else str(coinmarketcap_api_key),
            price_warning_pct=float(data_validation.get("price_warning_pct", 1.0)),
            price_error_pct=float(data_validation.get("price_error_pct", 2.0)),
            pct_24h_warning_points=float(data_validation.get("pct_24h_warning_points", 3.0)),
            request_timeout_seconds=int(data_validation.get("request_timeout_seconds", market.get("request_timeout_seconds", 30))),
            request_pause_seconds=float(data_validation.get("request_pause_seconds", market.get("request_pause_seconds", 0.04))),
            coin_id_overrides={str(k).upper(): str(v) for k, v in data_validation.get("coin_id_overrides", {}).items()},
            cmc_id_overrides={str(k).upper(): int(v) for k, v in data_validation.get("cmc_id_overrides", {}).items()},
        ),
        output=OutputSettings(
            database_path=_resolve_path(output.get("database_path"), PROJECT_ROOT),
            reports_dir=_resolve_path(output.get("reports_dir"), PROJECT_ROOT),
            obsidian_dir=_resolve_path(output.get("obsidian_dir"), PROJECT_ROOT),
        ),
    )
