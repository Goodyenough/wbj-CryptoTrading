---
created: 2026-06-10T03:00:30+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 73cadcfc0a45
variant_run_id: 400001fc7ad6
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `73cadcfc0a45`
- variant: `variant` / `400001fc7ad6`
- period: `2025-01-01T00:00:00+00:00` -> `2025-09-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 3 | 7 | 4.85 | 1.96 | 373.12 | 389.79 | 66.67% | 42.86% | 33.33% | 57.14% | 1.44 | 0.64 |
| RISK_OFF | 10 | 0 | 0.29 | n/a | -620.53 | 0.00 | 10.00% | n/a | 90.00% | n/a | -0.65 | n/a |
| RISK_ON | 29 | 31 | 0.51 | 0.86 | -1123.23 | -320.18 | 17.24% | 25.81% | 82.76% | 74.19% | -0.39 | -0.08 |

## Notes

- baseline UNKNOWN trades: 0
- variant UNKNOWN trades: 0
- Profit factor uses closed trade net PnL within each regime bucket.
- Drawdown is not attributed by regime in this report; use it as a trade-quality stratification view.

## Raw Buckets

```json
{
  "baseline": {
    "NEUTRAL": {
      "status": "NEUTRAL",
      "closed_trades": 3,
      "wins": 2,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 373.11572687168814,
      "gross_profit": 470.02245495489825,
      "gross_loss": 96.90672808321013,
      "avg_r": 1.4413790190805702
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 10,
      "wins": 1,
      "losses": 9,
      "stop_trades": 9,
      "net_pnl": -620.5323780471796,
      "gross_profit": 248.15705722194315,
      "gross_loss": 868.6894352691227,
      "avg_r": -0.6504690804941398
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 29,
      "wins": 5,
      "losses": 24,
      "stop_trades": 24,
      "net_pnl": -1123.233553027183,
      "gross_profit": 1165.5601521225792,
      "gross_loss": 2288.793705149762,
      "avg_r": -0.3898372725586018
    }
  },
  "variant": {
    "NEUTRAL": {
      "status": "NEUTRAL",
      "closed_trades": 7,
      "wins": 3,
      "losses": 4,
      "stop_trades": 4,
      "net_pnl": 389.79390593011726,
      "gross_profit": 794.43640748224,
      "gross_loss": 404.6425015521228,
      "avg_r": 0.6350781495081027
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 31,
      "wins": 8,
      "losses": 23,
      "stop_trades": 23,
      "net_pnl": -320.1797355231851,
      "gross_profit": 2017.2247484009256,
      "gross_loss": 2337.4044839241105,
      "avg_r": -0.08275964374241102
    }
  }
}
```
