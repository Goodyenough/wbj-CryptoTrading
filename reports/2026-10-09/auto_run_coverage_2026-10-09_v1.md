# daily / 4h 自动运行覆盖审计（2026-10-09）

## 结论

**进程恢复，连续证据未达标。** Windows 任务处于 Ready，最近 daily 与 4h run 均成功；但数据库仍有两条 2026-09-03 的 stale `running` 记录，近期 4h 仍出现 `ticker_error`/`kline_error` 的逐计划 skip，当前只有 2 个 forward tick 且 0 个 paired closed trade。因此结果是 `partial_pass / insufficient_continuous_coverage`。

## 调度器状态

| 任务 | 状态 | 最近成功 | 下次运行 | 关键配置 |
|---|---|---|---|---|
| `CryptoTrading_4H_PaperUpdate` | Ready | 2026-10-09 16:10:01 +08:00，result 0 | 2026-10-10 00:10 +08:00 | `StartWhenAvailable=true`, `MultipleInstances=IgnoreNew` |
| `CryptoTrading_DailyPaperUpdate` | Ready | 2026-10-09 20:05:01 +08:00，result 0 | 2026-10-10 20:05 +08:00 | `StartWhenAvailable=true` |

## 数据库运行证据

近期 `2026-10-08 16:10` 至 `2026-10-09 20:05` 的 daily/4h 运行均有成功记录。daily 成功后完成 post-check，最新摘要为 scans=90、candidates=431、buy_candidates=41、paper_plans=65；4h 成功后生成 paper report/dashboard/shadow report。

同时存在以下未结束记录，未做手工改写：

- `20260903_121720_67cc26a7`：`daily_full`，status=`running`；
- `20260903_121720_d001b186`：`paper_4h_update`，status=`running`。

## 逐计划覆盖与前向样本

- 2026-10-09 daily 的 funnel 有 candidate observation 5；import evaluation 为 `action_not_allowed=1`、`data_quality_blocked=4`；plan update 为 `closed_4h_available=3`、`reclaim_pending=5`、`ticker_update=5`。
- 近期 4h funnel 仍出现 `plan_update_skipped`：`ticker_error=13`、`kline_error=2`；因此不能宣称每个计划每个档位都完成有效评价。
- `paper_forward_ticks` 当前只有 `20261009_081003_bde516e3` 与 `20261009_120503_060f1481` 两个 `OK` tick；`paired_closed_trades=0`。

## 含义与下一步

自动任务已经恢复到“能按时启动并完成”的状态，但还没有恢复到“连续、逐计划、无 skip 的可信采样”。保持生产配置不变，继续观察完整自然 epoch；另行复核两条 stale running 记录的来源，未经明确授权不直接修改数据库历史状态。
