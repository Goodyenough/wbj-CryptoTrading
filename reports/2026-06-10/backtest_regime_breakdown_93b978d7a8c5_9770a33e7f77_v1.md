---
created: 2026-06-10T02:23:07+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 93b978d7a8c5
variant_run_id: 9770a33e7f77
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `93b978d7a8c5`
- variant: `variant` / `9770a33e7f77`
- period: `2025-06-01T00:00:00+00:00` -> `2026-06-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 4 | 6 | 0.87 | 2.57 | -40.41 | 538.70 | 25.00% | 50.00% | 75.00% | 50.00% | -0.10 | 0.82 |
| RISK_OFF | 9 | 9 | 0.32 | 0.33 | -541.46 | -606.29 | 11.11% | 11.11% | 88.89% | 88.89% | -0.61 | -0.61 |
| RISK_ON | 36 | 36 | 0.84 | 1.23 | -458.33 | 627.20 | 25.00% | 33.33% | 75.00% | 66.67% | -0.11 | 0.20 |

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
      "net_pnl": 538.7004698156161,
      "gross_profit": 881.3544045005663,
      "gross_loss": 342.6539346849501,
      "avg_r": 0.8216487408458425
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 9,
      "wins": 1,
      "losses": 8,
      "stop_trades": 8,
      "net_pnl": -606.2907209830573,
      "gross_profit": 295.1767024277629,
      "gross_loss": 901.4674234108202,
      "avg_r": -0.6098700678625575
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 36,
      "wins": 12,
      "losses": 24,
      "stop_trades": 24,
      "net_pnl": 627.1987011358037,
      "gross_profit": 3323.028220007238,
      "gross_loss": 2695.829518871434,
      "avg_r": 0.19798150631977707
    }
  }
}
```
