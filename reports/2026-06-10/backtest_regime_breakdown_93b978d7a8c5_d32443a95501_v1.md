---
created: 2026-06-10T03:44:06+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 93b978d7a8c5
variant_run_id: d32443a95501
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `93b978d7a8c5`
- variant: `variant` / `d32443a95501`
- period: `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 4 | 6 | 0.87 | 2.53 | -40.41 | 533.91 | 25.00% | 50.00% | 75.00% | 50.00% | -0.10 | 0.82 |
| RISK_OFF | 9 | 1 | 0.32 | 0.00 | -541.46 | -112.31 | 11.11% | 0.00% | 88.89% | 100.00% | -0.61 | -1.03 |
| RISK_ON | 36 | 39 | 0.84 | 1.10 | -458.33 | 289.35 | 25.00% | 30.77% | 75.00% | 69.23% | -0.11 | 0.10 |

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
      "wins": 3,
      "losses": 3,
      "stop_trades": 3,
      "net_pnl": 533.9096226783566,
      "gross_profit": 881.9467295772715,
      "gross_loss": 348.037106898915,
      "avg_r": 0.8230346221647552
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 1,
      "wins": 0,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": -112.30500894152706,
      "gross_profit": 0,
      "gross_loss": 112.30500894152706,
      "avg_r": -1.030920955667235
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 39,
      "wins": 12,
      "losses": 27,
      "stop_trades": 27,
      "net_pnl": 289.3473952171237,
      "gross_profit": 3321.5609555945125,
      "gross_loss": 3032.2135603773886,
      "avg_r": 0.10398405928547219
    }
  }
}
```
