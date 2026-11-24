# 短期趋势研究：审计与冻结协议

本目录当前只有机器协议和metadata预检，不包含新行情加载器或策略回放引擎。

- `PROTOCOL.md`：信号、Wilder ATR、共同风险、精确净目标、顺序敏感性、分年边界与验收。
- `protocol.json`：固定机器参数，主池BTC/ETH/SOL，ZEC仅探索。
- `preflight.py`：不联网、不读市场行或数据库；只读取指定协议/审计JSON，拒绝越界归档请求，缺历史规则时阻止历史账户验收。

```powershell
& 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\.venv\Scripts\python.exe' -X utf8 -m research.short_trend.preflight --evidence reports/2026-11-24/short_trend_preflight/historical_execution_evidence.json --output reports/2026-11-24/short_trend_preflight/preflight_receipt.json
& 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\.venv\Scripts\python.exe' -X utf8 -m unittest discover -s tests -p test_short_trend_preflight.py -v
```

在研究worktree根目录执行。预检进程成功退出仅代表检查完成；是否通过历史规则门看JSON字段，不能用退出码0宣称策略/账户通过。

历史审计附件位于`reports/2026-11-24/short_trend_preflight/`。2023–2025已用，不能作为新独立验证；2021/2022使用历史不明。后续整个2026年继续排除；已发生的摘要暴露与完整载入跨2026冻结JSON的失误详见`DATA_BOUNDARY_INCIDENTS.md`，不能声称零信息暴露。

`dated_order_filter_coverage_pass`仅是基本filters区间覆盖门；即便该局部门通过，`historical_account_acceptance_allowed`仍为false，直至另外完成保证金/触发/强平及完整回放验证。当前缺基本filters，所以两项均为false。

真正运行前必须按冻结协议实现事件层并做因果/执行合成测试；不得直接把旧ZEC回放的简单平均ATR和1倍名义规则当新引擎。历史真实账户高胜率验收继续受元数据缺口限制；连续数量事件结果只能回答条件方向问题。
