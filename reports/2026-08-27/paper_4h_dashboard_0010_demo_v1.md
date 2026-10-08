---
created: 2026-08-27 00:10:45 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-08-27 demo v1

- Run ID：`20260826_161004_a0afc2da`
- Run type：`paper_4h_update`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 367 |
| Reclaim trades | 8 |
| Reclaim fell below stop / invalidated | 0 |
| Reclaim later entered | 1 |
| Reclaim still waiting | 6 |
| TP1 EMA activations | 0 |
| TP1 EMA stop raises | 0 |
| TP1 EMA stop exits | 0 |
| Open entered/TP1 positions | 3 |
| Positions over 42 x 4h / 168h | 3 |
| Stale running runs >2h | 0 |

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
| `daily_full` | `20260826_120504_64db5169` | success | 2026-08-26 20:05:04 CST | 2026-08-26 20:06:57 CST |
| `paper_4h_update` | `20260826_161004_a0afc2da` | success | 2026-08-27 00:10:04 CST | 2026-08-27 00:10:45 CST |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| n/a | n/a | n/a | 0.0 | n/a | n/a |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 69.61 / -99.70 | stopped |
| `WLDUSDT` | `616e1bbfd4c6` | STOPPED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.297300 | 0.00 | 0.645900 / 0.297300 | 132.65 / -98.50 | stopped |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `UNIUSDT` | ENTERED | 52.1 |
| `ETHUSDT` | ENTERED | 16.0 |
| `TAOUSDT` | ENTERED | 4.1 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 0 | 0 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ZROUSDT` | WATCHING | 1.02834 | 1.131 | still_waiting | 2026-08-27 00:10:26 CST |
| `BNBUSDT` | WATCHING | 677.68 | 697.66 | still_waiting | 2026-08-27 00:10:27 CST |
| `SOLUSDT` | WATCHING | 90.2063 | 95.99 | still_waiting | 2026-08-27 00:10:24 CST |
| `BTCUSDT` | WATCHING | 74412.485 | 78132.51 | still_waiting | 2026-08-27 00:10:25 CST |
| `TAOUSDT` | ENTERED | 210.79 | 228.3 | reclaimed_entered | 2026-08-26 08:10:08 CST |
| `TRXUSDT` | WATCHING | 0.326626 | 0.3347 | still_waiting | 2026-08-27 00:10:18 CST |
| `ETHUSDT` | ARCHIVED | 1841.1325 | 1916.67 | archived | 2026-08-18 12:10:06 CST |
| `ONDOUSDT` | WATCHING | 0.338446 | 0.36 | still_waiting | 2026-08-27 00:10:17 CST |
