---
created: 2026-06-13T23:37:00+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: e04cfa632035
variant_run_id: c9adb1a79689
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `e04cfa632035`
- variant: `variant` / `c9adb1a79689`
- period: `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RISK_OFF | 4 | 4 | 0.00 | 0.00 | -438.20 | -401.00 | 0.00% | 0.00% | 100.00% | 75.00% | -1.06 | -0.82 |
| RISK_ON | 53 | 106 | 1.26 | 1.41 | 840.22 | 1996.22 | 43.40% | 49.06% | 84.91% | 44.34% | 0.16 | 0.18 |

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
      "stop_trades": 4,
      "net_pnl": -438.1984442573363,
      "gross_profit": 0,
      "gross_loss": 438.1984442573363,
      "avg_r": -1.056309036981132
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 53,
      "wins": 23,
      "losses": 30,
      "stop_trades": 45,
      "net_pnl": 840.221373720253,
      "gross_profit": 4105.600561556782,
      "gross_loss": 3265.379187836529,
      "avg_r": 0.16302849573441178
    }
  },
  "variant": {
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
  }
}
```
