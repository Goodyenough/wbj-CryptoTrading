from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tomllib
from typing import Callable, Any

from .backtest.universe import build_current_symbol_master
from .backtest.metrics import BacktestMetrics
from .backtest.runner import run_backtest
from .config import PROJECT_ROOT, Settings
from .report_versions import next_report_version, versioned_markdown_filename


ALLOWED_OVERRIDE_PATHS: dict[str, set[str]] = {
    "history": {"analysis.min_history_days"},
    "pump_chase": {
        "analysis.pump_chase_24h_pct",
        "analysis.pump_chase_distance_pct",
        "analysis.pump_chase_penalty",
    },
    "liquidity": {"market.min_quote_volume", "market.min_trades"},
    "regime": {"analysis.risk_off_core_buy_enabled"},
    "capacity": {"market.top_n"},
    "combined_regime_capacity": {"analysis.risk_off_core_buy_enabled", "market.top_n"},
    "entry_timing": {"analysis.entry_reclaim_close_enabled"},
    "combined_regime_entry": {"analysis.risk_off_core_buy_enabled", "analysis.entry_reclaim_close_enabled"},
    "exit_timing": {"analysis.tp1_move_stop_to_breakeven_enabled", "analysis.tp1_ema_trailing_stop_enabled"},
}


@dataclass(frozen=True)
class ExperimentDefinition:
    experiment_id: str
    description: str
    dimension: str
    enabled: bool
    requires_logic: bool
    overrides: dict[str, Any]


@dataclass(frozen=True)
class ChangedValue:
    path: str
    old_value: object
    new_value: object


@dataclass(frozen=True)
class AbtestSummary:
    experiment_id: str
    baseline_run_id: str
    variant_run_id: str
    changed_values: list[ChangedValue]
    baseline_metrics: BacktestMetrics
    variant_metrics: BacktestMetrics
    sample_sufficient: bool
    possible_over_filtering: bool
    verdict: str
    reason: str
    time_periods_tested: list[str]
    report_paths: list[Path]


def _local_date(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _local_timestamp(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


def _project_report_dir(settings: Settings, timestamp_utc: str) -> Path:
    return settings.output.reports_dir / _local_date(timestamp_utc)


def _obsidian_report_dir(settings: Settings, timestamp_utc: str) -> Path | None:
    if settings.output.obsidian_dir is None:
        return None
    return settings.output.obsidian_dir / "Reports" / _local_date(timestamp_utc)


def _fmt(value: float | None, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if value == float("inf"):
        return "inf"
    return f"{value:,.2f}{suffix}"


def _flatten_overrides(overrides: dict[str, Any], prefix: str = "") -> list[tuple[str, object]]:
    output: list[tuple[str, object]] = []
    for key, value in overrides.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            output.extend(_flatten_overrides(value, path))
        else:
            output.append((path, value))
    return output


def _get_path(settings: Settings, path: str) -> object:
    target: object = settings
    for part in path.split("."):
        target = getattr(target, part)
    return target


def _set_path(settings: Settings, path: str, value: object) -> None:
    parts = path.split(".")
    target: object = settings
    for part in parts[:-1]:
        target = getattr(target, part)
    setattr(target, parts[-1], value)


def load_experiment(experiment_id: str, path: Path | None = None) -> ExperimentDefinition:
    path = path or PROJECT_ROOT / "config" / "experiments.toml"
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    raw = data.get(experiment_id)
    if raw is None:
        available = ", ".join(sorted(data))
        raise ValueError(f"Unknown experiment '{experiment_id}'. Available experiments: {available}")

    enabled = bool(raw.get("enabled", False))
    requires_logic = bool(raw.get("requires_logic", False))
    dimension = str(raw.get("dimension", ""))
    if not enabled:
        reason = str(raw.get("description", "Experiment is disabled."))
        if requires_logic:
            reason = f"{reason} It requires logic support before it can run."
        raise ValueError(f"Experiment '{experiment_id}' is disabled. {reason}")

    overrides = raw.get("overrides", {})
    if not isinstance(overrides, dict) or not overrides:
        raise ValueError(f"Experiment '{experiment_id}' must define non-empty overrides.")

    return ExperimentDefinition(
        experiment_id=experiment_id,
        description=str(raw.get("description", "")),
        dimension=dimension,
        enabled=enabled,
        requires_logic=requires_logic,
        overrides=overrides,
    )


def apply_experiment_overrides(settings: Settings, definition: ExperimentDefinition) -> tuple[Settings, list[ChangedValue]]:
    allowed = ALLOWED_OVERRIDE_PATHS.get(definition.dimension)
    if not allowed:
        raise ValueError(f"Experiment '{definition.experiment_id}' has unsupported dimension '{definition.dimension}'.")

    variant = deepcopy(settings)
    changes: list[ChangedValue] = []
    for path, new_value in _flatten_overrides(definition.overrides):
        if path not in allowed:
            allowed_text = ", ".join(sorted(allowed))
            raise ValueError(f"Override path '{path}' is not allowed for dimension '{definition.dimension}'. Allowed: {allowed_text}")
        old_value = _get_path(settings, path)
        _set_path(variant, path, new_value)
        changes.append(ChangedValue(path=path, old_value=old_value, new_value=new_value))
    return variant, changes


def _first_trade_created_at(result_trades: list) -> str:
    if not result_trades:
        return "n/a"
    return min(trade.created_at_utc for trade in result_trades)


def _metric_rows(baseline: BacktestMetrics, variant: BacktestMetrics) -> list[tuple[str, str, str, str]]:
    specs = [
        ("closed_trades", baseline.closed_trades, variant.closed_trades, ""),
        ("stop_rate", baseline.stop_rate, variant.stop_rate, "%"),
        ("profit_factor", baseline.profit_factor, variant.profit_factor, ""),
        ("avg_r", baseline.avg_r, variant.avg_r, ""),
        ("max_drawdown_pct", baseline.max_drawdown_pct, variant.max_drawdown_pct, "%"),
        ("net_return_pct", baseline.net_return_pct, variant.net_return_pct, "%"),
        ("sharpe", baseline.sharpe, variant.sharpe, ""),
    ]
    rows: list[tuple[str, str, str, str]] = []
    for name, base_value, variant_value, suffix in specs:
        delta = None
        if isinstance(base_value, (int, float)) and isinstance(variant_value, (int, float)):
            delta = variant_value - base_value
        rows.append((name, _fmt(base_value, suffix), _fmt(variant_value, suffix), _fmt(delta, suffix)))
    return rows


def _verdict_and_reason(baseline: BacktestMetrics, variant: BacktestMetrics, possible_over_filtering: bool) -> tuple[str, str]:
    if not variant.sample_sufficient:
        return "retest", "Variant closed_trades is below 20, so the sample is insufficient for a keep decision."
    if possible_over_filtering:
        return "retest", "Variant trade count fell by more than 50%, so it may be over-filtering."
    if variant.net_return_pct < baseline.net_return_pct and variant.max_drawdown_pct >= baseline.max_drawdown_pct:
        return "reject_candidate", "Variant return is worse and max drawdown did not improve."
    return "retest", "Automatic report does not assign keep; review across additional time periods before adopting."


def _render_abtest_report(
    settings: Settings,
    definition: ExperimentDefinition,
    changes: list[ChangedValue],
    baseline_result,
    baseline_metrics: BacktestMetrics,
    variant_result,
    variant_metrics: BacktestMetrics,
    report_version: str,
    verdict: str,
    reason: str,
    possible_over_filtering: bool,
    start: str,
    end: str,
) -> str:
    created_at = variant_result.created_at_utc
    changed_param = ", ".join(change.path for change in changes)
    old_value = ", ".join(str(change.old_value) for change in changes)
    new_value = ", ".join(str(change.new_value) for change in changes)
    sample_sufficient = baseline_metrics.sample_sufficient and variant_metrics.sample_sufficient

    lines = [
        "---",
        f"created: {_local_timestamp(created_at)}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - abtest",
        f"experiment_id: {definition.experiment_id}",
        f"baseline_run_id: {baseline_result.run_id}",
        f"variant_run_id: {variant_result.run_id}",
        f"changed_param: {changed_param}",
        f"old_value: {old_value}",
        f"new_value: {new_value}",
        f"sample_sufficient: {str(sample_sufficient).lower()}",
        f"universe_mode: {getattr(baseline_result, 'universe_type', 'manual')}",
        f"verdict: {verdict}",
        f"report_version: {report_version}",
        "---",
        "",
        f"# A/B 实验报告 {definition.experiment_id} {report_version}",
        "",
        f"- experiment_id: `{definition.experiment_id}`",
        f"- description: {definition.description}",
        f"- baseline_run_id: `{baseline_result.run_id}`",
        f"- variant_run_id: `{variant_result.run_id}`",
        f"- symbols: {', '.join(f'`{symbol}`' for symbol in baseline_result.symbols)}",
        f"- universe_mode: {getattr(baseline_result, 'universe_type', 'manual')}",
        f"- time_periods_tested: `{start}` -> `{end}`",
        f"- changed_param: `{changed_param}`",
        f"- old_value: `{old_value}`",
        f"- new_value: `{new_value}`",
        f"- sample_sufficient: {str(sample_sufficient).lower()}",
        f"- possible_over_filtering: {str(possible_over_filtering).lower()}",
        f"- verdict: `{verdict}`",
        f"- reason: {reason}",
        "",
        *(
            [
                "## Dynamic Universe Metadata",
                "",
                f"- baseline_master_count: {baseline_result.dynamic_universe_summary.get('master_count', 'n/a')}",
                f"- variant_master_count: {variant_result.dynamic_universe_summary.get('master_count', 'n/a')}",
                f"- baseline_source_limit: {baseline_result.dynamic_universe_summary.get('source_limit', 'none')}",
                f"- variant_source_limit: {variant_result.dynamic_universe_summary.get('source_limit', 'none')}",
                (
                    "- shared_master_expected: true "
                    "(A/B runner builds the dynamic symbol master once before baseline and variant.)"
                ),
                f"- baseline_universe_refreshes: {baseline_result.dynamic_universe_summary.get('universe_refresh_count', 0)}",
                f"- variant_universe_refreshes: {variant_result.dynamic_universe_summary.get('universe_refresh_count', 0)}",
                "",
            ]
            if getattr(baseline_result, "universe_type", "manual") == "dynamic"
            and baseline_result.dynamic_universe_summary
            and variant_result.dynamic_universe_summary
            else []
        ),
        "## 指标对比",
        "",
        "| Metric | Baseline | Variant | Delta |",
        "|---|---:|---:|---:|",
    ]
    for name, base_value, variant_value, delta in _metric_rows(baseline_metrics, variant_metrics):
        lines.append(f"| {name} | {base_value} | {variant_value} | {delta} |")

    lines.extend(
        [
            f"| first_trade_created_at | { _first_trade_created_at(baseline_result.trades) } | { _first_trade_created_at(variant_result.trades) } | n/a |",
            "",
            "## 样本规则",
            "",
            "- closed_trades < 20 时，默认 verdict 为 `retest`。",
            "- 交易数下降超过 50% 时，标记 possible_over_filtering=true。",
            "- 自动报告不会直接写 `keep`；采用默认策略前需要跨时段复测和人工复盘。",
            "",
            "## 变更明细",
            "",
            "| changed_param | old_value | new_value |",
            "|---|---:|---:|",
        ]
    )
    for change in changes:
        lines.append(f"| `{change.path}` | `{change.old_value}` | `{change.new_value}` |")

    lines.extend(
        [
            "",
            "## Raw Metrics",
            "",
            "```json",
            json.dumps(
                {
                    "baseline": asdict(baseline_metrics),
                    "variant": asdict(variant_metrics),
                },
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def _write_abtest_report(
    settings: Settings,
    definition: ExperimentDefinition,
    changes: list[ChangedValue],
    baseline_result,
    baseline_metrics: BacktestMetrics,
    variant_result,
    variant_metrics: BacktestMetrics,
    include_obsidian: bool,
    verdict: str,
    reason: str,
    possible_over_filtering: bool,
    start: str,
    end: str,
) -> list[Path]:
    target_dirs = [_project_report_dir(settings, variant_result.created_at_utc)]
    obsidian_dir = _obsidian_report_dir(settings, variant_result.created_at_utc)
    if include_obsidian and obsidian_dir is not None:
        target_dirs.append(obsidian_dir)

    mode = "dynamic_universe" if getattr(baseline_result, "universe_type", "manual") == "dynamic" else "symbols"
    prefix = f"abtest_{mode}_{definition.experiment_id}_{start}_{end}"
    version_number = next_report_version(target_dirs, prefix)
    version = f"v{version_number}"
    filename = versioned_markdown_filename(prefix, version_number)
    markdown = _render_abtest_report(
        settings,
        definition,
        changes,
        baseline_result,
        baseline_metrics,
        variant_result,
        variant_metrics,
        version,
        verdict,
        reason,
        possible_over_filtering,
        start,
        end,
    )
    paths: list[Path] = []
    for directory in target_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(markdown, encoding="utf-8")
        paths.append(path)
    return paths


def run_abtest(
    settings: Settings,
    experiment_id: str,
    symbols: list[str],
    start: str,
    end: str,
    *,
    experiments_path: Path | None = None,
    interval: str | None = None,
    intrabar: str | None = None,
    allow_data_gaps: bool = False,
    dynamic_universe: bool = False,
    max_universe_symbols: int | None = None,
    source_limit: int | None = None,
    dynamic_symbol_master=None,
    include_obsidian: bool = True,
    progress: Callable[[str], None] | None = None,
) -> AbtestSummary:
    definition = load_experiment(experiment_id, experiments_path)
    baseline_settings = deepcopy(settings)
    variant_settings, changes = apply_experiment_overrides(settings, definition)
    if dynamic_universe:
        if dynamic_symbol_master is None and progress is not None:
            progress("building shared dynamic universe symbol master for A/B")
        if dynamic_symbol_master is None:
            dynamic_symbol_master = build_current_symbol_master(
                baseline_settings,
                source_limit=source_limit,
                progress=progress,
            )

    if progress is not None:
        progress(f"running baseline backtest for {experiment_id}")
    baseline_result, baseline_metrics, _ = run_backtest(
        baseline_settings,
        symbols,
        start,
        end,
        interval=interval,
        intrabar=intrabar,
        allow_data_gaps=allow_data_gaps,
        dynamic_universe_mode=dynamic_universe,
        max_universe_symbols=max_universe_symbols,
        source_limit=source_limit,
        dynamic_symbol_master=dynamic_symbol_master,
        include_obsidian=include_obsidian,
        progress=progress,
    )

    if progress is not None:
        progress(f"running variant backtest for {experiment_id}")
    variant_result, variant_metrics, _ = run_backtest(
        variant_settings,
        symbols,
        start,
        end,
        interval=interval,
        intrabar=intrabar,
        allow_data_gaps=allow_data_gaps,
        dynamic_universe_mode=dynamic_universe,
        max_universe_symbols=max_universe_symbols,
        source_limit=source_limit,
        dynamic_symbol_master=dynamic_symbol_master,
        include_obsidian=include_obsidian,
        progress=progress,
    )

    possible_over_filtering = (
        baseline_metrics.trades > 0
        and variant_metrics.trades < baseline_metrics.trades * 0.5
    )
    verdict, reason = _verdict_and_reason(baseline_metrics, variant_metrics, possible_over_filtering)
    report_paths = _write_abtest_report(
        settings,
        definition,
        changes,
        baseline_result,
        baseline_metrics,
        variant_result,
        variant_metrics,
        include_obsidian,
        verdict,
        reason,
        possible_over_filtering,
        start,
        end,
    )
    return AbtestSummary(
        experiment_id=definition.experiment_id,
        baseline_run_id=baseline_result.run_id,
        variant_run_id=variant_result.run_id,
        changed_values=changes,
        baseline_metrics=baseline_metrics,
        variant_metrics=variant_metrics,
        sample_sufficient=baseline_metrics.sample_sufficient and variant_metrics.sample_sufficient,
        possible_over_filtering=possible_over_filtering,
        verdict=verdict,
        reason=reason,
        time_periods_tested=[f"{start}->{end}"],
        report_paths=report_paths,
    )
