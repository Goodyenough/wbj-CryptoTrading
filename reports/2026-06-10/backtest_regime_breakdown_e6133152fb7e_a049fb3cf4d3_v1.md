---
created: 2026-06-10T02:36:21+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: e6133152fb7e
variant_run_id: a049fb3cf4d3
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `e6133152fb7e`
- variant: `variant` / `a049fb3cf4d3`
- period: `2025-01-01T00:00:00+00:00` -> `2025-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 2 | 2 | 2.40 | 2.40 | 135.90 | 135.59 | 50.00% | 50.00% | 50.00% | 50.00% | 0.77 | 0.77 |
| RISK_OFF | 8 | 8 | 0.36 | 0.36 | -438.22 | -443.84 | 12.50% | 12.50% | 87.50% | 87.50% | -0.55 | -0.56 |
| RISK_ON | 7 | 8 | 0.00 | 0.00 | -688.84 | -785.85 | 0.00% | 0.00% | 100.00% | 100.00% | -1.02 | -1.02 |

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
      "closed_trades": 2,
      "wins": 1,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 135.89647299638938,
      "gross_profit": 232.80320107959952,
      "gross_loss": 96.90672808321013,
      "avg_r": 0.7746059444329106
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 8,
      "wins": 1,
      "losses": 7,
      "stop_trades": 7,
      "net_pnl": -438.2203576597119,
      "gross_profit": 248.15705722194315,
      "gross_loss": 686.377414881655,
      "avg_r": -0.5541170586888031
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 7,
      "wins": 0,
      "losses": 7,
      "stop_trades": 7,
      "net_pnl": -688.8444534322534,
      "gross_profit": 0,
      "gross_loss": 688.8444534322534,
      "avg_r": -1.0150173718008875
    }
  },
  "variant": {
    "NEUTRAL": {
      "status": "NEUTRAL",
      "closed_trades": 2,
      "wins": 1,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 135.59221922349252,
      "gross_profit": 232.6041613107828,
      "gross_loss": 97.0119420872903,
      "avg_r": 0.7746059444329108
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 8,
      "wins": 1,
      "losses": 7,
      "stop_trades": 7,
      "net_pnl": -443.8394509552559,
      "gross_profit": 247.94489036568586,
      "gross_loss": 691.7843413209418,
      "avg_r": -0.5597954440193428
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 8,
      "wins": 0,
      "losses": 8,
      "stop_trades": 8,
      "net_pnl": -785.8527766487157,
      "gross_profit": 0,
      "gross_loss": 785.8527766487157,
      "avg_r": -1.018238847447926
    }
  }
}
```
