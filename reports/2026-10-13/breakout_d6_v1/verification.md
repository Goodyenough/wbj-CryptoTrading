# D6 vs C20 验证记录

- 协议SHA256：`f723b5b9f07fd147473d10e4b760dda443ef8dd0f2bd190155bd6a5fc62343e1`。
- 源码运行前后指纹一致：`True`。
- C20与既有cash-fix逐笔一致记录：15389笔（跨全部分支/层次计数，允许同一事件在不同分支重复计数）。
- 两窗C20信号均从冻结4h数组独立重算，并与冻结feature标记逐事件一致。
- D6/C20均使用同一回放器、同一资格frame、同一成本和同一资金约束；未读取网络、未写业务数据库。
- 生产配置、paper状态机和业务数据库未修改。

## 窗口检查

- `2024-07-01`：eligible_frames=792，recomputed_c20_events=650，D6_events=965，C20_events=650。
- `2025-06-01`：eligible_frames=719，recomputed_c20_events=457，D6_events=671，C20_events=457。
