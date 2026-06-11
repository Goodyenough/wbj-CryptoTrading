---
created: 2026-06-11 21:28:32 CST
tags:
  - crypto
  - trading-system
  - backtest
  - market-cap-split
report_version: v1
---

# 市值分层回测：当前 sensitive 组合 v1

## 背景

验证弱市中是否应该“一律少做”，还是只应该限制 altcoin，而保留 BTC/ETH/BNB/SOL 这类大市值交易机会。

## 样本

- 区间：`2025-06-01 -> 2026-06-01`
- 策略配置：当前 `config/settings.toml` sensitive 默认组合
  - `risk_off_core_buy_enabled=false`
  - `entry_reclaim_close_enabled=true`
  - `tp1_ema_trailing_stop_enabled=true`
  - `regime_btc_7d_drop_pct=-3.0`
  - `regime_eth_7d_drop_pct=-5.0`
  - `regime_require_both_trend=true`
- large-cap master：`reports/2026-06-11/dynamic_master_full_large_cap.json`
- altcoin master：`reports/2026-06-11/dynamic_master_full_altcoin.json`

## 结果

| Segment | Master Symbols | Max Symbols | Trades | Closed | Win Rate | Profit Factor | Net Return | Max Drawdown | Sample |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Large-cap (`BTC/ETH/BNB/SOL`) | 4 | 4 | 43 | 30 | 43.33% | 1.19 | +3.46% | 11.36% | true |
| Altcoin | 414 | 50 | 275 | 57 | 33.33% | 0.76 | -10.26% | 23.44% | true |

## 报告证据

- Large-cap：`reports/2026-06-11/backtest_dynamic_universe_2025-06-01_2026-06-01_v12.md`
- Altcoin：`reports/2026-06-11/backtest_dynamic_universe_2025-06-01_2026-06-01_v13.md`

## 结论

`retest / candidate_keep_review`：单窗口证据显示 current sensitive 组合在 large-cap 上转正且回撤较低，而 altcoin 仍显著负收益、回撤更大。弱市问题不是“所有币完全不能做”，更像是 altcoin 风险暴露仍然过高；BTC/ETH/BNB/SOL 可继续作为单独池观察。

## 下一步

1. 用非重叠窗口复测 large-cap vs altcoin，例如 `2024-07-01 -> 2025-06-01` 与 `2025-06-01 -> 2026-06-01`。
2. 若 large-cap 继续稳定，考虑将 RISK_OFF 下的 core/large-cap 规则从 altcoin 规则中拆出来单独管理。
