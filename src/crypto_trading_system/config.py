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
    min_history_days: int
    market_regime_filter_enabled: bool
    data_quality_filter_enabled: bool
    strict_data_quality_for_buy: bool
    pump_chase_24h_pct: float
    pump_chase_distance_pct: float
    pump_chase_penalty: float
    high_volatility_range_pct: float
    high_volatility_penalty: float
    risk_off_core_buy_enabled: bool
    entry_reclaim_close_enabled: bool
    validation_pool_multiplier: int
    validation_pool_max: int


@dataclass
class PaperSettings:
    account_name: str
    account_equity: float
    risk_per_trade_pct: float
    import_actions: tuple[str, ...]


@dataclass
class BacktestSettings:
    maker_fee_bps: float
    taker_fee_bps: float
    entry_slippage_bps: float
    stop_slippage_bps: float
    intrabar_policy: str
    primary_interval: str
    execution_interval: str
    initial_equity: float
    max_open_plans: int
    max_active_positions: int
    total_active_risk_pct: float
    risk_per_trade_pct: float
    max_position_notional_pct: float
    allow_leverage: bool
    watch_expiry_bars: int
    warmup_1h_bars: int
    warmup_4h_bars: int
    warmup_1d_bars: int


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
    backtest: BacktestSettings
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
    backtest = data.get("backtest", {})
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
            min_history_days=int(analysis.get("min_history_days", 180)),
            market_regime_filter_enabled=bool(analysis.get("market_regime_filter_enabled", True)),
            data_quality_filter_enabled=bool(analysis.get("data_quality_filter_enabled", True)),
            strict_data_quality_for_buy=bool(analysis.get("strict_data_quality_for_buy", True)),
            pump_chase_24h_pct=float(analysis.get("pump_chase_24h_pct", 20.0)),
            pump_chase_distance_pct=float(analysis.get("pump_chase_distance_pct", 8.0)),
            pump_chase_penalty=float(analysis.get("pump_chase_penalty", 8.0)),
            high_volatility_range_pct=float(analysis.get("high_volatility_range_pct", 35.0)),
            high_volatility_penalty=float(analysis.get("high_volatility_penalty", 6.0)),
            risk_off_core_buy_enabled=bool(analysis.get("risk_off_core_buy_enabled", True)),
            entry_reclaim_close_enabled=bool(analysis.get("entry_reclaim_close_enabled", False)),
            validation_pool_multiplier=int(analysis.get("validation_pool_multiplier", 2)),
            validation_pool_max=int(analysis.get("validation_pool_max", 10)),
        ),
        paper=PaperSettings(
            account_name=str(paper.get("account_name", "demo")),
            account_equity=float(paper.get("account_equity", 10_000)),
            risk_per_trade_pct=float(paper.get("risk_per_trade_pct", analysis.get("risk_per_trade_pct", 0.01))),
            import_actions=tuple(str(item).upper() for item in paper.get("import_actions", ["BUY_CANDIDATE"])),
        ),
        backtest=BacktestSettings(
            maker_fee_bps=float(backtest.get("maker_fee_bps", 4)),
            taker_fee_bps=float(backtest.get("taker_fee_bps", 10)),
            entry_slippage_bps=float(backtest.get("entry_slippage_bps", 5)),
            stop_slippage_bps=float(backtest.get("stop_slippage_bps", 10)),
            intrabar_policy=str(backtest.get("intrabar_policy", "stop_first")),
            primary_interval=str(backtest.get("primary_interval", "4h")),
            execution_interval=str(backtest.get("execution_interval", "4h")),
            initial_equity=float(backtest.get("initial_equity", 10_000)),
            max_open_plans=int(backtest.get("max_open_plans", 10)),
            max_active_positions=int(backtest.get("max_active_positions", 5)),
            total_active_risk_pct=float(backtest.get("total_active_risk_pct", 0.05)),
            risk_per_trade_pct=float(backtest.get("risk_per_trade_pct", analysis.get("risk_per_trade_pct", 0.01))),
            max_position_notional_pct=float(backtest.get("max_position_notional_pct", 1.0)),
            allow_leverage=bool(backtest.get("allow_leverage", False)),
            watch_expiry_bars=int(backtest.get("watch_expiry_bars", 18)),
            warmup_1h_bars=int(backtest.get("warmup_1h_bars", 200)),
            warmup_4h_bars=int(backtest.get("warmup_4h_bars", 100)),
            warmup_1d_bars=int(backtest.get("warmup_1d_bars", 80)),
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
