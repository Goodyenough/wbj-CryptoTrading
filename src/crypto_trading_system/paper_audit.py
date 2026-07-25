from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
import json
from pathlib import Path
import sqlite3

from .backtest.history import fetch_klines_cached
from .config import Settings
from .database import connect_db
from .report_versions import next_report_version, versioned_markdown_filename


BEIJING = timezone(timedelta(hours=8), name="CST")


@dataclass(frozen=True)
class BenchmarkRow:
    symbol: str
    status: str
    start_price: float | None
    end_price: float | None
    return_pct: float | None
    high_return_pct: float | None
    max_drawdown_pct: float | None
    trend: str
    note: str


@dataclass(frozen=True)
class OpportunityRow:
    source: str
    symbol: str
    plan_id: str
    first_time: str
    reason: str
    entry: float | None
    entry_low: float | None
    stop: float | None
    tp1: float | None
    max_price_after: float | None
    min_price_after: float | None
    reclaimed: bool
    hit_tp1: bool
    hit_stop: bool
    classification: str
    explanation: str
    observation_bars: int = 0
    required_bars: int = 42
    maturity_status: str = "data_gap"
    classification_final: bool = False
    risk_r: float | None = None
    mfe_r: float | None = None
    mae_r: float | None = None
    counterfactual_pnl_r: float | None = None
    first_hit: str = "none"
    time_to_first_hit_bars: int | None = None
    market_regime: str = "n/a"
    scanner_action: str = "n/a"
    scanner_score: float | None = None
    atr_4h: float | None = None
    support_level: float | None = None
    recent_high_4h_36: float | None = None
    pct_24h: float | None = None
    pct_3d: float | None = None
    pct_7d: float | None = None
    distance_to_support_atr: float | None = None
    stop_distance_atr: float | None = None
    pullback_from_recent_high_atr: float | None = None
    reclaim_margin_atr: float | None = None
    opportunity_set_key: str = ""


@dataclass(frozen=True)
class OpportunityReconciliation:
    account_total_reclaim_pending_events: int
    raw_reclaim_pending_events: int
    deduped_reclaim_plans: int
    scan_candidate_opportunities: int
    entered_false_entries: int
    final_classified_opportunities: int
    excluded_reclaim_duplicate_events: int
    dedupe_key: str
    note: str


@dataclass(frozen=True)
class FunnelRow:
    stage: str
    count: int
    mature_count: int
    right_censored_count: int
    conversion_rate_pct: float | None
    dedupe_key: str
    note: str


@dataclass(frozen=True)
class RunTypeHealth:
    run_type: str
    expected_runs: int
    observed_runs: int
    success_runs: int
    failed_runs: int
    running_runs: int
    success_rate_pct: float | None
    latest_started_at: str


@dataclass(frozen=True)
class DataLinkHealth:
    daily: RunTypeHealth
    paper_4h: RunTypeHealth
    config_hashes: list[str]
    config_hash_stable: bool
    stale_running_runs: int
    duplicate_events: int
    impossible_event_order: int
    verdict: str
    note: str


@dataclass(frozen=True)
class EnteredTradeRow:
    symbol: str
    plan_id: str
    status: str
    created_at: str
    entered_at: str
    market_regime: str
    entry_price: float | None
    stop: float | None
    tp1: float | None
    max_price_after: float | None
    min_price_after: float | None
    mfe_r: float | None
    mae_r: float | None
    near_tp1: bool
    tp1_hit: bool
    realized_pnl: float | None
    unrealized_pnl: float | None
    attribution: str
    explanation: str
    reason: str


def _local_now() -> datetime:
    return datetime.now(timezone.utc).astimezone(BEIJING)


def _parse_window(start_date: str, end_date: str) -> tuple[datetime, datetime]:
    start = datetime.combine(date.fromisoformat(start_date), time.min, tzinfo=BEIJING).astimezone(timezone.utc)
    end = datetime.combine(date.fromisoformat(end_date), time.max, tzinfo=BEIJING).astimezone(timezone.utc)
    return start, end


def _ms(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)


def _iso_z(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _local_timestamp(timestamp_utc: str) -> str:
    if not timestamp_utc:
        return "n/a"
    return datetime.fromisoformat(timestamp_utc.replace("Z", "+00:00")).astimezone(BEIJING).strftime("%Y-%m-%d %H:%M")


def _fmt(value: object, digits: int = 2) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def _pct(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}%"


def _json_text(row: sqlite3.Row, key: str) -> str:
    raw = row[key] if key in row.keys() else None
    if not raw:
        return ""
    try:
        data = json.loads(str(raw))
    except json.JSONDecodeError:
        return ""
    for field in ("setup", "reason", "verdict", "notes"):
        value = data.get(field)
        if value:
            return str(value)
    return ""


def _prices_from_rows(rows: list[sqlite3.Row], price_column: str) -> list[float]:
    prices = []
    for row in rows:
        value = row[price_column]
        if value is not None:
            prices.append(float(value))
    return prices


def _risk(entry: float | None, stop: float | None) -> float | None:
    if entry is None or stop is None:
        return None
    risk = entry - stop
    return risk if risk > 0 else None


def _float_or_none(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _payload_float(payload: dict[str, object], key: str) -> float | None:
    return _float_or_none(payload.get(key))


def _standardized_fields(
    *,
    entry_high: float | None,
    entry_low: float | None,
    stop: float | None,
    payload: dict[str, object] | None = None,
) -> dict[str, float | None]:
    payload = payload or {}
    atr_4h = _payload_float(payload, "atr_4h")
    support = _payload_float(payload, "support_level")
    recent_high = _payload_float(payload, "recent_high_4h_36")
    price = _payload_float(payload, "price")
    entry_mid = None
    if entry_high is not None and entry_low is not None:
        entry_mid = (entry_high + entry_low) / 2
    elif entry_high is not None:
        entry_mid = entry_high
    if atr_4h is None or atr_4h <= 0:
        return {
            "atr_4h": atr_4h,
            "support_level": support,
            "recent_high_4h_36": recent_high,
            "distance_to_support_atr": None,
            "stop_distance_atr": None,
            "pullback_from_recent_high_atr": None,
            "reclaim_margin_atr": None,
        }
    distance_to_support_atr = None
    if entry_mid is not None and support is not None:
        distance_to_support_atr = (entry_mid - support) / atr_4h
    stop_distance_atr = None
    if entry_mid is not None and stop is not None:
        stop_distance_atr = (entry_mid - stop) / atr_4h
    pullback_from_recent_high_atr = None
    if price is not None and recent_high is not None:
        pullback_from_recent_high_atr = (recent_high - price) / atr_4h
    reclaim_margin_atr = None
    if price is not None and entry_high is not None:
        reclaim_margin_atr = (price - entry_high) / atr_4h
    return {
        "atr_4h": atr_4h,
        "support_level": support,
        "recent_high_4h_36": recent_high,
        "distance_to_support_atr": distance_to_support_atr,
        "stop_distance_atr": stop_distance_atr,
        "pullback_from_recent_high_atr": pullback_from_recent_high_atr,
        "reclaim_margin_atr": reclaim_margin_atr,
    }


def _opportunity_path_stats(
    *,
    entry: float | None,
    stop: float | None,
    tp1: float | None,
    price_path: list[float],
    required_bars: int = 42,
) -> dict[str, object]:
    risk = _risk(entry, stop)
    max_price = max(price_path) if price_path else None
    min_price = min(price_path) if price_path else None
    mfe_r = None if risk is None or max_price is None or entry is None else (max_price - entry) / risk
    mae_r = None if risk is None or min_price is None or entry is None else (min_price - entry) / risk
    near_tp1 = None if entry is None or tp1 is None else entry + 0.8 * (tp1 - entry)

    first_hit = "none"
    time_to_first_hit_bars = None
    for index, price in enumerate(price_path, start=1):
        if stop is not None and price <= stop:
            first_hit = "stop_first"
            time_to_first_hit_bars = index
            break
        if tp1 is not None and price >= tp1:
            first_hit = "tp1_first"
            time_to_first_hit_bars = index
            break
        if near_tp1 is not None and price >= near_tp1:
            first_hit = "near_tp1_first"
            time_to_first_hit_bars = index
            break

    if first_hit == "stop_first":
        counterfactual_pnl_r = -1.0
    elif first_hit in {"tp1_first", "near_tp1_first"}:
        counterfactual_pnl_r = None if risk is None or entry is None or price_path is None else max(0.0, float(mfe_r or 0.0))
    else:
        counterfactual_pnl_r = None

    has_decisive_path = first_hit != "none"
    if not price_path:
        maturity_status = "data_gap"
    elif len(price_path) >= required_bars or has_decisive_path:
        maturity_status = "mature"
    else:
        maturity_status = "right_censored"

    return {
        "observation_bars": len(price_path),
        "required_bars": required_bars,
        "maturity_status": maturity_status,
        "classification_final": maturity_status == "mature",
        "risk_r": risk,
        "mfe_r": mfe_r,
        "mae_r": mae_r,
        "counterfactual_pnl_r": counterfactual_pnl_r,
        "first_hit": first_hit,
        "time_to_first_hit_bars": time_to_first_hit_bars,
    }


def _return_pct(start: float, end: float) -> float:
    return (end / start - 1.0) * 100.0


def _max_drawdown_pct(prices: list[float]) -> float | None:
    if not prices:
        return None
    peak = prices[0]
    max_dd = 0.0
    for price in prices:
        peak = max(peak, price)
        if peak > 0:
            max_dd = min(max_dd, (price / peak - 1.0) * 100.0)
    return max_dd


def _trend_label(return_pct: float | None) -> str:
    if return_pct is None:
        return "benchmark_unavailable"
    if return_pct >= 3.0:
        return "up"
    if return_pct <= -3.0:
        return "down"
    return "sideways"


def build_benchmark_rows(settings: Settings, start_date: str, end_date: str) -> list[BenchmarkRow]:
    start_utc, end_utc = _parse_window(start_date, end_date)
    rows: list[BenchmarkRow] = []
    for symbol in ("BTCUSDT", "ETHUSDT"):
        try:
            fetched = fetch_klines_cached(
                settings,
                symbol,
                "4h",
                _ms(start_utc - timedelta(hours=4)),
                _ms(end_utc + timedelta(hours=4)),
                allow_data_gaps=True,
            )
            klines = [
                kline for kline in fetched.klines
                if int(kline[6]) >= _ms(start_utc) and int(kline[6]) <= _ms(end_utc)
            ]
        except Exception as exc:  # noqa: BLE001 - report should continue when benchmark fetch fails.
            rows.append(BenchmarkRow(symbol, "benchmark_unavailable", None, None, None, None, None, "benchmark_unavailable", str(exc)))
            continue
        closes = [float(kline[4]) for kline in klines]
        if len(closes) < 2:
            rows.append(BenchmarkRow(symbol, "benchmark_unavailable", None, None, None, None, None, "benchmark_unavailable", "not enough closed 4h candles"))
            continue
        start_price = closes[0]
        end_price = closes[-1]
        ret = _return_pct(start_price, end_price)
        high_ret = _return_pct(start_price, max(closes))
        rows.append(
            BenchmarkRow(
                symbol=symbol,
                status="ok",
                start_price=start_price,
                end_price=end_price,
                return_pct=ret,
                high_return_pct=high_ret,
                max_drawdown_pct=_max_drawdown_pct(closes),
                trend=_trend_label(ret),
                note=f"closed_4h_candles={len(closes)} fetched_from_api={fetched.fetched_from_api}",
            )
        )
    return rows


def _load_snapshots_after(
    connection: sqlite3.Connection,
    plan_id: str,
    start_time: str,
    end_time: str,
) -> list[sqlite3.Row]:
    return connection.execute(
        """
        SELECT *
        FROM paper_snapshots
        WHERE plan_id = ? AND snapshot_time >= ? AND snapshot_time <= ?
        ORDER BY snapshot_time
        """,
        (plan_id, start_time, end_time),
    ).fetchall()


def _classify_opportunity(
    *,
    entry: float | None,
    stop: float | None,
    tp1: float | None,
    max_price: float | None,
    min_price: float | None,
    price_path: list[float] | None = None,
) -> tuple[str, bool, bool, bool, str]:
    target = None if entry is None or tp1 is None else entry + 0.8 * (tp1 - entry)
    reclaimed = entry is not None and max_price is not None and max_price >= entry
    near_tp1 = target is not None and max_price is not None and max_price >= target
    hit_tp1 = tp1 is not None and max_price is not None and max_price >= tp1
    hit_stop = stop is not None and min_price is not None and min_price <= stop
    if price_path:
        first_stop = next((idx for idx, price in enumerate(price_path) if stop is not None and price <= stop), None)
        first_target = next((idx for idx, price in enumerate(price_path) if target is not None and price >= target), None)
        if first_stop is not None and (first_target is None or first_stop <= first_target):
            return "avoided_loser", reclaimed, hit_tp1, hit_stop, "blocked candidate hit stop before reaching a near-TP1 path"
        if first_target is not None:
            return "missed_winner", reclaimed, hit_tp1, hit_stop, "blocked candidate reached a near-TP1 path before stop"
    if reclaimed and (hit_tp1 or near_tp1):
        return "missed_winner", reclaimed, hit_tp1, hit_stop, "blocked candidate later reclaimed and reached/approached TP1"
    if hit_stop:
        return "avoided_loser", reclaimed, hit_tp1, hit_stop, "blocked candidate later traded below stop"
    if max_price is None or min_price is None:
        return "neutral_or_unknown", reclaimed, hit_tp1, hit_stop, "insufficient post-block price path"
    return "neutral_or_unknown", reclaimed, hit_tp1, hit_stop, "no decisive missed winner or avoided loser evidence"


def build_reclaim_opportunities(settings: Settings, account: str, start_date: str, end_date: str) -> list[OpportunityRow]:
    start_utc, end_utc = _parse_window(start_date, end_date)
    start_text = _iso_z(start_utc)
    end_text = _iso_z(end_utc)
    with connect_db(settings.output.database_path) as connection:
        rows = connection.execute(
            """
            SELECT p.*, e.event_time, e.reason AS event_reason
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
              AND e.event_type IN ('RECLAIM_PENDING', 'RECLAIM_PENDING_SET')
              AND e.event_time >= ? AND e.event_time <= ?
            ORDER BY e.event_time
            """,
            (account, start_text, end_text),
        ).fetchall()
        first_by_plan: dict[str, sqlite3.Row] = {}
        for row in rows:
            first_by_plan.setdefault(str(row["plan_id"]), row)
        output: list[OpportunityRow] = []
        for plan_id, row in first_by_plan.items():
            snapshots = _load_snapshots_after(connection, plan_id, str(row["event_time"]), end_text)
            prices = _prices_from_rows(snapshots, "current_price")
            max_price = max(prices) if prices else None
            min_price = min(prices) if prices else None
            entry = row["entry_high"]
            entry_low = row["entry_low"]
            stop = row["stop_current"] if row["stop_current"] is not None else row["stop_initial"]
            tp1 = row["tp1"]
            raw_payload = row["raw_json"] if "raw_json" in row.keys() else None
            try:
                payload = json.loads(str(raw_payload or "{}"))
            except json.JSONDecodeError:
                payload = {}
            standardized = _standardized_fields(
                entry_high=_float_or_none(entry),
                entry_low=_float_or_none(entry_low),
                stop=_float_or_none(stop),
                payload=payload,
            )
            classification, reclaimed, hit_tp1, hit_stop, explanation = _classify_opportunity(
                entry=None if entry is None else float(entry),
                stop=None if stop is None else float(stop),
                tp1=None if tp1 is None else float(tp1),
                max_price=max_price,
                min_price=min_price,
                price_path=prices,
            )
            stats = _opportunity_path_stats(
                entry=None if entry is None else float(entry),
                stop=None if stop is None else float(stop),
                tp1=None if tp1 is None else float(tp1),
                price_path=prices,
            )
            output.append(
                OpportunityRow(
                    source="RECLAIM_PENDING",
                    symbol=str(row["symbol"]),
                    plan_id=plan_id,
                    first_time=str(row["event_time"]),
                    reason=str(row["event_reason"] or row["created_reason"] or _json_text(row, "raw_json") or ""),
                    entry=None if entry is None else float(entry),
                    entry_low=None if entry_low is None else float(entry_low),
                    stop=None if stop is None else float(stop),
                    tp1=None if tp1 is None else float(tp1),
                    max_price_after=max_price,
                    min_price_after=min_price,
                    reclaimed=reclaimed,
                    hit_tp1=hit_tp1,
                    hit_stop=hit_stop,
                    classification=classification,
                    explanation=explanation,
                    **stats,
                    market_regime=str(row["market_regime"] or "n/a"),
                    scanner_action="BUY_CANDIDATE",
                    scanner_score=_payload_float(payload, "score"),
                    pct_24h=_payload_float(payload, "pct_24h"),
                    pct_3d=_payload_float(payload, "pct_3d"),
                    pct_7d=_payload_float(payload, "pct_7d"),
                    opportunity_set_key=f"RECLAIM_PENDING:{plan_id}",
                    **standardized,
                )
            )
    return output


def build_scan_candidate_opportunities(settings: Settings, start_date: str, end_date: str) -> list[OpportunityRow]:
    start_utc, end_utc = _parse_window(start_date, end_date)
    start_text = _iso_z(start_utc)
    end_text = _iso_z(end_utc)
    with connect_db(settings.output.database_path) as connection:
        candidates = connection.execute(
            """
            SELECT c.*, m.scan_time
            FROM scan_candidates c
            JOIN market_scans m ON m.scan_id = c.scan_id
            WHERE m.scan_time >= ? AND m.scan_time <= ?
              AND c.action IN ('WATCH_ONLY', 'REJECT')
            ORDER BY m.scan_time, c.scan_id, c.symbol
            """,
            (start_text, end_text),
        ).fetchall()
        output: list[OpportunityRow] = []
        seen: set[tuple[str, str, str]] = set()
        for row in candidates:
            key = (str(row["scan_id"]), str(row["symbol"]), str(row["action"]))
            if key in seen:
                continue
            seen.add(key)
            entry = row["entry_high"] if row["entry_high"] is not None else row["price"]
            entry_low = row["entry_low"]
            stop = row["stop"]
            tp1 = row["tp1"]
            try:
                payload = json.loads(str(row["payload_json"] or "{}"))
            except json.JSONDecodeError:
                payload = {}
            standardized = _standardized_fields(
                entry_high=_float_or_none(entry),
                entry_low=_float_or_none(entry_low),
                stop=_float_or_none(stop),
                payload=payload,
            )
            try:
                fetched = fetch_klines_cached(
                    settings,
                    str(row["symbol"]),
                    "4h",
                    _ms(datetime.fromisoformat(str(row["scan_time"]).replace("Z", "+00:00"))),
                    _ms(end_utc + timedelta(hours=4)),
                    allow_data_gaps=True,
                )
                prices = [float(kline[4]) for kline in fetched.klines]
            except Exception:
                prices = []
            max_price = max(prices) if prices else None
            min_price = min(prices) if prices else None
            classification, reclaimed, hit_tp1, hit_stop, explanation = _classify_opportunity(
                entry=None if entry is None else float(entry),
                stop=None if stop is None else float(stop),
                tp1=None if tp1 is None else float(tp1),
                max_price=max_price,
                min_price=min_price,
                price_path=prices,
            )
            stats = _opportunity_path_stats(
                entry=None if entry is None else float(entry),
                stop=None if stop is None else float(stop),
                tp1=None if tp1 is None else float(tp1),
                price_path=prices,
            )
            output.append(
                OpportunityRow(
                    source=str(row["action"]),
                    symbol=str(row["symbol"]),
                    plan_id=f"{row['scan_id']}:{row['symbol']}",
                    first_time=str(row["scan_time"]),
                    reason=str(row["reason"] or _json_text(row, "raw_json") or ""),
                    entry=None if entry is None else float(entry),
                    entry_low=None if entry_low is None else float(entry_low),
                    stop=None if stop is None else float(stop),
                    tp1=None if tp1 is None else float(tp1),
                    max_price_after=max_price,
                    min_price_after=min_price,
                    reclaimed=reclaimed,
                    hit_tp1=hit_tp1,
                    hit_stop=hit_stop,
                    classification=classification,
                    explanation=explanation,
                    **stats,
                    market_regime=str(row["market_regime"] or "n/a"),
                    scanner_action=str(row["action"] or "n/a"),
                    scanner_score=None if row["score"] is None else float(row["score"]),
                    pct_24h=_payload_float(payload, "pct_24h"),
                    pct_3d=_payload_float(payload, "pct_3d"),
                    pct_7d=_payload_float(payload, "pct_7d"),
                    opportunity_set_key=f"{row['action']}:{row['scan_id']}:{row['symbol']}",
                    **standardized,
                )
            )
    return output


def build_opportunity_reconciliation(
    settings: Settings,
    account: str,
    start_date: str,
    end_date: str,
    *,
    reclaim_rows: list[OpportunityRow],
    scan_rows: list[OpportunityRow],
    false_entries: list[OpportunityRow],
) -> OpportunityReconciliation:
    start_utc, end_utc = _parse_window(start_date, end_date)
    start_text = _iso_z(start_utc)
    end_text = _iso_z(end_utc)
    with connect_db(settings.output.database_path) as connection:
        total_reclaim = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
              AND e.event_type IN ('RECLAIM_PENDING', 'RECLAIM_PENDING_SET')
            """,
            (account,),
        ).fetchone()["count"]
        raw_reclaim = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
              AND e.event_type IN ('RECLAIM_PENDING', 'RECLAIM_PENDING_SET')
              AND e.event_time >= ? AND e.event_time <= ?
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]
    final_count = len(reclaim_rows) + len(scan_rows) + len(false_entries)
    return OpportunityReconciliation(
        account_total_reclaim_pending_events=int(total_reclaim),
        raw_reclaim_pending_events=int(raw_reclaim),
        deduped_reclaim_plans=len(reclaim_rows),
        scan_candidate_opportunities=len(scan_rows),
        entered_false_entries=len(false_entries),
        final_classified_opportunities=final_count,
        excluded_reclaim_duplicate_events=max(0, int(raw_reclaim) - len(reclaim_rows)),
        dedupe_key="RECLAIM_PENDING: plan_id; WATCH_ONLY/REJECT: scan_id+symbol+action; false_entry: plan_id",
        note="final opportunities combine deduped reclaim plans, scan WATCH_ONLY/REJECT candidates, and stopped entered trades classified as false_entry",
    )


def _rate(numerator: int, denominator: int) -> float | None:
    if denominator <= 0:
        return None
    return numerator / denominator * 100.0


def _window_days(start_date: str, end_date: str) -> int:
    return (date.fromisoformat(end_date) - date.fromisoformat(start_date)).days + 1


def _build_run_type_health(rows: list[sqlite3.Row], run_type: str, expected_runs: int) -> RunTypeHealth:
    matching = [row for row in rows if str(row["run_type"]) == run_type]
    success = sum(1 for row in matching if str(row["status"]) == "success")
    failed = sum(1 for row in matching if str(row["status"]) == "failed")
    running = sum(1 for row in matching if str(row["status"]) == "running")
    latest = max((str(row["started_at"]) for row in matching), default="n/a")
    return RunTypeHealth(
        run_type=run_type,
        expected_runs=expected_runs,
        observed_runs=len(matching),
        success_runs=success,
        failed_runs=failed,
        running_runs=running,
        success_rate_pct=_rate(success, expected_runs),
        latest_started_at=latest,
    )


def build_data_link_health(settings: Settings, account: str, start_date: str, end_date: str) -> DataLinkHealth:
    start_utc, end_utc = _parse_window(start_date, end_date)
    start_text = _iso_z(start_utc)
    end_text = _iso_z(end_utc)
    days = _window_days(start_date, end_date)
    with connect_db(settings.output.database_path) as connection:
        run_rows = connection.execute(
            """
            SELECT *
            FROM runs
            WHERE started_at >= ? AND started_at <= ?
              AND run_type IN ('daily_full', 'paper_4h_update')
            ORDER BY started_at
            """,
            (start_text, end_text),
        ).fetchall()
        config_hashes = sorted(
            {
                str(row["config_hash"])
                for row in run_rows
                if "config_hash" in row.keys() and row["config_hash"]
            }
        )
        stale_running = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM runs
            WHERE status = 'running'
              AND started_at <= ?
            """,
            (_iso_z(_local_now().astimezone(timezone.utc) - timedelta(hours=2)),),
        ).fetchone()["count"]
        duplicate_events = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM (
                SELECT plan_id, event_type, event_time, COUNT(*) AS n
                FROM paper_events
                WHERE event_time >= ? AND event_time <= ?
                GROUP BY plan_id, event_type, event_time
                HAVING n > 1
            )
            """,
            (start_text, end_text),
        ).fetchone()["count"]
        impossible_order = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM paper_events entered
            JOIN paper_events terminal
              ON terminal.plan_id = entered.plan_id
             AND terminal.event_time < entered.event_time
            JOIN paper_plans p ON p.plan_id = entered.plan_id
            WHERE p.account_name = ?
              AND entered.event_time >= ? AND entered.event_time <= ?
              AND entered.event_type IN ('ENTERED', 'RECLAIM_CONFIRMED_ENTERED')
              AND terminal.event_type IN ('STOPPED', 'INVALIDATED', 'EXPIRED', 'ARCHIVED')
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]

    daily = _build_run_type_health(run_rows, "daily_full", days)
    paper_4h = _build_run_type_health(run_rows, "paper_4h_update", days * 5)
    config_hash_stable = len(config_hashes) <= 1
    if not config_hash_stable or int(stale_running) > 0 or int(duplicate_events) > 0 or int(impossible_order) > 0:
        verdict = "fix"
    elif daily.success_runs < daily.expected_runs or paper_4h.failed_runs > 0:
        verdict = "partial_pass"
    else:
        verdict = "pass"
    note = (
        "expected paper_4h runs assume five scheduled updates per Beijing day "
        "(00:10, 04:10, 08:10, 12:10, 16:10)"
    )
    return DataLinkHealth(
        daily=daily,
        paper_4h=paper_4h,
        config_hashes=config_hashes,
        config_hash_stable=config_hash_stable,
        stale_running_runs=int(stale_running),
        duplicate_events=int(duplicate_events),
        impossible_event_order=int(impossible_order),
        verdict=verdict,
        note=note,
    )


def build_opportunity_funnel(
    settings: Settings,
    account: str,
    start_date: str,
    end_date: str,
    *,
    opportunities: list[OpportunityRow],
) -> list[FunnelRow]:
    start_utc, end_utc = _parse_window(start_date, end_date)
    start_text = _iso_z(start_utc)
    end_text = _iso_z(end_utc)
    maturity_counts = Counter(row.maturity_status for row in opportunities)
    with connect_db(settings.output.database_path) as connection:
        scanned = connection.execute(
            """
            SELECT COUNT(DISTINCT c.scan_id || ':' || c.symbol) AS count
            FROM scan_candidates c
            JOIN market_scans m ON m.scan_id = c.scan_id
            WHERE m.scan_time >= ? AND m.scan_time <= ?
            """,
            (start_text, end_text),
        ).fetchone()["count"]
        action_rows = connection.execute(
            """
            SELECT c.action, COUNT(DISTINCT c.scan_id || ':' || c.symbol) AS count
            FROM scan_candidates c
            JOIN market_scans m ON m.scan_id = c.scan_id
            WHERE m.scan_time >= ? AND m.scan_time <= ?
            GROUP BY c.action
            """,
            (start_text, end_text),
        ).fetchall()
        action_counts = {str(row["action"]): int(row["count"]) for row in action_rows}
        risk_off_blocked = connection.execute(
            """
            SELECT COUNT(DISTINCT c.scan_id || ':' || c.symbol) AS count
            FROM scan_candidates c
            JOIN market_scans m ON m.scan_id = c.scan_id
            WHERE m.scan_time >= ? AND m.scan_time <= ?
              AND (
                UPPER(COALESCE(c.market_regime, '')) = 'RISK_OFF'
                OR LOWER(COALESCE(c.reason, '')) LIKE '%risk_off%'
                OR LOWER(COALESCE(c.payload_json, '')) LIKE '%risk_off%'
              )
              AND c.action IN ('WATCH_ONLY', 'REJECT')
            """,
            (start_text, end_text),
        ).fetchone()["count"]
        reclaim_pending = connection.execute(
            """
            SELECT COUNT(DISTINCT e.plan_id) AS count
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
              AND e.event_type IN ('RECLAIM_PENDING', 'RECLAIM_PENDING_SET')
              AND e.event_time >= ? AND e.event_time <= ?
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]
        reclaim_confirmed = connection.execute(
            """
            SELECT COUNT(DISTINCT e.plan_id) AS count
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
              AND e.event_type IN ('RECLAIM_CONFIRMED_ENTERED', 'ENTERED')
              AND e.event_time >= ? AND e.event_time <= ?
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]
        entered = connection.execute(
            """
            SELECT COUNT(DISTINCT plan_id) AS count
            FROM paper_plans
            WHERE account_name = ?
              AND entered_at_utc IS NOT NULL
              AND entered_at_utc >= ? AND entered_at_utc <= ?
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]
        terminal_rows = connection.execute(
            """
            SELECT status, COUNT(DISTINCT plan_id) AS count
            FROM paper_plans
            WHERE account_name = ?
              AND entered_at_utc IS NOT NULL
              AND entered_at_utc >= ? AND entered_at_utc <= ?
              AND status IN ('STOPPED', 'CLOSED', 'ARCHIVED', 'INVALIDATED')
            GROUP BY status
            """,
            (account, start_text, end_text),
        ).fetchall()
        terminal_counts = {str(row["status"]): int(row["count"]) for row in terminal_rows}
        tp1 = connection.execute(
            """
            SELECT COUNT(DISTINCT plan_id) AS count
            FROM paper_plans
            WHERE account_name = ?
              AND entered_at_utc IS NOT NULL
              AND entered_at_utc >= ? AND entered_at_utc <= ?
              AND tp1_hit_at_utc IS NOT NULL
            """,
            (account, start_text, end_text),
        ).fetchone()["count"]

    scanned_count = int(scanned or 0)
    buy_count = action_counts.get("BUY_CANDIDATE", 0)
    watch_count = action_counts.get("WATCH_ONLY", 0)
    reject_count = action_counts.get("REJECT", 0)
    rows = [
        FunnelRow("scanned_candidates", scanned_count, 0, 0, None, "scan_id+symbol", "all scan candidates in the window"),
        FunnelRow("buy_candidates", buy_count, 0, 0, _rate(buy_count, scanned_count), "scan_id+symbol", "candidates allowed to become plans"),
        FunnelRow("watch_only_candidates", watch_count, 0, 0, _rate(watch_count, scanned_count), "scan_id+symbol", "defensive or lower-confidence candidates"),
        FunnelRow("reject_candidates", reject_count, 0, 0, _rate(reject_count, scanned_count), "scan_id+symbol", "rejected scan candidates"),
        FunnelRow("risk_off_blocked_candidates", int(risk_off_blocked or 0), 0, 0, _rate(int(risk_off_blocked or 0), scanned_count), "scan_id+symbol", "WATCH_ONLY/REJECT candidates tied to RISK_OFF evidence"),
        FunnelRow("reclaim_pending_plans", int(reclaim_pending or 0), maturity_counts.get("mature", 0), maturity_counts.get("right_censored", 0), _rate(int(reclaim_pending or 0), buy_count), "plan_id", "deduped plans with reclaim pending events"),
        FunnelRow("reclaim_confirmed_or_entered_events", int(reclaim_confirmed or 0), 0, 0, _rate(int(reclaim_confirmed or 0), int(reclaim_pending or 0)), "plan_id", "plans with ENTERED or RECLAIM_CONFIRMED_ENTERED events"),
        FunnelRow("entered_plans", int(entered or 0), 0, 0, _rate(int(entered or 0), buy_count), "plan_id", "paper plans that actually entered during the window"),
        FunnelRow("tp1_hit_plans", int(tp1 or 0), 0, 0, _rate(int(tp1 or 0), int(entered or 0)), "plan_id", "entered plans that reached TP1"),
        FunnelRow("stopped_plans", terminal_counts.get("STOPPED", 0), 0, 0, _rate(terminal_counts.get("STOPPED", 0), int(entered or 0)), "plan_id", "entered plans currently marked STOPPED"),
    ]
    return rows


def _classify_entered_trade(
    *,
    status: str,
    market_regime: str,
    mfe_r: float | None,
    mae_r: float | None,
    near_tp1: bool,
) -> tuple[str, str]:
    if status not in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"}:
        return "open_unknown", "trade is still open or not terminal"
    if mfe_r is None:
        return "open_unknown", "insufficient price path to classify"
    if mfe_r < 0.5:
        if market_regime.upper() == "RISK_OFF":
            return "market_issue", "entered in RISK_OFF and never built enough favorable excursion"
        return "entry_issue", "entry failed before producing meaningful favorable excursion"
    if near_tp1 or mfe_r >= 1.0:
        return "exit_issue", "trade had meaningful favorable excursion but still ended poorly"
    if mae_r is not None and mae_r <= -1.0:
        return "selection_issue", "trade reached full risk without strong upside follow-through"
    return "entry_issue", "limited favorable excursion before terminal loss"


def build_entered_trade_rows(settings: Settings, account: str, start_date: str, end_date: str) -> list[EnteredTradeRow]:
    _start_utc, end_utc = _parse_window(start_date, end_date)
    end_text = _iso_z(end_utc)
    with connect_db(settings.output.database_path) as connection:
        plans = connection.execute(
            """
            SELECT *
            FROM paper_plans
            WHERE account_name = ? AND entry_price IS NOT NULL
            ORDER BY entered_at_utc, created_at
            """,
            (account,),
        ).fetchall()
        output: list[EnteredTradeRow] = []
        for plan in plans:
            entered_at = str(plan["entered_at_utc"] or plan["created_at"])
            snapshots = _load_snapshots_after(connection, str(plan["plan_id"]), entered_at, end_text)
            prices = _prices_from_rows(snapshots, "current_price")
            if not prices:
                events = connection.execute(
                    """
                    SELECT price
                    FROM paper_events
                    WHERE plan_id = ? AND event_time >= ? AND event_time <= ? AND price IS NOT NULL
                    ORDER BY event_time
                    """,
                    (plan["plan_id"], entered_at, end_text),
                ).fetchall()
                prices = _prices_from_rows(events, "price")
            entry = None if plan["entry_price"] is None else float(plan["entry_price"])
            stop = plan["stop_initial"] if plan["stop_initial"] is not None else plan["stop_current"]
            stop_float = None if stop is None else float(stop)
            tp1 = None if plan["tp1"] is None else float(plan["tp1"])
            max_price = max(prices) if prices else None
            min_price = min(prices) if prices else None
            risk = _risk(entry, stop_float)
            mfe_r = None if risk is None or max_price is None or entry is None else (max_price - entry) / risk
            mae_r = None if risk is None or min_price is None or entry is None else (min_price - entry) / risk
            near_tp1 = bool(entry is not None and tp1 is not None and max_price is not None and max_price >= entry + 0.8 * (tp1 - entry))
            tp1_hit = bool(plan["tp1_hit_at_utc"] or (tp1 is not None and max_price is not None and max_price >= tp1))
            attribution, explanation = _classify_entered_trade(
                status=str(plan["status"]),
                market_regime=str(plan["market_regime"] or ""),
                mfe_r=mfe_r,
                mae_r=mae_r,
                near_tp1=near_tp1,
            )
            output.append(
                EnteredTradeRow(
                    symbol=str(plan["symbol"]),
                    plan_id=str(plan["plan_id"]),
                    status=str(plan["status"]),
                    created_at=str(plan["created_at"]),
                    entered_at=entered_at,
                    market_regime=str(plan["market_regime"] or "n/a"),
                    entry_price=entry,
                    stop=stop_float,
                    tp1=tp1,
                    max_price_after=max_price,
                    min_price_after=min_price,
                    mfe_r=mfe_r,
                    mae_r=mae_r,
                    near_tp1=near_tp1,
                    tp1_hit=tp1_hit,
                    realized_pnl=None if plan["realized_pnl"] is None else float(plan["realized_pnl"]),
                    unrealized_pnl=None if plan["unrealized_pnl"] is None else float(plan["unrealized_pnl"]),
                    attribution=attribution,
                    explanation=explanation,
                    reason=str(plan["created_reason"] or plan["setup"] or _json_text(plan, "raw_json") or ""),
                )
            )
    return output


def _benchmark_context(rows: list[BenchmarkRow]) -> str:
    available = [row for row in rows if row.return_pct is not None]
    if not available:
        return "benchmark_unavailable"
    avg = sum(float(row.return_pct) for row in available) / len(available)
    trend = _trend_label(avg)
    if trend == "up":
        return "BTC/ETH formal-window benchmark rose; strategy losses or inactivity need selection/entry/defense review."
    if trend == "down":
        return "BTC/ETH formal-window benchmark fell; defensive inactivity or fewer entries may be justified."
    return "BTC/ETH formal-window benchmark was broadly sideways; stopped trades point more toward entry quality."


def _opportunity_verdict(counter: Counter) -> str:
    missed = counter.get("missed_winner", 0)
    avoided = counter.get("avoided_loser", 0)
    false_entries = counter.get("false_entry", 0)
    if missed > avoided:
        return "review_defense_rules"
    if avoided > 0 and missed == 0:
        return "keep_observing_defense_rules"
    if false_entries > 0:
        return "review_entry_quality"
    return "sample_insufficient_or_neutral"


def _entered_trade_verdict(rows: list[EnteredTradeRow]) -> str:
    counts = Counter(row.attribution for row in rows)
    if not rows:
        return "sample_insufficient"
    if counts.get("exit_issue", 0) >= max(2, len(rows) // 2):
        return "review_exit_rules"
    if counts.get("entry_issue", 0) + counts.get("selection_issue", 0) >= max(2, len(rows) // 2):
        return "review_selection_and_entry"
    if counts.get("market_issue", 0) >= max(2, len(rows) // 2):
        return "market_regime_explains_losses"
    return "mixed_causes_keep_observing"


def render_paper_audit_report(
    *,
    account: str,
    start_date: str,
    end_date: str,
    report_version: int,
    benchmarks: list[BenchmarkRow],
    opportunities: list[OpportunityRow],
    entered_trades: list[EnteredTradeRow],
    reconciliation: OpportunityReconciliation | None = None,
    funnel: list[FunnelRow] | None = None,
    data_link: DataLinkHealth | None = None,
) -> str:
    now = _local_now()
    opportunity_counts = Counter(row.classification for row in opportunities)
    maturity_counts = Counter(row.maturity_status for row in opportunities)
    entered_counts = Counter(row.attribution for row in entered_trades)
    symbol_counts = Counter(row.symbol for row in opportunities)
    final_opportunities = [row for row in opportunities if row.classification_final]
    avoided_loss_r = abs(sum(float(row.counterfactual_pnl_r or 0.0) for row in final_opportunities if row.classification == "avoided_loser"))
    missed_profit_r = sum(float(row.counterfactual_pnl_r or 0.0) for row in final_opportunities if row.classification == "missed_winner")
    defense_net_r = avoided_loss_r - missed_profit_r
    lines = [
        "---",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - paper-audit",
        f"account: {account}",
        f"start_date: {start_date}",
        f"end_date: {end_date}",
        f"report_version: v{report_version}",
        "---",
        "",
        f"# Paper Opportunity Audit {start_date} -> {end_date} {account} v{report_version}",
        "",
        "本报告只解释 paper 阶段没有赚钱的来源，不证明策略长期盈利能力。",
        "",
        "## Final Readout",
        "",
        f"- benchmark_context: {_benchmark_context(benchmarks)}",
        f"- opportunity_verdict: {_opportunity_verdict(opportunity_counts)}",
        f"- entered_trade_verdict: {_entered_trade_verdict(entered_trades)}",
        f"- mature_opportunities: {maturity_counts.get('mature', 0)}",
        f"- right_censored_opportunities: {maturity_counts.get('right_censored', 0)}",
        f"- defense_net_R: {defense_net_r:.2f}",
        f"- data_link_verdict: {data_link.verdict if data_link else 'not_checked'}",
        "- next_action: keep current settings while the next window collects more entered/TP1/reclaim evidence.",
        "",
        "## Data Link Health",
        "",
        "| Run Type | Expected | Observed | Success | Failed | Running | Success Rate | Latest Started |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    if data_link:
        for row in [data_link.daily, data_link.paper_4h]:
            lines.append(
                f"| {row.run_type} | {row.expected_runs} | {row.observed_runs} | {row.success_runs} | "
                f"{row.failed_runs} | {row.running_runs} | {_pct(row.success_rate_pct)} | {_local_timestamp(row.latest_started_at)} |"
            )
        lines.extend([
            "",
            "| Check | Value |",
            "|---|---|",
            f"| verdict | {data_link.verdict} |",
            f"| config_hash_stable | {str(data_link.config_hash_stable).lower()} |",
            f"| config_hashes | {', '.join(data_link.config_hashes) if data_link.config_hashes else 'n/a'} |",
            f"| stale_running_runs | {data_link.stale_running_runs} |",
            f"| duplicate_events | {data_link.duplicate_events} |",
            f"| impossible_event_order | {data_link.impossible_event_order} |",
            f"| note | {data_link.note} |",
        ])
    else:
        lines.append("| n/a | 0 | 0 | 0 | 0 | 0 | n/a | n/a |")
    lines.extend([
        "",
        "## BTC/ETH Benchmark",
        "",
        "| Symbol | Status | Start | End | Return | High Return | Max Drawdown | Trend | Note |",
        "|---|---|---:|---:|---:|---:|---:|---|---|",
    ])
    for row in benchmarks:
        lines.append(
            f"| `{row.symbol}` | {row.status} | {_fmt(row.start_price, 2)} | {_fmt(row.end_price, 2)} | "
            f"{_pct(row.return_pct)} | {_pct(row.high_return_pct)} | {_pct(row.max_drawdown_pct)} | {row.trend} | {row.note} |"
        )
    lines.extend([
        "",
        "## Opportunity Audit Summary",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ])
    for label in ["avoided_loser", "missed_winner", "false_entry", "neutral_or_unknown"]:
        lines.append(f"| {label} | {opportunity_counts.get(label, 0)} |")
    lines.extend([
        "",
        "### Opportunity Maturity",
        "",
        "| Maturity Status | Count |",
        "|---|---:|",
    ])
    for label in ["mature", "right_censored", "open_unknown", "data_gap"]:
        lines.append(f"| {label} | {maturity_counts.get(label, 0)} |")
    lines.extend([
        "",
        "### Opportunity Funnel",
        "",
        "| Stage | Count | Conversion | Mature | Right Censored | Dedupe Key | Note |",
        "|---|---:|---:|---:|---:|---|---|",
    ])
    if funnel:
        for row in funnel:
            lines.append(
                f"| {row.stage} | {row.count} | {_pct(row.conversion_rate_pct)} | "
                f"{row.mature_count} | {row.right_censored_count} | {row.dedupe_key} | {row.note} |"
            )
    else:
        lines.append("| n/a | 0 | n/a | 0 | 0 | n/a | funnel unavailable |")
    lines.extend([
        "",
        "### Reclaim Reconciliation",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ])
    if reconciliation is None:
        lines.append("| raw_RECLAIM_PENDING_events | n/a |")
        lines.append("| final_classified_opportunities | n/a |")
    else:
        lines.extend([
            f"| account_total_RECLAIM_PENDING_events | {reconciliation.account_total_reclaim_pending_events} |",
            f"| window_raw_RECLAIM_PENDING_events | {reconciliation.raw_reclaim_pending_events} |",
            f"| deduped_reclaim_plans | {reconciliation.deduped_reclaim_plans} |",
            f"| excluded_reclaim_duplicate_events | {reconciliation.excluded_reclaim_duplicate_events} |",
            f"| scan_candidate_opportunities | {reconciliation.scan_candidate_opportunities} |",
            f"| entered_false_entries | {reconciliation.entered_false_entries} |",
            f"| final_classified_opportunities | {reconciliation.final_classified_opportunities} |",
        ])
        lines.extend([
            "",
            f"- dedupe_key: {reconciliation.dedupe_key}",
            f"- note: {reconciliation.note}",
        ])
    lines.extend([
        "",
        "### Counterfactual R Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| mature_avoided_loss_R | {avoided_loss_r:.2f} |",
        f"| mature_missed_profit_R | {missed_profit_r:.2f} |",
        f"| mature_defense_net_R | {defense_net_r:.2f} |",
    ])
    lines.extend([
        "",
        "### Symbol Repeats",
        "",
        "| Symbol | Opportunity Rows |",
        "|---|---:|",
    ])
    for symbol, count in symbol_counts.most_common():
        lines.append(f"| `{symbol}` | {count} |")
    if not symbol_counts:
        lines.append("| n/a | 0 |")
    lines.extend([
        "",
        "### Opportunity Details",
        "",
        "| Source | Symbol | ID | First Time | Entry | Stop | TP1 | Max/Min After | Bars | Maturity | MFE_R | MAE_R | First Hit | Classification | Final | Explanation |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|---|",
    ])
    for row in opportunities:
        lines.append(
            f"| {row.source} | `{row.symbol}` | `{row.plan_id}` | {_local_timestamp(row.first_time)} | "
            f"{_fmt(row.entry, 6)} | {_fmt(row.stop, 6)} | {_fmt(row.tp1, 6)} | "
            f"{_fmt(row.max_price_after, 6)} / {_fmt(row.min_price_after, 6)} | "
            f"{row.observation_bars}/{row.required_bars} | {row.maturity_status} | "
            f"{_fmt(row.mfe_r, 2)} | {_fmt(row.mae_r, 2)} | {row.first_hit} | "
            f"{row.classification} | {str(row.classification_final).lower()} | {row.explanation} |"
        )
    if not opportunities:
        lines.append("| n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 0/42 | data_gap | n/a | n/a | none | neutral_or_unknown | false | no opportunity rows |")
    lines.extend([
        "",
        "## Entered Trades Review",
        "",
        "| Attribution | Count |",
        "|---|---:|",
    ])
    for label in ["entry_issue", "selection_issue", "exit_issue", "market_issue", "risk_rule_issue", "open_unknown"]:
        lines.append(f"| {label} | {entered_counts.get(label, 0)} |")
    lines.extend([
        "",
        "| Symbol | Plan | Status | Entered | Regime | Entry | Stop | TP1 | MFE_R | MAE_R | Near TP1 | TP1 Hit | PnL | Attribution | Explanation |",
        "|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|---|",
    ])
    for row in entered_trades:
        pnl = (row.realized_pnl or 0.0) + (row.unrealized_pnl or 0.0)
        lines.append(
            f"| `{row.symbol}` | `{row.plan_id}` | {row.status} | {_local_timestamp(row.entered_at)} | "
            f"{row.market_regime} | {_fmt(row.entry_price, 6)} | {_fmt(row.stop, 6)} | {_fmt(row.tp1, 6)} | "
            f"{_fmt(row.mfe_r, 2)} | {_fmt(row.mae_r, 2)} | {str(row.near_tp1).lower()} | "
            f"{str(row.tp1_hit).lower()} | {pnl:.2f} | {row.attribution} | {row.explanation} |"
        )
    if not entered_trades:
        lines.append("| n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | false | false | 0.00 | open_unknown | no entered trades |")
    lines.extend([
        "",
        "## Raw Classification Counts",
        "",
        "```json",
        json.dumps(
            {
                "opportunities": dict(opportunity_counts),
                "opportunity_maturity": dict(maturity_counts),
                "opportunity_r": {
                    "avoided_loss_R": avoided_loss_r,
                    "missed_profit_R": missed_profit_r,
                    "defense_net_R": defense_net_r,
                },
                "entered_trades": dict(entered_counts),
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
    ])
    return "\n".join(lines) + "\n"


def write_paper_audit_report(
    settings: Settings,
    *,
    account_name: str | None,
    start_date: str,
    end_date: str,
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    benchmarks = build_benchmark_rows(settings, start_date, end_date)
    reclaim = build_reclaim_opportunities(settings, account, start_date, end_date)
    scan_opportunities = build_scan_candidate_opportunities(settings, start_date, end_date)
    entered = build_entered_trade_rows(settings, account, start_date, end_date)
    false_entries = [
        OpportunityRow(
            source="ENTERED_TRADE",
            symbol=row.symbol,
            plan_id=row.plan_id,
            first_time=row.entered_at,
            reason=row.reason,
            entry=row.entry_price,
            entry_low=row.entry_price,
            stop=row.stop,
            tp1=row.tp1,
            max_price_after=row.max_price_after,
            min_price_after=row.min_price_after,
            reclaimed=True,
            hit_tp1=row.tp1_hit,
            hit_stop=row.status == "STOPPED",
            classification="false_entry",
            explanation=row.explanation,
            observation_bars=0,
            required_bars=42,
            maturity_status="mature" if row.status in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"} else "open_unknown",
            classification_final=row.status in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"},
            risk_r=_risk(row.entry_price, row.stop),
            mfe_r=row.mfe_r,
            mae_r=row.mae_r,
            counterfactual_pnl_r=-1.0 if row.status == "STOPPED" else None,
            first_hit="stop_first" if row.status == "STOPPED" else "none",
            time_to_first_hit_bars=None,
            market_regime=row.market_regime,
            scanner_action="ENTERED",
            opportunity_set_key=f"ENTERED_TRADE:{row.plan_id}",
        )
        for row in entered
        if row.attribution in {"entry_issue", "selection_issue", "market_issue"} and row.status == "STOPPED"
    ]
    opportunities = reclaim + scan_opportunities + false_entries
    reconciliation = build_opportunity_reconciliation(
        settings,
        account,
        start_date,
        end_date,
        reclaim_rows=reclaim,
        scan_rows=scan_opportunities,
        false_entries=false_entries,
    )
    funnel = build_opportunity_funnel(
        settings,
        account,
        start_date,
        end_date,
        opportunities=opportunities,
    )
    data_link = build_data_link_health(settings, account, start_date, end_date)

    now = _local_now()
    report_dir = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    obsidian_dir = None if settings.output.obsidian_dir is None else settings.output.obsidian_dir / "Reports" / now.strftime("%Y-%m-%d")
    prefix = f"paper_opportunity_audit_{start_date}_{end_date}_{account}"
    version = next_report_version([report_dir, obsidian_dir], prefix)
    filename = versioned_markdown_filename(prefix, version)
    text = render_paper_audit_report(
        account=account,
        start_date=start_date,
        end_date=end_date,
        report_version=version,
        benchmarks=benchmarks,
        opportunities=opportunities,
        entered_trades=entered,
        reconciliation=reconciliation,
        funnel=funnel,
        data_link=data_link,
    )
    paths: list[Path] = []
    for directory in [report_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        out = directory / filename
        out.write_text(text, encoding="utf-8")
        paths.append(out)
    return text, paths
