---
created: 2026-06-09T21:26:35+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: e6133152fb7e
variant_run_id: 2ec5278f62cb
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `e6133152fb7e`
- variant: `variant` / `2ec5278f62cb`
- period: `2025-01-01T00:00:00+00:00` -> `2025-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 2 | 6 | 2.40 | 1.35 | 135.90 | 140.07 | 50.00% | 33.33% | 50.00% | 66.67% | 0.77 | 0.28 |
| RISK_OFF | 8 | 0 | 0.36 | n/a | -438.22 | 0.00 | 12.50% | n/a | 87.50% | n/a | -0.55 | n/a |
| RISK_ON | 7 | 7 | 0.00 | 0.00 | -688.84 | -710.59 | 0.00% | 0.00% | 100.00% | 100.00% | -1.02 | -1.02 |

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
      "closed_trades": 6,
      "wins": 2,
      "losses": 4,
      "stop_trades": 4,
      "net_pnl": 140.06936973407102,
      "gross_profit": 543.8519554072805,
      "gross_loss": 403.78258567320944,
      "avg_r": 0.27843697969680503
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 7,
      "wins": 0,
      "losses": 7,
      "stop_trades": 7,
      "net_pnl": -710.5888658155848,
      "gross_profit": 0,
      "gross_loss": 710.5888658155848,
      "avg_r": -1.0162726628206609
    }
  }
}
```
