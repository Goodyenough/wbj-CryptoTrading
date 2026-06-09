---
created: 2026-06-10T03:12:18+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: e6133152fb7e
variant_run_id: c7be05461e78
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `e6133152fb7e`
- variant: `variant` / `c7be05461e78`
- period: `2025-01-01T00:00:00+00:00` -> `2025-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 2 | 6 | 2.40 | 1.34 | 135.90 | 139.03 | 50.00% | 33.33% | 50.00% | 66.67% | 0.77 | 0.28 |
| RISK_OFF | 8 | 0 | 0.36 | n/a | -438.22 | 0.00 | 12.50% | n/a | 87.50% | n/a | -0.55 | n/a |
| RISK_ON | 7 | 9 | 0.00 | 0.00 | -688.84 | -912.17 | 0.00% | 0.00% | 100.00% | 100.00% | -1.02 | -1.02 |

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
      "net_pnl": 139.02698911667864,
      "gross_profit": 543.6694906688015,
      "gross_loss": 404.6425015521228,
      "avg_r": 0.278436979696805
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 9,
      "wins": 0,
      "losses": 9,
      "stop_trades": 9,
      "net_pnl": -912.1662771303488,
      "gross_profit": 0,
      "gross_loss": 912.1662771303488,
      "avg_r": -1.0191583482628186
    }
  }
}
```
