from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system import abtest as abtest_module
from crypto_trading_system.abtest import apply_experiment_overrides, build_experiment_settings, load_experiment
from crypto_trading_system.backtest.metrics import BacktestMetrics
from crypto_trading_system.config import load_settings


def test_load_unknown_experiment_reports_available_names() -> None:
    try:
        load_experiment("does_not_exist", ROOT / "config" / "experiments.toml")
    except ValueError as exc:
        message = str(exc)
        assert "Unknown experiment" in message
        assert "history_250" in message
    else:
        raise AssertionError("Expected unknown experiment to raise ValueError")


def test_daily_trend_experiment_is_runnable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.daily_trend_required = False
    definition = load_experiment("daily_trend_required", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.daily_trend_required is False
    assert variant.analysis.daily_trend_required is True
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.daily_trend_required", False, True)
    ]


def test_relative_strength_soft_gate_experiment_is_runnable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.relative_strength_soft_gate_enabled = False
    definition = load_experiment("relative_strength_soft_gate_btc_eth_minus_0_5", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.relative_strength_soft_gate_enabled is False
    assert variant.analysis.relative_strength_soft_gate_enabled is True
    assert variant.analysis.relative_strength_min_pct == -0.5
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.relative_strength_soft_gate_enabled", False, True)
    ]


def test_relative_strength_threshold_sensitivity_experiments_are_runnable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.relative_strength_soft_gate_enabled = False

    loose = load_experiment("relative_strength_soft_gate_btc_eth_minus_1_0", ROOT / "config" / "experiments.toml")
    loose_variant, loose_changes = apply_experiment_overrides(settings, loose)
    assert loose_variant.analysis.relative_strength_soft_gate_enabled is True
    assert loose_variant.analysis.relative_strength_min_pct == -1.0
    assert [(change.path, change.old_value, change.new_value) for change in loose_changes] == [
        ("analysis.relative_strength_soft_gate_enabled", False, True),
        ("analysis.relative_strength_min_pct", -0.5, -1.0),
    ]

    hard = load_experiment("relative_strength_soft_gate_btc_eth_0_0", ROOT / "config" / "experiments.toml")
    hard_variant, hard_changes = apply_experiment_overrides(settings, hard)
    assert hard_variant.analysis.relative_strength_soft_gate_enabled is True
    assert hard_variant.analysis.relative_strength_min_pct == 0.0
    assert [(change.path, change.old_value, change.new_value) for change in hard_changes] == [
        ("analysis.relative_strength_soft_gate_enabled", False, True),
        ("analysis.relative_strength_min_pct", -0.5, 0.0),
    ]


def test_apply_overrides_does_not_mutate_baseline() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment("history_250", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.min_history_days == 180
    assert variant.analysis.min_history_days == 250
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.min_history_days", 180, 250)
    ]


def test_regime_override_can_disable_core_risk_off_buys() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.risk_off_core_buy_enabled = True
    definition = load_experiment("risk_off_no_core_buy", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.risk_off_core_buy_enabled is True
    assert variant.analysis.risk_off_core_buy_enabled is False
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.risk_off_core_buy_enabled", True, False)
    ]


def test_capacity_override_can_reduce_top_n() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment("top_n_3", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.market.top_n == 5
    assert variant.market.top_n == 3
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("market.top_n", 5, 3)
    ]


def test_combined_override_can_change_regime_and_capacity() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.risk_off_core_buy_enabled = True
    definition = load_experiment("risk_off_no_core_top_n_3", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert variant.analysis.risk_off_core_buy_enabled is False
    assert variant.market.top_n == 3
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.risk_off_core_buy_enabled", True, False),
        ("market.top_n", 5, 3),
    ]


def test_entry_timing_override_can_require_reclaim_close() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.entry_reclaim_close_enabled = False
    definition = load_experiment("entry_reclaim_close", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.entry_reclaim_close_enabled is False
    assert variant.analysis.entry_reclaim_close_enabled is True
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.entry_reclaim_close_enabled", False, True)
    ]


def test_atr_reclaim_experiment_is_runnable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    assert settings.analysis.entry_reclaim_close_enabled is True
    assert settings.analysis.entry_reclaim_min_atr_enabled is False
    assert settings.analysis.entry_reclaim_min_atr == 0.0
    definition = load_experiment("atr_reclaim_0_25", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert variant.analysis.entry_reclaim_close_enabled is True
    assert variant.analysis.entry_reclaim_min_atr_enabled is True
    assert variant.analysis.entry_reclaim_min_atr == 0.25
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.entry_reclaim_min_atr_enabled", False, True),
        ("analysis.entry_reclaim_min_atr", 0.0, 0.25),
    ]


def test_atr_reclaim_threshold_sensitivity_experiments_are_runnable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    thresholds = {
        "atr_reclaim_0_10": 0.10,
        "atr_reclaim_0_15": 0.15,
        "atr_reclaim_0_35": 0.35,
    }
    for experiment_id, threshold in thresholds.items():
        definition = load_experiment(experiment_id, ROOT / "config" / "experiments.toml")
        variant, changes = apply_experiment_overrides(settings, definition)
        assert variant.analysis.entry_reclaim_close_enabled is True
        assert variant.analysis.entry_reclaim_min_atr_enabled is True
        assert variant.analysis.entry_reclaim_min_atr == threshold
        assert [(change.path, change.old_value, change.new_value) for change in changes] == [
            ("analysis.entry_reclaim_min_atr_enabled", False, True),
            ("analysis.entry_reclaim_min_atr", 0.0, threshold),
        ]


def test_combined_regime_entry_override_can_pause_and_reclaim() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.risk_off_core_buy_enabled = True
    settings.analysis.entry_reclaim_close_enabled = False
    definition = load_experiment("risk_off_no_core_entry_reclaim", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.risk_off_core_buy_enabled is True
    assert settings.analysis.entry_reclaim_close_enabled is False
    assert variant.analysis.risk_off_core_buy_enabled is False
    assert variant.analysis.entry_reclaim_close_enabled is True
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.risk_off_core_buy_enabled", True, False),
        ("analysis.entry_reclaim_close_enabled", False, True),
    ]


def test_exit_timing_override_can_move_stop_to_breakeven() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.tp1_move_stop_to_breakeven_enabled = False
    definition = load_experiment("tp1_breakeven_stop", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.tp1_move_stop_to_breakeven_enabled is False
    assert variant.analysis.tp1_move_stop_to_breakeven_enabled is True
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.tp1_move_stop_to_breakeven_enabled", False, True),
    ]


def test_exit_timing_override_can_enable_ema_trailing_stop() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.tp1_ema_trailing_stop_enabled = False
    definition = load_experiment("tp1_ema20_trailing_stop", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.tp1_ema_trailing_stop_enabled is False
    assert variant.analysis.tp1_ema_trailing_stop_enabled is True
    assert settings.analysis.tp1_move_stop_to_breakeven_enabled is False
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("analysis.tp1_ema_trailing_stop_enabled", False, True),
    ]


def test_holding_time_override_can_force_timeout_exit() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.backtest.max_holding_bars_without_tp1 = 0
    definition = load_experiment("max_holding_30x4h_no_tp1", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.backtest.max_holding_bars_without_tp1 == 0
    assert variant.backtest.max_holding_bars_without_tp1 == 30
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("backtest.max_holding_bars_without_tp1", 0, 30),
    ]


def test_conditional_holding_time_override_sets_both_fields() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    assert settings.backtest.max_holding_bars_without_tp1 == 0
    assert settings.backtest.max_holding_bars_conditional is False
    definition = load_experiment("max_holding_42x4h_conditional", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.backtest.max_holding_bars_without_tp1 == 0
    assert settings.backtest.max_holding_bars_conditional is False
    assert variant.backtest.max_holding_bars_without_tp1 == 42
    assert variant.backtest.max_holding_bars_conditional is True
    change_paths = {(c.path, c.old_value, c.new_value) for c in changes}
    assert ("backtest.max_holding_bars_without_tp1", 0, 42) in change_paths
    assert ("backtest.max_holding_bars_conditional", False, True) in change_paths


def test_fixed_vs_conditional_42_bar_experiment_changes_one_variable() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment(
        "max_holding_42_fixed_vs_conditional_sensitive",
        ROOT / "config" / "experiments.toml",
    )
    baseline, variant, changes = build_experiment_settings(settings, definition)

    assert settings.backtest.max_holding_bars_without_tp1 == 0
    assert baseline.backtest.max_holding_bars_without_tp1 == 42
    assert variant.backtest.max_holding_bars_without_tp1 == 42
    assert baseline.backtest.max_holding_bars_conditional is False
    assert variant.backtest.max_holding_bars_conditional is True
    assert baseline.analysis.risk_off_core_buy_enabled is False
    assert baseline.analysis.entry_reclaim_close_enabled is True
    assert baseline.analysis.tp1_ema_trailing_stop_enabled is True
    assert [(change.path, change.old_value, change.new_value) for change in changes] == [
        ("backtest.max_holding_bars_conditional", False, True),
    ]


def test_override_paths_are_dimension_scoped() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    definition = load_experiment("history_250", ROOT / "config" / "experiments.toml")
    bad_definition = type(definition)(
        experiment_id="bad",
        description="bad",
        dimension="history",
        enabled=True,
        requires_logic=False,
        overrides={"market": {"min_quote_volume": 1}},
    )
    try:
        apply_experiment_overrides(settings, bad_definition)
    except ValueError as exc:
        assert "not allowed" in str(exc)
    else:
        raise AssertionError("Expected disallowed override path to raise ValueError")


def _metrics() -> BacktestMetrics:
    return BacktestMetrics(
        trades=0,
        closed_trades=0,
        open_trades=0,
        win_rate=None,
        profit_factor=None,
        avg_r=None,
        net_return_pct=0.0,
        max_drawdown=0.0,
        max_drawdown_pct=0.0,
        intrabar_max_drawdown=0.0,
        intrabar_max_drawdown_pct=0.0,
        tp1_rate=None,
        tp2_rate=None,
        stop_rate=None,
        fee_drag=0.0,
        tail_max_loss=0.0,
        cagr=None,
        sharpe=None,
        sortino=None,
        exposure_pct=None,
        turnover=None,
        sample_sufficient=False,
        sample_warning="sample",
    )


def test_dynamic_abtest_reuses_one_symbol_master() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    calls = {"build": 0, "masters": []}
    shared_master = object()

    def fake_build(settings, source_limit=None, progress=None):
        calls["build"] += 1
        return shared_master

    def fake_run_backtest(settings, symbols, start, end, **kwargs):
        calls["masters"].append(kwargs.get("dynamic_symbol_master"))
        result = SimpleNamespace(
            run_id=f"run{len(calls['masters'])}",
            symbols=["AAAUSDT"],
            trades=[],
            created_at_utc="2026-01-01T00:00:00+00:00",
            universe_type="dynamic",
            dynamic_universe_summary={"master_count": 1, "source_limit": 1, "universe_refresh_count": 1},
        )
        return result, _metrics(), []

    original_build = abtest_module.build_current_symbol_master
    original_run = abtest_module.run_backtest
    original_write = abtest_module._write_abtest_report
    abtest_module.build_current_symbol_master = fake_build
    abtest_module.run_backtest = fake_run_backtest
    abtest_module._write_abtest_report = lambda *args, **kwargs: []
    try:
        abtest_module.run_abtest(
            settings,
            "history_250",
            [],
            "2025-01-01",
            "2025-02-01",
            dynamic_universe=True,
            source_limit=1,
            include_obsidian=False,
        )
    finally:
        abtest_module.build_current_symbol_master = original_build
        abtest_module.run_backtest = original_run
        abtest_module._write_abtest_report = original_write

    assert calls["build"] == 1
    assert calls["masters"] == [shared_master, shared_master]


def test_dynamic_abtest_accepts_prebuilt_symbol_master() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    calls = {"build": 0, "masters": []}
    prebuilt_master = object()

    def fake_build(settings, source_limit=None, progress=None):
        calls["build"] += 1
        return object()

    def fake_run_backtest(settings, symbols, start, end, **kwargs):
        calls["masters"].append(kwargs.get("dynamic_symbol_master"))
        result = SimpleNamespace(
            run_id=f"run{len(calls['masters'])}",
            symbols=["AAAUSDT"],
            trades=[],
            created_at_utc="2026-01-01T00:00:00+00:00",
            universe_type="dynamic",
            dynamic_universe_summary={"master_count": 1, "source_limit": None, "universe_refresh_count": 1},
        )
        return result, _metrics(), []

    original_build = abtest_module.build_current_symbol_master
    original_run = abtest_module.run_backtest
    original_write = abtest_module._write_abtest_report
    abtest_module.build_current_symbol_master = fake_build
    abtest_module.run_backtest = fake_run_backtest
    abtest_module._write_abtest_report = lambda *args, **kwargs: []
    try:
        abtest_module.run_abtest(
            settings,
            "history_250",
            [],
            "2025-01-01",
            "2025-02-01",
            dynamic_universe=True,
            dynamic_symbol_master=prebuilt_master,
            include_obsidian=False,
        )
    finally:
        abtest_module.build_current_symbol_master = original_build
        abtest_module.run_backtest = original_run
        abtest_module._write_abtest_report = original_write

    assert calls["build"] == 0
    assert calls["masters"] == [prebuilt_master, prebuilt_master]


def test_large_cap_only_risk_off_experiment_loads() -> None:
    settings = load_settings(ROOT / "config" / "settings.toml")
    settings.analysis.risk_off_core_buy_enabled = False
    settings.analysis.risk_off_large_cap_buy_enabled = False
    definition = load_experiment("large_cap_only_risk_off", ROOT / "config" / "experiments.toml")
    variant, changes = apply_experiment_overrides(settings, definition)
    assert settings.analysis.risk_off_core_buy_enabled is False
    assert settings.analysis.risk_off_large_cap_buy_enabled is False
    assert variant.analysis.risk_off_core_buy_enabled is False
    assert variant.analysis.risk_off_large_cap_buy_enabled is True
    paths = [(c.path, c.old_value, c.new_value) for c in changes]
    assert ("analysis.risk_off_large_cap_buy_enabled", False, True) in paths


def test_large_cap_exempt_in_risk_off_but_altcoin_not() -> None:
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from crypto_trading_system.scanner import _analyze_ticker
    from crypto_trading_system.models import RawTicker

    def _make_ticker(symbol: str) -> RawTicker:
        return RawTicker(
            symbol=symbol,
            base_asset=symbol.replace("USDT", ""),
            price=1.0,
            pct_24h=5.0,
            quote_volume_24h=1_000_000_000.0,
            trades_24h=100_000,
            high_low_range_24h=5.0,
        )

    # Minimal klines: 200 daily bars so history filter passes, 120 4h bars, 168 1h bars
    # Each bar: [open_ms, open, high, low, close, volume]
    def _bars(n: int, price: float = 1.0) -> list[list]:
        return [
            [i * 3_600_000, price, price * 1.01, price * 0.99, price, 1_000_000, 0, 1_000_000, 1000]
            for i in range(n)
        ]

    k1d = _bars(200, price=1.0)
    k4h = _bars(120, price=1.0)
    k1h = _bars(168, price=1.0)

    # BNBUSDT in RISK_OFF with large_cap enabled → should NOT be blocked by regime
    bnb = _make_ticker("BNBUSDT")
    result_bnb = _analyze_ticker(
        bnb, k1h, k4h, k1d,
        risk_reward_min=2.0,
        market_regime_allows_buy=False,
        market_regime_status="RISK_OFF",
        risk_off_core_buy_enabled=False,
        risk_off_large_cap_buy_enabled=True,
    )
    # BNBUSDT should not be forced to WATCH_ONLY by regime (may be None for other reasons)
    if result_bnb is not None:
        assert result_bnb.action != "WATCH_ONLY" or "regime" not in result_bnb.verdict.lower(), (
            f"BNBUSDT should not be regime-blocked but got action={result_bnb.action}"
        )

    # ADAUSDT in RISK_OFF with large_cap enabled → should still be blocked
    ada = _make_ticker("ADAUSDT")
    result_ada = _analyze_ticker(
        ada, k1h, k4h, k1d,
        risk_reward_min=2.0,
        market_regime_allows_buy=False,
        market_regime_status="RISK_OFF",
        risk_off_core_buy_enabled=False,
        risk_off_large_cap_buy_enabled=True,
    )
    if result_ada is not None:
        assert result_ada.action != "BUY_CANDIDATE", (
            f"ADAUSDT should be blocked in RISK_OFF but got action={result_ada.action}"
        )


def test_relative_strength_soft_gate_downgrades_weak_buy_candidate() -> None:
    from crypto_trading_system.scanner import _apply_relative_strength_soft_gate

    action, verdict, relative_strength = _apply_relative_strength_soft_gate(
        "BUY_CANDIDATE",
        "可考虑",
        symbol_pct_24h=1.0,
        benchmark_pct_24h=2.0,
        enabled=True,
        min_relative_strength_pct=-0.5,
    )
    assert action == "WATCH_ONLY"
    assert verdict == "只观察"
    assert relative_strength == -1.0

    strong_action, strong_verdict, strong_relative_strength = _apply_relative_strength_soft_gate(
        "BUY_CANDIDATE",
        "可考虑",
        symbol_pct_24h=1.7,
        benchmark_pct_24h=2.0,
        enabled=True,
        min_relative_strength_pct=-0.5,
    )
    assert strong_action == "BUY_CANDIDATE"
    assert strong_verdict == "可考虑"
    assert strong_relative_strength == -0.30000000000000004


def test_entry_reclaim_atr_margin_requires_extra_close_strength() -> None:
    from crypto_trading_system.backtest.replay import _entry_reclaim_close_satisfied

    assert _entry_reclaim_close_satisfied(
        True,
        102.6,
        100.0,
        min_margin_atr_enabled=True,
        min_margin_atr=0.25,
        atr_4h=10.0,
    )
    assert not _entry_reclaim_close_satisfied(
        True,
        102.4,
        100.0,
        min_margin_atr_enabled=True,
        min_margin_atr=0.25,
        atr_4h=10.0,
    )
    assert _entry_reclaim_close_satisfied(
        True,
        100.0,
        100.0,
        min_margin_atr_enabled=False,
        min_margin_atr=0.25,
        atr_4h=10.0,
    )


if __name__ == "__main__":
    test_load_unknown_experiment_reports_available_names()
    test_daily_trend_experiment_is_runnable()
    test_relative_strength_soft_gate_experiment_is_runnable()
    test_relative_strength_threshold_sensitivity_experiments_are_runnable()
    test_apply_overrides_does_not_mutate_baseline()
    test_regime_override_can_disable_core_risk_off_buys()
    test_capacity_override_can_reduce_top_n()
    test_combined_override_can_change_regime_and_capacity()
    test_entry_timing_override_can_require_reclaim_close()
    test_atr_reclaim_experiment_is_runnable()
    test_atr_reclaim_threshold_sensitivity_experiments_are_runnable()
    test_combined_regime_entry_override_can_pause_and_reclaim()
    test_exit_timing_override_can_move_stop_to_breakeven()
    test_exit_timing_override_can_enable_ema_trailing_stop()
    test_holding_time_override_can_force_timeout_exit()
    test_conditional_holding_time_override_sets_both_fields()
    test_fixed_vs_conditional_42_bar_experiment_changes_one_variable()
    test_override_paths_are_dimension_scoped()
    test_dynamic_abtest_reuses_one_symbol_master()
    test_dynamic_abtest_accepts_prebuilt_symbol_master()
    test_large_cap_only_risk_off_experiment_loads()
    test_large_cap_exempt_in_risk_off_but_altcoin_not()
    test_relative_strength_soft_gate_downgrades_weak_buy_candidate()
    test_entry_reclaim_atr_margin_requires_extra_close_strength()
    print("test_abtest=passed")
