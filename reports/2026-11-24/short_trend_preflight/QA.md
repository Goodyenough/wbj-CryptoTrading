# 范围检查与合成验证

- 新测试：`tests/test_short_trend_preflight.py`，18项通过；不读取行情、不联网、不打开数据库。
- 覆盖：排除月份、URL字段注入、放宽cutoff、实时/生产端点、跨年OHLC及资金费时间戳、资金费原始毫秒、缺历史规则、当前快照冒充历史、局部公告冒充全区间、规则区间缺口、非有限值、错误数量范围、删空required_fields绕过。
- 局部门与账户验收分开：即使合成dated filters全覆盖，账户验收也保持false，另需margin/trigger/liquidation及完整回放验证。
- 独立数学审核确认精确含费TP、共同风险仅减量、2倍保证金加开仓费约束、资金费双顺序及65%样本/总体区别；审查发现的必需字段可删及局部filters误称账户通过问题已修复并增加回归测试。
- 运行metadata预检，结果为`data_boundary_check=PASS`、`dated_order_filter_coverage_pass=false`、`historical_account_acceptance_allowed=false`。PASS只描述该预检进程，不描述此前完整审计。
- `protocol_sha256`采用UTF-8、键排序、紧凑JSON语义序列化，避免CRLF/LF造成假变更；其他文本哈希在冻结清单中按LF规范化。
- 没有实现/运行新事件回放器，没有新增胜率/收益结果；无必要重复运行生产系统测试。
- 预检不能追溯消除本次三项数据边界失误，详情以`DATA_BOUNDARY_INCIDENTS.md`为准。

命令在`research/short_trend/README.md`，具体metadata结果在`preflight_receipt.json`。
