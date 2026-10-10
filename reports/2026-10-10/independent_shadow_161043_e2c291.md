# 独立前向 shadow 状态

执行口径：每个 4h 档的一次 ticker 采样；不模拟常驻保护单。controls_paper=false。

incumbent 与 ATR 0.35 为同义线，不重复计数。GAP_AFFECTED/CONFIG_CHANGED 的金额仅供诊断，不属于可信组合成绩。paired_terminal 含未入场终态；paired_closed_trades 才是两线都入场并退出。

工程接入与自然运行验收分开；当前不据此判断 ATR 收益有效。

```json
{
  "account": "demo",
  "controls_paper": false,
  "execution": "sampled_quote_v1",
  "research_incumbent_alias": "atr_reclaim_0_35_shadow",
  "epochs": [
    {
      "epoch_id": "0cb1e94cbf934b77b97abbd597e6ae52",
      "started_at": "2026-10-09T08:10:03Z",
      "updated_at": "2026-10-09T16:10:49Z",
      "status": "CONFIG_CHANGED",
      "reason": "policy_or_code_changed",
      "lines": {
        "atr_reclaim_0_35_shadow": {
          "opportunities": 0,
          "entered": 0,
          "closed_trades": 0,
          "open": 0,
          "censored": 0,
          "cash": 10000.0,
          "equity": 10000.0,
          "fees": 0,
          "closed_net_pnl": 0,
          "quality_counts": {
            "CLEAN": 0,
            "DEGRADED": 0
          }
        },
        "reference_baseline": {
          "opportunities": 0,
          "entered": 0,
          "closed_trades": 0,
          "open": 0,
          "censored": 0,
          "cash": 10000.0,
          "equity": 10000.0,
          "fees": 0,
          "closed_net_pnl": 0,
          "quality_counts": {
            "CLEAN": 0,
            "DEGRADED": 0
          }
        }
      },
      "paired_terminal": 0,
      "paired_closed_trades": 0
    },
    {
      "epoch_id": "bd62d1bac7e248d6adaa9ee26ef87a59",
      "started_at": "2026-10-09T16:10:49Z",
      "updated_at": "2026-10-10T08:10:43Z",
      "status": "ACTIVE",
      "reason": null,
      "lines": {
        "atr_reclaim_0_35_shadow": {
          "opportunities": 0,
          "entered": 0,
          "closed_trades": 0,
          "open": 0,
          "censored": 0,
          "cash": 10000.0,
          "equity": 10000.0,
          "fees": 0,
          "closed_net_pnl": 0,
          "quality_counts": {
            "CLEAN": 0,
            "DEGRADED": 0
          }
        },
        "reference_baseline": {
          "opportunities": 0,
          "entered": 0,
          "closed_trades": 0,
          "open": 0,
          "censored": 0,
          "cash": 10000.0,
          "equity": 10000.0,
          "fees": 0,
          "closed_net_pnl": 0,
          "quality_counts": {
            "CLEAN": 0,
            "DEGRADED": 0
          }
        }
      },
      "paired_terminal": 0,
      "paired_closed_trades": 0
    }
  ],
  "verdict": "insufficient_paired_forward_evidence"
}
```
