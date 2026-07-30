from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path

from .backtest.history import fetch_klines_cached
from .config import Settings
from .paper_audit import (
    OpportunityRow,
    _fmt,
    _iso_z,
    _local_now,
    _local_timestamp,
    _ms,
    _parse_window,
    _pct,
    build_reclaim_opportunities,
    build_scan_candidate_opportunities,
)
from .paper_shadow_replay import (
    _benchmark_return_pct,
    _entry_reclaim_confirm_1bar_row,
    _fetch_closed_4h_path,
    _kline_time,
    _relative_strength_gate_row,
)
from .report_versions import next_report_version, versioned_markdown_filename


EXPERIMENTS = {
    "atr_reclaim_incumbent_shadow",
    "reclaim_quality_matrix",
    "momentum_pullback_definition_ab",
    "relative_strength_soft_gate",
}


@dataclass(frozen=True)
class OpportunitySet:
    account: str
    start_date: str
    end_date: str
    rows: list[OpportunityRow]
    hash: str


@dataclass(frozen=True)
class ExperimentDecisionRow:
    experiment: str
    variant: str
    symbol: str
    opportunity_key: str
    source: str
    first_time: str
    market_regime: str
    accepted: bool
    outcome: str
    pnl_r: float | None
    mfe_r: float | None
    mae_r: float | None
    reason: str
    reclaim_margin_atr: float | None = None
    capacity_state: str = "not_available_in_offline_opportunity_set"
    active_positions: int | None = None
    direct_filter_contribution_r: float | None = None
    path_capacity_contribution_r: float | None = None


def _opportunity_dict(row: OpportunityRow) -> dict[str, object]:
    data = asdict(row)
    return {key: data[key] for key in sorted(data)}


def build_opportunity_set(settings: Settings, account: str, start_date: str, end_date: str) -> OpportunitySet:
    rows = build_reclaim_opportunities(settings, account, start_date, end_date)
    rows += build_scan_candidate_opportunities(settings, start_date, end_date)
    seen: set[str] = set()
    deduped: list[OpportunityRow] = []
    for row in rows:
        key = row.opportunity_set_key or f"{row.source}:{row.plan_id}"
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)
    payload = json.dumps([_opportunity_dict(row) for row in deduped], ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
    return OpportunitySet(account=account, start_date=start_date, end_date=end_date, rows=deduped, hash=digest)


def _outcome_from_opportunity(row: OpportunityRow, accepted: bool) -> tuple[str, float | None]:
    if accepted:
        if row.first_hit == "stop_first":
            return "accepted_loser", -1.0
        if row.first_hit in {"near_tp1_first", "tp1_first"}:
            return "accepted_winner_path", row.counterfactual_pnl_r or row.mfe_r
        if row.maturity_status == "right_censored":
            return "accepted_right_censored", None
        return "accepted_neutral", None
    if row.first_hit == "stop_first":
        return "filtered_loser", 1.0
    if row.first_hit in {"near_tp1_first", "tp1_first"}:
        value = row.counterfactual_pnl_r or row.mfe_r
        return "missed_winner", None if value is None else -abs(value)
    if row.maturity_status == "right_censored":
        return "filtered_right_censored", None
    return "filtered_neutral", None


def _decision(
    *,
    experiment: str,
    variant: str,
    row: OpportunityRow,
    accepted: bool,
    reason: str,
) -> ExperimentDecisionRow:
    outcome, pnl_r = _outcome_from_opportunity(row, accepted)
    direct_filter_contribution_r = None
    if variant == "atr_reclaim_0_35_shadow" and not accepted:
        direct_filter_contribution_r = pnl_r
    return ExperimentDecisionRow(
        experiment=experiment,
        variant=variant,
        symbol=row.symbol,
        opportunity_key=row.opportunity_set_key or f"{row.source}:{row.plan_id}",
        source=row.source,
        first_time=row.first_time,
        market_regime=row.market_regime,
        accepted=accepted,
        outcome=outcome,
        pnl_r=pnl_r,
        mfe_r=row.mfe_r,
        mae_r=row.mae_r,
        reason=reason,
        reclaim_margin_atr=row.reclaim_margin_atr,
        direct_filter_contribution_r=direct_filter_contribution_r,
    )


def _passes_reclaim_variant(settings: Settings, row: OpportunityRow, end_utc: datetime, variant: str) -> tuple[bool, str]:
    if row.entry is None:
        return False, "missing entry_high"
    if variant == "current_4h_close_reclaim":
        replay = _entry_reclaim_confirm_1bar_row(settings, row, end_utc)
        return replay.baseline_entry_time is not None, "first 4h close >= entry_high"
    if variant == "confirm_1bar":
        replay = _entry_reclaim_confirm_1bar_row(settings, row, end_utc)
        return replay.variant_entry_time is not None, "next 4h candle confirms close >= entry_high and low > stop"
    path = _fetch_closed_4h_path(settings, row.symbol, row.first_time, end_utc)
    if not path:
        return False, "missing 4h path"
    atr = row.atr_4h
    for kline in path:
        open_ = float(kline[1])
        high = float(kline[2])
        low = float(kline[3])
        close = float(kline[4])
        body = abs(close - open_)
        candle_range = max(high - low, 0.0)
        if variant == "atr_reclaim_0_25":
            if atr is not None and atr > 0 and close >= row.entry + 0.25 * atr:
                return True, "close >= entry_high + 0.25 ATR"
        elif variant == "atr_reclaim_0_35_shadow":
            if atr is not None and atr > 0 and close >= row.entry + 0.35 * atr:
                return True, "close >= entry_high + 0.35 ATR"
        elif variant == "quality_close":
            strong_body = candle_range > 0 and body / candle_range >= 0.35
            upper_close = candle_range > 0 and (high - close) / candle_range <= 0.35
            if close >= row.entry and strong_body and upper_close:
                return True, "close reclaimed with body >= 35% range and close in upper 65%"
    return False, f"{variant} condition not met"


def run_reclaim_quality_matrix(settings: Settings, opportunity_set: OpportunitySet) -> list[ExperimentDecisionRow]:
    _start_utc, end_utc = _parse_window(opportunity_set.start_date, opportunity_set.end_date)
    output: list[ExperimentDecisionRow] = []
    variants = ["current_4h_close_reclaim", "confirm_1bar", "atr_reclaim_0_25", "quality_close"]
    for row in opportunity_set.rows:
        for variant in variants:
            try:
                accepted, reason = _passes_reclaim_variant(settings, row, end_utc, variant)
            except Exception as exc:  # noqa: BLE001 - report the data gap per row.
                accepted, reason = False, f"data_gap: {exc}"
            output.append(_decision(experiment="reclaim_quality_matrix", variant=variant, row=row, accepted=accepted, reason=reason))
    return output


def run_atr_reclaim_incumbent_shadow(settings: Settings, opportunity_set: OpportunitySet) -> list[ExperimentDecisionRow]:
    _start_utc, end_utc = _parse_window(opportunity_set.start_date, opportunity_set.end_date)
    output: list[ExperimentDecisionRow] = []
    variants = [
        "reference_baseline",
        "atr_reclaim_0_35_shadow",
        "research_incumbent",
    ]
    for row in opportunity_set.rows:
        for variant in variants:
            try:
                if variant == "reference_baseline":
                    accepted, reason = _passes_reclaim_variant(settings, row, end_utc, "current_4h_close_reclaim")
                    reason = f"reference baseline: {reason}"
                else:
                    accepted, reason = _passes_reclaim_variant(settings, row, end_utc, "atr_reclaim_0_35_shadow")
                    reason = f"{variant}: {reason}"
            except Exception as exc:  # noqa: BLE001 - report the data gap per row.
                accepted, reason = False, f"data_gap: {exc}"
            output.append(_decision(experiment="atr_reclaim_incumbent_shadow", variant=variant, row=row, accepted=accepted, reason=reason))
    return output


def _passes_momentum_variant(row: OpportunityRow, variant: str) -> tuple[bool, str]:
    pct_24h = row.pct_24h
    pct_7d = row.pct_7d
    if variant == "current_24h_7d_positive":
        return bool(pct_24h is not None and pct_7d is not None and pct_24h > 0 and pct_7d > 0), "pct_24h > 0 and pct_7d > 0"
    if variant == "allow_minor_24h_pullback":
        return bool(pct_24h is not None and pct_7d is not None and pct_24h >= -2.0 and pct_7d > 0), "pct_24h >= -2 and pct_7d > 0"
    if variant == "recent_high_atr_pullback":
        value = row.pullback_from_recent_high_atr
        return bool(value is not None and 0.25 <= value <= 2.5), "recent high pullback is 0.25-2.5 ATR"
    if variant == "trend_support_atr_pullback":
        return bool(
            pct_7d is not None
            and pct_7d > 0
            and row.distance_to_support_atr is not None
            and row.distance_to_support_atr <= 1.5
            and row.stop_distance_atr is not None
            and 0.5 <= row.stop_distance_atr <= 4.0
        ), "pct_7d > 0, distance_to_support <= 1.5 ATR, stop_distance 0.5-4 ATR"
    return False, "unknown variant"


def run_momentum_pullback_definition_ab(opportunity_set: OpportunitySet) -> list[ExperimentDecisionRow]:
    output: list[ExperimentDecisionRow] = []
    variants = [
        "current_24h_7d_positive",
        "allow_minor_24h_pullback",
        "recent_high_atr_pullback",
        "trend_support_atr_pullback",
    ]
    for row in opportunity_set.rows:
        for variant in variants:
            accepted, reason = _passes_momentum_variant(row, variant)
            output.append(_decision(experiment="momentum_pullback_definition_ab", variant=variant, row=row, accepted=accepted, reason=reason))
    return output


def _alt_benchmark_return_pct(settings: Settings, start_time: str, end_utc: datetime, bars: int) -> float | None:
    values: list[float] = []
    for symbol in ("BNBUSDT", "SOLUSDT", "XRPUSDT", "ADAUSDT"):
        try:
            path = _fetch_closed_4h_path(settings, symbol, start_time, end_utc)
        except Exception:
            continue
        if len(path) < 2:
            continue
        end_index = min(bars, len(path) - 1)
        start = float(path[0][4])
        end = float(path[end_index][4])
        if start > 0:
            values.append((end / start - 1.0) * 100.0)
    return None if not values else sum(values) / len(values)


def _relative_strength_value(settings: Settings, row: OpportunityRow, end_utc: datetime, benchmark: str) -> float | None:
    bars = 6
    try:
        path = _fetch_closed_4h_path(settings, row.symbol, row.first_time, end_utc)
    except Exception:
        return None
    if len(path) < 2:
        return None
    end_index = min(bars, len(path) - 1)
    start = float(path[0][4])
    end = float(path[end_index][4])
    if start <= 0:
        return None
    symbol_return = (end / start - 1.0) * 100.0
    if benchmark == "btc_eth":
        benchmark_return = _benchmark_return_pct(settings, row.first_time, end_utc, bars)
    elif benchmark == "alt_equal":
        benchmark_return = _alt_benchmark_return_pct(settings, row.first_time, end_utc, bars)
    else:
        benchmark_return = None
    if benchmark_return is None:
        return None
    return symbol_return - benchmark_return


def run_relative_strength_soft_gate(settings: Settings, opportunity_set: OpportunitySet) -> list[ExperimentDecisionRow]:
    _start_utc, end_utc = _parse_window(opportunity_set.start_date, opportunity_set.end_date)
    output: list[ExperimentDecisionRow] = []
    variants = [
        ("btc_eth_hard_0", "btc_eth", 0.0, "all"),
        ("btc_eth_soft_minus_0_5", "btc_eth", -0.5, "all"),
        ("risk_off_hard_0", "btc_eth", 0.0, "risk_off_only"),
        ("alt_equal_hard_0", "alt_equal", 0.0, "all"),
    ]
    for row in opportunity_set.rows:
        for variant, benchmark, threshold, scope in variants:
            rs = _relative_strength_value(settings, row, end_utc, benchmark)
            if rs is None:
                accepted = False
                reason = f"{benchmark} relative strength unavailable"
            elif scope == "risk_off_only" and row.market_regime.upper() != "RISK_OFF":
                accepted = True
                reason = f"non-RISK_OFF kept; RS={rs:.2f}%"
            else:
                accepted = rs >= threshold
                reason = f"{benchmark} RS {rs:.2f}% >= {threshold:.2f}%"
            output.append(_decision(experiment="relative_strength_soft_gate", variant=variant, row=row, accepted=accepted, reason=reason))
    return output


def _experiment_rows(settings: Settings, opportunity_set: OpportunitySet, experiment: str) -> list[ExperimentDecisionRow]:
    if experiment == "atr_reclaim_incumbent_shadow":
        return run_atr_reclaim_incumbent_shadow(settings, opportunity_set)
    if experiment == "reclaim_quality_matrix":
        return run_reclaim_quality_matrix(settings, opportunity_set)
    if experiment == "momentum_pullback_definition_ab":
        return run_momentum_pullback_definition_ab(opportunity_set)
    if experiment == "relative_strength_soft_gate":
        return run_relative_strength_soft_gate(settings, opportunity_set)
    raise ValueError(f"unsupported shadow experiment: {experiment}")


def _variant_summary(rows: list[ExperimentDecisionRow]) -> list[dict[str, object]]:
    grouped: dict[str, list[ExperimentDecisionRow]] = defaultdict(list)
    for row in rows:
        grouped[row.variant].append(row)
    output: list[dict[str, object]] = []
    for variant, items in sorted(grouped.items()):
        accepted = [row for row in items if row.accepted]
        filtered = [row for row in items if not row.accepted]
        outcomes = Counter(row.outcome for row in items)
        pnl_values = [row.pnl_r for row in items if row.pnl_r is not None]
        direct_filter_values = [row.direct_filter_contribution_r for row in items if row.direct_filter_contribution_r is not None]
        output.append(
            {
                "variant": variant,
                "opportunities": len(items),
                "accepted": len(accepted),
                "filtered": len(filtered),
                "accepted_loser": outcomes.get("accepted_loser", 0),
                "accepted_winner_path": outcomes.get("accepted_winner_path", 0),
                "filtered_loser": outcomes.get("filtered_loser", 0),
                "missed_winner": outcomes.get("missed_winner", 0),
                "total_decision_R": None if not pnl_values else sum(pnl_values),
                "direct_filter_R": None if not direct_filter_values else sum(direct_filter_values),
                "outcomes": dict(outcomes),
            }
        )
    return output


def _verdict(summary: list[dict[str, object]]) -> str:
    usable = [row for row in summary if int(row["opportunities"]) >= 20]
    if not usable:
        return "sample_insufficient"
    return "retest"


def render_shadow_experiment_report(
    *,
    account: str,
    start_date: str,
    end_date: str,
    experiment: str,
    report_version: int,
    opportunity_set: OpportunitySet,
    rows: list[ExperimentDecisionRow],
    opportunity_set_path: Path,
) -> str:
    now = _local_now()
    summary = _variant_summary(rows)
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - shadow-experiment",
        f"account: {account}",
        f"start_date: {start_date}",
        f"end_date: {end_date}",
        f"experiment: {experiment}",
        f"report_version: v{report_version}",
        f"opportunity_set_hash: {opportunity_set.hash}",
        "---",
        "",
        f"# Paper Shadow Experiment {experiment} {start_date} -> {end_date} {account} v{report_version}",
        "",
        "This is an offline diagnostic experiment. It uses a fixed opportunity set and does not modify settings, plans, events, snapshots, or paper state.",
        "",
    ]
    if experiment == "atr_reclaim_incumbent_shadow":
        lines.extend([
            "## Incumbent Framework",
            "",
            "| Line | Definition | Controls paper? | Purpose |",
            "|---|---|---|---|",
            "| reference_baseline | Original strategy without `atr_reclaim_0_35` | no | Long-term calibration reference. |",
            "| atr_reclaim_0_35_shadow | Original strategy plus frozen `0.35 ATR` reclaim requirement | no | Independent forward comparison line. |",
            "| research_incumbent | Same decision rule as `atr_reclaim_0_35_shadow` for this MVP | no | Current research reference for future challengers. |",
            "",
            "Capacity/path fields are explicit placeholders in this offline MVP. They require live decision-state logging before they can be treated as complete path attribution.",
            "",
        ])
    lines.extend([
        "## Decision",
        "",
        f"- verdict: {_verdict(summary)}",
        f"- opportunity_set_hash: {opportunity_set.hash}",
        f"- opportunity_set_path: `{opportunity_set_path}`",
        "- config_action: do_not_modify_settings_toml",
        "",
        "## Variant Summary",
        "",
        "| Variant | Opportunities | Accepted | Filtered | Accepted Loser | Accepted Winner Path | Filtered Loser | Missed Winner | Total Decision R | Direct Filter R |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for item in summary:
        lines.append(
            f"| {item['variant']} | {item['opportunities']} | {item['accepted']} | {item['filtered']} | "
            f"{item['accepted_loser']} | {item['accepted_winner_path']} | {item['filtered_loser']} | "
            f"{item['missed_winner']} | {_fmt(item['total_decision_R'], 2)} | {_fmt(item['direct_filter_R'], 2)} |"
        )
    lines.extend([
        "",
        "## Outcome Counts",
        "",
    ])
    for item in summary:
        lines.extend([
            f"### {item['variant']}",
            "",
            "| Outcome | Count |",
            "|---|---:|",
        ])
        outcomes = item["outcomes"]
        if isinstance(outcomes, dict) and outcomes:
            for label, count in sorted(outcomes.items()):
                lines.append(f"| {label} | {count} |")
        else:
            lines.append("| n/a | 0 |")
        lines.append("")
    lines.extend([
        "## Detail Rows",
        "",
        "| Variant | Source | Symbol | Time | Regime | Accepted | Outcome | PnL_R | MFE_R | MAE_R | Reclaim Margin ATR | Capacity State | Active Positions | Direct Filter R | Path/Capacity R | Reason |",
        "|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|---:|---:|---|",
    ])
    for row in rows:
        lines.append(
            f"| {row.variant} | {row.source} | `{row.symbol}` | {_local_timestamp(row.first_time)} | "
            f"{row.market_regime} | {str(row.accepted).lower()} | {row.outcome} | {_fmt(row.pnl_r, 2)} | "
            f"{_fmt(row.mfe_r, 2)} | {_fmt(row.mae_r, 2)} | {_fmt(row.reclaim_margin_atr, 2)} | "
            f"{row.capacity_state} | {_fmt(row.active_positions, 0)} | {_fmt(row.direct_filter_contribution_r, 2)} | "
            f"{_fmt(row.path_capacity_contribution_r, 2)} | {row.reason} |"
        )
    lines.extend([
        "",
        "## Raw Summary",
        "",
        "```json",
        json.dumps(
            {
                "experiment": experiment,
                "opportunity_set_hash": opportunity_set.hash,
                "opportunities": len(opportunity_set.rows),
                "summary": summary,
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
    ])
    return "\n".join(lines) + "\n"


def write_shadow_experiment_report(
    settings: Settings,
    *,
    account_name: str | None,
    start_date: str,
    end_date: str,
    experiment: str,
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    opportunity_set = build_opportunity_set(settings, account, start_date, end_date)
    rows = _experiment_rows(settings, opportunity_set, experiment)
    now = _local_now()
    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    prefix = f"paper_shadow_experiment_{experiment}_{start_date}_{end_date}_{account}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    set_filename = versioned_markdown_filename(f"paper_shadow_opportunity_set_{start_date}_{end_date}_{account}_{opportunity_set.hash}", version).replace(".md", ".json")
    paths: list[Path] = []
    opportunity_set_path = report_dir / set_filename
    text = render_shadow_experiment_report(
        account=account,
        start_date=start_date,
        end_date=end_date,
        experiment=experiment,
        report_version=version,
        opportunity_set=opportunity_set,
        rows=rows,
        opportunity_set_path=opportunity_set_path,
    )
    set_payload = {
        "account": account,
        "start_date": start_date,
        "end_date": end_date,
        "hash": opportunity_set.hash,
        "rows": [_opportunity_dict(row) for row in opportunity_set.rows],
    }
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
        set_out = directory / set_filename
        set_out.write_text(json.dumps(set_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        paths.append(set_out)
    return text, paths
