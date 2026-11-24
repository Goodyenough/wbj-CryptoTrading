# 短期趋势研究：审计与冻结协议

本目录包含冻结协议、metadata预检，以及独立旧期数据加载、事件镜像回放、统计和逐笔对账；不包含已认证的真实账户模拟。

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

## 2026-11-25 事件层实现

`data.py`、`engine.py`、`stats.py`、`audit.py`和`run.py`已实现；`IMPLEMENTATION_NOTES.md`记录首次策略运行前的执行澄清。先提交实施代码，再按该说明中的命令离线运行已校验缓存。运行器没有窗口、成本、目标、币池覆盖参数，固定协议语义哈希不匹配即拒绝。

研究环境使用已有Python3.12.10、numpy2.5.4；没有升级/安装依赖。验证两组命令合计117项（unittest发现76项，另41项pytest数据测试）：

```powershell
& 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\.venv\Scripts\python.exe' -X utf8 -m unittest discover -s tests -p 'test_short_trend*.py' -v
& 'D:\OneDrive - whut.edu.cn\文档\CryptoTradingPorjects\.venv\Scripts\python.exe' -X utf8 -m pytest tests/test_short_trend_data.py -q
```

全部为合成数据；测试通过不代表策略盈利。真实数据结果、数据清单、首次运行前源码哈希和逐笔对账保存到新reports目录，不覆盖原审计记录。
