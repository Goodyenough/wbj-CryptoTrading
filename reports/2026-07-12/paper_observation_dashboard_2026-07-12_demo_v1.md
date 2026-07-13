---
created: 2026-07-12 20:05:56 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-07-12 demo v1

- Run ID：`20260712_120503_54b76c1f`
- Run type：`daily_full`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 134 |
| Reclaim trades | 1 |
| Reclaim fell below stop / invalidated | 1 |
| Reclaim later entered | 0 |
| Reclaim still waiting | 0 |
| TP1 EMA activations | 0 |
| TP1 EMA stop raises | 0 |
| TP1 EMA stop exits | 0 |
| Open entered/TP1 positions | 1 |
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
| `daily_full` | `20260712_120503_54b76c1f` | running | 2026-07-12 20:05:03 CST | n/a |
| `paper_4h_update` | `20260712_081003_9121f237` | success | 2026-07-12 16:10:03 CST | 2026-07-12 16:10:13 CST |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| n/a | n/a | n/a | 0.0 | n/a | n/a |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 69.61 / -99.70 | stopped |
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.429200 | -20.58 | 0.645900 / 0.359600 | 132.65 / -69.79 | still_open |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `WLDUSDT` | ENTERED | 752.5 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 4 | 1 | 0 |
| RISK_OFF-tagged | 0 | 0 | 4 | 1 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ONDOUSDT` | WATCHING | 0.338446 | 0.3292 | fell_below_stop_or_invalidated | 2026-07-12 20:05:54 CST |
