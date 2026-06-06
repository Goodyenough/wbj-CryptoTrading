# CryptoTradingSystem TODO

## Strategy Optimization Roadmap

Context: the latest backtest shows the system can scan the market, generate plans, and replay history, but the current trade quality is still weak.

Baseline issues to improve:
- Win rate: 25.42%
- Stop-loss rate: 74.58%
- Profit factor: 0.85
- Maximum drawdown: 19.64%

These numbers suggest the system is still opening too many low-quality plans, or the current entry and stop rules are too easy to trigger in noisy markets.

## Priority 1: Improve Coin Selection

- [x] Add data quality filter: prioritize `DATA_OK`; downgrade or reject `DATA_WARNING` and `DATA_ERROR` buy candidates.
- [x] Validate a larger candidate pool before final ranking: cross-check `min(top_n * 2, 10)` candidates, then refill final `top_n` after data-quality downgrades.
- [x] Add history length filter: require at least 180 daily candles by default before a coin can become a buy candidate.
- [x] Fix backtest warmup so historical replay fetches at least `min_history_days + 60` daily candles before the start date.
- [x] Add BTC/ETH market regime filter: when the broad market is weak or unclear, downgrade altcoin buy candidates to watch-only.
- [x] Parameterize pump-chasing and high-volatility score penalties while keeping default behavior equivalent to the old hard-coded rules.
- [x] Align paper trading imports with backtest behavior: default `paper add-from-scan` imports only `BUY_CANDIDATE`.
- [x] Add `sample_sufficient` to backtest reports so closed-trade samples below 20 are explicitly marked as insufficient.
- [ ] A/B test stricter history filter options: current 180 daily candles versus 250 and 365.
- [ ] Split history handling into `min_indicator_history_days`, hard-reject days, and short-history score penalty.
- [ ] A/B test stricter pump-chasing rules: exclude or downgrade coins that are far from support after a strong 24h move.
- [ ] Raise liquidity thresholds and test the impact on trade count, win rate, and drawdown.
- [ ] A/B test stronger trend filter: only allow buy candidates with daily `price > EMA20 > EMA50`.
- [ ] A/B test high-volatility penalties that depend on missing trend confirmation, not just raw 24h range.
- [ ] Add an experiment comparison note after each A/B run: keep, revert, or retest.

## Priority 2: Improve Entry Rules

- [ ] Do not enter immediately on the first touch of the entry zone; require a 4h close reclaiming support.
- [ ] Test entry closer to `entry_low` instead of assuming entry near `entry_high`.
- [ ] Require RSI recovery, for example RSI moving back upward from the 45-55 area.
- [ ] Reject setups where volume expansion is mainly bearish selling volume.
- [ ] Avoid catching falling knives when the 4h trend is still clearly down.

## Priority 3: Improve Exit Rules

- [ ] Test taking partial profit at TP1, for example selling 50% at TP1.
- [ ] Move stop to breakeven after TP1 is hit.
- [ ] Test 4h EMA20 trailing stop after TP1.
- [ ] Test ATR trailing stop after TP1.
- [ ] Compare fixed TP2 versus trend-following exit rules.
- [ ] Test ATR-based dynamic stop instead of only structure-based fixed stop.

## Priority 4: Backtest A/B Testing Discipline

- [x] Add `backtest-universe` snapshot mode: select symbols from the current Binance market snapshot, replay historical klines, and write snapshot metadata plus survivorship-bias warning into the report.
- [ ] Build full historical dynamic universe backtest: at each historical decision point, reconstruct the tradable universe from historical data before selecting candidates. Source: universe snapshot smoke test on 2026-06-06.
- [ ] Change only one strategy dimension per experiment.
- [ ] Run each experiment on the same symbol universe and date range.
- [ ] Compare net return, max drawdown, win rate, profit factor, average R, stop-loss rate, and trade count.
- [ ] Save each experiment report with a clear rule name and version.
- [ ] Keep a short decision note explaining whether the rule should be kept, reverted, or retested.
