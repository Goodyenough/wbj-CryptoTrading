---
created: 2026-06-18 23:24:16 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v3
---

# 三周观察仪表 2026-06-18 demo v3

- Run ID：`n/a`
- Run type：`manual`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 8 |
| Reclaim trades | 1 |
| Reclaim fell below stop / invalidated | 0 |
| Reclaim later entered | 0 |
| Reclaim still waiting | 1 |
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
| 4h success last 24h | 0 |
| 4h failed last 24h | 0 |
| 4h running last 24h | 0 |
| daily success last 24h | 1 |
| daily failed last 24h | 0 |

| Latest Run Type | Run ID | Status | Started | Finished |
|---|---|---|---|---|
| `daily_full` | `20260618_120504_52821c3b` | success | 2026-06-18 20:05:04 CST | 2026-06-18 20:07:21 CST |
| `paper_4h_update` | n/a | n/a | n/a | n/a |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| n/a | n/a | n/a | 0.0 | n/a | n/a |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | ENTERED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.360800 | -3.26 | 0.384000 / 0.355500 | 65.58 / -18.99 | still_open |
| `ONDOUSDT` | `5d1c3b7ddf56` | ENTERED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.360800 | -0.91 | 0.384000 / 0.355500 | 69.61 / -17.02 | still_open |
| `WLDUSDT` | `616e1bbfd4c6` | ENTERED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.628200 | 120.13 | 0.628200 / 0.628200 | 120.13 / 120.13 | still_open |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `ONDOUSDT` | ENTERED | 720.2 |
| `ONDOUSDT` | ENTERED | 720.0 |
| `WLDUSDT` | ENTERED | 179.8 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 1 | 4 | 0 | 0 |
| RISK_OFF-tagged | 0 | 1 | 4 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `ONDOUSDT` | WATCHING | 0.338446 | 0.3608 | still_waiting | 2026-06-18 20:07:19 CST |
