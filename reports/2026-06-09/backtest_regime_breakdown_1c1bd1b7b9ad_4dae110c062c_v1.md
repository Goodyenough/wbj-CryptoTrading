---
created: 2026-06-09T19:00:13+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 1c1bd1b7b9ad
variant_run_id: 4dae110c062c
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `1c1bd1b7b9ad`
- variant: `variant` / `4dae110c062c`
- period: `2025-01-01T00:00:00+00:00` -> `2025-09-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 3 | 3 | 4.85 | 4.85 | 373.12 | 373.56 | 66.67% | 66.67% | 33.33% | 33.33% | 1.44 | 1.44 |
| RISK_OFF | 10 | 9 | 0.29 | 0.32 | -620.53 | -531.32 | 10.00% | 11.11% | 90.00% | 88.89% | -0.65 | -0.61 |
| RISK_ON | 29 | 29 | 0.51 | 0.64 | -1123.23 | -800.96 | 17.24% | 20.69% | 82.76% | 79.31% | -0.39 | -0.27 |

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
      "closed_trades": 3,
      "wins": 2,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 373.55930418479215,
      "gross_profit": 470.46603226800227,
      "gross_loss": 96.90672808321013,
      "avg_r": 1.4413790190805702
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 9,
      "wins": 1,
      "losses": 8,
      "stop_trades": 8,
      "net_pnl": -531.32000212823,
      "gross_profit": 248.15705722194315,
      "gross_loss": 779.4770593501731,
      "avg_r": -0.6077008860144445
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 29,
      "wins": 6,
      "losses": 23,
      "stop_trades": 23,
      "net_pnl": -800.9646175903531,
      "gross_profit": 1447.8360770289012,
      "gross_loss": 2248.8006946192545,
      "avg_r": -0.2711221776016794
    }
  }
}
```
