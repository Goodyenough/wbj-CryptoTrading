---
created: 2026-06-09T23:47:52+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 359a6c461f6c
variant_run_id: 1f9a0a132e6f
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `359a6c461f6c`
- variant: `variant` / `1f9a0a132e6f`
- period: `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 4 | 6 | 0.87 | 1.21 | -40.41 | 95.48 | 25.00% | 33.33% | 75.00% | 66.67% | -0.10 | 0.17 |
| RISK_OFF | 9 | 1 | 0.32 | 0.00 | -541.46 | -106.97 | 11.11% | 0.00% | 88.89% | 100.00% | -0.61 | -1.03 |
| RISK_ON | 36 | 39 | 0.84 | 0.86 | -458.33 | -447.78 | 25.00% | 25.64% | 75.00% | 74.36% | -0.11 | -0.10 |

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
      "closed_trades": 4,
      "wins": 1,
      "losses": 3,
      "stop_trades": 3,
      "net_pnl": -40.40591278767238,
      "gross_profit": 272.72093304517983,
      "gross_loss": 313.1268458328522,
      "avg_r": -0.10223669202494107
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 9,
      "wins": 1,
      "losses": 8,
      "stop_trades": 8,
      "net_pnl": -541.4588360211944,
      "gross_profit": 255.6335157798321,
      "gross_loss": 797.0923518010264,
      "avg_r": -0.6076459831607844
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 36,
      "wins": 9,
      "losses": 27,
      "stop_trades": 27,
      "net_pnl": -458.3298513905966,
      "gross_profit": 2335.3026177299153,
      "gross_loss": 2793.632469120512,
      "avg_r": -0.10650920241001424
    }
  },
  "variant": {
    "NEUTRAL": {
      "status": "NEUTRAL",
      "closed_trades": 6,
      "wins": 2,
      "losses": 4,
      "stop_trades": 4,
      "net_pnl": 95.48128819387321,
      "gross_profit": 544.6231005843656,
      "gross_loss": 449.1418123904924,
      "avg_r": 0.17117634510099508
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 1,
      "wins": 0,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": -106.96757909108119,
      "gross_profit": 0,
      "gross_loss": 106.96757909108119,
      "avg_r": -1.030920955667235
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 39,
      "wins": 10,
      "losses": 29,
      "stop_trades": 29,
      "net_pnl": -447.7784266550194,
      "gross_profit": 2685.240402113522,
      "gross_loss": 3133.0188287685414,
      "avg_r": -0.09564191177608873
    }
  }
}
```
