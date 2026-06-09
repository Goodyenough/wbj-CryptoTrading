from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
from collections.abc import Callable
import math
import time
import uuid

from .config import Settings
from .data_validation import cross_validate_candidates
from .data_quality import filter_tickers, tradable_spot_symbols
from .indicators import atr, ema, macd, percent_change, rsi
from .market_data import BinanceClient
from .market_regime import MarketRegime, classify_market_regime
from .models import RawTicker, ScanResult, TradeCandidate
from .risk import reward_to_risk


ACTION_PRIORITY = {
    "BUY_CANDIDATE": 0,
    "WAIT_PULLBACK": 1,
    "WATCH_ONLY": 2,
    "REJECT": 3,
}


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _action_sort_key(candidate: TradeCandidate) -> tuple[int, float]:
    return (ACTION_PRIORITY.get(candidate.action, 99), -candidate.score)


def _validation_pool_size(settings: Settings, candidate_count: int) -> int:
    pool_target = settings.market.top_n * settings.analysis.validation_pool_multiplier
    pool_target = min(pool_target, settings.analysis.validation_pool_max)
    pool_target = max(settings.market.top_n, pool_target)
    return min(candidate_count, pool_target)


def _rank_final_candidates(candidates: list[TradeCandidate], top_n: int) -> list[TradeCandidate]:
    sorted_candidates = sorted(candidates, key=_action_sort_key)
    return [
        replace(candidate, rank=rank)
        for rank, candidate in enumerate(sorted_candidates[:top_n], start=1)
    ]


def _quote_closes(klines: list[list]) -> list[float]:
    return [float(kline[4]) for kline in klines]


def _quote_volumes(klines: list[list]) -> list[float]:
    return [float(kline[7]) for kline in klines]


def _recent_low(klines: list[list], count: int) -> float:
    return min(float(kline[3]) for kline in klines[-count:])


def _recent_high(klines: list[list], count: int) -> float:
    return max(float(kline[2]) for kline in klines[-count:])


def _recent_kline_evidence(klines: list[list], count: int = 36) -> list[dict[str, float | int | str]]:
    evidence: list[dict[str, float | int | str]] = []
    for kline in klines[-count:]:
        opened_at = datetime.fromtimestamp(int(kline[0]) / 1000, tz=timezone.utc)
        evidence.append(
            {
                "open_time_utc": opened_at.isoformat(timespec="minutes"),
                "open": float(kline[1]),
                "high": float(kline[2]),
                "low": float(kline[3]),
                "close": float(kline[4]),
                "quote_volume": float(kline[7]),
                "trades": int(kline[8]),
            }
        )
    return evidence


def _choose_support(price: float, levels: list[float | None]) -> float | None:
    valid = [level for level in levels if level is not None and level > 0 and level <= price * 1.01]
    below = [level for level in valid if level <= price]
    if below:
        return max(below)
    return min(valid) if valid else None


def _build_entry_plan(
    price: float,
    support: float,
    recent_low: float,
    recent_high: float,
    atr_4h: float,
    risk_reward_min: float,
) -> tuple[str, str, float, float, float, float, float, float, float, str] | None:
    distance_to_support = (price / support - 1) * 100

    if distance_to_support <= 4:
        setup = "回踩支撑/4h EMA 附近"
        verdict = "可考虑"
        entry_low = support * 1.002
        entry_high = min(price * 1.003, support + atr_4h * 0.7)
    elif distance_to_support <= 10:
        setup = "趋势中，等回调入场"
        verdict = "只等回调"
        entry_low = max(support * 1.002, price - atr_4h * 1.05)
        entry_high = price - atr_4h * 0.25
    else:
        setup = "涨幅较远，只等深回调"
        verdict = "只等回调"
        entry_low = max(support * 1.002, price - atr_4h * 1.7)
        entry_high = price - atr_4h * 0.75

    if entry_high < entry_low:
        entry_low, entry_high = entry_high, entry_low

    entry = (entry_low + entry_high) / 2
    stop_loss = min(recent_low * 0.985, entry - atr_4h * 1.15)
    if stop_loss <= 0 or entry <= stop_loss:
        return None

    risk = entry - stop_loss
    take_profit_1 = max(recent_high * 0.995, entry + risk * risk_reward_min)
    take_profit_2 = max(entry + risk * 3.0, take_profit_1 * 1.04)
    rr1 = reward_to_risk(entry, stop_loss, take_profit_1)
    rr2 = reward_to_risk(entry, stop_loss, take_profit_2)
    if rr1 is None or rr2 is None or rr1 < risk_reward_min * 0.85:
        return None

    invalidation = f"跌破 {stop_loss:.8g} 或 4h 收盘重新失守关键支撑"
    return setup, verdict, entry_low, entry_high, stop_loss, take_profit_1, take_profit_2, rr1, rr2, invalidation


def _analyze_ticker(
    ticker: RawTicker,
    k1h: list[list],
    k4h: list[list],
    k1d: list[list],
    risk_reward_min: float,
    min_history_days: int = 60,
    market_regime_allows_buy: bool = True,
    market_regime_status: str | None = None,
    risk_off_core_buy_enabled: bool = True,
    pump_chase_24h_pct: float = 20.0,
    pump_chase_distance_pct: float = 8.0,
    pump_chase_penalty: float = 8.0,
    high_volatility_range_pct: float = 35.0,
    high_volatility_penalty: float = 6.0,
) -> TradeCandidate | None:
    closes_1h = _quote_closes(k1h)
    closes_4h = _quote_closes(k4h)
    closes_1d = _quote_closes(k1d)
    volumes_1h = _quote_volumes(k1h)
    if len(closes_1h) < 168 or len(closes_4h) < 80 or len(closes_1d) < max(60, min_history_days):
        return None

    price = closes_1h[-1]
    ema20_4h = ema(closes_4h, 20)
    ema50_4h = ema(closes_4h, 50)
    ema20_1d = ema(closes_1d, 20)
    ema50_1d = ema(closes_1d, 50)
    rsi_1h = rsi(closes_1h)
    rsi_4h = rsi(closes_4h)
    atr_4h = atr(k4h)
    _, _, macd_hist_4h = macd(closes_4h)
    if atr_4h is None or atr_4h <= 0:
        return None

    pct_7d = percent_change(closes_1h[-168], closes_1h[-1])
    pct_3d = percent_change(closes_1h[-72], closes_1h[-1])
    recent_low = _recent_low(k4h, 18)
    recent_high = _recent_high(k4h, 36)
    support = _choose_support(price, [recent_low, ema20_4h, ema50_4h, ema20_1d])
    if support is None:
        return None

    distance_to_support = (price / support - 1) * 100
    previous_volume = sum(volumes_1h[-168:-24])
    volume_ratio = None
    if previous_volume > 0:
        volume_ratio = (sum(volumes_1h[-24:]) / 24) / (previous_volume / 144)

    trend_4h = bool(price > (ema20_4h or math.inf) > (ema50_4h or math.inf))
    trend_1d = bool(price > (ema20_1d or math.inf) and (ema20_1d or 0) >= (ema50_1d or 0) * 0.98)

    score = math.log10(max(ticker.quote_volume_24h, 1)) * 2.5
    score += _clamp(ticker.pct_24h, -10, 18) * 0.65
    score += _clamp(pct_7d or -20, -20, 35) * 0.55
    score += _clamp(pct_3d or -15, -15, 25) * 0.3
    if trend_4h:
        score += 12
    if trend_1d:
        score += 8
    if rsi_4h is not None:
        if 48 <= rsi_4h <= 70:
            score += 8
        elif 70 < rsi_4h <= 78:
            score += 3
        elif rsi_4h > 78:
            score -= 8
        elif rsi_4h < 35:
            score -= 4
    if macd_hist_4h is not None and macd_hist_4h > 0:
        score += 4
    if volume_ratio is not None:
        if 0.8 <= volume_ratio <= 3:
            score += min(volume_ratio, 2.5) * 2
        elif volume_ratio > 5:
            score -= 3
    if distance_to_support <= 4:
        score += 6
    elif distance_to_support > 12:
        score -= 10
    if ticker.high_low_range_24h > high_volatility_range_pct:
        score -= high_volatility_penalty
    if ticker.pct_24h > pump_chase_24h_pct and distance_to_support > pump_chase_distance_pct:
        score -= pump_chase_penalty
    if ticker.pct_24h < 0:
        score -= 4
    if pct_7d is not None and pct_7d < 0:
        score -= 6
    core_symbol = ticker.symbol in {"BTCUSDT", "ETHUSDT"}
    core_allowed_in_regime = core_symbol and (
        market_regime_status != "RISK_OFF" or risk_off_core_buy_enabled
    )
    market_regime_risk = not market_regime_allows_buy and not core_allowed_in_regime
    if market_regime_risk:
        score -= 10

    plan = _build_entry_plan(
        price=price,
        support=support,
        recent_low=recent_low,
        recent_high=recent_high,
        atr_4h=atr_4h,
        risk_reward_min=risk_reward_min,
    )
    if plan is None:
        return None

    setup, verdict, entry_low, entry_high, stop_loss, tp1, tp2, rr1, rr2, invalidation = plan
    if score < 35 or not (trend_4h or trend_1d):
        verdict = "只观察"
    if ticker.pct_24h <= 0 or (pct_7d is not None and pct_7d <= 0):
        verdict = "只观察"
    if distance_to_support > 10 or (rsi_4h is not None and rsi_4h > 75):
        verdict = "只等回调"

    trend_ok = trend_4h or trend_1d
    score_ok = score >= 35
    momentum_ok = ticker.pct_24h > 0 and (pct_7d is None or pct_7d > 0)
    distance_buy_ok = distance_to_support <= 4
    distance_wait_ok = distance_to_support <= 10
    rsi_ok = rsi_4h is None or rsi_4h <= 75
    if score_ok and trend_ok and momentum_ok and distance_buy_ok and rsi_ok:
        action = "BUY_CANDIDATE"
    elif trend_ok and momentum_ok and distance_wait_ok and rsi_ok:
        action = "WAIT_PULLBACK"
    elif score < 20:
        action = "REJECT"
    else:
        action = "WATCH_ONLY"
    if market_regime_risk and action == "BUY_CANDIDATE":
        action = "WATCH_ONLY"
        verdict = "只观察"

    risks: list[str] = []
    if distance_to_support > 8:
        risks.append("距离支撑偏远，不能追市价")
    if rsi_4h is not None and rsi_4h > 75:
        risks.append("4h RSI 偏热")
    if ticker.high_low_range_24h > 25:
        risks.append("24h 振幅较大，回撤风险高")
    if volume_ratio is not None and volume_ratio > 3:
        risks.append("成交量突增，可能是事件驱动")
    if not trend_1d:
        risks.append("日线趋势未完全确认")
    if market_regime_risk:
        risks.append("BTC/ETH 大盘环境未确认强势，山寨币买入信号降级")
    if ticker.pct_24h <= 0:
        risks.append("24h 动量未确认")
    if pct_7d is not None and pct_7d <= 0:
        risks.append("7d 趋势未确认")
    if not risks:
        risks.append("主要风险是大盘同步回撤")

    return TradeCandidate(
        rank=0,
        symbol=ticker.symbol,
        base_asset=ticker.base_asset,
        price=price,
        score=score,
        setup=setup,
        verdict=verdict,
        entry_low=entry_low,
        entry_high=entry_high,
        stop_loss=stop_loss,
        take_profit_1=tp1,
        take_profit_2=tp2,
        risk_reward_1=rr1,
        risk_reward_2=rr2,
        pct_24h=ticker.pct_24h,
        pct_3d=pct_3d,
        pct_7d=pct_7d,
        quote_volume_24h=ticker.quote_volume_24h,
        trades_24h=ticker.trades_24h,
        high_low_range_24h=ticker.high_low_range_24h,
        rsi_1h=rsi_1h,
        rsi_4h=rsi_4h,
        ema20_4h=ema20_4h,
        ema50_4h=ema50_4h,
        ema20_1d=ema20_1d,
        ema50_1d=ema50_1d,
        atr_4h=atr_4h,
        macd_hist_4h=macd_hist_4h,
        volume_ratio_24h=volume_ratio,
        support_level=support,
        recent_low_4h_18=recent_low,
        recent_high_4h_36=recent_high,
        distance_to_support_pct=distance_to_support,
        binance_trade_url=f"https://www.binance.com/en/trade/{ticker.base_asset}_{ticker.symbol.removeprefix(ticker.base_asset)}",
        tradingview_url=f"https://www.tradingview.com/chart/?symbol=BINANCE%3A{ticker.symbol}",
        coingecko_search_url=f"https://www.coingecko.com/en/search?query={ticker.base_asset}",
        coinmarketcap_search_url=f"https://coinmarketcap.com/search/?q={ticker.base_asset}",
        invalidation=invalidation,
        recent_4h_klines=_recent_kline_evidence(k4h),
        risks=risks,
        action=action,
    )


def _detect_market_regime(client: BinanceClient, settings: Settings, limitations: list[str], progress: Callable[[str], None] | None) -> MarketRegime | None:
    if not settings.analysis.market_regime_filter_enabled:
        limitations.append("大盘环境过滤未启用。")
        return None
    try:
        if progress is not None:
            progress("checking BTC/ETH market regime")
        btc_1d = client.klines("BTCUSDT", "1d", max(80, settings.analysis.min_history_days))
        eth_1d = client.klines("ETHUSDT", "1d", max(80, settings.analysis.min_history_days))
        regime = classify_market_regime(btc_1d, eth_1d)
        limitations.append(
            "大盘环境过滤："
            f"{regime.status}; {regime.summary} "
            f"BTC 7d={regime.btc_pct_7d if regime.btc_pct_7d is not None else 'n/a'}; "
            f"ETH 7d={regime.eth_pct_7d if regime.eth_pct_7d is not None else 'n/a'}."
        )
        return regime
    except Exception as exc:
        limitations.append(f"大盘环境过滤失败：{exc}；默认不放开山寨币买入信号。")
        return MarketRegime(
            status="UNKNOWN",
            allows_alt_buy=False,
            btc_trend_ok=False,
            eth_trend_ok=False,
            btc_pct_7d=None,
            eth_pct_7d=None,
            summary="大盘环境检测失败。",
        )


def _apply_data_quality_filter(candidates: list[TradeCandidate], settings: Settings) -> list[TradeCandidate]:
    if not settings.analysis.data_quality_filter_enabled:
        return candidates
    filtered: list[TradeCandidate] = []
    for candidate in candidates:
        if (
            settings.analysis.strict_data_quality_for_buy
            and candidate.action == "BUY_CANDIDATE"
            and candidate.data_quality_status != "DATA_OK"
        ):
            filtered.append(
                replace(
                    candidate,
                    action="WATCH_ONLY",
                    verdict="只观察",
                    risks=[
                        *candidate.risks,
                        f"数据交叉验证状态为 {candidate.data_quality_status}，买入候选降级为观察",
                    ],
                )
            )
        else:
            filtered.append(candidate)
    return filtered


def run_market_scan(settings: Settings, progress: Callable[[str], None] | None = None) -> ScanResult:
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    if progress is not None:
        progress("loading Binance exchange info")
    exchange_info = client.exchange_info()
    symbol_meta = tradable_spot_symbols(exchange_info, settings.market.quote_asset)
    if progress is not None:
        progress("loading Binance 24h tickers")
    tickers = client.ticker_24hr()
    raw_tickers = filter_tickers(
        tickers,
        symbol_meta,
        settings.market.min_quote_volume,
        settings.market.min_trades,
        settings.market.exclude_bases,
    )
    raw_tickers.sort(
        key=lambda ticker: (
            math.log10(max(ticker.quote_volume_24h, 1)) * 5
            + max(ticker.pct_24h, 0) * 2
            - max(ticker.high_low_range_24h - 40, 0)
        ),
        reverse=True,
    )
    raw_tickers = raw_tickers[: settings.market.max_universe]
    if progress is not None:
        progress(f"analyzing {len(raw_tickers)} filtered symbols")

    candidates: list[TradeCandidate] = []
    limitations: list[str] = [
        "交易信号仍以 Binance 现货公开 K 线为主源；外部数据源用于一致性复核。",
        "结果是研究和模拟盘计划，不是确定收益或实盘下单指令。",
        f"历史长度过滤：候选币至少需要 {settings.analysis.min_history_days} 根 1d K 线。",
        (
            "数据质量验证池：先验证 score 排名前 "
            f"min(top_n * {settings.analysis.validation_pool_multiplier}, "
            f"{settings.analysis.validation_pool_max}) 的候选，再按 action + score 补足最终名单。"
        ),
    ]
    market_regime = _detect_market_regime(client, settings, limitations, progress)
    market_regime_allows_buy = True if market_regime is None else market_regime.allows_alt_buy
    market_regime_status = None if market_regime is None else market_regime.status

    total = len(raw_tickers)
    for index, ticker in enumerate(raw_tickers, start=1):
        try:
            if progress is not None:
                progress(f"analyzing {index}/{total} {ticker.symbol}")
            k1h = client.klines(ticker.symbol, "1h", 168)
            k4h = client.klines(ticker.symbol, "4h", 120)
            k1d = client.klines(ticker.symbol, "1d", max(100, settings.analysis.min_history_days))
            candidate = _analyze_ticker(
                ticker,
                k1h,
                k4h,
                k1d,
                settings.analysis.risk_reward_min,
                min_history_days=settings.analysis.min_history_days,
                market_regime_allows_buy=market_regime_allows_buy,
                market_regime_status=market_regime_status,
                risk_off_core_buy_enabled=settings.analysis.risk_off_core_buy_enabled,
                pump_chase_24h_pct=settings.analysis.pump_chase_24h_pct,
                pump_chase_distance_pct=settings.analysis.pump_chase_distance_pct,
                pump_chase_penalty=settings.analysis.pump_chase_penalty,
                high_volatility_range_pct=settings.analysis.high_volatility_range_pct,
                high_volatility_penalty=settings.analysis.high_volatility_penalty,
            )
            if candidate is not None:
                candidates.append(candidate)
                if progress is not None:
                    progress(f"candidate found: {ticker.symbol} score={candidate.score:.2f}")
        except Exception as exc:
            limitations.append(f"{ticker.symbol} 数据获取或分析失败：{exc}")
            if progress is not None:
                progress(f"analysis failed for {ticker.symbol}: {exc}")
        time.sleep(settings.market.request_pause_seconds)

    candidates.sort(key=lambda item: item.score, reverse=True)
    pool_size = _validation_pool_size(settings, len(candidates))
    validation_pool = candidates[:pool_size]
    if progress is not None:
        progress(f"cross-checking {len(validation_pool)} candidate validation pool")
    checked_pool, validation_notes = cross_validate_candidates(settings, validation_pool, progress=progress)
    checked_pool = _apply_data_quality_filter(checked_pool, settings)
    ranked = _rank_final_candidates(checked_pool, settings.market.top_n)
    limitations.extend(validation_notes)
    if progress is not None:
        progress("market scan complete")

    now = datetime.now(timezone.utc)
    return ScanResult(
        scan_id=uuid.uuid4().hex[:12],
        timestamp_utc=now.isoformat(timespec="seconds"),
        source="Binance public spot API + CoinGecko/CoinMarketCap cross-check",
        filters=(
            f"{settings.market.quote_asset} spot; 24h quote volume >= "
            f"{settings.market.min_quote_volume:,.0f}; trades >= {settings.market.min_trades:,}; "
            "exclude stables/leveraged tokens; analyze 1h/4h/1d klines"
        ),
        limitations=limitations,
        candidates=ranked,
    )
