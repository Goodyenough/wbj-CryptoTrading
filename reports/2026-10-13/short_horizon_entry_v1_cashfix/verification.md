# 最终验证记录

- 51项测试通过：`python -m pytest tests/test_short_horizon_entry_study.py tests/test_replay_ema_execution.py tests/test_scanner_regime.py -q`。
- 两窗各50个真实共同合格时点，共100次快速/完整scanner一致性检查通过。
- `python scripts/audit_short_horizon_entries.py --cash-fix`：32,713条导出记录逐笔及独立账户对账通过；最大误差 `1.000444171950221e-11 USDT`。
- 首次/现金纠错版24个 `all_events / symbol_only` 逐笔gzip解压内容逐字节相同。
- 主账户收益不变：早B/C `-35.9029674411 / -34.1794576042%`；近B/C `-12.3540580009 / -32.1832269870%`。早C计数337→336、近B229→228。
- 全部分支0缺口删失/0期末删失，主结果0细周期回退；主C早4/近2个1h双触事件保留两种顺序。
- 全压力分支仍有20条重复计入的非零小额订单记录低于10 USDT，其中主结果4笔；无<=1e-8 USDT虚假仓位。没有将10 USDT当作真实历史最小订单。
- 原生产配置SHA256：`be7ec39ec21f6a838571511cb2cd0e290263031b521a9a07a6fb70164b8ef4bf`。协议SHA256：`9a03a08a50822379086922bc245c38af82c1f98197f1c14f3a16fdc51ddc709a`。
- 原始数据仅只读导出、生产配置未修改；用户既有 `scripts/run_logged_paper_task.ps1` 修改保留，不纳入提交。
- 一次验证命令曾引用不存在的 `tests/test_market_regime.py`，未执行任何测试；随后定位真实 `tests/test_scanner_regime.py`，上述51项为实际成功结果。
- Git归档复核：限定本轮冻结报告为原字节存储，并重新暂存以消除此前自动换行转换；113份冻结报告暂存内容与本地原始字节一致，协议、两窗输入、输入manifest和最终9份执行源码/配置的暂存SHA256闭合。未更改冻结指纹或回测数值。
