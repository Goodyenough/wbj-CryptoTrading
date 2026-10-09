"""Isolated, sampled-quote forward portfolios. Never writes legacy paper state.

Each committed tick contains its inputs and complete resulting state. An epoch
is the unit of continuity: missing observations censor its whole portfolio path.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import uuid

from .backtest.costs import entry_fill, stop_exit_fill, target_exit_fill
from .database import connect_db, utc_now
from .indicators import atr, ema
from .market_data import BinanceClient
from .models import PaperTrade
from .trade_state import step_trade

LINES = {"reference_baseline": 0.0, "atr_reclaim_0_35_shadow": 0.35}
ACTIVE = {"ENTERED", "TP1_HIT"}
OPEN = ACTIVE | {"WATCHING"}
BAR_MS = 4 * 60 * 60 * 1000
SCHEMA = """
CREATE TABLE IF NOT EXISTS paper_forward_epochs (
    epoch_id TEXT PRIMARY KEY, account_name TEXT NOT NULL,
    started_at TEXT NOT NULL, updated_at TEXT NOT NULL,
    status TEXT NOT NULL, reason TEXT, policy_json TEXT NOT NULL,
    state_json TEXT NOT NULL, last_bar INTEGER, last_tick TEXT
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_forward_active_account
ON paper_forward_epochs(account_name) WHERE status='ACTIVE';
CREATE TABLE IF NOT EXISTS paper_forward_ticks (
    tick_id TEXT PRIMARY KEY, epoch_id TEXT NOT NULL,
    account_name TEXT NOT NULL, run_id TEXT NOT NULL,
    observed_at TEXT NOT NULL, bar_close INTEGER NOT NULL,
    status TEXT NOT NULL, reason TEXT, input_json TEXT NOT NULL,
    state_json TEXT NOT NULL,
    UNIQUE(account_name, run_id),
    FOREIGN KEY(epoch_id) REFERENCES paper_forward_epochs(epoch_id)
);
CREATE INDEX IF NOT EXISTS idx_forward_tick_epoch
ON paper_forward_ticks(epoch_id, observed_at);
"""


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False)


def _dt(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("naive observation time")
    return parsed.astimezone(timezone.utc)


def policy(settings):
    files = [Path(__file__), Path(__file__).with_name("trade_state.py"),
             Path(__file__).with_name("indicators.py"),
             Path(__file__).with_name("scanner.py"),
             Path(__file__).with_name("market_regime.py"),
             Path(__file__).parent / "backtest" / "costs.py"]
    return {
        "version": "sampled_quote_v1", "controls_paper": False,
        "code_sha256": hashlib.sha256(b"".join(p.read_bytes() for p in files)).hexdigest(),
        "lines": LINES, "research_incumbent_alias": "atr_reclaim_0_35_shadow",
        "initial_equity": settings.paper.account_equity,
        "risk_per_trade_pct": settings.paper.risk_per_trade_pct,
        "backtest": asdict(settings.backtest),
        "signal_analysis": asdict(settings.analysis),
        "signal_market": {key: getattr(settings.market, key) for key in (
            "quote_asset", "min_quote_volume", "min_trades", "max_universe", "top_n", "exclude_bases")},
        "breakeven": settings.analysis.tp1_move_stop_to_breakeven_enabled,
        "ema_trailing": settings.analysis.tp1_ema_trailing_stop_enabled,
        "execution": "one_current_quote_per_closed_4h_bar_no_intrabar_protection",
        "max_delay_minutes": 30,
    }


def _empty_state(settings):
    return {"seen": [], "lines": {name: {
        "cash": settings.paper.account_equity, "trades": {},
    } for name in LINES}}


def _censor(state, reason):
    state = deepcopy(state)
    for line in state["lines"].values():
        for record in line["trades"].values():
            record["trusted"] = False
            if record["trade"]["status"] in OPEN:
                record["right_censored"] = True
                record["censor_reason"] = reason
    return state


def ensure_epoch(settings, account_name=None, *, now=None):
    """Start empty prospectively; call before daily scan to admit that scan."""
    account = account_name or settings.paper.account_name
    now = now or utc_now()
    frozen = _json(policy(settings))
    with connect_db(settings.output.database_path) as connection:
        connection.executescript(SCHEMA)
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute(
            "SELECT * FROM paper_forward_epochs WHERE account_name=? AND status='ACTIVE'", (account,)
        ).fetchone()
        if row and row["policy_json"] != frozen:
            connection.execute(
                "UPDATE paper_forward_epochs SET status='CONFIG_CHANGED', reason=?, state_json=?, updated_at=? WHERE epoch_id=?",
                ("policy_or_code_changed", _json(_censor(json.loads(row["state_json"]), "policy_or_code_changed")), now, row["epoch_id"]),
            )
            row = None
        if row is None:
            epoch_id = uuid.uuid4().hex
            connection.execute(
                "INSERT INTO paper_forward_epochs(epoch_id,account_name,started_at,updated_at,status,policy_json,state_json) VALUES (?,?,?,?,'ACTIVE',?,?)",
                (epoch_id, account, now, now, frozen, _json(_empty_state(settings))),
            )
            row = connection.execute("SELECT * FROM paper_forward_epochs WHERE epoch_id=?", (epoch_id,)).fetchone()
        return dict(row)


def _validate_market(market, symbols, now):
    now_ms = int(_dt(now).timestamp() * 1000)
    bar_close = now_ms // BAR_MS * BAR_MS - 1
    if now_ms - bar_close > 30 * 60 * 1000:
        raise ValueError("late_observation_over_30_minutes")
    for symbol in symbols:
        item = market[symbol]
        quote = float(item["price"])
        if not math.isfinite(quote) or quote <= 0:
            raise ValueError(f"invalid_quote:{symbol}")
        quote_time = int(item["quote_time_ms"])
        if not 0 <= now_ms - quote_time <= 5 * 60 * 1000:
            raise ValueError(f"stale_or_future_quote:{symbol}")
        bars = item["bars"]
        if len(bars) < 20 or int(bars[-1][6]) != bar_close:
            raise ValueError(f"stale_or_short_klines:{symbol}")
        previous = None
        for row in bars:
            start, end = int(row[0]), int(row[6])
            o, h, l, c, v = map(float, row[1:6])
            if (start % BAR_MS or end != start + BAR_MS - 1
                    or end > now_ms - 60_000
                    or (previous is not None and start != previous + BAR_MS)
                    or not all(math.isfinite(x) for x in (o, h, l, c, v))
                    or not 0 < l <= min(o, c) <= max(o, c) <= h or v <= 0):
                raise ValueError(f"invalid_or_gapped_klines:{symbol}")
            previous = start
        if not atr(bars) or atr(bars) <= 0:
            raise ValueError(f"invalid_atr:{symbol}")
    return bar_close


def _new_record(candidate, account, now, settings):
    lo, hi, stop, tp1, tp2 = (float(candidate[k]) for k in ("entry_low", "entry_high", "stop_loss", "tp1", "tp2"))
    if not all(math.isfinite(x) for x in (lo, hi, stop, tp1, tp2)) or not 0 < stop < lo <= hi < tp1 <= tp2:
        raise ValueError(f"invalid_candidate_levels:{candidate['observation_id']}")
    trade = PaperTrade(
        paper_trade_id=candidate["observation_id"], account_name=account,
        source_scan_id=candidate["scan_id"], source_rank=candidate["source_rank"],
        symbol=candidate["symbol"], base_asset=candidate["symbol"], status="WATCHING",
        created_at_utc=now, updated_at_utc=now, setup="independent_forward", verdict="BUY_CANDIDATE",
        entry_low=lo, entry_high=hi, planned_entry_mid=(lo + hi) / 2,
        stop_loss=stop, take_profit_1=tp1, take_profit_2=tp2,
        risk_reward_1=(tp1-hi)/(hi-stop), risk_reward_2=(tp2-hi)/(hi-stop),
        account_equity=settings.paper.account_equity, risk_per_trade_pct=settings.paper.risk_per_trade_pct,
        cash_risk=0,
    )
    return {"trade": asdict(trade), "data_quality_state": candidate["data_quality_state"],
            "fees": 0.0, "slippage": 0.0, "trusted": True, "right_censored": False,
            "scan_time": candidate["scan_time"], "decision": "registered"}


def _equity(line, market):
    return line["cash"] + sum(
        r["trade"]["quantity"] * market[r["trade"]["symbol"]]["price"]
        for r in line["trades"].values() if r["trade"]["status"] in ACTIVE
    )


def _step(record, line, item, settings, now, *, entering=False):
    trade = PaperTrade(**record["trade"])
    quote, bars = float(item["price"]), item["bars"]
    ema_value = ema([float(row[4]) for row in bars], 20) if settings.analysis.tp1_ema_trailing_stop_enabled else None
    # The stop trigger may rise inside step_trade; quote-based fill must not use
    # the old stop. All indicators precede this quote, never this bar's low.
    stop_fill = stop_exit_fill(quote, trade.quantity or 0, settings.backtest)
    events = step_trade(
        trade, high=quote, low=quote, close=quote, event_time_utc=now,
        entry_price_override=entry_fill(quote, 0, settings.backtest).filled_price,
        stop_exit_price_override=stop_fill.filled_price,
        move_stop_to_breakeven_on_tp1=settings.analysis.tp1_move_stop_to_breakeven_enabled,
        tp1_trailing_ema_stop=ema_value, tp1_trailing_ema_stop_ready=ema_value is not None,
    )
    if entering and trade.entered_at_utc == now:
        cost = entry_fill(quote, trade.quantity, settings.backtest)
        record["fees"] += cost.fee
        record["slippage"] += cost.slippage_cost
        line["cash"] -= trade.entry_price * trade.quantity + cost.fee
    if trade.status in {"CLOSED", "STOPPED"}:
        cost = (stop_exit_fill(quote, trade.quantity, settings.backtest) if trade.status == "STOPPED"
                else target_exit_fill(trade.take_profit_2, trade.quantity, settings.backtest))
        record["fees"] += cost.fee
        record["slippage"] += cost.slippage_cost
        line["cash"] += trade.exit_price * trade.quantity - cost.fee
        record["net_pnl"] = trade.realized_pnl - record["fees"]
    record["trade"] = asdict(trade)
    record["events"] = [asdict(event) for event in events]


def advance(state, candidates, market, settings, account, now):
    """Pure deterministic transition. Caller validates and persists atomically."""
    state = deepcopy(state)
    new = [c for c in candidates if c["observation_id"] not in state["seen"]]
    new.sort(key=lambda c: (_dt(c["scan_time"]), c["source_rank"], c["observation_id"]))
    state["seen"].extend(c["observation_id"] for c in new)
    for name, threshold in LINES.items():
        line = state["lines"][name]
        for record in line["trades"].values():
            record["events"] = []
            if record["trade"]["status"] in ACTIVE:
                _step(record, line, market[record["trade"]["symbol"]], settings, now)
        for candidate in new:
            record = _new_record(candidate, account, now, settings)
            same_symbol = [r for r in line["trades"].values() if r["trade"]["symbol"] == candidate["symbol"]]
            for old in same_symbol:
                if old["trade"]["status"] == "WATCHING":
                    old["trade"].update(status="ARCHIVED", closed_at_utc=now, updated_at_utc=now)
                    old["decision"] = "replaced_by_new_scan"
            if any(r["trade"]["status"] in ACTIVE for r in same_symbol):
                record["trade"].update(status="REJECTED", closed_at_utc=now)
                record["decision"] = "symbol_already_active"
            elif sum(r["trade"]["status"] in OPEN for r in line["trades"].values()) >= settings.backtest.max_open_plans:
                record["trade"].update(status="REJECTED", closed_at_utc=now)
                record["decision"] = "plan_capacity"
            line["trades"][candidate["observation_id"]] = record
        watchers = sorted((r for r in line["trades"].values() if r["trade"]["status"] == "WATCHING"),
                          key=lambda r: (_dt(r["scan_time"]), r["trade"]["source_rank"], r["trade"]["paper_trade_id"]))
        for record in watchers:
            trade = record["trade"]
            item = market[trade["symbol"]]
            quote, bars = float(item["price"]), item["bars"]
            if quote <= trade["stop_loss"]:
                _step(record, line, item, settings, now)
                record["decision"] = "invalidated_before_entry"
                continue
            if not trade["entry_low"] <= quote <= trade["entry_high"]:
                record["decision"] = "outside_entry_zone"
                continue
            if float(bars[-1][4]) < trade["entry_high"] + threshold * atr(bars):
                record["decision"] = "reclaim_pending"
                continue
            active = [r["trade"] for r in line["trades"].values() if r["trade"]["status"] in ACTIVE]
            equity = _equity(line, market)
            risk = equity * settings.paper.risk_per_trade_pct
            filled = entry_fill(quote, 0, settings.backtest).filled_price
            if equity <= 0 or filled >= trade["take_profit_1"]:
                record["decision"] = "unexecutable_entry"
                continue
            qty = risk / (filled - trade["stop_loss"])
            cfg = settings.backtest
            if len(active) >= cfg.max_active_positions or sum(t["cash_risk"] for t in active) + risk > equity * cfg.total_active_risk_pct + 1e-8:
                record["decision"] = "position_or_risk_capacity"
                continue
            # Size down to available cash and the frozen per-position cap.
            qty = min(qty, equity * cfg.max_position_notional_pct / filled,
                      max(0, line["cash"]) / (filled * (1 + cfg.maker_fee_bps / 10_000)))
            if qty <= 0:
                record["decision"] = "cash_capacity"
                continue
            trade.update(cash_risk=qty * (filled - trade["stop_loss"]), account_equity=equity)
            _step(record, line, item, settings, now, entering=True)
            record["decision"] = "entered"
        line["equity"] = _equity(line, market)
    return state


def run_forward_shadow(settings, account_name=None, *, run_id, now=None, market=None):
    """Persist one tick. Network happens outside the write transaction.

    Explicit market/now injection is for deterministic tests only. Normal callers
    fetch fresh public data and cannot turn a historical replay into forward data.
    """
    account = account_name or settings.paper.account_name
    now = now or utc_now()
    with connect_db(settings.output.database_path) as connection:
        connection.executescript(SCHEMA)
        previous = connection.execute("SELECT * FROM paper_forward_ticks WHERE account_name=? AND run_id=?", (account, run_id)).fetchone()
        if previous:
            return dict(previous)
    epoch = ensure_epoch(settings, account, now=now)
    bar_close = int(_dt(now).timestamp() * 1000) // BAR_MS * BAR_MS - 1
    if epoch["last_bar"] == bar_close:
        return {"status": "DUPLICATE_BAR", "epoch_id": epoch["epoch_id"]}
    state = json.loads(epoch["state_json"])
    with connect_db(settings.output.database_path) as connection:
        candidates = [dict(row) for row in connection.execute(
            """SELECT * FROM paper_shadow_candidate_observations WHERE account_name=?
            AND julianday(scan_time)>=julianday(?) AND julianday(scan_time)<=julianday(?)
            AND scanner_action='BUY_CANDIDATE' AND data_quality_state IN ('CLEAN','DEGRADED')""",
            (account, epoch["started_at"], now),
        ) if row["observation_id"] not in state["seen"]]
    symbols = {r["trade"]["symbol"] for line in state["lines"].values() for r in line["trades"].values() if r["trade"]["status"] in OPEN}
    symbols.update(c["symbol"] for c in candidates)
    input_data = {"candidates": candidates, "market": {}, "source": "public_forward" if market is None else "injected_fixture"}
    status, reason = "OK", None
    try:
        if epoch["last_bar"] is not None and bar_close != epoch["last_bar"] + BAR_MS:
            raise ValueError("missing_or_out_of_order_4h_slot")
        if epoch["last_bar"] is None and (_dt(now) - _dt(epoch["started_at"])).total_seconds() > 4.5 * 3600:
            raise ValueError("missing_first_observation")
        if settings.backtest.allow_leverage:
            raise ValueError("unsupported_leveraged_shadow_policy")
        if market is None:
            market = {}
            if symbols:
                client = BinanceClient(settings.market.base_url, timeout_seconds=settings.market.request_timeout_seconds,
                                       pause_seconds=settings.market.request_pause_seconds)
                tickers = {x["symbol"]: x for x in client.ticker_24hr()}
                for symbol in sorted(symbols):
                    rows = client.klines(symbol, "4h", limit=25)
                    market[symbol] = {"price": float(tickers[symbol]["lastPrice"]),
                                      "quote_time_ms": int(tickers[symbol]["closeTime"]),
                                      "ticker": tickers[symbol],
                                      "bars": [r for r in rows if int(r[6]) <= bar_close]}
            # Reject fetches straddling the allowed slot; never timestamp them earlier.
            now = utc_now()
            if int(_dt(now).timestamp() * 1000) // BAR_MS * BAR_MS - 1 != bar_close:
                raise ValueError("fetch_crossed_4h_boundary")
        input_data["market"] = market
        _validate_market(market, symbols, now)
        state = advance(state, candidates, market, settings, account, now)
    except Exception as exc:
        status, reason = "GAP_AFFECTED", f"{type(exc).__name__}: {exc}"
        state = _censor(json.loads(epoch["state_json"]), reason)
        # Invalid float inputs remain diagnostics, never trusted executable state.
        input_data["market"] = repr(market) if market is not None else None
    tick_id = uuid.uuid4().hex
    with connect_db(settings.output.database_path) as connection:
        connection.execute("BEGIN IMMEDIATE")
        current = connection.execute("SELECT * FROM paper_forward_epochs WHERE epoch_id=?", (epoch["epoch_id"],)).fetchone()
        if current["status"] != "ACTIVE" or current["last_tick"] != epoch["last_tick"]:
            raise RuntimeError("shadow epoch changed concurrently; retry with a fresh observation")
        connection.execute(
            "INSERT INTO paper_forward_ticks VALUES (?,?,?,?,?,?,?,?,?,?)",
            (tick_id, epoch["epoch_id"], account, run_id, now, bar_close, status, reason, _json(input_data), _json(state)),
        )
        connection.execute(
            "UPDATE paper_forward_epochs SET updated_at=?,status=?,reason=?,state_json=?,last_bar=?,last_tick=? WHERE epoch_id=?",
            (now, "ACTIVE" if status == "OK" else status, reason, _json(state), bar_close, tick_id, epoch["epoch_id"]),
        )
    return {"status": status, "reason": reason, "epoch_id": epoch["epoch_id"], "tick_id": tick_id}


def forward_summary(settings, account_name=None):
    account = account_name or settings.paper.account_name
    with connect_db(settings.output.database_path) as connection:
        exists = connection.execute("SELECT 1 FROM sqlite_master WHERE name='paper_forward_epochs'").fetchone()
        rows = connection.execute("SELECT * FROM paper_forward_epochs WHERE account_name=? ORDER BY started_at, rowid", (account,)).fetchall() if exists else []
    result = {"account": account, "controls_paper": False, "execution": "sampled_quote_v1",
              "research_incumbent_alias": "atr_reclaim_0_35_shadow", "epochs": [],
              "verdict": "insufficient_paired_forward_evidence"}
    for row in rows:
        state = json.loads(row["state_json"])
        item = {"epoch_id": row["epoch_id"], "started_at": row["started_at"], "updated_at": row["updated_at"],
                "status": row["status"], "reason": row["reason"], "lines": {}, "paired_terminal": 0, "paired_closed_trades": 0}
        for name, line in state["lines"].items():
            records = list(line["trades"].values())
            item["lines"][name] = {
                "opportunities": len(records), "entered": sum(r["trade"]["entered_at_utc"] is not None for r in records),
                "closed_trades": sum(r["trade"]["status"] in {"CLOSED", "STOPPED"} for r in records),
                "open": sum(r["trade"]["status"] in OPEN for r in records),
                "censored": sum(r["right_censored"] for r in records),
                "cash": line["cash"], "equity": line.get("equity", line["cash"]),
                "fees": sum(r["fees"] for r in records),
                "closed_net_pnl": sum(r.get("net_pnl", 0) for r in records),
                "quality_counts": {q: sum(r["data_quality_state"] == q for r in records) for q in ("CLEAN", "DEGRADED")},
            }
        if row["status"] == "ACTIVE":
            for oid in state["seen"]:
                pair = [line["trades"][oid] for line in state["lines"].values()]
                item["paired_terminal"] += int(all(r["trade"]["status"] not in OPEN and r["trusted"] for r in pair))
                item["paired_closed_trades"] += int(all(r["trade"]["status"] in {"CLOSED", "STOPPED"} and r["trusted"] for r in pair))
        result["epochs"].append(item)
    return result


def write_forward_report(settings, account_name=None):
    summary = forward_summary(settings, account_name)
    now = datetime.now(timezone.utc).astimezone()
    directory = settings.output.reports_dir / now.strftime("%Y-%m-%d")
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"independent_shadow_{now:%H%M%S}_{uuid.uuid4().hex[:6]}.md"
    path.write_text(
        "# 独立前向 shadow 状态\n\n"
        "执行口径：每个 4h 档的一次 ticker 采样；不模拟常驻保护单。controls_paper=false。\n\n"
        "incumbent 与 ATR 0.35 为同义线，不重复计数。GAP_AFFECTED/CONFIG_CHANGED 的金额仅供诊断，"
        "不属于可信组合成绩。paired_terminal 含未入场终态；paired_closed_trades 才是两线都入场并退出。\n\n"
        "工程接入与自然运行验收分开；当前不据此判断 ATR 收益有效。\n\n```json\n" +
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n```\n", encoding="utf-8",
    )
    return path
