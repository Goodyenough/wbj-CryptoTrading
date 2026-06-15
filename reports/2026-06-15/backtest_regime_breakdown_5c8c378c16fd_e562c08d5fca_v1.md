---
created: 2026-06-16T00:07:42+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 5c8c378c16fd
variant_run_id: e562c08d5fca
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `5c8c378c16fd`
- variant: `variant` / `e562c08d5fca`
- period: `2024-07-01T00:00:00+00:00` -> `2025-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RISK_ON | 134 | 134 | 1.48 | 1.38 | 3226.48 | 2911.83 | 50.00% | 44.78% | 50.00% | 54.48% | 0.23 | 0.22 |

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
      "closed_trades": 134,
      "wins": 67,
      "losses": 67,
      "stop_trades": 67,
      "net_pnl": 3226.4830422702353,
      "gross_profit": 9986.502831113618,
      "gross_loss": 6760.019788843382,
      "avg_r": 0.23463119542659508
    }
  },
  "variant": {
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 134,
      "wins": 60,
      "losses": 74,
      "stop_trades": 73,
      "net_pnl": 2911.825939431185,
      "gross_profit": 10506.523954644786,
      "gross_loss": 7594.698015213602,
      "avg_r": 0.2192827966155529
    }
  }
}
```
