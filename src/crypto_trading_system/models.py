from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DataSourceCheck:
    provider: str
    status: str
    provider_asset_id: str | None
    provider_symbol: str | None
    price_usd: float | None
    pct_24h: float | None
    volume_24h: float | None
    last_updated: str | None
    fetched_at_utc: str
    price_diff_pct: float | None
    pct_24h_diff: float | None
    volume_note: str
    message: str


@dataclass
class RawTicker:
    symbol: str
    base_asset: str
    price: float
    pct_24h: float
    quote_volume_24h: float
    trades_24h: int
    high_low_range_24h: float


@dataclass
class TradeCandidate:
    rank: int
    symbol: str
    base_asset: str
    price: float
    score: float
    setup: str
    verdict: str
    entry_low: float
    entry_high: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    risk_reward_1: float
    risk_reward_2: float
    pct_24h: float
    pct_3d: float | None
    pct_7d: float | None
    quote_volume_24h: float
    trades_24h: int
    high_low_range_24h: float
    rsi_1h: float | None
    rsi_4h: float | None
    ema20_4h: float | None
    ema50_4h: float | None
    ema20_1d: float | None
    ema50_1d: float | None
    atr_4h: float | None
    macd_hist_4h: float | None
    volume_ratio_24h: float | None
    support_level: float | None
    recent_low_4h_18: float | None
    recent_high_4h_36: float | None
    distance_to_support_pct: float | None
    binance_trade_url: str
    tradingview_url: str
    coingecko_search_url: str
    coinmarketcap_search_url: str
    invalidation: str
    recent_4h_klines: list[dict[str, float | int | str]] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    data_quality_status: str = "DATA_NOT_CHECKED"
    data_quality_message: str = "Data cross-check has not run."
    data_checks: list[DataSourceCheck] = field(default_factory=list)
    action: str = "WATCH_ONLY"


@dataclass
class ScanResult:
    scan_id: str
    timestamp_utc: str
    source: str
    filters: str
    limitations: list[str]
    candidates: list[TradeCandidate]
    context_candidates: list[TradeCandidate] = field(default_factory=list)


@dataclass
class PaperTrade:
    paper_trade_id: str
    account_name: str
    source_scan_id: str
    source_rank: int
    symbol: str
    base_asset: str
    status: str
    created_at_utc: str
    updated_at_utc: str
    setup: str
    verdict: str
    entry_low: float
    entry_high: float
    planned_entry_mid: float
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    risk_reward_1: float
    risk_reward_2: float
    account_equity: float
    risk_per_trade_pct: float
    cash_risk: float
    quantity: float | None = None
    entry_price: float | None = None
    entered_at_utc: str | None = None
    tp1_hit_at_utc: str | None = None
    closed_at_utc: str | None = None
    exit_price: float | None = None
    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    last_price: float | None = None
    notes: str = ""
    tp1_trailing_ema_stop_active: bool = False


@dataclass
class PaperTradeEvent:
    event_id: str
    paper_trade_id: str
    account_name: str
    symbol: str
    event_type: str
    event_time_utc: str
    price: float | None
    quantity: float | None
    realized_pnl: float
    unrealized_pnl: float
    message: str


@dataclass
class StepEvent:
    event_type: str
    message: str
    event_time_utc: str
    price: float | None
