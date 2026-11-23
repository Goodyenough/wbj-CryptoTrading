# CryptoTrading 回测引擎只读审计

日期：2026-11-23（Asia/Shanghai）。仅审查源码和合成数据测试；未读取行情、数据库、data/、reports/、exports/、实验结果或 Obsidian 实验日志，未运行回测或网络取数，也未修改原仓库。

系统目标：检验 ZEC 短线顺势多空能否在交易成本后，按入场前账户净值实现单笔 1%–2% 净盈利。单一问题：现有引擎能否在严格隔离最近五个月的前提下正确模拟这一交易行为？本审计位于实验前的执行与数据边界检查阶段。

封存边界：2026-06-23 00:00 Asia/Shanghai = 2026-06-22 16:00 UTC。行情使用严格结束时间，任何被读取或取回的 K 线必须完整收盘于边界之前；禁止为了热身、指标、退出、基准、选币或最终估值读取边界之后的数据。

## 主要事实

1. **默认引擎是 4H 现货多头，不能直接复用为 USDM 多空短线引擎。** `run_backtest_replay` 明确拒绝非 4h 主周期，并拒绝 allow_leverage；行情客户端写死现货 `/api/v3/klines`。改变 base_url 仍不会改变端点。来源：[replay.py:530](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:530>)、[market_data.py:63](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/market_data.py:63>)。

2. **现有取数会跨越请求结束时刻。** `fetch_end_ms = end_ms + interval_ms(primary_interval)`，因此即使 end 指定封存边界，默认仍加载到边界之后四小时。数据缓存 SQL 按 open_time 过滤，没有 close_time < 独立封存边界条件；1D 跨界 K 线也可能被读入。来源：[replay.py:540](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:540>)、[history.py:70](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/history.py:70>)、[history.py:386](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/history.py:386>)。这是默认入口不可直接运行的决定性原因。

3. **低周期仅得到取数常量支持，尚未获得执行支持。** history 支持 5m、15m、1h；replay 只抓取 1h/4h/1d、只在 4h 执行，代码明确声明未用 5m/15m 重建路径。BacktestSettings 有 execution_interval 字段，但本 backtest 代码无执行引用。来源：[history.py:14](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/history.py:14>)、[replay.py:575](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:575>)、[replay.py:663](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:663>)、[config.py:64](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/config.py:64>)。

4. **存在可复用的收盘对齐方法，但默认成交时序有歧义。** `_closed_slice` 按 open+interval<=decision_time 截断；现有测试覆盖未收盘日线排除和边界包含。新 WATCHING 计划在本 bar 收盘之后产生；默认 legacy_same_bar 会在后续 bar 收盘确认后按该 bar 的 entry_high 成交，并可能使用同一 bar 的止盈止损，源码明确承认这是诊断假设。可选 confirmation_close 避免重用此前的高低价退出，但仍是零延迟的理想收盘成交；runner 没有暴露此选项。来源：[replay.py:200](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:200>)、[test_replay.py:59](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/tests/test_replay.py:59>)、[replay.py:456](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:456>)、[replay.py:668](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:668>)、[runner.py:572](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/runner.py:572>)。

5. **费用、权益、成交模型都按现货多头书写。** entry_fill 的买入滑点向上、stop_exit_fill 的卖出滑点向下；没有 side 参数、资金费、保证金与强平模型。账户权益=cash+quantity*mark，入场扣全部名义本金；仓位又被现金和名义比例限制。不能仅把 quantity 改成负数获得可靠空头模拟。来源：[costs.py:20](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/costs.py:20>)、[replay.py:229](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:229>)、[replay.py:425](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:425>)、[replay.py:826](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/replay.py:826>)。

6. **独立数据库、独立报告目录可以通过 Settings 注入。** OutputSettings 持有 database_path、reports_dir、obsidian_dir；所有 history 缓存使用传入数据库。tests/test_history.py 已有临时数据库示例。注意 runner 默认 include_obsidian=True，还会额外取基准和保存结果；研究入口应显式关闭 Obsidian、绕开自动基准、指定全新目录。来源：[config.py:103](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/config.py:103>)、[history.py:277](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/history.py:277>)、[test_history.py:27](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/tests/test_history.py:27>)、[runner.py:586](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/runner.py:586>)、[runner.py:604](<D:/OneDrive - whut.edu.cn/文档/CryptoTradingPorjects/src/crypto_trading_system/backtest/runner.py:604>)。

## 最小复用方案（工程判断，尚未执行）

- 不改线上策略。建立独立 research adapter，复用 interval_ms、收盘截断思路、质量检查、指标函数与通用统计；不要将默认 run_backtest 当作期货多空引擎使用。
- 固定 symbol=ZECUSDT 与 USDM 来源，禁止当前 ticker/exchangeInfo/动态选币；全新数据库给 source 明确命名 Binance_USDM，避免现货和期货同键缓存。
- 数据提供层先校验请求 end<=cutoff；请求、反序列化、入库、查询、指标输入各层都校验 candle close boundary<=cutoff，拒绝跨界日线和 end+4h 逻辑。运行前仅用合成数据验证边界拒绝行为，禁止打开共享数据库。
- 1H 已收盘指标确定方向；15M 已收盘信号，最早下一根 5M 开盘成交；5M 模拟 TP/SL，若同一 5M 同触及两者且无更细历史，采用止损优先并报告歧义数量。
- 新写方向敏感的 USDM 费用、净盈亏与风险账户模型，明确有限杠杆、可用保证金、费用、历史资金费与可能强平；不能沿用现货现金流公式。
- 账户目标按入场前 equity 的 1%–2% 反推包含双边成本的 TP；风险预算不能等同于盈利目标，止损/仓位需要独立预注册。
- 总结事实与假设分开：本报告证明默认引擎存在能力缺口，不证明策略能盈利。假设支持应来自冻结规则后未参与调参的旧历史验证集，成本后均值为正、回撤满足事先阈值；负净期望支持拒绝；样本不足、置信区间跨零或成本缺失属于证据不足。最近五个月始终不打开。

验证状态：只读静态审计；未运行现有测试，以免配置或 fixture 打开共享状态。仓库文件零改动，本文件保存在聊天 work 目录。

