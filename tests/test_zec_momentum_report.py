from research.zec_momentum.run import monthly_bootstrap, monthly_rows, stats, timestamp, verdict


def test_cluster_bootstrap_and_metrics_use_net_results_and_initial_risk():
    t = timestamp("2025-01-03")
    trades = [dict(side="long", entry_ms=t, exit_ms=t+3600000, net_pnl_usdt=2,
                   initial_risk_usdt=1, fees_usdt=.2, funding_cost_usdt=.1,
                   exit_reason="target", ambiguous=False),
              dict(side="short", entry_ms=t+7200000, exit_ms=t+10800000, net_pnl_usdt=-1,
                   initial_risk_usdt=2, fees_usdt=.3, funding_cost_usdt=-.1,
                   exit_reason="stop", ambiguous=True)]
    months = monthly_rows(trades, timestamp("2025-01-01"), timestamp("2026-01-01"))
    result = stats(trades, [{"time_ms":t,"equity":112},{"time_ms":t+1,"equity":111}], 111, months)
    assert result["mean_net_r"] == .75
    assert result["profit_factor"] == 2
    assert result["fees_usdt"] == .5
    assert result["funding_cost_usdt"] == 0
    assert result["by_side"]["short"]["net_pnl_usdt"] == -1
    assert result["ambiguous_bars"] == 1
    assert len(months) == 12
    assert monthly_bootstrap(months) == monthly_bootstrap(months)


def test_cost_stress_failure_rejects_before_parameter_ranking():
    metrics = dict(trades=200, mean_net_r=.1, net_pnl_usdt=10,
                   by_side={"long":{"trades":100,"net_pnl_usdt":5,"mean_net_r":.1},
                            "short":{"trades":100,"net_pnl_usdt":5,"mean_net_r":.1}},
                   largest_win_usdt=1,
                   monthly_cluster_mean_r_ci95=[.01,.2])
    normal = {"metrics": metrics, "monthly": [{"net_pnl_usdt": 2}]}
    stress = {"metrics": {**metrics,"net_pnl_usdt": -2}}
    assert verdict(normal, stress)[0] == "reject"


def test_direction_conflict_and_single_trade_dependency_do_not_pass():
    metrics = dict(trades=200, mean_net_r=.1, net_pnl_usdt=10,
                   by_side={"long":{"trades":100,"net_pnl_usdt":11,"mean_net_r":.2},
                            "short":{"trades":100,"net_pnl_usdt":-1,"mean_net_r":-.02}},
                   largest_win_usdt=1, monthly_cluster_mean_r_ci95=[.01,.2])
    row = {"metrics": metrics, "monthly": [{"net_pnl_usdt":2}]}
    assert verdict(row, row)[0] == "insufficient"
    metrics["by_side"]["short"].update(net_pnl_usdt=1,mean_net_r=.01)
    metrics["largest_win_usdt"] = 10
    assert verdict(row,row)[0] == "insufficient"


def test_empty_stress_sample_cannot_pass():
    metrics = dict(trades=200, mean_net_r=.1, net_pnl_usdt=10,
                   by_side={"long":{"trades":100,"net_pnl_usdt":5,"mean_net_r":.1},
                            "short":{"trades":100,"net_pnl_usdt":5,"mean_net_r":.1}},
                   largest_win_usdt=1, monthly_cluster_mean_r_ci95=[.01,.2])
    normal = {"metrics":metrics,"monthly":[{"net_pnl_usdt":2}]}
    stress = {"metrics":{**metrics,"trades":0,"mean_net_r":None,"net_pnl_usdt":0}}
    assert verdict(normal,stress)[0] == "insufficient"
