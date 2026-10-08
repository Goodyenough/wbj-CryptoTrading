---
created: 2026-09-06 12:10:37 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-09-06 demo v1

- Run ID：`20260906_041003_cf4a58f5`
- Run type：`paper_4h_update`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 461 |
| Reclaim trades | 15 |
| Reclaim fell below stop / invalidated | 0 |
| Reclaim later entered | 4 |
| Reclaim still waiting | 6 |
| TP1 EMA activations | 1 |
| TP1 EMA stop raises | 1 |
| TP1 EMA stop exits | 0 |
| Open entered/TP1 positions | 6 |
| Positions over 42 x 4h / 168h | 8 |
| Stale running runs >2h | 2 |

## Run Health / 自动任务健康

| Metric | Value |
|---|---:|
| Expected 4h runs per full day | 5 |
| 4h success last 24h | 3 |
| 4h failed last 24h | 0 |
| 4h running last 24h | 0 |
| daily success last 24h | 1 |
| daily failed last 24h | 0 |

| Latest Run Type | Run ID | Status | Started | Finished |
|---|---|---|---|---|
| `daily_full` | `20260905_120502_1c9e7ed5` | success | 2026-09-05 20:05:02 CST | 2026-09-05 20:06:17 CST |
| `paper_4h_update` | `20260906_041003_cf4a58f5` | success | 2026-09-06 12:10:03 CST | 2026-09-06 12:10:37 CST |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| `20260903_121720_67cc26a7` | `daily_full` | 2026-09-03 20:17:20 CST | 63.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\daily_paper_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_67cc26a7 --reason "stale run inspected manually"` |
| `20260903_121720_d001b186` | `paper_4h_update` | 2026-09-03 20:17:20 CST | 63.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\paper_4h_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_d001b186 --reason "stale run inspected manually"` |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 69.61 / -99.70 | stopped |
| `UNIUSDT` | `ecdc3e95f224` | CLOSED | 2026-09-03 20:17:21 CST (240.2h) | 6.208000 | 0.00 | 6.208000 | 0.00 | 6.208000 / 6.208000 | 0.00 / 0.00 | tp2_hit |
| `ETHUSDT` | `bffd2fdd7e2b` | ENTERED | 2026-09-03 20:17:21 CST (204.1h) | 2410.880000 | -22.10 | 2508.020000 | 61.51 | 2515.540000 / 2410.880000 | 67.98 / -22.10 | still_open |
| `TAOUSDT` | `0a265e9f2163` | ENTERED | 2026-09-03 20:17:21 CST (192.2h) | 223.100000 | -46.27 | 238.700000 | 21.82 | 239.600000 / 223.100000 | 25.75 / -46.27 | still_open |
| `WLDUSDT` | `616e1bbfd4c6` | STOPPED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.297300 | 0.00 | 0.645900 / 0.297300 | 132.65 / -98.50 | stopped |
| `TRXUSDT` | `56474a1c8879` | ENTERED | 2026-09-04 12:10:05 CST (172.0h) | 0.329300 | -75.41 | 0.333300 | -38.62 | 0.334300 / 0.328000 | -29.43 / -87.36 | still_open |
| `BNBUSDT` | `d6075516aea8` | TP1_HIT | 2026-09-03 20:17:21 CST (168.2h) | 711.250000 | 16.48 | 764.760000 | 202.15 | 765.950000 / 711.250000 | 206.28 / 16.48 | tp1_hit |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `ETHUSDT` | ENTERED | 268.0 |
| `TAOUSDT` | ENTERED | 256.1 |
| `BNBUSDT` | TP1_HIT | 232.0 |
| `TRXUSDT` | ENTERED | 220.0 |
| `SOLUSDT` | ENTERED | 60.0 |
| `ETHUSDT` | ENTERED | 60.0 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 0 | 0 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `SOLUSDT` | ENTERED | 93.52575 | 106.03 | reclaimed_entered | 2026-09-03 20:17:47 CST |
| `BTCUSDT` | WATCHING | 76468.091 | 79977.99 | still_waiting | 2026-09-05 20:06:10 CST |
| `LINKUSDT` | WATCHING | 10.90001 | 12.198 | still_waiting | 2026-09-05 20:06:10 CST |
| `ETHUSDT` | ENTERED | 2378.4204 | 2508.02 | reclaimed_entered | 2026-09-03 20:17:49 CST |
| `ENAUSDT` | WATCHING | 0.1328765 | 0.1762 | still_waiting | 2026-08-27 20:07:47 CST |
| `ETHUSDT` | ARCHIVED | 2378.4204 | 2499.13 | archived | 2026-08-28 12:10:09 CST |
| `PEPEUSDT` | WATCHING | 3.59525e-06 | 3.64e-06 | still_waiting | 2026-09-06 12:10:20 CST |
| `ZROUSDT` | WATCHING | 1.02834 | 1.076 | still_waiting | 2026-09-06 12:10:19 CST |
| `BNBUSDT` | ARCHIVED | 677.68 | 703.16 | archived | 2026-08-27 12:10:11 CST |
| `SOLUSDT` | ARCHIVED | 90.2063 | 106.58 | archived | 2026-08-27 04:10:10 CST |
| `BTCUSDT` | ARCHIVED | 74412.485 | 79818.65 | archived | 2026-08-27 04:10:10 CST |
| `TAOUSDT` | ENTERED | 210.79 | 238.7 | reclaimed_entered | 2026-08-26 08:10:08 CST |
| `TRXUSDT` | ENTERED | 0.326626 | 0.3333 | reclaimed_entered | 2026-08-27 20:07:45 CST |
| `ETHUSDT` | ARCHIVED | 1841.1325 | 1916.67 | archived | 2026-08-18 12:10:06 CST |
| `ONDOUSDT` | WATCHING | 0.338446 | 0.3753 | still_waiting | 2026-09-06 12:10:13 CST |
