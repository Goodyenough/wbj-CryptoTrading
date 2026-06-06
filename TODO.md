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
- [x] Add history length filter: require at least 180 daily candles by default before a coin can become a buy candidate.
- [x] Add BTC/ETH market regime filter: when the broad market is weak or unclear, downgrade altcoin buy candidates to watch-only.
- [ ] Test stricter history filter options, especially 365 daily candles versus the current 180 daily candles.
- [ ] Exclude coins that have already pumped too far from support after a strong 24h move.
- [ ] Raise liquidity thresholds and test the impact on trade count, win rate, and drawdown.
- [ ] Add stronger trend filter: only allow coins with daily `EMA20 > EMA50` and price above both averages.
- [ ] Add candidate score penalties for high volatility without confirmed trend continuation.

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

- [ ] Change only one strategy dimension per experiment.
- [ ] Run each experiment on the same symbol universe and date range.
- [ ] Compare net return, max drawdown, win rate, profit factor, average R, stop-loss rate, and trade count.
- [ ] Save each experiment report with a clear rule name and version.
- [ ] Keep a short decision note explaining whether the rule should be kept, reverted, or retested.

