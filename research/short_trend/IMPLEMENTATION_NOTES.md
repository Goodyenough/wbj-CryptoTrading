# 首次事件回放前的实现说明

本说明写于2026-11-25，北京时间，首次策略结果计算之前；原冻结协议/JSON未改。用户已要求开始回测，本阶段实现并运行旧期事件层，不把未知历史规则当账户通过。

## 不改变信号的执行澄清

1. 普通有利价格缺口跨越已经存在的TP，按冻结TP参考成交，再扣退出滑点，不给缺口改善。但资金费更新首次使净目标满足时，不能回填一个从未出现的阈值：使用首次可观察的开盘，记录`cashflow_target_at_open`。这落实“资金费更新不能虚构柱外成交”和price-first不回借先前极值；不修改净目标、信号、止损或风险。
2. 年度/剔除一币点估计正的检查属于normal成本层；stress主门为pooled平均净R≥0，细分结果照报，不新增stress子组优化。
3. 两种预先固定周块法或资金费顺序裁决冲突时，总判证据不足。只有双方都明确满足拒绝区间条件才给总体事件拒绝；保留各方法原裁决，不挑较好结果。零事件bootstrap副本>1%时，该方法的事件证据同样保守记不足。
4. 方向1/2/4H评估采用entry+h之前最后5M已收盘close，距整点上界1ms，不按交易提前退出价改变。Wilder必须从2023-12-01起延续，2025不重新seed。
5. 账户层不造假设规则、不输出虚构权益曲线；`NOT_EVALUATED_UNKNOWN_METADATA`与事件层拒绝/支持分开。

## 冻结与运行

- `protocol.json`语义SHA256固定为`240e2a60cdbfc3eda09615063114cb04a2277ff9d034a5286e021cfced5e8462`，运行器拒绝变更。
- 数据层先独立通过保护/质量合成测试，再获取四币各75个明确旧期ZIP及CHECKSUM，缓存位于repo外。没有市场发现或实时接口。
- 在实现与合成测试通过并提交代码后，运行器写`pre_run_manifest.json`，记录实现Git、源码哈希、Python/numpy版本；离线读取旧期已校验缓存后运行全部既定成本/顺序。
- 独立`audit.py`对照原始旧期路径检查每个事件两臂的PnL、费用、资金费、数量、预算、镜像、触价与时界，不通过就停止而不发布结论。
- 出错不得覆盖首次目录；保留尝试及失败说明。技术修复同参数重算需新增记录，不能借修复选参。

示例命令（worktree根目录，待缓存全部完成）：

```powershell
& 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\.venv\Scripts\python.exe' -X utf8 -m research.short_trend.run --cache-root 'C:\Users\wbjun\Documents\Codex\2026-11-23\cha-j-n\work\short_trend_archive_cache' --output reports/2026-11-25/short_trend_48h_recheck/attempt_01
```

本次只读取2023-12预热、2024–2025旧期；此前审计的边界事件仍保留，不能将本次保护校验当成对过去失误的消除。
