---
created: 2026-06-09T20:05:07+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 1d0037a773ff
variant_run_id: b4ef9a870efb
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `1d0037a773ff`
- variant: `variant` / `b4ef9a870efb`
- period: `2025-01-01T00:00:00+00:00` -> `2025-09-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 3 | 7 | 4.85 | 1.97 | 373.12 | 391.54 | 66.67% | 42.86% | 33.33% | 57.14% | 1.44 | 0.64 |
| RISK_OFF | 10 | 0 | 0.29 | n/a | -620.53 | 0.00 | 10.00% | n/a | 90.00% | n/a | -0.65 | n/a |
| RISK_ON | 29 | 30 | 0.51 | 0.50 | -1123.23 | -1243.74 | 17.24% | 16.67% | 82.76% | 83.33% | -0.39 | -0.40 |

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
      "net_pnl": 391.5407839857789,
      "gross_profit": 795.3233696589883,
      "gross_loss": 403.78258567320944,
      "avg_r": 0.6350781495081027
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 30,
      "wins": 5,
      "losses": 25,
      "stop_trades": 25,
      "net_pnl": -1243.7386483185646,
      "gross_profit": 1258.8510189904832,
      "gross_loss": 2502.589667309048,
      "avg_r": -0.40473986414770013
    }
  }
}
```
