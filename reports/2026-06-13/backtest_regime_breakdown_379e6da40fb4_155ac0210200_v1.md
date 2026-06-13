---
created: 2026-06-13T23:37:00+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 379e6da40fb4
variant_run_id: 155ac0210200
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `379e6da40fb4`
- variant: `variant` / `155ac0210200`
- period: `2024-07-01T00:00:00+00:00` -> `2025-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RISK_ON | 76 | 134 | 1.04 | 1.48 | 203.60 | 3226.48 | 39.47% | 50.00% | 84.21% | 50.00% | 0.05 | 0.23 |

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
      "closed_trades": 76,
      "wins": 30,
      "losses": 46,
      "stop_trades": 64,
      "net_pnl": 203.59853817357788,
      "gross_profit": 5146.230495547139,
      "gross_loss": 4942.631957373562,
      "avg_r": 0.05373777931702029
    }
  },
  "variant": {
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
  }
}
```
