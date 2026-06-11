from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sqlite3
import uuid

from .config import Settings
from .market_data import BinanceClient
from .market_regime import classify_market_regime
from .models import PaperTrade, PaperTradeEvent
from .report_versions import next_report_version, versioned_markdown_filename
from .trade_state import step_trade
from .indicators import ema as _ema


OPEN_STATUSES = {"WATCHING", "ENTERED", "TP1_HIT"}
CLOSED_STATUSES = {"STOPPED", "CLOSED", "INVALIDATED", "ARCHIVED"}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


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


def _paper_trade_from_row(row: sqlite3.Row) -> PaperTrade:
    return PaperTrade(
        paper_trade_id=row["paper_trade_id"],
        account_name=row["account_name"],
        source_scan_id=row["source_scan_id"],
        source_rank=int(row["source_rank"]),
        symbol=row["symbol"],
        base_asset=row["base_asset"],
        status=row["status"],
        created_at_utc=row["created_at_utc"],
        updated_at_utc=row["updated_at_utc"],
        setup=row["setup"],
        verdict=row["verdict"],
        entry_low=float(row["entry_low"]),
        entry_high=float(row["entry_high"]),
        planned_entry_mid=float(row["planned_entry_mid"]),
        stop_loss=float(row["stop_loss"]),
        take_profit_1=float(row["take_profit_1"]),
        take_profit_2=float(row["take_profit_2"]),
        risk_reward_1=float(row["risk_reward_1"]),
        risk_reward_2=float(row["risk_reward_2"]),
        account_equity=float(row["account_equity"]),
        risk_per_trade_pct=float(row["risk_per_trade_pct"]),
        cash_risk=float(row["cash_risk"]),
        quantity=None if row["quantity"] is None else float(row["quantity"]),
        entry_price=None if row["entry_price"] is None else float(row["entry_price"]),
        entered_at_utc=row["entered_at_utc"],
        tp1_hit_at_utc=row["tp1_hit_at_utc"],
        closed_at_utc=row["closed_at_utc"],
        exit_price=None if row["exit_price"] is None else float(row["exit_price"]),
        realized_pnl=float(row["realized_pnl"]),
        unrealized_pnl=float(row["unrealized_pnl"]),
        last_price=None if row["last_price"] is None else float(row["last_price"]),
        notes=row["notes"],
    )


def _paper_event_from_row(row: sqlite3.Row) -> PaperTradeEvent:
    return PaperTradeEvent(
        event_id=row["event_id"],
        paper_trade_id=row["paper_trade_id"],
        account_name=row["account_name"],
        symbol=row["symbol"],
        event_type=row["event_type"],
        event_time_utc=row["event_time_utc"],
        price=None if row["price"] is None else float(row["price"]),
        quantity=None if row["quantity"] is None else float(row["quantity"]),
        realized_pnl=float(row["realized_pnl"]),
        unrealized_pnl=float(row["unrealized_pnl"]),
        message=row["message"],
    )


def _record_event(
    connection: sqlite3.Connection,
    trade: PaperTrade,
    event_type: str,
    message: str,
    event_time_utc: str | None = None,
    price: float | None = None,
) -> None:
    event_time = event_time_utc or _utc_now()
    connection.execute(
        """
        INSERT INTO paper_trade_events (
            event_id, paper_trade_id, account_name, symbol, event_type, event_time_utc,
            price, quantity, realized_pnl, unrealized_pnl, message
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            uuid.uuid4().hex[:12],
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
                realized_pnl, unrealized_pnl, last_price, notes, payload_json
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?
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
) -> int:
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT *
        FROM paper_trades
        WHERE account_name = ?
          AND symbol = ?
          AND status = 'WATCHING'
          AND source_scan_id <> ?
        """,
        (account_name, symbol, replacement_scan_id),
    ).fetchall()

    archived = 0
    for row in rows:
        old_trade = _paper_trade_from_row(row)
        old_trade.status = "ARCHIVED"
        old_trade.updated_at_utc = now
        old_trade.closed_at_utc = now
        old_trade.notes = f"Archived because scan {replacement_scan_id} created a newer WATCHING plan for {symbol}."
        _save_trade_update(connection, old_trade)
        _record_event(
            connection,
            old_trade,
            "ARCHIVED",
            old_trade.notes,
            event_time_utc=now,
            price=old_trade.last_price,
        )
        archived += 1
    return archived


def add_from_scan(settings: Settings, scan_id: str | None = None, account_name: str | None = None) -> dict:
    account = account_name or settings.paper.account_name
    now = _utc_now()
    added = 0
    skipped = 0
    skipped_action = 0
    archived = 0
    allowed_actions = {action.upper() for action in settings.paper.import_actions}

    with sqlite3.connect(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        chosen_scan_id = scan_id or _latest_scan_id(connection)
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

        for row in rows:
            payload = json.loads(row["payload_json"])
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
        FROM paper_trades
        WHERE account_name = ? AND status IN ('WATCHING', 'ENTERED', 'TP1_HIT')
        ORDER BY created_at_utc, source_rank
        """,
        (account_name,),
    ).fetchall()
    return [_paper_trade_from_row(row) for row in rows]


def _save_trade_update(connection: sqlite3.Connection, trade: PaperTrade) -> None:
    connection.execute(
        """
        UPDATE paper_trades
        SET status = ?, updated_at_utc = ?, quantity = ?, entry_price = ?,
            entered_at_utc = ?, tp1_hit_at_utc = ?, closed_at_utc = ?, exit_price = ?,
            realized_pnl = ?, unrealized_pnl = ?, last_price = ?, notes = ?
        WHERE paper_trade_id = ?
        """,
        (
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
            trade.paper_trade_id,
        ),
    )


def update_paper_trades(settings: Settings, account_name: str | None = None) -> list[PaperTrade]:
    account = account_name or settings.paper.account_name
    client = BinanceClient(
        settings.market.base_url,
        timeout_seconds=settings.market.request_timeout_seconds,
        pause_seconds=settings.market.request_pause_seconds,
    )
    ticker_map = {item["symbol"]: float(item["lastPrice"]) for item in client.ticker_24hr()}
    updated: list[PaperTrade] = []
    now = _utc_now()

    entry_reclaim_enabled = settings.analysis.entry_reclaim_close_enabled
    ema_trailing_enabled = settings.analysis.tp1_ema_trailing_stop_enabled

    # 按需批量拉 4h K线：entry_reclaim 需要当前收盘价（用 lastPrice 代替），
    # ema_trailing 需要最近 20 根 4h K线。两者共用同一次 API 请求。
    klines_4h_cache: dict[str, list[list]] = {}

    def _get_4h_closes(symbol: str) -> list[float]:
        if symbol not in klines_4h_cache:
            klines_4h_cache[symbol] = client.klines(symbol, "4h", limit=25)
        # 只取已完全收盘的 K线（排除最后一根未收盘的）
        closed = klines_4h_cache[symbol][:-1]
        return [float(k[4]) for k in closed]

    with sqlite3.connect(settings.output.database_path) as connection:
        trades = _load_open_trades(connection, account)
        for trade in trades:
            current_price = ticker_map.get(trade.symbol)
            if current_price is None:
                trade.notes = f"{trade.notes} | No ticker price found during update."
                continue

            # entry_reclaim_close：WATCHING 状态下，entry zone 已触碰但 4h 收盘未重新站上 entry_high
            # 用当前价格作为"最新 4h 收盘"的近似值（模拟盘每次更新间隔远大于 1 tick）
            if (
                entry_reclaim_enabled
                and trade.status == "WATCHING"
                and current_price <= trade.entry_high
            ):
                closes_4h = _get_4h_closes(trade.symbol)
                last_close = closes_4h[-1] if closes_4h else current_price
                if last_close < trade.entry_high:
                    trade.last_price = current_price
                    trade.updated_at_utc = now
                    trade.notes = "Watching: entry zone touched, but 4h close has not reclaimed entry_high."
                    _record_event(
                        connection,
                        trade,
                        "RECLAIM_PENDING",
                        f"Entry zone touched (price={_fmt_price(current_price)}) but 4h close {_fmt_price(last_close)} < entry_high {_fmt_price(trade.entry_high)}; waiting for reclaim.",
                        price=current_price,
                    )
                    _save_trade_update(connection, trade)
                    updated.append(trade)
                    continue

            # tp1_ema_trailing_stop：ENTERED/TP1_HIT 状态下计算 4h EMA20
            ema20_4h: float | None = None
            if ema_trailing_enabled and trade.status in {"ENTERED", "TP1_HIT"}:
                closes_4h = _get_4h_closes(trade.symbol)
                if len(closes_4h) >= 20:
                    ema20_4h = _ema(closes_4h, 20)

            events = step_trade(
                trade,
                high=current_price,
                low=current_price,
                close=current_price,
                event_time_utc=now,
                move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
                tp1_trailing_ema_stop=ema20_4h,
            )
            for event in events:
                _record_event(
                    connection,
                    trade,
                    event.event_type,
                    event.message,
                    event_time_utc=event.event_time_utc,
                    price=event.price,
                )

            _save_trade_update(connection, trade)
            updated.append(trade)

    return updated


def load_paper_events(settings: Settings, account_name: str | None = None) -> dict[str, list[PaperTradeEvent]]:
    account = account_name or settings.paper.account_name
    with sqlite3.connect(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT *
            FROM paper_trade_events
            WHERE account_name = ?
            ORDER BY event_time_utc, event_type
            """,
            (account,),
        ).fetchall()

    events_by_trade: dict[str, list[PaperTradeEvent]] = {}
    for row in rows:
        event = _paper_event_from_row(row)
        events_by_trade.setdefault(event.paper_trade_id, []).append(event)
    return events_by_trade


def backfill_missing_events(settings: Settings, account_name: str | None = None) -> int:
    account = account_name or settings.paper.account_name
    inserted = 0
    with sqlite3.connect(settings.output.database_path) as connection:
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
    with sqlite3.connect(settings.output.database_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT *
            FROM paper_trades
            WHERE account_name = ?
            ORDER BY created_at_utc DESC, source_rank
            """,
            (account,),
        ).fetchall()
    return [_paper_trade_from_row(row) for row in rows]


def generate_paper_report(settings: Settings, account_name: str | None = None) -> tuple[str, list[Path]]:
    account = account_name or settings.paper.account_name
    backfill_missing_events(settings, account)
    trades = load_all_paper_trades(settings, account)
    events_by_trade = load_paper_events(settings, account)
    now = _utc_now()
    project_report_dir = _project_report_dir(settings, now)
    obsidian_report_dir = _obsidian_report_dir(settings, now)
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
    winning_closed = [trade for trade in closed_trades if trade.realized_pnl > 0]
    losing_closed = [trade for trade in closed_trades if trade.realized_pnl < 0]
    win_rate = (len(winning_closed) / len(closed_trades) * 100) if closed_trades else None
    tp1_hits = [trade for trade in trades if trade.tp1_hit_at_utc is not None or trade.status == "TP1_HIT"]
    tp1_rate = (len(tp1_hits) / len(entered_trades) * 100) if entered_trades else None

    # 统计 entry_reclaim 拦截次数（所有 RECLAIM_PENDING 事件数）
    all_events = [e for evs in events_by_trade.values() for e in evs]
    reclaim_pending_count = sum(1 for e in all_events if e.event_type == "RECLAIM_PENDING")

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
