# 验证记录

- `python -m pytest tests/test_breakout_lateness_diagnostic.py tests/test_short_horizon_entry_study.py tests/test_replay_ema_execution.py tests/test_scanner_regime.py -q`：57项通过。
- 独立回读 `events.csv`：1,107条事件、1,107个唯一 `(window, symbol, entry_ms)`；逐行布尔分类与数值阈值一致。
- 两窗事件集合、入场时间和退出状态与冻结 `taker / stop_first / all_events / C` 源文件完全一致：650 + 457条。
- 两份npz SHA256与冻结输入manifest一致；协议SHA256为 `048b79dfe7fa3983b05205370ad753a1a1b67f8c8a2230d8d776ead4ca1e7352`。
- 脚本SHA256为 `ea2ffffb77819e8371284b66ea6115a7750021489ced27d54c5cbd107d06986d`。
- 首轮合成测试曾错误抬高突破前高点，使测试事件不再满足突破定义；研究运行前已将夹具修正为只改变未来K线。该失败不产生研究结果。
- 数据库、生产配置、paper状态均未写入或修改。
