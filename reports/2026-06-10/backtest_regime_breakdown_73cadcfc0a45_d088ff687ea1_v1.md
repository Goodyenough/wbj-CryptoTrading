---
created: 2026-06-10T00:48:37+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 73cadcfc0a45
variant_run_id: d088ff687ea1
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `73cadcfc0a45`
- variant: `variant` / `d088ff687ea1`
- period: `2025-01-01T00:00:00+00:00` -> `2025-09-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 3 | 3 | 4.85 | 4.89 | 373.12 | 377.65 | 66.67% | 66.67% | 33.33% | 33.33% | 1.44 | 1.44 |
| RISK_OFF | 10 | 9 | 0.29 | 0.32 | -620.53 | -535.78 | 10.00% | 11.11% | 90.00% | 88.89% | -0.65 | -0.61 |
| RISK_ON | 29 | 29 | 0.51 | 0.94 | -1123.23 | -121.79 | 17.24% | 27.59% | 82.76% | 72.41% | -0.39 | -0.02 |

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
      "closed_trades": 3,
      "wins": 2,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 373.11572687168814,
      "gross_profit": 470.02245495489825,
      "gross_loss": 96.90672808321013,
      "avg_r": 1.4413790190805702
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 10,
      "wins": 1,
      "losses": 9,
      "stop_trades": 9,
      "net_pnl": -620.5323780471796,
      "gross_profit": 248.15705722194315,
      "gross_loss": 868.6894352691227,
      "avg_r": -0.6504690804941398
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 29,
      "wins": 5,
      "losses": 24,
      "stop_trades": 24,
      "net_pnl": -1123.233553027183,
      "gross_profit": 1165.5601521225792,
      "gross_loss": 2288.793705149762,
      "avg_r": -0.3898372725586018
    }
  },
  "variant": {
    "NEUTRAL": {
      "status": "NEUTRAL",
      "closed_trades": 3,
      "wins": 2,
      "losses": 1,
      "stop_trades": 1,
      "net_pnl": 377.6546341596212,
      "gross_profit": 474.6665762469115,
      "gross_loss": 97.0119420872903,
      "avg_r": 1.4413790190805702
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 9,
      "wins": 1,
      "losses": 8,
      "stop_trades": 8,
      "net_pnl": -535.7814212834053,
      "gross_profit": 247.94489036568586,
      "gross_loss": 783.7263116490911,
      "avg_r": -0.6127483396415908
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 29,
      "wins": 8,
      "losses": 21,
      "stop_trades": 21,
      "net_pnl": -121.79069745750124,
      "gross_profit": 1945.010900379876,
      "gross_loss": 2066.801597837377,
      "avg_r": -0.0171349776952155
    }
  }
}
```
