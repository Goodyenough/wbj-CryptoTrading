---
name: crypto-market-buy-screener
description: Scan the cryptocurrency market and rank the top buy candidates with conditional trade plans. Use when the user asks to sweep the market, find the best coins to buy now, rank top crypto opportunities, or produce entry, stop-loss, take-profit, and sell guidance from public market data.
---

# Crypto Market Buy Screener

Use this skill to combine market scanning, data quality checks, technical analysis, and risk management into a ranked list of conditional crypto trade candidates. Treat all outputs as research and trade planning, not financial advice or live execution.

## Required Inputs

If the user does not specify them, choose conservative defaults:

- Universe: liquid spot markets, preferably Binance USDT spot plus CoinGecko/CoinMarketCap top-market-cap assets.
- Timeframes: 1h for short-term timing, 4h for trade structure, 1d for trend context.
- Minimum liquidity: at least 20M USD 24h volume for general screening; raise the threshold for larger accounts.
- Output count: 5 buy candidates.
- Risk per trade: 0.5%-1% of account equity unless the user specifies otherwise.

Do not include stablecoins, wrapped duplicates, leveraged tokens, obvious synthetic mirrors, gold-backed tokens, or assets with suspicious volume/data.

## Workflow

1. Gather public market data.
   - Prefer CoinGecko/CoinMarketCap for broad rankings, market cap, and cross-market context.
   - Prefer Binance public spot data for executable USDT pairs, 24h ticker data, and recent OHLCV.
   - If one source is rate-limited or unavailable, state the limitation and continue with the available source.

2. Apply data quality filters.
   - Confirm symbol identity, quote asset, venue, current trading status, and 24h volume.
   - Reject missing candles, stale prices, zero-volume bars, extreme one-off wicks, obvious depegs, and suspicious provider disagreement.
   - Reject assets where bad data could materially change entry, stop, or PnL.

3. Score technical strength.
   - Trend: price above rising MA/EMA 20 and MA/EMA 50, with daily or 4h structure not obviously bearish.
   - Momentum: positive 24h and 7d performance, RSI preferably 50-70. Penalize RSI above 80 unless trend is exceptionally strong and entry is pullback-based.
   - MACD: prefer bullish or improving MACD, especially above or approaching the zero line.
   - Volume: prefer breakout volume expansion or healthy pullback volume contraction.
   - Structure: prefer coins near support, on confirmed breakout retest, or emerging from volatility contraction. Penalize coins far above support after a vertical candle.

4. Build trade plan for each candidate.
   - Entry: use an entry zone, not a single magic price. Prefer pullback-to-support or breakout-retest entries.
   - Stop loss: place below invalidation, such as swing low, support, or ATR-based level. Avoid stops so tight that normal volatility will trigger them.
   - Take profit / sell plan: give at least two exits, such as TP1 near next resistance and TP2 using a trailing stop or higher resistance.
   - Risk/reward: reject plans where realistic reward-to-risk is below 2:1 unless the user explicitly wants scalp-style trades.
   - Position sizing: if account equity is provided, calculate size from risk. Otherwise explain how to size it.

5. Rank the final 5.
   - Prefer candidates with good liquidity, clear trend, clean entry, defined invalidation, and acceptable reward-to-risk.
   - A coin with smaller 24h gain but cleaner structure can rank above a coin that already spiked.
   - Label each as: "可考虑", "只等回调", "只观察", or "不建议追".

## Output Format

Start with timestamp, data sources, filters, and any source limitations.

Then provide a table:

| Rank | Coin | Setup | Entry Zone | Stop Loss | TP1 | TP2 / Exit Rule | Risk/Reward | Verdict |
|---:|---|---|---:|---:|---:|---|---:|---|

After the table, add concise notes for each candidate:

- Why it made the list.
- What would invalidate the trade.
- Main risk: overbought, low liquidity, event-driven pump, market-wide weakness, exchange risk, funding risk, or news risk.

End with portfolio-level risk rules:

- Do not enter all 5 at full size if they are highly correlated.
- Cap total open risk across all candidates.
- Avoid leverage unless the user explicitly requests derivatives analysis.
- If BTC/ETH market structure breaks down, cancel altcoin long plans or reduce size.

## Hard Rules

- Never claim certainty.
- Never present the list as guaranteed profit.
- Never recommend market buying a coin after a vertical spike without a defined pullback or invalidation.
- Never place live orders or ask for API keys unless the user explicitly asks to automate execution.
- Always separate "current market ranking" from "actionable entry plan".

