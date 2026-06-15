---
created: 2026-06-16T00:07:42+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 31f5e44d3d40
variant_run_id: eb11621e6738
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `31f5e44d3d40`
- variant: `variant` / `eb11621e6738`
- period: `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RISK_OFF | 4 | 4 | 0.00 | 0.00 | -401.00 | -405.70 | 0.00% | 0.00% | 75.00% | 75.00% | -0.82 | -0.82 |
| RISK_ON | 106 | 106 | 1.41 | 1.79 | 1996.22 | 3480.82 | 49.06% | 50.94% | 44.34% | 46.23% | 0.18 | 0.29 |

## Notes

- baseline UNKNOWN trades: 0
- variant UNKNOWN trades: 0
- Profit factor uses closed trade net PnL within each regime bucket.
- Drawdown is not attributed by regime in this report; use it as a trade-quality stratification view.

## Raw Buckets

```json
{
  "baseline": {
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 4,
      "wins": 0,
      "losses": 4,
      "stop_trades": 3,
      "net_pnl": -401.0047518476923,
      "gross_profit": 0,
      "gross_loss": 401.0047518476923,
      "avg_r": -0.8166987339064091
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 106,
      "wins": 52,
      "losses": 54,
      "stop_trades": 47,
      "net_pnl": 1996.2226582198873,
      "gross_profit": 6810.010706842614,
      "gross_loss": 4813.788048622727,
      "avg_r": 0.1760371035497899
    }
  },
  "variant": {
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 4,
      "wins": 0,
      "losses": 4,
      "stop_trades": 3,
      "net_pnl": -405.6970237161915,
      "gross_profit": 0,
      "gross_loss": 405.6970237161915,
      "avg_r": -0.8166987339064091
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 106,
      "wins": 54,
      "losses": 52,
      "stop_trades": 49,
      "net_pnl": 3480.8228733807614,
      "gross_profit": 7874.279858000254,
      "gross_loss": 4393.456984619492,
      "avg_r": 0.2895943987580803
    }
  }
}
```
