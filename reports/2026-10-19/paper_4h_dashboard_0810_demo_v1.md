---
created: 2026-10-19 08:10:16 CST
tags:
  - crypto
  - trading-system
  - paper-observation
account: demo
report_version: v1
---

# 三周观察仪表 2026-10-19 demo v1

- Run ID：`20261019_001002_38d2b57c`
- Run type：`paper_4h_update`
- 数据来源：SQLite

## 核心指标

| Metric | Value |
|---|---:|
| RECLAIM_PENDING events | 778 |
| Reclaim trades | 25 |
| Reclaim fell below stop / invalidated | 2 |
| Reclaim later entered | 8 |
| Reclaim still waiting | 8 |
| TP1 EMA activations | 9 |
| TP1 EMA stop raises | 56 |
| TP1 EMA stop exits | 6 |
| Open entered/TP1 positions | 2 |
| Positions over 42 x 4h / 168h | 15 |
| Stale running runs >2h | 2 |

## Run Health / 自动任务健康

| Metric | Value |
|---|---:|
| Expected 4h runs per full day | 5 |
| 4h success last 24h | 5 |
| 4h failed last 24h | 0 |
| 4h running last 24h | 0 |
| daily success last 24h | 0 |
| daily failed last 24h | 0 |

| Latest Run Type | Run ID | Status | Started | Finished |
|---|---|---|---|---|
| `daily_full` | `20261016_120503_6504f6a9` | success | 2026-10-16 20:05:03 CST | 2026-10-16 20:06:37 CST |
| `paper_4h_update` | `20261019_001002_38d2b57c` | success | 2026-10-19 08:10:02 CST | 2026-10-19 08:10:16 CST |

## Stale Running Run 检测

| Run ID | Type | Started | Age Hours | Log | Suggested Action |
|---|---|---|---:|---|---|
| `20260903_121720_67cc26a7` | `daily_full` | 2026-09-03 20:17:20 CST | 1091.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\daily_paper_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_67cc26a7 --reason "stale run inspected manually"` |
| `20260903_121720_d001b186` | `paper_4h_update` | 2026-09-03 20:17:20 CST | 1091.9 | `D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\logs\paper_4h_update.log` | `python main.py db mark-run-failed --run-id 20260903_121720_d001b186 --reason "stale run inspected manually"` |

## 42-bar Holding Review

| Symbol | Plan | Status | First observed >=168h | Price@first | PnL@first | Latest Price | Latest PnL | Max/Min Price After | Max/Min PnL After | Outcome |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| `ONDOUSDT` | `2ed171ff8ada` | STOPPED | 2026-06-13 20:06:36 CST (596.9h) | 0.367200 | 15.73 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 65.58 / -99.71 | stopped |
| `ONDOUSDT` | `5d1c3b7ddf56` | STOPPED | 2026-06-13 20:06:36 CST (596.7h) | 0.367200 | 18.54 | 0.324400 | 0.00 | 0.384000 / 0.324400 | 69.61 / -99.70 | stopped |
| `ETHUSDT` | `4f2f0f1fa0e7` | STOPPED | 2026-09-22 00:10:04 CST (432.0h) | 2747.520000 | 201.38 | 2664.470000 | 0.00 | 2776.160000 / 2664.470000 | 224.77 / 0.00 | ema_trailing_stopped |
| `SOLUSDT` | `d058835e1b0f` | ENTERED | 2026-09-22 00:10:04 CST (432.0h) | 117.740000 | 121.05 | 104.220000 | -2.37 | 119.110000 / 100.980000 | 133.56 / -31.95 | still_open |
| `ZROUSDT` | `67ed9d733634` | STOPPED | 2026-10-09 00:10:03 CST (404.0h) | 1.955000 | 0.00 | 1.955000 | 0.00 | 1.955000 / 1.955000 | 0.00 / 0.00 | ema_trailing_stopped |
| `AAVEUSDT` | `94119a9f7aee` | STOPPED | 2026-10-09 00:10:03 CST (364.1h) | 165.580000 | 125.29 | 171.550000 | 0.00 | 174.510000 / 165.580000 | 186.90 / 0.00 | ema_trailing_stopped |
| `ADAUSDT` | `2d74b7ff6191` | CLOSED | 2026-09-22 00:10:04 CST (356.0h) | 0.244700 | 197.14 | 0.255400 | 0.00 | 0.255400 / 0.244500 | 250.07 / 0.00 | tp2_hit |
| `BTCUSDT` | `5ff6dab72dfa` | STOPPED | 2026-09-22 00:10:04 CST (356.0h) | 85754.300000 | 180.68 | 83934.010000 | 0.00 | 86844.390000 / 83934.010000 | 213.62 / 0.00 | ema_trailing_stopped |
| `DOGEUSDT` | `549cfdd6bdc4` | STOPPED | 2026-09-22 00:10:04 CST (320.0h) | 0.097100 | 125.76 | 0.093190 | 0.00 | 0.104470 / 0.093190 | 239.91 / 0.00 | ema_trailing_stopped |
| `UNIUSDT` | `ecdc3e95f224` | CLOSED | 2026-09-03 20:17:21 CST (240.2h) | 6.208000 | 0.00 | 6.208000 | 0.00 | 6.208000 / 6.208000 | 0.00 / 0.00 | tp2_hit |
| `ETHUSDT` | `bffd2fdd7e2b` | CLOSED | 2026-09-03 20:17:21 CST (204.1h) | 2410.880000 | -22.10 | 2770.450000 | 0.00 | 2770.450000 / 2410.880000 | 267.64 / -22.10 | tp2_hit |
| `TAOUSDT` | `0a265e9f2163` | CLOSED | 2026-09-03 20:17:21 CST (192.2h) | 223.100000 | -46.27 | 306.200000 | 0.00 | 306.200000 / 223.100000 | 236.58 / -46.27 | tp2_hit |
| `WLDUSDT` | `616e1bbfd4c6` | STOPPED | 2026-06-18 20:07:18 CST (176.5h) | 0.628200 | 120.13 | 0.297300 | 0.00 | 0.645900 / 0.297300 | 132.65 / -98.50 | stopped |
| `TRXUSDT` | `56474a1c8879` | ENTERED | 2026-09-04 12:10:05 CST (172.0h) | 0.329300 | -75.41 | 0.332600 | -45.06 | 0.348600 / 0.327400 | 102.08 / -92.88 | still_open |
| `BNBUSDT` | `d6075516aea8` | STOPPED | 2026-09-03 20:17:21 CST (168.2h) | 711.250000 | 16.48 | 736.450000 | 0.00 | 765.950000 / 711.250000 | 206.28 / 0.00 | ema_trailing_stopped |

## 开放持仓时长

| Symbol | Status | Holding Hours |
|---|---|---:|
| `TRXUSDT` | ENTERED | 1248.0 |
| `SOLUSDT` | ENTERED | 1088.0 |

## 今日扫描 Action 与 RISK_OFF

| Scope | BUY_CANDIDATE | WAIT_PULLBACK | WATCH_ONLY | REJECT | Other |
|---|---:|---:|---:|---:|---:|
| All candidates | 0 | 0 | 0 | 0 | 0 |
| RISK_OFF-tagged | 0 | 0 | 0 | 0 | 0 |

## RECLAIM_PENDING 明细

| Symbol | Status | Stop | Last Price | Outcome | Last Pending |
|---|---|---:|---:|---|---|
| `DOGEUSDT` | WATCHING | 0.08432585 | 0.07941 | fell_below_stop_or_invalidated | 2026-10-19 08:10:05 CST |
| `XRPUSDT` | WATCHING | 1.366786 | 1.3092 | fell_below_stop_or_invalidated | 2026-10-19 08:10:05 CST |
| `HBARUSDT` | WATCHING | 0.08324235 | 0.08534 | still_waiting | 2026-10-19 08:10:05 CST |
| `LTCUSDT` | WATCHING | 55.68205 | 59.18 | still_waiting | 2026-10-19 08:10:04 CST |
| `SUIUSDT` | WATCHING | 0.7362875 | 0.9984 | still_waiting | 2026-09-10 04:10:09 CST |
| `ENAUSDT` | WATCHING | 0.154645 | 0.1889 | still_waiting | 2026-09-10 04:10:08 CST |
| `DOGEUSDT` | STOPPED | 0.095269728 | 0.09319 | reclaimed_entered | 2026-09-07 00:10:33 CST |
| `SUIUSDT` | ARCHIVED | 0.727915 | 0.8105 | archived | 2026-09-07 00:10:34 CST |
| `ADAUSDT` | CLOSED | 0.23855728 | 0.2554 | reclaimed_entered | 2026-09-07 00:10:35 CST |
| `BNBUSDT` | WATCHING | 698.2468 | 724.24 | still_waiting | 2026-10-19 08:10:04 CST |
| `SOLUSDT` | ENTERED | 93.52575 | 104.22 | reclaimed_entered | 2026-09-03 20:17:47 CST |
| `BTCUSDT` | STOPPED | 84250.979 | 83934.01 | reclaimed_entered | 2026-09-07 00:10:31 CST |
| `LINKUSDT` | WATCHING | 10.90001 | 12.067 | still_waiting | 2026-10-19 04:10:05 CST |
| `ETHUSDT` | STOPPED | 2702.3371 | 2664.47 | reclaimed_entered | 2026-09-03 20:17:49 CST |
| `ENAUSDT` | ARCHIVED | 0.1328765 | 0.1741 | archived | 2026-08-27 20:07:47 CST |
| `ETHUSDT` | ARCHIVED | 2378.4204 | 2499.13 | archived | 2026-08-28 12:10:09 CST |
| `PEPEUSDT` | WATCHING | 3.59525e-06 | 4.01e-06 | still_waiting | 2026-10-19 04:10:04 CST |
| `ZROUSDT` | STOPPED | 2.0938614 | 1.955 | reclaimed_entered | 2026-09-10 04:10:07 CST |
| `BNBUSDT` | ARCHIVED | 677.68 | 703.16 | archived | 2026-08-27 12:10:11 CST |
| `SOLUSDT` | ARCHIVED | 90.2063 | 106.58 | archived | 2026-08-27 04:10:10 CST |
| `BTCUSDT` | ARCHIVED | 74412.485 | 79818.65 | archived | 2026-08-27 04:10:10 CST |
| `TAOUSDT` | CLOSED | 266.088 | 306.2 | reclaimed_entered | 2026-08-26 08:10:08 CST |
| `TRXUSDT` | ENTERED | 0.326626 | 0.3326 | reclaimed_entered | 2026-08-27 20:07:45 CST |
| `ETHUSDT` | ARCHIVED | 1841.1325 | 1916.67 | archived | 2026-08-18 12:10:06 CST |
| `ONDOUSDT` | WATCHING | 0.338446 | 0.4363 | still_waiting | 2026-09-10 04:10:05 CST |
