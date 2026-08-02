from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import uuid

from .config import Settings
from .database import connect_db, utc_now
from .market_data import BinanceClient
from .market_regime import classify_market_regime
from .models import PaperTrade, PaperTradeEvent
from .report_versions import next_report_version, versioned_markdown_filename
from .trade_state import step_trade
from .indicators import atr as _atr
from .indicators import ema as _ema


OPEN_STATUSES = {"WATCHING", "ENTERED", "TP1_HIT"}
CLOSED_STATUSES = {"STOPPED", "CLOSED", "EXPIRED", "INVALIDATED", "ARCHIVED"}
ALLOWED_TRANSITIONS = {
    "WATCHING": {"WATCHING", "ENTERED", "EXPIRED", "INVALIDATED", "ARCHIVED"},
    "ENTERED": {"ENTERED", "TP1_HIT", "STOPPED", "CLOSED"},
    "TP1_HIT": {"TP1_HIT", "STOPPED", "CLOSED"},
    "STOPPED": {"STOPPED"},
    "CLOSED": {"CLOSED"},
    "EXPIRED": {"EXPIRED"},
    "INVALIDATED": {"INVALIDATED"},
    "ARCHIVED": {"ARCHIVED"},
}


def _utc_now() -> str:
    return utc_now()


def _local_timestamp(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d %H:%M:%S %Z")


def _local_date(timestamp_utc: str) -> str:
    dt = datetime.fromisoformat(timestamp_utc)
    return dt.astimezone(timezone(timedelta(hours=8), name="CST")).strftime("%Y-%m-%d")


def _project_report_dir(settings: Settings, timestamp_utc: str) -> Path:
    return settings.output.reports_dir / _local_date(timestamp_utc)


def _obsidian_report_dir(settings: Settings, timestamp_utc: str) -> Path | None:
    if settings.output.obsidian_dir is None:
        return None
    return settings.output.obsidian_dir / "Reports" / _local_date(timestamp_utc)


def _fmt_price(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value >= 10_000:
        return f"{value:,.2f}"
    if value >= 100:
        return f"{value:,.2f}"
    if value >= 1:
        return f"{value:.4f}"
    if value >= 0.01:
        return f"{value:.5f}"
    return f"{value:.8g}"


def _fmt_money(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:,.2f}"


def _latest_scan_id(connection: sqlite3.Connection) -> str:
    row = connection.execute(
        """
        SELECT scan_id
        FROM scan_runs
        WHERE scan_id NOT LIKE 'verify_%'
        ORDER BY timestamp_utc DESC
        LIMIT 1
        """
    ).fetchone()
    if row is None:
        raise ValueError("No market scan found. Run `python main.py scan` first.")
    return str(row[0])


def _paper_trade_from_plan_row(row: sqlite3.Row) -> PaperTrade:
    entry_low = float(row["entry_low"] or 0)
    entry_high = float(row["entry_high"] or entry_low)
    stop = float(row["stop_current"] or row["stop_initial"] or 0)
    tp1 = float(row["tp1"] or 0)
    tp2 = float(row["tp2"] or 0)
    return PaperTrade(
        paper_trade_id=str(row["plan_id"]),
        account_name=str(row["account_name"]),
        source_scan_id=str(row["source_scan_id"] or ""),
        source_rank=int(row["source_rank"] or 0),
        symbol=str(row["symbol"]),
        base_asset=str(row["base_asset"] or str(row["symbol"]).removesuffix("USDT")),
        status=str(row["status"]),
        created_at_utc=str(row["created_at"]),
        updated_at_utc=str(row["updated_at"]),
        setup=str(row["setup"] or ""),
        verdict=str(row["verdict"] or ""),
        entry_low=entry_low,
        entry_high=entry_high,
        planned_entry_mid=float(row["planned_entry_mid"] or ((entry_low + entry_high) / 2)),
        stop_loss=stop,
        take_profit_1=tp1,
        take_profit_2=tp2,
        risk_reward_1=float(row["risk_reward_1"] or 0),
        risk_reward_2=float(row["risk_reward_2"] or 0),
        account_equity=float(row["account_equity"] or 0),
        risk_per_trade_pct=float(row["risk_per_trade_pct"] or 0),
        cash_risk=float(row["cash_risk"] or 0),
        quantity=None if row["quantity"] is None else float(row["quantity"]),
        entry_price=None if row["entry_price"] is None else float(row["entry_price"]),
        entered_at_utc=row["entered_at_utc"],
        tp1_hit_at_utc=row["tp1_hit_at_utc"],
        closed_at_utc=row["closed_at"],
        exit_price=None if row["exit_price"] is None else float(row["exit_price"]),
        realized_pnl=float(row["realized_pnl"] or 0),
        unrealized_pnl=float(row["unrealized_pnl"] or 0),
        last_price=None if row["last_price"] is None else float(row["last_price"]),
        notes=str(row["notes"] or row["created_reason"] or ""),
        tp1_trailing_ema_stop_active=bool(row["tp1_trailing_ema_stop_active"]),
    )


def _paper_event_from_structured_row(row: sqlite3.Row) -> PaperTradeEvent:
    payload = json.loads(row["raw_json"] or "{}")
    return PaperTradeEvent(
        event_id=str(row["event_id"]),
        paper_trade_id=str(row["plan_id"]),
        account_name=str(row["account_name"]),
        symbol=str(row["symbol"]),
        event_type=str(row["event_type"]),
        event_time_utc=str(row["event_time"]),
        price=None if row["price"] is None else float(row["price"]),
        quantity=None if payload.get("quantity") is None else float(payload["quantity"]),
        realized_pnl=float(payload.get("realized_pnl") or 0),
        unrealized_pnl=float(payload.get("unrealized_pnl") or 0),
        message=str(row["reason"] or ""),
    )


def _record_event(
    connection: sqlite3.Connection,
    trade: PaperTrade,
    event_type: str,
    message: str,
    event_time_utc: str | None = None,
    price: float | None = None,
    run_id: str | None = None,
    old_status: str | None = None,
    new_status: str | None = None,
    old_stop: float | None = None,
    new_stop: float | None = None,
    kline_time: str | None = None,
    structured_event_type: str | None = None,
) -> None:
    event_time = event_time_utc or _utc_now()
    database_event_type = structured_event_type or event_type
    if run_id is not None and database_event_type == "API_DELAY_SKIPPED" and kline_time is not None:
        existing = connection.execute(
            """
            SELECT 1 FROM paper_events
            WHERE plan_id = ? AND event_type = 'API_DELAY_SKIPPED' AND kline_time = ?
            LIMIT 1
            """,
            (trade.paper_trade_id, kline_time),
        ).fetchone()
        if existing is not None:
            return
    event_id = uuid.uuid4().hex[:12]
    if run_id is not None:
        cursor = connection.execute(
            """
            INSERT OR IGNORE INTO paper_events(
                event_id, plan_id, run_id, event_time, event_type, symbol, price,
                old_status, new_status, old_stop, new_stop, kline_time,
                reason, raw_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                trade.paper_trade_id,
                run_id,
                event_time,
                database_event_type,
                trade.symbol,
                trade.last_price if price is None else price,
                old_status,
                new_status,
                old_stop,
                new_stop,
                kline_time,
                message,
                json.dumps(
                    {
                        "quantity": trade.quantity,
                        "realized_pnl": trade.realized_pnl,
                        "unrealized_pnl": trade.unrealized_pnl,
                    },
                    ensure_ascii=False,
                ),
                event_time,
            ),
        )
        if cursor.rowcount == 0:
            return
    legacy_plan = connection.execute(
        "SELECT 1 FROM paper_trades WHERE paper_trade_id = ?",
        (trade.paper_trade_id,),
    ).fetchone()
    if legacy_plan is not None:
        connection.execute(
            """
            INSERT INTO paper_trade_events (
                event_id, paper_trade_id, account_name, symbol, event_type, event_time_utc,
                price, quantity, realized_pnl, unrealized_pnl, message
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event_id,
                trade.paper_trade_id,
                trade.account_name,
                trade.symbol,
                event_type,
                event_time,
                trade.last_price if price is None else price,
                trade.quantity,
                trade.realized_pnl,
                trade.unrealized_pnl,
                message,
            ),
        )


def _decision_label(accepted: bool) -> str:
    return "accept" if accepted else "reject"


def _active_position_count(connection: sqlite3.Connection, account_name: str) -> int:
    return int(
        connection.execute(
            """
            SELECT COUNT(*)
            FROM paper_plans
            WHERE account_name = ? AND status IN ('ENTERED', 'TP1_HIT')
            """,
            (account_name,),
        ).fetchone()[0]
    )


def _record_atr_reclaim_shadow_decisions(
    connection: sqlite3.Connection,
    *,
    settings: Settings,
    trade: PaperTrade,
    account_name: str,
    run_id: str | None,
    decision_time_utc: str,
    current_price: float,
    last_4h_close: float,
    kline_time: str | None,
    closed_4h: list[list],
) -> None:
    atr_4h = _atr(closed_4h)
    reference_accepted = last_4h_close >= trade.entry_high
    atr_accepted = bool(
        atr_4h is not None
        and atr_4h > 0
        and last_4h_close >= trade.entry_high + 0.35 * atr_4h
    )
    reclaim_margin_atr = None
    if atr_4h is not None and atr_4h > 0:
        reclaim_margin_atr = (last_4h_close - trade.entry_high) / atr_4h
    active_positions = _active_position_count(connection, account_name)
    max_active_positions = settings.backtest.max_active_positions
    capacity_state = "at_capacity" if active_positions >= max_active_positions else "capacity_available"
    opportunity_id = f"paper_plan:{trade.paper_trade_id}"
    reference_decision = _decision_label(reference_accepted)
    atr_decision = _decision_label(atr_accepted)
    lines = [
        (
            "reference_baseline",
            reference_accepted,
            "first 4h close >= entry_high" if reference_accepted else "4h close below entry_high",
        ),
        (
            "atr_reclaim_0_35_shadow",
            atr_accepted,
            "close >= entry_high + 0.35 ATR" if atr_accepted else "close below entry_high + 0.35 ATR",
        ),
        (
            "research_incumbent",
            atr_accepted,
            "same decision as atr_reclaim_0_35_shadow",
        ),
    ]
    for line_name, accepted, reason in lines:
        decision = _decision_label(accepted)
        payload = {
            "paper_deployment": "not_controlled_by_shadow",
            "entry_reclaim_min_atr": 0.35,
            "line_name": line_name,
            "reference_baseline_decision": reference_decision,
            "atr_reclaim_0_35_decision": atr_decision,
            "research_incumbent_decision": atr_decision,
        }
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_shadow_decisions(
                decision_id, run_id, account_name, opportunity_id, plan_id, symbol,
                decision_time, kline_time, line_name, controls_paper, decision,
                accepted, reject_reason, reference_baseline_decision,
                atr_reclaim_0_35_decision, research_incumbent_decision,
                current_price, last_4h_close, entry_high, atr_4h,
                reclaim_margin_atr, active_positions, max_active_positions,
                capacity_state, direct_filter_contribution_r,
                path_capacity_contribution_r, raw_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                uuid.uuid4().hex[:12],
                run_id,
                account_name,
                opportunity_id,
                trade.paper_trade_id,
                trade.symbol,
                decision_time_utc,
                kline_time,
                line_name,
                decision,
                1 if accepted else 0,
                None if accepted else reason,
                reference_decision,
                atr_decision,
                atr_decision,
                current_price,
                last_4h_close,
                trade.entry_high,
                atr_4h,
                reclaim_margin_atr,
                active_positions,
                max_active_positions,
                capacity_state,
                None,
                None,
                json.dumps(payload, ensure_ascii=False, sort_keys=True),
                decision_time_utc,
            ),
        )


def _record_candidate_shadow_context(
    connection: sqlite3.Connection,
    *,
    settings: Settings,
    account_name: str,
    run_id: str | None,
    scan_id: str,
    scan_time: str,
    payload: dict,
    source_rank: int,
    plan_id: str | None = None,
) -> None:
    symbol = str(payload["symbol"])
    action = str(payload.get("action", "WATCH_ONLY")).upper()
    entry_high = None if payload.get("entry_high") is None else float(payload["entry_high"])
    current_price = None if payload.get("price") is None else float(payload["price"])
    active_positions = _active_position_count(connection, account_name)
    max_active_positions = settings.backtest.max_active_positions
    capacity_state = "at_capacity" if active_positions >= max_active_positions else "capacity_available"
    opportunity_id = f"scan_candidate:{scan_id}:{symbol}"
    lines = ("reference_baseline", "atr_reclaim_0_35_shadow", "research_incumbent")
    for line_name in lines:
        line_decision = "candidate_registered"
        decision_key = f"{opportunity_id}:{line_name}:{scan_time}"
        decision_id = hashlib.sha256(decision_key.encode("utf-8")).hexdigest()[:12]
        payload_json = {
            "stage": "daily_import_candidate_context",
            "paper_deployment": "not_controlled_by_shadow",
            "line_name": line_name,
            "scan_id": scan_id,
            "source_rank": source_rank,
            "scanner_action": action,
            "entry_reclaim_min_atr": 0.35 if line_name != "reference_baseline" else 0.0,
        }
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_shadow_decisions(
                decision_id, run_id, account_name, opportunity_id, plan_id, symbol,
                decision_time, kline_time, line_name, controls_paper, decision,
                accepted, reject_reason, reference_baseline_decision,
                atr_reclaim_0_35_decision, research_incumbent_decision,
                current_price, last_4h_close, entry_high, atr_4h,
                reclaim_margin_atr, active_positions, max_active_positions,
                capacity_state, direct_filter_contribution_r,
                path_capacity_contribution_r, raw_json, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, 0, ?, 1, NULL, ?, ?, ?, ?, NULL, ?, NULL, NULL, ?, ?, ?, NULL, NULL, ?, ?)
            """,
            (
                decision_id,
                run_id,
                account_name,
                opportunity_id,
                plan_id,
                symbol,
                scan_time,
                line_name,
                line_decision,
                line_decision,
                line_decision,
                line_decision,
                current_price,
                entry_high,
                active_positions,
                max_active_positions,
                capacity_state,
                json.dumps(payload_json, ensure_ascii=False, sort_keys=True),
                scan_time,
            ),
        )


def _candidate_float(payload: dict, key: str) -> float | None:
    value = payload.get(key)
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _record_candidate_observation(
    connection: sqlite3.Connection,
    *,
    settings: Settings,
    account_name: str,
    run_id: str | None,
    scan_id: str,
    scan_time: str,
    payload: dict,
    source_rank: int,
    signal_density: int,
) -> str:
    symbol = str(payload["symbol"])
    active_positions = _active_position_count(connection, account_name)
    max_active_positions = settings.backtest.max_active_positions
    capacity_state = "at_capacity" if active_positions >= max_active_positions else "capacity_available"
    observation_key = f"{account_name}:{scan_id}:{symbol}"
    observation_id = hashlib.sha256(observation_key.encode("utf-8")).hexdigest()[:12]
    action = str(payload.get("action", "WATCH_ONLY")).upper()
    market_regime = payload.get("market_regime")
    if not market_regime:
        scan_row = connection.execute(
            "SELECT market_regime FROM market_scans WHERE scan_id = ?",
            (scan_id,),
        ).fetchone()
        market_regime = None if scan_row is None else scan_row["market_regime"]
    values = {
        "observation_id": observation_id,
        "account_name": account_name,
        "run_id": run_id,
        "scan_id": scan_id,
        "scan_time": scan_time,
        "symbol": symbol,
        "source_rank": source_rank,
        "scanner_action": action,
        "score": _candidate_float(payload, "score"),
        "market_regime": market_regime,
        "signal_density": signal_density,
        "active_positions": active_positions,
        "max_active_positions": max_active_positions,
        "capacity_state": capacity_state,
        "would_be_blocked_by_capacity": 1 if capacity_state == "at_capacity" else 0,
        "price": _candidate_float(payload, "price"),
        "entry_low": _candidate_float(payload, "entry_low"),
        "entry_high": _candidate_float(payload, "entry_high"),
        "stop_loss": _candidate_float(payload, "stop_loss"),
        "tp1": _candidate_float(payload, "take_profit_1"),
        "tp2": _candidate_float(payload, "take_profit_2"),
        "atr_4h": _candidate_float(payload, "atr_4h"),
        "rsi_1h": _candidate_float(payload, "rsi_1h"),
        "rsi_4h": _candidate_float(payload, "rsi_4h"),
        "ema20_4h": _candidate_float(payload, "ema20_4h"),
        "ema50_4h": _candidate_float(payload, "ema50_4h"),
        "ema20_1d": _candidate_float(payload, "ema20_1d"),
        "ema50_1d": _candidate_float(payload, "ema50_1d"),
        "pct_24h": _candidate_float(payload, "pct_24h"),
        "pct_3d": _candidate_float(payload, "pct_3d"),
        "pct_7d": _candidate_float(payload, "pct_7d"),
        "quote_volume_24h": _candidate_float(payload, "quote_volume_24h"),
        "volume_ratio_24h": _candidate_float(payload, "volume_ratio_24h"),
        "high_low_range_24h": _candidate_float(payload, "high_low_range_24h"),
        "raw_json": json.dumps(payload, ensure_ascii=False, sort_keys=True),
        "created_at": scan_time,
        "updated_at": scan_time,
    }
    connection.execute(
        """
        INSERT INTO paper_shadow_candidate_observations(
            observation_id, account_name, run_id, scan_id, scan_time, symbol, source_rank,
            scanner_action, score, market_regime, sample_level, signal_density,
            active_positions, max_active_positions, capacity_state, would_be_blocked_by_capacity,
            price, entry_low, entry_high, stop_loss, tp1, tp2, atr_4h, rsi_1h, rsi_4h,
            ema20_4h, ema50_4h, ema20_1d, ema50_1d, pct_24h, pct_3d, pct_7d,
            quote_volume_24h, volume_ratio_24h, high_low_range_24h, raw_json,
            created_at, updated_at
        ) VALUES (
            :observation_id, :account_name, :run_id, :scan_id, :scan_time, :symbol, :source_rank,
            :scanner_action, :score, :market_regime, 'candidate_level', :signal_density,
            :active_positions, :max_active_positions, :capacity_state, :would_be_blocked_by_capacity,
            :price, :entry_low, :entry_high, :stop_loss, :tp1, :tp2, :atr_4h, :rsi_1h, :rsi_4h,
            :ema20_4h, :ema50_4h, :ema20_1d, :ema50_1d, :pct_24h, :pct_3d, :pct_7d,
            :quote_volume_24h, :volume_ratio_24h, :high_low_range_24h, :raw_json,
            :created_at, :updated_at
        )
        ON CONFLICT(account_name, scan_id, symbol) DO UPDATE SET
            run_id=COALESCE(excluded.run_id, paper_shadow_candidate_observations.run_id),
            scanner_action=excluded.scanner_action,
            score=excluded.score,
            market_regime=COALESCE(excluded.market_regime, paper_shadow_candidate_observations.market_regime),
            signal_density=excluded.signal_density,
            active_positions=excluded.active_positions,
            max_active_positions=excluded.max_active_positions,
            capacity_state=excluded.capacity_state,
            would_be_blocked_by_capacity=excluded.would_be_blocked_by_capacity,
            price=excluded.price,
            entry_low=excluded.entry_low,
            entry_high=excluded.entry_high,
            stop_loss=excluded.stop_loss,
            tp1=excluded.tp1,
            tp2=excluded.tp2,
            atr_4h=excluded.atr_4h,
            raw_json=excluded.raw_json,
            updated_at=excluded.updated_at
        """,
        values,
    )
    for line_name in ("reference_baseline", "atr_reclaim_0_35_shadow", "research_incumbent"):
        outcome_key = f"{observation_id}:{line_name}"
        outcome_id = hashlib.sha256(outcome_key.encode("utf-8")).hexdigest()[:12]
        connection.execute(
            """
            INSERT OR IGNORE INTO paper_shadow_counterfactual_outcomes(
                outcome_id, observation_id, account_name, run_id, line_name, symbol,
                maturity_state, right_censored, raw_json, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, 'not_entered', 1, ?, ?, ?)
            """,
            (
                outcome_id,
                observation_id,
                account_name,
                run_id,
                line_name,
                symbol,
                json.dumps({"paper_deployment": "not_controlled_by_shadow"}, sort_keys=True),
                scan_time,
                scan_time,
            ),
        )
    return observation_id


def _virtual_trade_from_observation(row: sqlite3.Row, status: str = "WATCHING") -> PaperTrade | None:
    entry_low = row["entry_low"]
    entry_high = row["entry_high"]
    stop_loss = row["stop_loss"]
    tp1 = row["tp1"]
    tp2 = row["tp2"]
    price = row["price"]
    if None in (entry_low, entry_high, stop_loss, tp1, tp2):
        return None
    return PaperTrade(
        paper_trade_id=str(row["observation_id"]),
        account_name=str(row["account_name"]),
        source_scan_id=str(row["scan_id"]),
        source_rank=int(row["source_rank"] or 0),
        symbol=str(row["symbol"]),
        base_asset=str(row["symbol"]).removesuffix("USDT"),
        status=status,
        created_at_utc=str(row["scan_time"]),
        updated_at_utc=str(row["scan_time"]),
        setup="counterfactual_shadow_candidate",
        verdict=str(row["scanner_action"] or ""),
        entry_low=float(entry_low),
        entry_high=float(entry_high),
        planned_entry_mid=(float(entry_low) + float(entry_high)) / 2,
        stop_loss=float(stop_loss),
        take_profit_1=float(tp1),
        take_profit_2=float(tp2),
        risk_reward_1=0.0,
        risk_reward_2=0.0,
        account_equity=0.0,
        risk_per_trade_pct=0.0,
        cash_risk=1.0,
        last_price=None if price is None else float(price),
        notes="Counterfactual candidate path.",
    )


def _restore_virtual_trade(row: sqlite3.Row) -> PaperTrade | None:
    raw = json.loads(row["outcome_raw_json"] or "{}")
    trade_state = raw.get("trade_state")
    if isinstance(trade_state, dict):
        try:
            return PaperTrade(**trade_state)
        except TypeError:
            pass
    return _virtual_trade_from_observation(row)


def _counterfactual_entry_allowed(row: sqlite3.Row, line_name: str, last_close: float, atr_4h: float | None) -> bool:
    entry_high = row["entry_high"]
    if entry_high is None:
        return False
    if line_name == "reference_baseline":
        return last_close >= float(entry_high)
    if atr_4h is None or atr_4h <= 0:
        return False
    return last_close >= float(entry_high) + 0.35 * atr_4h


def _update_shadow_counterfactual_outcomes(
    connection: sqlite3.Connection,
    *,
    settings: Settings,
    account_name: str,
    run_id: str | None,
    now: str,
    get_closed_4h,
) -> int:
    rows = connection.execute(
        """
        SELECT
            o.outcome_id,
            o.line_name,
            o.would_enter,
            o.entry_triggered_at,
            o.entry_price_assumption,
            o.mfe_r,
            o.mae_r,
            o.bars_observed,
            o.maturity_state,
            o.last_observed_at,
            o.raw_json AS outcome_raw_json,
            c.*
        FROM paper_shadow_counterfactual_outcomes o
        JOIN paper_shadow_candidate_observations c ON c.observation_id = o.observation_id
        WHERE o.account_name = ?
          AND o.maturity_state NOT IN ('terminal_stopped', 'terminal_closed', 'terminal_invalidated', 'terminal_time_exit')
        ORDER BY c.scan_time, c.source_rank, o.line_name
        """,
        (account_name,),
    ).fetchall()
    updated = 0
    closed_4h_cache: dict[str, list] = {}
    for row in rows:
        symbol = str(row["symbol"])
        try:
            if symbol not in closed_4h_cache:
                closed_4h_cache[symbol] = get_closed_4h(symbol)
            closed_4h = closed_4h_cache[symbol]
        except Exception:
            continue
        if not closed_4h:
            continue
        latest = closed_4h[-1]
        kline_time = datetime.fromtimestamp(
            int(latest[6]) / 1000,
            tz=timezone.utc,
        ).isoformat(timespec="seconds").replace("+00:00", "Z")
        if str(row["scan_time"]) >= kline_time or str(row["last_observed_at"] or "") == kline_time:
            continue
        high = float(latest[2])
        low = float(latest[3])
        close = float(latest[4])
        atr_4h = _atr(closed_4h)
        trade = _restore_virtual_trade(row)
        if trade is None:
            continue
        raw = json.loads(row["outcome_raw_json"] or "{}")
        events_payload: list[dict] = list(raw.get("events", [])) if isinstance(raw.get("events"), list) else []
        would_enter = int(row["would_enter"] or 0)
        entry_triggered_at = row["entry_triggered_at"]
        entry_price = None if row["entry_price_assumption"] is None else float(row["entry_price_assumption"])

        if not would_enter:
            if not _counterfactual_entry_allowed(row, str(row["line_name"]), close, atr_4h):
                connection.execute(
                    """
                    UPDATE paper_shadow_counterfactual_outcomes
                    SET bars_observed = bars_observed + 1,
                        maturity_state = 'not_entered',
                        right_censored = 1,
                        last_observed_at = ?,
                        raw_json = ?,
                        updated_at = ?
                    WHERE outcome_id = ?
                    """,
                    (
                        kline_time,
                        json.dumps(
                            {
                                "paper_deployment": "not_controlled_by_shadow",
                                "last_close": close,
                                "atr_4h": atr_4h,
                                "entry_reclaim_min_atr": 0.0 if row["line_name"] == "reference_baseline" else 0.35,
                            },
                            ensure_ascii=False,
                            sort_keys=True,
                        ),
                        now,
                        row["outcome_id"],
                    ),
                )
                updated += 1
                continue
            would_enter = 1
            entry_triggered_at = kline_time
            entry_price = float(row["entry_high"])
            trade.status = "ENTERED"
            trade.entry_price = entry_price
            trade.entered_at_utc = kline_time
            risk = entry_price - trade.stop_loss
            if risk > 0:
                trade.quantity = trade.cash_risk / risk
            trade.updated_at_utc = kline_time
            events_payload.append(
                {
                    "event_type": "COUNTERFACTUAL_ENTERED",
                    "event_time_utc": kline_time,
                    "price": entry_price,
                }
            )

        events = step_trade(
            trade,
            high=high,
            low=low,
            close=close,
            event_time_utc=kline_time,
            entry_price_override=entry_price,
            move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
        )
        events_payload.extend(asdict(event) for event in events)
        risk_per_unit = None
        if entry_price is not None:
            risk_per_unit = entry_price - trade.stop_loss if trade.status == "WATCHING" else entry_price - float(row["stop_loss"])
        mfe_r = row["mfe_r"]
        mae_r = row["mae_r"]
        if risk_per_unit is not None and risk_per_unit > 0:
            bar_mfe = (high - entry_price) / risk_per_unit
            bar_mae = (low - entry_price) / risk_per_unit
            mfe_r = bar_mfe if mfe_r is None else max(float(mfe_r), bar_mfe)
            mae_r = bar_mae if mae_r is None else min(float(mae_r), bar_mae)
        first_terminal_event = None
        terminal_at = None
        terminal_price = None
        realized_r = None
        maturity_state = "open_entered"
        right_censored = 1
        if trade.status in {"STOPPED", "CLOSED", "INVALIDATED"}:
            first_terminal_event = trade.status
            terminal_at = trade.closed_at_utc
            terminal_price = trade.exit_price
            if entry_price is not None and terminal_price is not None and risk_per_unit is not None and risk_per_unit > 0:
                realized_r = (terminal_price - entry_price) / risk_per_unit
            maturity_state = {
                "STOPPED": "terminal_stopped",
                "CLOSED": "terminal_closed",
                "INVALIDATED": "terminal_invalidated",
            }[trade.status]
            right_censored = 0
        raw_json = json.dumps(
            {
                "paper_deployment": "not_controlled_by_shadow",
                "trade_state": asdict(trade),
                "events": events_payload,
                "last_close": close,
                "atr_4h": atr_4h,
                "entry_reclaim_min_atr": 0.0 if row["line_name"] == "reference_baseline" else 0.35,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        connection.execute(
            """
            UPDATE paper_shadow_counterfactual_outcomes
            SET run_id = COALESCE(?, run_id),
                would_enter = ?,
                entry_triggered_at = ?,
                entry_price_assumption = ?,
                first_terminal_event = COALESCE(?, first_terminal_event),
                terminal_at = COALESCE(?, terminal_at),
                terminal_price = COALESCE(?, terminal_price),
                realized_r = COALESCE(?, realized_r),
                mfe_r = ?,
                mae_r = ?,
                bars_observed = bars_observed + 1,
                maturity_state = ?,
                right_censored = ?,
                last_observed_at = ?,
                raw_json = ?,
                updated_at = ?
            WHERE outcome_id = ?
            """,
            (
                run_id,
                would_enter,
                entry_triggered_at,
                entry_price,
                first_terminal_event,
                terminal_at,
                terminal_price,
                realized_r,
                mfe_r,
                mae_r,
                maturity_state,
                right_censored,
                kline_time,
                raw_json,
                now,
                row["outcome_id"],
            ),
        )
        updated += 1
    return updated


def _sync_paper_plan(
    connection: sqlite3.Connection,
    trade: PaperTrade,
    *,
    run_id: str | None = None,
    payload: dict | None = None,
) -> None:
    raw_json = json.dumps(
        {"trade_state": asdict(trade), "source_payload": payload or {}},
        ensure_ascii=False,
    )
    initial_stop = trade.stop_loss
    if payload is not None and payload.get("stop_loss") is not None:
        initial_stop = float(payload["stop_loss"])
    market_regime_row = connection.execute(
        "SELECT market_regime FROM market_scans WHERE scan_id = ?",
        (trade.source_scan_id,),
    ).fetchone()
    market_regime = None if market_regime_row is None else market_regime_row["market_regime"]
    values = {
        "plan_id": trade.paper_trade_id,
        "account_name": trade.account_name,
        "source_scan_id": trade.source_scan_id,
        "source_symbol": trade.symbol,
        "created_run_id": run_id,
        "created_at": trade.created_at_utc,
        "symbol": trade.symbol,
        "entry_low": trade.entry_low,
        "entry_high": trade.entry_high,
        "stop_initial": initial_stop,
        "stop_current": trade.stop_loss,
        "tp1": trade.take_profit_1,
        "tp2": trade.take_profit_2,
        "status": trade.status,
        "created_reason": trade.notes,
        "market_regime": market_regime,
        "raw_json": raw_json,
        "updated_at": trade.updated_at_utc,
        "closed_at": trade.closed_at_utc,
        "source_rank": trade.source_rank,
        "base_asset": trade.base_asset,
        "setup": trade.setup,
        "verdict": trade.verdict,
        "planned_entry_mid": trade.planned_entry_mid,
        "risk_reward_1": trade.risk_reward_1,
        "risk_reward_2": trade.risk_reward_2,
        "account_equity": trade.account_equity,
        "risk_per_trade_pct": trade.risk_per_trade_pct,
        "cash_risk": trade.cash_risk,
        "quantity": trade.quantity,
        "entry_price": trade.entry_price,
        "entered_at_utc": trade.entered_at_utc,
        "tp1_hit_at_utc": trade.tp1_hit_at_utc,
        "exit_price": trade.exit_price,
        "realized_pnl": trade.realized_pnl,
        "unrealized_pnl": trade.unrealized_pnl,
        "last_price": trade.last_price,
        "notes": trade.notes,
        "tp1_trailing_ema_stop_active": 1 if trade.tp1_trailing_ema_stop_active else 0,
    }
    connection.execute(
        """
        INSERT INTO paper_plans(
            plan_id, account_name, source_scan_id, source_symbol, created_run_id,
            created_at, symbol, entry_low, entry_high, stop_initial, stop_current,
            tp1, tp2, status, created_reason, market_regime, raw_json, updated_at, closed_at,
            source_rank, base_asset, setup, verdict, planned_entry_mid, risk_reward_1,
            risk_reward_2, account_equity, risk_per_trade_pct, cash_risk, quantity,
            entry_price, entered_at_utc, tp1_hit_at_utc, exit_price, realized_pnl,
            unrealized_pnl, last_price, notes, tp1_trailing_ema_stop_active
        ) VALUES (
            :plan_id, :account_name, :source_scan_id, :source_symbol, :created_run_id,
            :created_at, :symbol, :entry_low, :entry_high, :stop_initial, :stop_current,
            :tp1, :tp2, :status, :created_reason, :market_regime, :raw_json, :updated_at, :closed_at,
            :source_rank, :base_asset, :setup, :verdict, :planned_entry_mid, :risk_reward_1,
            :risk_reward_2, :account_equity, :risk_per_trade_pct, :cash_risk, :quantity,
            :entry_price, :entered_at_utc, :tp1_hit_at_utc, :exit_price, :realized_pnl,
            :unrealized_pnl, :last_price, :notes, :tp1_trailing_ema_stop_active
        )
        ON CONFLICT(plan_id) DO UPDATE SET
            stop_current=excluded.stop_current,
            status=excluded.status,
            created_reason=excluded.created_reason,
            market_regime=COALESCE(excluded.market_regime, paper_plans.market_regime),
            raw_json=excluded.raw_json,
            updated_at=excluded.updated_at,
            closed_at=excluded.closed_at,
            source_rank=excluded.source_rank,
            base_asset=excluded.base_asset,
            setup=excluded.setup,
            verdict=excluded.verdict,
            planned_entry_mid=excluded.planned_entry_mid,
            risk_reward_1=excluded.risk_reward_1,
            risk_reward_2=excluded.risk_reward_2,
            account_equity=excluded.account_equity,
            risk_per_trade_pct=excluded.risk_per_trade_pct,
            cash_risk=excluded.cash_risk,
            quantity=excluded.quantity,
            entry_price=excluded.entry_price,
            entered_at_utc=excluded.entered_at_utc,
            tp1_hit_at_utc=excluded.tp1_hit_at_utc,
            exit_price=excluded.exit_price,
            realized_pnl=excluded.realized_pnl,
            unrealized_pnl=excluded.unrealized_pnl,
            last_price=excluded.last_price,
            notes=excluded.notes,
            tp1_trailing_ema_stop_active=excluded.tp1_trailing_ema_stop_active
        """,
        values,
    )


def _write_snapshot(connection: sqlite3.Connection, trade: PaperTrade, run_id: str, snapshot_time: str) -> None:
    holding_hours = None
    if trade.entered_at_utc:
        entered = datetime.fromisoformat(trade.entered_at_utc.replace("Z", "+00:00"))
        end = datetime.fromisoformat((trade.closed_at_utc or snapshot_time).replace("Z", "+00:00"))
        holding_hours = max(0.0, (end - entered).total_seconds() / 3600)
    connection.execute(
        """
        INSERT INTO paper_snapshots(
            snapshot_id, run_id, snapshot_time, plan_id, symbol, status,
            current_price, entry_price, stop_current, tp1, tp2, tp1_hit,
            ema_trailing_active, ema_stop, unrealized_pnl, realized_pnl,
            holding_hours, raw_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(run_id, plan_id) DO UPDATE SET
            snapshot_time=excluded.snapshot_time,
            status=excluded.status,
            current_price=excluded.current_price,
            entry_price=excluded.entry_price,
            stop_current=excluded.stop_current,
            tp1_hit=excluded.tp1_hit,
            ema_trailing_active=excluded.ema_trailing_active,
            ema_stop=excluded.ema_stop,
            unrealized_pnl=excluded.unrealized_pnl,
            realized_pnl=excluded.realized_pnl,
            holding_hours=excluded.holding_hours,
            raw_json=excluded.raw_json
        """,
        (
            uuid.uuid4().hex,
            run_id,
            snapshot_time,
            trade.paper_trade_id,
            trade.symbol,
            trade.status,
            trade.last_price,
            trade.entry_price,
            trade.stop_loss,
            trade.take_profit_1,
            trade.take_profit_2,
            1 if trade.tp1_hit_at_utc or trade.status == "TP1_HIT" else 0,
            1 if trade.tp1_trailing_ema_stop_active else 0,
            trade.stop_loss if trade.tp1_trailing_ema_stop_active else None,
            trade.unrealized_pnl,
            trade.realized_pnl,
            holding_hours,
            json.dumps(asdict(trade), ensure_ascii=False),
            snapshot_time,
        ),
    )


def _structured_step_event_type(event_type: str, message: str, had_reclaim_pending: bool) -> str:
    if event_type == "ENTERED" and had_reclaim_pending:
        return "RECLAIM_CONFIRMED_ENTERED"
    if event_type == "STOPPED" and "EMA20 trailing stop" in message:
        return "EMA_TRAILING_STOPPED"
    if event_type == "CLOSED" and "TP2 hit" in message:
        return "TP2_HIT"
    return event_type


def _insert_paper_trade(connection: sqlite3.Connection, trade: PaperTrade, payload: dict) -> bool:
    try:
        connection.execute(
            """
            INSERT INTO paper_trades (
                paper_trade_id, account_name, source_scan_id, source_rank,
                symbol, base_asset, status, created_at_utc, updated_at_utc,
                setup, verdict, entry_low, entry_high, planned_entry_mid,
                stop_loss, take_profit_1, take_profit_2, risk_reward_1, risk_reward_2,
                account_equity, risk_per_trade_pct, cash_risk, quantity, entry_price,
                entered_at_utc, tp1_hit_at_utc, closed_at_utc, exit_price,
                realized_pnl, unrealized_pnl, last_price, notes,
                tp1_trailing_ema_stop_active, payload_json
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                trade.paper_trade_id,
                trade.account_name,
                trade.source_scan_id,
                trade.source_rank,
                trade.symbol,
                trade.base_asset,
                trade.status,
                trade.created_at_utc,
                trade.updated_at_utc,
                trade.setup,
                trade.verdict,
                trade.entry_low,
                trade.entry_high,
                trade.planned_entry_mid,
                trade.stop_loss,
                trade.take_profit_1,
                trade.take_profit_2,
                trade.risk_reward_1,
                trade.risk_reward_2,
                trade.account_equity,
                trade.risk_per_trade_pct,
                trade.cash_risk,
                trade.quantity,
                trade.entry_price,
                trade.entered_at_utc,
                trade.tp1_hit_at_utc,
                trade.closed_at_utc,
                trade.exit_price,
                trade.realized_pnl,
                trade.unrealized_pnl,
                trade.last_price,
                trade.notes,
                1 if trade.tp1_trailing_ema_stop_active else 0,
                json.dumps(payload, ensure_ascii=False),
            ),
        )
        return True
    except sqlite3.IntegrityError:
        return False


def _archive_replaced_watching_trades(
    connection: sqlite3.Connection,
    account_name: str,
    symbol: str,
    replacement_scan_id: str,
    now: str,
    run_id: str | None = None,
) -> int:
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT *
        FROM paper_plans
        WHERE account_name = ?
          AND symbol = ?
          AND status = 'WATCHING'
          AND source_scan_id <> ?
        """,
        (account_name, symbol, replacement_scan_id),
    ).fetchall()

    archived = 0
    for row in rows:
        old_trade = _paper_trade_from_plan_row(row)
        old_trade.status = "ARCHIVED"
        old_trade.updated_at_utc = now
        old_trade.closed_at_utc = now
        old_trade.notes = f"Archived because scan {replacement_scan_id} created a newer WATCHING plan for {symbol}."
        _save_trade_update(connection, old_trade, expected_status="WATCHING")
        _record_event(
            connection,
            old_trade,
            "ARCHIVED",
            old_trade.notes,
            event_time_utc=now,
            price=old_trade.last_price,
            run_id=run_id,
            old_status="WATCHING",
            new_status="ARCHIVED",
            old_stop=old_trade.stop_loss,
            new_stop=old_trade.stop_loss,
            structured_event_type="ARCHIVED",
        )
        archived += 1
    return archived


def add_from_scan(
    settings: Settings,
    scan_id: str | None = None,
    account_name: str | None = None,
    run_id: str | None = None,
) -> dict:
    account = account_name or settings.paper.account_name
    now = _utc_now()
    added = 0
    skipped = 0
    skipped_action = 0
    archived = 0
    allowed_actions = {action.upper() for action in settings.paper.import_actions}

    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        chosen_scan_id = scan_id or _latest_scan_id(connection)
        scan_time_row = connection.execute(
            "SELECT scan_time FROM market_scans WHERE scan_id = ?",
            (chosen_scan_id,),
        ).fetchone()
        if scan_time_row is None:
            scan_time_row = connection.execute(
                "SELECT timestamp_utc FROM scan_runs WHERE scan_id = ?",
                (chosen_scan_id,),
            ).fetchone()
        scan_time = str(scan_time_row[0]) if scan_time_row is not None else now
        rows = connection.execute(
            """
            SELECT rank, payload_json
            FROM scan_candidates
            WHERE scan_id = ?
            ORDER BY rank
            """,
            (chosen_scan_id,),
        ).fetchall()
        if not rows:
            raise ValueError(f"No candidates found for scan_id={chosen_scan_id}")
        signal_density = len(rows)

        for row in rows:
            payload = json.loads(row["payload_json"])
            _record_candidate_observation(
                connection,
                settings=settings,
                account_name=account,
                run_id=run_id,
                scan_id=chosen_scan_id,
                scan_time=scan_time,
                payload=payload,
                source_rank=int(row["rank"]),
                signal_density=signal_density,
            )
            _record_candidate_shadow_context(
                connection,
                settings=settings,
                account_name=account,
                run_id=run_id,
                scan_id=chosen_scan_id,
                scan_time=scan_time,
                payload=payload,
                source_rank=int(row["rank"]),
            )
            action = str(payload.get("action", "WATCH_ONLY")).upper()
            if action not in allowed_actions:
                skipped += 1
                skipped_action += 1
                continue
            archived += _archive_replaced_watching_trades(
                connection,
                account,
                payload["symbol"],
                chosen_scan_id,
                now,
                run_id,
            )
            entry_low = float(payload["entry_low"])
            entry_high = float(payload["entry_high"])
            planned_entry_mid = (entry_low + entry_high) / 2
            cash_risk = settings.paper.account_equity * settings.paper.risk_per_trade_pct
            trade = PaperTrade(
                paper_trade_id=uuid.uuid4().hex[:12],
                account_name=account,
                source_scan_id=chosen_scan_id,
                source_rank=int(row["rank"]),
                symbol=payload["symbol"],
                base_asset=payload["base_asset"],
                status="WATCHING",
                created_at_utc=now,
                updated_at_utc=now,
                setup=payload["setup"],
                verdict=payload["verdict"],
                entry_low=entry_low,
                entry_high=entry_high,
                planned_entry_mid=planned_entry_mid,
                stop_loss=float(payload["stop_loss"]),
                take_profit_1=float(payload["take_profit_1"]),
                take_profit_2=float(payload["take_profit_2"]),
                risk_reward_1=float(payload["risk_reward_1"]),
                risk_reward_2=float(payload["risk_reward_2"]),
                account_equity=settings.paper.account_equity,
                risk_per_trade_pct=settings.paper.risk_per_trade_pct,
                cash_risk=cash_risk,
                last_price=float(payload["price"]),
                notes="Imported from scan candidate.",
            )
            if _insert_paper_trade(connection, trade, payload):
                _sync_paper_plan(connection, trade, run_id=run_id, payload=payload)
                _record_event(
                    connection,
                    trade,
                    "WATCHLIST_ADDED",
                    (
                        f"Imported rank {trade.source_rank} from scan {trade.source_scan_id}; "
                        f"entry zone {trade.entry_low:.8g}-{trade.entry_high:.8g}."
                    ),
                    event_time_utc=now,
                    price=trade.last_price,
                    run_id=run_id,
                    old_status=None,
                    new_status="WATCHING",
                    old_stop=None,
                    new_stop=trade.stop_loss,
                    structured_event_type="PLAN_CREATED",
                )
                added += 1
            else:
                skipped += 1

    return {
        "scan_id": chosen_scan_id,
        "account_name": account,
        "added": added,
        "skipped": skipped,
        "skipped_action": skipped_action,
        "import_actions": sorted(allowed_actions),
        "archived": archived,
    }


def _load_open_trades(connection: sqlite3.Connection, account_name: str) -> list[PaperTrade]:
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT *
        FROM paper_plans
        WHERE account_name = ? AND status IN ('WATCHING', 'ENTERED', 'TP1_HIT')
        ORDER BY created_at, source_rank
        """,
        (account_name,),
    ).fetchall()
    return [_paper_trade_from_plan_row(row) for row in rows]


def _save_trade_update(
    connection: sqlite3.Connection,
    trade: PaperTrade,
    expected_status: str | None = None,
) -> None:
    if expected_status is not None and trade.status not in ALLOWED_TRANSITIONS.get(expected_status, set()):
        raise ValueError(f"Illegal paper state transition: {expected_status} -> {trade.status}")
    current = connection.execute(
        "SELECT status, stop_current, raw_json FROM paper_plans WHERE plan_id = ?",
        (trade.paper_trade_id,),
    ).fetchone()
    if current is None:
        raise RuntimeError(f"Paper plan not found: {trade.paper_trade_id}")
    current_stop = float(current["stop_current"])
    if trade.stop_loss + 1e-12 < current_stop:
        raise ValueError(
            f"Paper stop cannot decrease for {trade.paper_trade_id}: {current_stop} -> {trade.stop_loss}"
        )
    current_payload = json.loads(current["raw_json"] or "{}")
    source_payload = current_payload.get("source_payload", current_payload)
    raw_json = json.dumps(
        {"trade_state": asdict(trade), "source_payload": source_payload},
        ensure_ascii=False,
    )
    plan_sql = """
        UPDATE paper_plans
        SET status = ?, updated_at = ?, stop_current = ?, closed_at = ?,
            quantity = ?, entry_price = ?, entered_at_utc = ?, tp1_hit_at_utc = ?,
            exit_price = ?, realized_pnl = ?, unrealized_pnl = ?, last_price = ?,
            notes = ?, created_reason = ?, tp1_trailing_ema_stop_active = ?, raw_json = ?
        WHERE plan_id = ?
    """
    plan_params: list = [
        trade.status,
        trade.updated_at_utc,
        trade.stop_loss,
        trade.closed_at_utc,
        trade.quantity,
        trade.entry_price,
        trade.entered_at_utc,
        trade.tp1_hit_at_utc,
        trade.exit_price,
        trade.realized_pnl,
        trade.unrealized_pnl,
        trade.last_price,
        trade.notes,
        trade.notes,
        1 if trade.tp1_trailing_ema_stop_active else 0,
        raw_json,
        trade.paper_trade_id,
    ]
    if expected_status is not None:
        plan_sql += " AND status = ?"
        plan_params.append(expected_status)
    plan_cursor = connection.execute(plan_sql, tuple(plan_params))
    if plan_cursor.rowcount != 1:
        raise RuntimeError(
            f"Stale paper plan update rejected for {trade.paper_trade_id}: expected status {expected_status}."
        )

    legacy_sql = """
        UPDATE paper_trades
        SET status = ?, updated_at_utc = ?, quantity = ?, entry_price = ?,
            entered_at_utc = ?, tp1_hit_at_utc = ?, closed_at_utc = ?, exit_price = ?,
            realized_pnl = ?, unrealized_pnl = ?, last_price = ?, notes = ?,
            tp1_trailing_ema_stop_active = ?, stop_loss = ?
        WHERE paper_trade_id = ?
    """
    legacy_params: list = [
        trade.status,
        trade.updated_at_utc,
        trade.quantity,
        trade.entry_price,
        trade.entered_at_utc,
        trade.tp1_hit_at_utc,
        trade.closed_at_utc,
        trade.exit_price,
        trade.realized_pnl,
        trade.unrealized_pnl,
        trade.last_price,
        trade.notes,
        1 if trade.tp1_trailing_ema_stop_active else 0,
        trade.stop_loss,
        trade.paper_trade_id,
    ]
    connection.execute(legacy_sql, tuple(legacy_params))


def update_paper_trades(
    settings: Settings,
    account_name: str | None = None,
    run_id: str | None = None,
) -> list[PaperTrade]:
    account = account_name or settings.paper.account_name
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    updated: list[PaperTrade] = []
    now = _utc_now()

    with connect_db(settings.output.database_path) as connection:
        trades = _load_open_trades(connection, account)

    try:
        ticker_map = {item["symbol"]: float(item["lastPrice"]) for item in client.ticker_24hr()}
    except Exception as exc:
        expected_time = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
        for trade in trades:
            trade.updated_at_utc = now
            trade.notes = f"24h ticker unavailable; state update skipped: {type(exc).__name__}: {exc}"
            with connect_db(settings.output.database_path) as connection:
                _record_event(
                    connection,
                    trade,
                    "API_DELAY_SKIPPED",
                    trade.notes,
                    event_time_utc=now,
                    price=trade.last_price,
                    run_id=run_id,
                    old_status=trade.status,
                    new_status=trade.status,
                    old_stop=trade.stop_loss,
                    new_stop=trade.stop_loss,
                    kline_time=expected_time,
                    structured_event_type="API_DELAY_SKIPPED",
                )
                if run_id is not None:
                    _write_snapshot(connection, trade, run_id, now)
            updated.append(trade)
        return updated

    entry_reclaim_enabled = settings.analysis.entry_reclaim_close_enabled
    ema_trailing_enabled = settings.analysis.tp1_ema_trailing_stop_enabled

    # API 请求全部在写事务之外完成，避免网络等待期间占用 SQLite 锁。
    klines_4h_cache: dict[str, list[list]] = {}

    def _get_closed_4h(symbol: str) -> list[list]:
        if symbol not in klines_4h_cache:
            klines_4h_cache[symbol] = client.klines(symbol, "4h", limit=25)
        now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
        safety_buffer_ms = 60_000
        return [row for row in klines_4h_cache[symbol] if int(row[6]) <= now_ms - safety_buffer_ms]

    def _expected_4h_close_time() -> str:
        current = datetime.now(timezone.utc)
        boundary_hour = current.hour - (current.hour % 4)
        boundary = current.replace(hour=boundary_hour, minute=0, second=0, microsecond=0)
        return boundary.isoformat(timespec="seconds").replace("+00:00", "Z")

    errors: list[str] = []
    for trade in trades:
        try:
            current_price = ticker_map.get(trade.symbol)
            if current_price is None:
                trade.notes = f"{trade.notes} | No ticker price found during update."
                with connect_db(settings.output.database_path) as connection:
                    _save_trade_update(connection, trade, expected_status=trade.status)
                    if run_id is not None:
                        _write_snapshot(connection, trade, run_id, now)
                continue

            needs_closed_4h = (
                entry_reclaim_enabled and trade.status == "WATCHING" and current_price <= trade.entry_high
            ) or (ema_trailing_enabled and trade.status in {"ENTERED", "TP1_HIT"})
            try:
                closed_4h = _get_closed_4h(trade.symbol) if needs_closed_4h else []
            except Exception as exc:
                trade.last_price = current_price
                trade.updated_at_utc = now
                trade.notes = f"4h kline unavailable; state update skipped: {type(exc).__name__}: {exc}"
                with connect_db(settings.output.database_path) as connection:
                    _record_event(
                        connection,
                        trade,
                        "API_DELAY_SKIPPED",
                        trade.notes,
                        event_time_utc=now,
                        price=current_price,
                        run_id=run_id,
                        old_status=trade.status,
                        new_status=trade.status,
                        old_stop=trade.stop_loss,
                        new_stop=trade.stop_loss,
                        kline_time=_expected_4h_close_time(),
                        structured_event_type="API_DELAY_SKIPPED",
                    )
                    if run_id is not None:
                        _write_snapshot(connection, trade, run_id, now)
                updated.append(trade)
                continue
            if needs_closed_4h and not closed_4h:
                with connect_db(settings.output.database_path) as connection:
                    _record_event(
                        connection,
                        trade,
                        "API_DELAY_SKIPPED",
                        "4h kline not closed at update time, skip state update.",
                        event_time_utc=now,
                        price=current_price,
                        run_id=run_id,
                        old_status=trade.status,
                        new_status=trade.status,
                        old_stop=trade.stop_loss,
                        new_stop=trade.stop_loss,
                        kline_time=_expected_4h_close_time(),
                        structured_event_type="API_DELAY_SKIPPED",
                    )
                    if run_id is not None:
                        _write_snapshot(connection, trade, run_id, now)
                updated.append(trade)
                continue

            last_closed_time = None
            if closed_4h:
                last_closed_time = datetime.fromtimestamp(
                    int(closed_4h[-1][6]) / 1000,
                    tz=timezone.utc,
                ).isoformat(timespec="seconds").replace("+00:00", "Z")

            if (
                entry_reclaim_enabled
                and trade.status == "WATCHING"
                and current_price <= trade.entry_high
            ):
                last_close = float(closed_4h[-1][4])
                with connect_db(settings.output.database_path) as connection:
                    _record_atr_reclaim_shadow_decisions(
                        connection,
                        settings=settings,
                        trade=trade,
                        account_name=account,
                        run_id=run_id,
                        decision_time_utc=now,
                        current_price=current_price,
                        last_4h_close=last_close,
                        kline_time=last_closed_time,
                        closed_4h=closed_4h,
                    )
                if last_close < trade.entry_high:
                    old_status = trade.status
                    old_stop = trade.stop_loss
                    trade.last_price = current_price
                    trade.updated_at_utc = now
                    trade.notes = "Watching: entry zone touched, but 4h close has not reclaimed entry_high."
                    with connect_db(settings.output.database_path) as connection:
                        _save_trade_update(connection, trade, expected_status=old_status)
                        _record_event(
                            connection,
                            trade,
                            "RECLAIM_PENDING",
                            f"Entry zone touched (price={_fmt_price(current_price)}) but 4h close {_fmt_price(last_close)} < entry_high {_fmt_price(trade.entry_high)}; waiting for reclaim.",
                            price=current_price,
                            run_id=run_id,
                            old_status=old_status,
                            new_status=trade.status,
                            old_stop=old_stop,
                            new_stop=trade.stop_loss,
                            kline_time=last_closed_time,
                            structured_event_type="RECLAIM_PENDING_SET",
                        )
                        if run_id is not None:
                            _write_snapshot(connection, trade, run_id, now)
                    updated.append(trade)
                    continue

            ema20_4h: float | None = None
            ema20_4h_ready = False
            if ema_trailing_enabled and trade.status in {"ENTERED", "TP1_HIT"}:
                closes_4h = [float(row[4]) for row in closed_4h]
                if len(closes_4h) >= 20:
                    ema20_4h = _ema(closes_4h, 20)
                    ema20_4h_ready = True

            old_status = trade.status
            old_stop = trade.stop_loss
            had_reclaim_pending = False
            if old_status == "WATCHING":
                with connect_db(settings.output.database_path) as connection:
                    had_reclaim_pending = connection.execute(
                        """
                        SELECT 1 FROM paper_events
                        WHERE plan_id = ? AND event_type IN ('RECLAIM_PENDING', 'RECLAIM_PENDING_SET')
                        LIMIT 1
                        """,
                        (trade.paper_trade_id,),
                    ).fetchone() is not None
            events = step_trade(
                trade,
                high=current_price,
                low=current_price,
                close=current_price,
                event_time_utc=now,
                move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
                tp1_trailing_ema_stop=ema20_4h,
                tp1_trailing_ema_stop_ready=ema20_4h_ready,
            )
            with connect_db(settings.output.database_path) as connection:
                _save_trade_update(connection, trade, expected_status=old_status)
                for event in events:
                    structured_type = _structured_step_event_type(
                        event.event_type,
                        event.message,
                        had_reclaim_pending,
                    )
                    _record_event(
                        connection,
                        trade,
                        event.event_type,
                        event.message,
                        event_time_utc=event.event_time_utc,
                        price=event.price,
                        run_id=run_id,
                        old_status=old_status,
                        new_status=trade.status,
                        old_stop=old_stop,
                        new_stop=trade.stop_loss,
                        kline_time=last_closed_time,
                        structured_event_type=structured_type,
                    )
                if run_id is not None:
                    _write_snapshot(connection, trade, run_id, now)
            updated.append(trade)
        except Exception as exc:
            errors.append(f"{trade.paper_trade_id}/{trade.symbol}: {type(exc).__name__}: {exc}")
    if errors:
        raise RuntimeError("Paper update completed with plan errors: " + " | ".join(errors))
    with connect_db(settings.output.database_path) as connection:
        _update_shadow_counterfactual_outcomes(
            connection,
            settings=settings,
            account_name=account,
            run_id=run_id,
            now=now,
            get_closed_4h=_get_closed_4h,
        )
    return updated


def load_paper_events(settings: Settings, account_name: str | None = None) -> dict[str, list[PaperTradeEvent]]:
    account = account_name or settings.paper.account_name
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT e.*, p.account_name
            FROM paper_events e
            JOIN paper_plans p ON p.plan_id = e.plan_id
            WHERE p.account_name = ?
            ORDER BY e.event_time, e.event_type
            """,
            (account,),
        ).fetchall()

    events_by_trade: dict[str, list[PaperTradeEvent]] = {}
    for row in rows:
        event = _paper_event_from_structured_row(row)
        events_by_trade.setdefault(event.paper_trade_id, []).append(event)
    return events_by_trade


def backfill_missing_events(settings: Settings, account_name: str | None = None) -> int:
    account = account_name or settings.paper.account_name
    inserted = 0
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        trades = load_all_paper_trades(settings, account)
        for trade in trades:
            existing = connection.execute(
                "SELECT COUNT(*) FROM paper_trade_events WHERE paper_trade_id = ?",
                (trade.paper_trade_id,),
            ).fetchone()[0]
            if existing:
                continue
            _record_event(
                connection,
                trade,
                "WATCHLIST_ADDED",
                "Backfilled event: trade existed before event logging was enabled.",
                event_time_utc=trade.created_at_utc,
                price=trade.last_price,
            )
            inserted += 1
            if trade.entered_at_utc:
                _record_event(
                    connection,
                    trade,
                    "ENTERED",
                    "Backfilled event: trade was already entered before event logging was enabled.",
                    event_time_utc=trade.entered_at_utc,
                    price=trade.entry_price,
                )
                inserted += 1
            if trade.tp1_hit_at_utc:
                _record_event(
                    connection,
                    trade,
                    "TP1_HIT",
                    "Backfilled event: TP1 had already been hit before event logging was enabled.",
                    event_time_utc=trade.tp1_hit_at_utc,
                    price=trade.take_profit_1,
                )
                inserted += 1
            if trade.closed_at_utc:
                event_type = trade.status if trade.status in CLOSED_STATUSES else "CLOSED"
                _record_event(
                    connection,
                    trade,
                    event_type,
                    "Backfilled event: trade had already closed before event logging was enabled.",
                    event_time_utc=trade.closed_at_utc,
                    price=trade.exit_price,
                )
                inserted += 1
    return inserted


def load_all_paper_trades(settings: Settings, account_name: str | None = None) -> list[PaperTrade]:
    account = account_name or settings.paper.account_name
    with connect_db(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT *
            FROM paper_plans
            WHERE account_name = ?
            ORDER BY created_at DESC, source_rank
            """,
            (account,),
        ).fetchall()
    return [_paper_trade_from_plan_row(row) for row in rows]


def _event_time(event: PaperTradeEvent) -> datetime | None:
    try:
        return datetime.fromisoformat(event.event_time_utc)
    except ValueError:
        return None


def _events_after(events: list[PaperTradeEvent], anchor: PaperTradeEvent) -> list[PaperTradeEvent]:
    anchor_time = _event_time(anchor)
    if anchor_time is None:
        return []
    later: list[PaperTradeEvent] = []
    for event in events:
        event_time = _event_time(event)
        if event_time is not None and event_time > anchor_time:
            later.append(event)
    return later


def _reclaim_outcome(trade: PaperTrade, events: list[PaperTradeEvent]) -> tuple[str, str]:
    pending = [event for event in events if event.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}]
    if not pending:
        return "n/a", ""

    first_pending = pending[0]
    later = _events_after(events, first_pending)
    entered = next(
        (event for event in later if event.event_type in {"ENTERED", "RECLAIM_CONFIRMED_ENTERED"}),
        None,
    )
    if entered is not None:
        after_entry = _events_after(events, entered)
        terminal = next(
            (event for event in after_entry if event.event_type in {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"}),
            None,
        )
        if terminal is not None:
            return f"reclaimed_then_{terminal.event_type.lower()}", terminal.message
        return "reclaimed_entered", entered.message

    terminal = next(
        (event for event in later if event.event_type in {"INVALIDATED", "ARCHIVED", "STOPPED", "CLOSED"}),
        None,
    )
    if terminal is not None:
        return terminal.event_type.lower(), terminal.message
    if trade.status == "WATCHING":
        return "still_waiting", trade.notes
    return trade.status.lower(), trade.notes


def _load_structured_run_events(settings: Settings, run_id: str | None) -> list[sqlite3.Row]:
    if run_id is None:
        return []
    with connect_db(settings.output.database_path) as connection:
        return connection.execute(
            """
            SELECT event_time, event_type, symbol, price, old_status, new_status,
                   old_stop, new_stop, kline_time, reason
            FROM paper_events
            WHERE run_id = ?
            ORDER BY event_time, event_id
            """,
            (run_id,),
        ).fetchall()


def generate_paper_report(
    settings: Settings,
    account_name: str | None = None,
    run_id: str | None = None,
    run_type: str = "manual",
) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    backfill_missing_events(settings, account)
    trades = load_all_paper_trades(settings, account)
    events_by_trade = load_paper_events(settings, account)
    now = _utc_now()
    project_report_dir = _project_report_dir(settings, now)
    obsidian_report_dir = _obsidian_report_dir(settings, now)
    if run_type == "paper_4h_update":
        local_hhmm = datetime.fromisoformat(now.replace("Z", "+00:00")).astimezone(
            timezone(timedelta(hours=8))
        ).strftime("%H%M")
        filename_prefix = f"paper_4h_update_{local_hhmm}_{account}"
    else:
        filename_prefix = f"paper_report_{_local_date(now)}_{account}"
    target_dirs = [project_report_dir]
    if obsidian_report_dir is not None:
        target_dirs.append(obsidian_report_dir)
    report_version_number = next_report_version(target_dirs, filename_prefix)
    report_version = f"v{report_version_number}"
    open_trades = [trade for trade in trades if trade.status in OPEN_STATUSES]
    closed_trades = [trade for trade in trades if trade.status in CLOSED_STATUSES]
    realized = sum(trade.realized_pnl for trade in trades)
    unrealized = sum(trade.unrealized_pnl for trade in open_trades)
    entered_trades = [trade for trade in trades if trade.entered_at_utc is not None]
    run_events = _load_structured_run_events(settings, run_id)
    api_delay_count = sum(1 for event in run_events if event["event_type"] == "API_DELAY_SKIPPED")
    winning_closed = [trade for trade in closed_trades if trade.realized_pnl > 0]
    losing_closed = [trade for trade in closed_trades if trade.realized_pnl < 0]
    win_rate = (len(winning_closed) / len(closed_trades) * 100) if closed_trades else None
    tp1_hits = [trade for trade in trades if trade.tp1_hit_at_utc is not None or trade.status == "TP1_HIT"]
    tp1_rate = (len(tp1_hits) / len(entered_trades) * 100) if entered_trades else None

    # 统计 entry_reclaim 拦截次数（所有 RECLAIM_PENDING 事件数）
    all_events = [e for evs in events_by_trade.values() for e in evs]
    reclaim_pending_count = sum(
        1 for e in all_events if e.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
    )
    ema_trailing_activated_count = sum(1 for e in all_events if e.event_type == "TP1_EMA_TRAILING_ACTIVATED")
    ema_trailing_raised_count = sum(1 for e in all_events if e.event_type == "TP1_EMA_TRAILING_RAISED")
    ema_trailing_stop_count = sum(
        1
        for e in all_events
        if e.event_type == "EMA_TRAILING_STOPPED"
        or (e.event_type == "STOPPED" and "EMA20 trailing stop" in e.message)
    )
    ema_trailing_active_trades = [
        trade
        for trade in open_trades
        if any(e.event_type == "TP1_EMA_TRAILING_ACTIVATED" for e in events_by_trade.get(trade.paper_trade_id, []))
    ]
    reclaim_trades = [
        trade
        for trade in trades
        if any(
            e.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
            for e in events_by_trade.get(trade.paper_trade_id, [])
        )
    ]

    # 计算已结束入场交易的平均持仓时长（小时）
    holding_durations: list[float] = []
    for trade in closed_trades:
        if trade.entered_at_utc and trade.closed_at_utc:
            try:
                entered = datetime.fromisoformat(trade.entered_at_utc)
                closed = datetime.fromisoformat(trade.closed_at_utc)
                holding_durations.append((closed - entered).total_seconds() / 3600)
            except ValueError:
                pass
    avg_holding_hours = (sum(holding_durations) / len(holding_durations)) if holding_durations else None

    # 拉取当日 regime 快照
    regime = None
    try:
        client = BinanceClient(
            settings.market.base_url,
            timeout_seconds=settings.market.request_timeout_seconds,
            pause_seconds=settings.market.request_pause_seconds,
        )
        btc_1d = client.klines("BTCUSDT", "1d", limit=80)
        eth_1d = client.klines("ETHUSDT", "1d", limit=80)
        regime = classify_market_regime(
            btc_1d,
            eth_1d,
            btc_7d_drop_pct=settings.analysis.regime_btc_7d_drop_pct,
            eth_7d_drop_pct=settings.analysis.regime_eth_7d_drop_pct,
            require_both_trend=settings.analysis.regime_require_both_trend,
        )
    except Exception:
        pass

    lines = [
        "---",
        f"created: {_local_timestamp(now)}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - paper-trading",
        f"account: {account}",
        f"report_version: {report_version}",
        "---",
        "",
        f"# 模拟盘报告 {account} {report_version}",
        "",
        f"- 报告时间：{_local_timestamp(now)}",
        f"- Run ID：`{run_id or 'n/a'}`",
        f"- Run type：`{run_type}`",
        "- 数据来源：SQLite",
        f"- 报告版本：{report_version}",
        f"- 模拟账户权益基准：{settings.paper.account_equity:,.2f} USDT",
        f"- 单笔计划风险：{settings.paper.risk_per_trade_pct * 100:.2f}%",
        f"- 开放交易/观察：{len(open_trades)}",
        f"- 已结束交易：{len(closed_trades)}",
        f"- 已实现 PnL：{realized:,.2f} USDT",
        f"- 未实现 PnL：{unrealized:,.2f} USDT",
        f"- 已入场交易数：{len(entered_trades)}",
        f"- 胜率：{'n/a' if win_rate is None else f'{win_rate:.2f}%'}",
        f"- TP1 命中率：{'n/a' if tp1_rate is None else f'{tp1_rate:.2f}%'}",
        "",
        "## 今日大盘环境",
        "",
    ]

    if regime is None:
        lines.append("_大盘环境数据获取失败。_")
    else:
        def _trend_str(ok: bool) -> str:
            return "✓ 趋势确认 (price > EMA20 > EMA50)" if ok else "✗ 趋势未确认"

        def _pct_str(val: float | None) -> str:
            return "n/a" if val is None else f"{val:+.2f}%"

        btc_threshold = settings.analysis.regime_btc_7d_drop_pct
        eth_threshold = settings.analysis.regime_eth_7d_drop_pct
        btc_pct_flag = "" if regime.btc_pct_7d is None or regime.btc_pct_7d >= btc_threshold else f" ⚠ 低于阈值 {btc_threshold:+.1f}%"
        eth_pct_flag = "" if regime.eth_pct_7d is None or regime.eth_pct_7d >= eth_threshold else f" ⚠ 低于阈值 {eth_threshold:+.1f}%"

        lines.extend([
            f"- **状态：{regime.status}** — {regime.summary}",
            f"- BTC 7d 涨跌：{_pct_str(regime.btc_pct_7d)}{btc_pct_flag}（阈值 {btc_threshold:+.1f}%）",
            f"- ETH 7d 涨跌：{_pct_str(regime.eth_pct_7d)}{eth_pct_flag}（阈值 {eth_threshold:+.1f}%）",
            f"- BTC 日线趋势：{_trend_str(regime.btc_trend_ok)}",
            f"- ETH 日线趋势：{_trend_str(regime.eth_trend_ok)}",
            f"- require_both_trend：{'是' if settings.analysis.regime_require_both_trend else '否'}",
        ])

    lines.extend([
        "",
        "## 复盘统计",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Total plans | {len(trades)} |",
        f"| Open watching/positions | {len(open_trades)} |",
        f"| Entered trades | {len(entered_trades)} |",
        f"| Closed trades | {len(closed_trades)} |",
        f"| Winning closed trades | {len(winning_closed)} |",
        f"| Losing closed trades | {len(losing_closed)} |",
        f"| Win rate | {'n/a' if win_rate is None else f'{win_rate:.2f}%'} |",
        f"| TP1 hit rate | {'n/a' if tp1_rate is None else f'{tp1_rate:.2f}%'} |",
        f"| Realized PnL | {realized:,.2f} USDT |",
        f"| Unrealized PnL | {unrealized:,.2f} USDT |",
        f"| Entry reclaim blocks | {reclaim_pending_count} |",
        f"| Avg holding time | {'n/a' if avg_holding_hours is None else f'{avg_holding_hours:.1f}h'} |",
        f"| TP1 EMA trailing activated | {ema_trailing_activated_count} |",
        f"| TP1 EMA trailing raises | {ema_trailing_raised_count} |",
        f"| TP1 EMA trailing stops | {ema_trailing_stop_count} |",
        f"| TP1 EMA trailing active trades | {len(ema_trailing_active_trades)} |",
        f"| This run events | {len(run_events)} |",
        f"| This run API delay skipped | {api_delay_count} |",
        "",
        "## Entry Reclaim 后续追踪",
        "",
        "| Symbol | Status | Pending Events | First Pending | Last Pending | Outcome | Detail |",
        "|---|---|---:|---|---|---|---|",
    ])

    if reclaim_trades:
        for trade in reclaim_trades:
            trade_events = events_by_trade.get(trade.paper_trade_id, [])
            pending_events = [
                event
                for event in trade_events
                if event.event_type in {"RECLAIM_PENDING", "RECLAIM_PENDING_SET"}
            ]
            outcome, detail = _reclaim_outcome(trade, trade_events)
            lines.append(
                "| "
                f"`{trade.symbol}` | "
                f"{trade.status} | "
                f"{len(pending_events)} | "
                f"{_local_timestamp(pending_events[0].event_time_utc)} | "
                f"{_local_timestamp(pending_events[-1].event_time_utc)} | "
                f"{outcome} | "
                f"{detail} |"
            )
    else:
        lines.append("| n/a | n/a | 0 | n/a | n/a | no_reclaim_pending | No RECLAIM_PENDING events recorded yet. |")

    lines.extend([
        "",
        "## TP1 EMA Trailing Stop 追踪",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Activated events | {ema_trailing_activated_count} |",
        f"| Stop raise events | {ema_trailing_raised_count} |",
        f"| Stop exits from EMA trailing | {ema_trailing_stop_count} |",
        f"| Currently active trades | {len(ema_trailing_active_trades)} |",
        "",
        "## 本次 Run 状态变化",
        "",
        "| Time | Event | Symbol | Old Status | New Status | Price | Old Stop | New Stop | Kline Time | Reason |",
        "|---|---|---|---|---|---:|---:|---:|---|---|",
    ])
    if run_events:
        for event in run_events:
            lines.append(
                "| "
                f"{_local_timestamp(event['event_time'])} | {event['event_type']} | `{event['symbol']}` | "
                f"{event['old_status'] or 'n/a'} | {event['new_status'] or 'n/a'} | "
                f"{_fmt_price(event['price'])} | {_fmt_price(event['old_stop'])} | "
                f"{_fmt_price(event['new_stop'])} | {event['kline_time'] or 'n/a'} | "
                f"{event['reason'] or ''} |"
            )
    else:
        lines.append("| n/a | NO_STATE_CHANGE | n/a | n/a | n/a | n/a | n/a | n/a | n/a | No structured events for this run. |")
    lines.extend([
        "",
        "## 当前观察与持仓",
        "",
        "| Status | Symbol | Last | Entry Zone | Entry | Stop | TP1 | TP2 | Qty | Unrealized | Notes |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ])

    for trade in open_trades:
        lines.append(
            "| "
            f"{trade.status} | "
            f"`{trade.symbol}` | "
            f"{_fmt_price(trade.last_price)} | "
            f"{_fmt_price(trade.entry_low)} - {_fmt_price(trade.entry_high)} | "
            f"{_fmt_price(trade.entry_price)} | "
            f"{_fmt_price(trade.stop_loss)} | "
            f"{_fmt_price(trade.take_profit_1)} | "
            f"{_fmt_price(trade.take_profit_2)} | "
            f"{_fmt_money(trade.quantity)} | "
            f"{_fmt_money(trade.unrealized_pnl)} | "
            f"{trade.notes} |"
        )

    lines.extend(
        [
            "",
            "## 已结束交易",
            "",
            "| Status | Symbol | Entry | Exit | Qty | Realized PnL | Source Scan | Notes |",
            "|---|---|---:|---:|---:|---:|---|---|",
        ]
    )
    for trade in closed_trades:
        lines.append(
            "| "
            f"{trade.status} | "
            f"`{trade.symbol}` | "
            f"{_fmt_price(trade.entry_price)} | "
            f"{_fmt_price(trade.exit_price)} | "
            f"{_fmt_money(trade.quantity)} | "
            f"{_fmt_money(trade.realized_pnl)} | "
            f"{trade.source_scan_id} | "
            f"{trade.notes} |"
        )

    lines.extend(["", "## 交易生命周期", ""])
    for trade in trades:
        lines.extend(
            [
                f"### {trade.symbol} `{trade.paper_trade_id}`",
                "",
                f"- 当前状态：`{trade.status}`",
                f"- 来源扫描：`{trade.source_scan_id}` rank {trade.source_rank}",
                "",
                "| Time | Event | Price | Qty | Realized | Unrealized | Message |",
                "|---|---|---:|---:|---:|---:|---|",
            ]
        )
        for event in events_by_trade.get(trade.paper_trade_id, []):
            lines.append(
                "| "
                f"{_local_timestamp(event.event_time_utc)} | "
                f"{event.event_type} | "
                f"{_fmt_price(event.price)} | "
                f"{_fmt_money(event.quantity)} | "
                f"{_fmt_money(event.realized_pnl)} | "
                f"{_fmt_money(event.unrealized_pnl)} | "
                f"{event.message} |"
            )
        if not events_by_trade.get(trade.paper_trade_id):
            lines.append("| n/a | n/a | n/a | n/a | n/a | n/a | No events recorded. |")
        lines.append("")

    lines.extend(
        [
            "",
            "## 状态说明",
            "",
            "- `WATCHING`：计划已加入模拟盘，等待价格进入入场区间。",
            "- `ENTERED`：价格触发入场区，已模拟买入。",
            "- `TP1_HIT`：已触发第一止盈，继续跟踪第二止盈。",
            "- `STOPPED`：入场后触发止损。",
            "- `CLOSED`：触发 TP2 后模拟平仓。",
            "- `INVALIDATED`：尚未入场就跌破止损，计划失效。",
            "- `ARCHIVED`：尚未入场的旧计划被同币种新计划替换。",
            "",
        ]
    )

    markdown = "\n".join(lines)
    filename = versioned_markdown_filename(filename_prefix, report_version_number)
    paths: list[Path] = []

    project_report_dir.mkdir(parents=True, exist_ok=True)
    project_path = project_report_dir / filename
    project_path.write_text(markdown, encoding="utf-8")
    paths.append(project_path)

    if obsidian_report_dir is not None:
        obsidian_report_dir.mkdir(parents=True, exist_ok=True)
        obsidian_path = obsidian_report_dir / filename
        obsidian_path.write_text(markdown, encoding="utf-8")
        paths.append(obsidian_path)

    return markdown, paths
