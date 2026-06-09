from __future__ import annotations

from pathlib import Path
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system import abtest as abtest_module
from crypto_trading_system.abtest import apply_experiment_overrides, load_experiment
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


def test_disabled_logic_experiment_is_not_runnable() -> None:
    try:
        load_experiment("daily_trend_required", ROOT / "config" / "experiments.toml")
    except ValueError as exc:
        assert "disabled" in str(exc)
        assert "requires logic support" in str(exc)
    else:
        raise AssertionError("Expected disabled experiment to raise ValueError")


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


if __name__ == "__main__":
    test_load_unknown_experiment_reports_available_names()
    test_disabled_logic_experiment_is_not_runnable()
    test_apply_overrides_does_not_mutate_baseline()
    test_regime_override_can_disable_core_risk_off_buys()
    test_capacity_override_can_reduce_top_n()
    test_override_paths_are_dimension_scoped()
    test_dynamic_abtest_reuses_one_symbol_master()
    test_dynamic_abtest_accepts_prebuilt_symbol_master()
    print("test_abtest=passed")
