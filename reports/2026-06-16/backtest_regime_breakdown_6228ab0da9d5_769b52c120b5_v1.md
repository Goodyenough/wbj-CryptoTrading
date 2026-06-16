---
created: 2026-06-16T10:01:30+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 6228ab0da9d5
variant_run_id: 769b52c120b5
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `6228ab0da9d5`
- variant: `variant` / `769b52c120b5`
- period: `2023-07-01T00:00:00+00:00` -> `2024-07-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RISK_ON | 207 | 197 | 1.32 | 1.20 | 3896.37 | 2225.91 | 49.76% | 45.69% | 47.34% | 48.22% | 0.17 | 0.12 |

## Notes

- baseline UNKNOWN trades: 0
- variant UNKNOWN trades: 0
- Profit factor uses closed trade net PnL within each regime bucket.
- Drawdown is not attributed by regime in this report; use it as a trade-quality stratification view.

## Raw Buckets

```json
{
  "baseline": {
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 207,
      "wins": 103,
      "losses": 104,
      "stop_trades": 98,
      "net_pnl": 3896.3711154307093,
      "gross_profit": 15973.504703305845,
      "gross_loss": 12077.133587875136,
      "avg_r": 0.173378749223807
    }
  },
  "variant": {
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 197,
      "wins": 90,
      "losses": 107,
      "stop_trades": 95,
      "net_pnl": 2225.911814307615,
      "gross_profit": 13187.617040077645,
      "gross_loss": 10961.70522577003,
      "avg_r": 0.11714919375969644
    }
  }
}
```
