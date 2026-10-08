---
created: 2026-09-08 12:10:47 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-09-08 demo v1

- Run ID：`20260908_041004_edf8fe01`
- Run type：`paper_4h_update`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 515 |
| Reclaim trades | 20 |
| Reclaim fell below stop / invalidated | 0 |
| Reclaim later entered | 6 |
| Reclaim still waiting | 7 |
| TP1 EMA activations | 1 |
| TP1 EMA stop raises | 9 |
| TP1 EMA stop exits | 1 |
| Open entered/TP1 positions | 7 |
| Positions over 42 x 4h / 168h | 8 |
| Stale running runs >2h | 2 |

## Run Health / 自动任务健康

| Metric | Value |
|---|---:|
| Expected 4h runs per full day | 5 |
| 4h success last 24h | 5 |
| 4h failed last 24h | 0 |
| 4h running last 24h | 0 |
| daily success last 24h | 1 |
| daily failed last 24h | 0 |

| Latest Run Type | Run ID | Status | Started | Finished |
|---|---|---|---|---|
| `daily_full` | `20260907_120502_264e4661` | success | 2026-09-07 20:05:02 CST | 2026-09-07 20:07:12 CST |
| `paper_4h_update` | `20260908_041004_edf8fe01` | success | 2026-09-08 12:10:04 CST | 2026-09-08 12:10:47 CST |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| `20260903_121720_67cc26a7` | `daily_full` | 2026-09-03 20:17:20 CST | 111.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\daily_paper_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_67cc26a7 --reason "stale run inspected manually"` |
| `20260903_121720_d001b186` | `paper_4h_update` | 2026-09-03 20:17:20 CST | 111.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\paper_4h_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_d001b186 --reason "stale run inspected manually"` |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 69.61 / -99.70 | stopped |
| `UNIUSDT` | `ecdc3e95f224` | CLOSED | 2026-09-03 20:17:21 CST (240.2h) | 6.208000 | 0.00 | 6.208000 | 0.00 | 6.208000 / 6.208000 | 0.00 / 0.00 | tp2_hit |
| `ETHUSDT` | `bffd2fdd7e2b` | ENTERED | 2026-09-03 20:17:21 CST (204.1h) | 2410.880000 | -22.10 | 2484.200000 | 41.00 | 2515.820000 / 2410.880000 | 68.22 / -22.10 | still_open |
| `TAOUSDT` | `0a265e9f2163` | ENTERED | 2026-09-03 20:17:21 CST (192.2h) | 223.100000 | -46.27 | 256.000000 | 97.34 | 269.900000 / 223.100000 | 158.01 / -46.27 | still_open |
| `WLDUSDT` | `616e1bbfd4c6` | STOPPED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.297300 | 0.00 | 0.645900 / 0.297300 | 132.65 / -98.50 | stopped |
| `TRXUSDT` | `56474a1c8879` | ENTERED | 2026-09-04 12:10:05 CST (172.0h) | 0.329300 | -75.41 | 0.334900 | -23.91 | 0.336600 / 0.328000 | -8.28 / -87.36 | still_open |
| `BNBUSDT` | `d6075516aea8` | STOPPED | 2026-09-03 20:17:21 CST (168.2h) | 711.250000 | 16.48 | 736.450000 | 0.00 | 765.950000 / 711.250000 | 206.28 / 0.00 | ema_trailing_stopped |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `ETHUSDT` | ENTERED | 316.0 |
| `TAOUSDT` | ENTERED | 304.1 |
| `TRXUSDT` | ENTERED | 268.0 |
| `SOLUSDT` | ENTERED | 108.0 |
| `ETHUSDT` | ENTERED | 108.0 |
| `ADAUSDT` | ENTERED | 32.0 |
| `BTCUSDT` | ENTERED | 32.0 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 0 | 0 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ENAUSDT` | WATCHING | 0.154645 | 0.1643 | still_waiting | 2026-09-08 12:10:26 CST |
| `DOGEUSDT` | WATCHING | 0.0825233 | 0.08989 | still_waiting | 2026-09-07 00:10:33 CST |
| `SUIUSDT` | ARCHIVED | 0.727915 | 0.8105 | archived | 2026-09-07 00:10:34 CST |
| `ADAUSDT` | ENTERED | 0.2059635 | 0.218 | reclaimed_entered | 2026-09-07 00:10:35 CST |
| `BNBUSDT` | WATCHING | 698.2468 | 743.08 | still_waiting | 2026-09-08 12:10:27 CST |
| `SOLUSDT` | ENTERED | 93.52575 | 103.24 | reclaimed_entered | 2026-09-03 20:17:47 CST |
| `BTCUSDT` | ENTERED | 76468.091 | 78863.6 | reclaimed_entered | 2026-09-07 00:10:31 CST |
| `LINKUSDT` | WATCHING | 10.90001 | 12.644 | still_waiting | 2026-09-05 20:06:10 CST |
| `ETHUSDT` | ENTERED | 2378.4204 | 2484.2 | reclaimed_entered | 2026-09-03 20:17:49 CST |
| `ENAUSDT` | ARCHIVED | 0.1328765 | 0.1741 | archived | 2026-08-27 20:07:47 CST |
| `ETHUSDT` | ARCHIVED | 2378.4204 | 2499.13 | archived | 2026-08-28 12:10:09 CST |
| `PEPEUSDT` | WATCHING | 3.59525e-06 | 3.6e-06 | still_waiting | 2026-09-08 12:10:23 CST |
| `ZROUSDT` | WATCHING | 1.02834 | 1.14 | still_waiting | 2026-09-08 12:10:23 CST |
| `BNBUSDT` | ARCHIVED | 677.68 | 703.16 | archived | 2026-08-27 12:10:11 CST |
| `SOLUSDT` | ARCHIVED | 90.2063 | 106.58 | archived | 2026-08-27 04:10:10 CST |
| `BTCUSDT` | ARCHIVED | 74412.485 | 79818.65 | archived | 2026-08-27 04:10:10 CST |
| `TAOUSDT` | ENTERED | 210.79 | 256 | reclaimed_entered | 2026-08-26 08:10:08 CST |
| `TRXUSDT` | ENTERED | 0.326626 | 0.3349 | reclaimed_entered | 2026-08-27 20:07:45 CST |
| `ETHUSDT` | ARCHIVED | 1841.1325 | 1916.67 | archived | 2026-08-18 12:10:06 CST |
| `ONDOUSDT` | WATCHING | 0.338446 | 0.3788 | still_waiting | 2026-09-08 12:10:21 CST |
