---
created: 2026-06-10T04:05:23+08:00
tags:
  - crypto
  - trading-system
  - regime-analysis
baseline_run_id: 73cadcfc0a45
variant_run_id: 1d313ac1b8eb
report_version: v1
---

# Market Regime Breakdown v1

- baseline: `baseline` / `73cadcfc0a45`
- variant: `variant` / `1d313ac1b8eb`
- period: `2025-01-01T00:00:00+00:00` -> `2025-09-01T00:00:00+00:00`
- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.

## Regime Metrics

| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NEUTRAL | 3 | 3 | 4.85 | 4.85 | 373.12 | 373.11 | 66.67% | 66.67% | 33.33% | 33.33% | 1.44 | 1.44 |
| RISK_OFF | 10 | 10 | 0.29 | 0.29 | -620.53 | -618.86 | 10.00% | 10.00% | 90.00% | 90.00% | -0.65 | -0.65 |
| RISK_ON | 29 | 35 | 0.51 | 0.47 | -1123.23 | -1318.06 | 17.24% | 14.29% | 82.76% | 85.71% | -0.39 | -0.39 |

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
      "net_pnl": 373.1058950865121,
      "gross_profit": 470.01262316972225,
      "gross_loss": 96.90672808321013,
      "avg_r": 1.4413790190805702
    },
    "RISK_OFF": {
      "status": "RISK_OFF",
      "closed_trades": 10,
      "wins": 1,
      "losses": 9,
      "stop_trades": 9,
      "net_pnl": -618.8606522289638,
      "gross_profit": 248.15705722194315,
      "gross_loss": 867.017709450907,
      "avg_r": -0.6504690804941398
    },
    "RISK_ON": {
      "status": "RISK_ON",
      "closed_trades": 35,
      "wins": 5,
      "losses": 30,
      "stop_trades": 30,
      "net_pnl": -1318.0596425774415,
      "gross_profit": 1165.5218584183442,
      "gross_loss": 2483.5815009957855,
      "avg_r": -0.3857390324695553
    }
  }
}
```
