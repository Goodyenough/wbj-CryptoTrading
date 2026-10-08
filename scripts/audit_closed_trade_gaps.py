"""Read-only, fixed-cohort evidence collection for the 2026-10-09 gap audit.

Never imports production database writers or changes paper state. Public Binance
responses and original plan/event/snapshot/funnel rows are saved under reports.
Run from the repository root: python scripts/audit_closed_trade_gaps.py
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sqlite3
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from crypto_trading_system.models import PaperTrade
from crypto_trading_system.trade_state import step_trade
from crypto_trading_system.indicators import ema
OUT = ROOT / "reports/2026-10-09/closed_trade_gap_evidence"
PLAN_IDS = (
    "ecdc3e95f224", "bffd2fdd7e2b", "0a265e9f2163", "d6075516aea8",
    "4f2f0f1fa0e7", "2d74b7ff6191", "5ff6dab72dfa", "549cfdd6bdc4",
)


def dt(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def iso(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).isoformat()


def ms(value):
    return int(dt(value).timestamp() * 1000)


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def fetch(symbol, interval, start, end):
    """Persist each bounded request; reject missing/duplicate/invalid bars."""
    path = OUT / f"{symbol}_{interval}_{start}_{end}.json"
    step = {"1m": 60_000, "1h": 3_600_000, "4h": 14_400_000}[interval]
    first = start // step * step
    last = end // step * step
    if path.exists():
        record = json.loads(path.read_text(encoding="utf-8"))
        bars = record["bars"]
    else:
        cursor = first
        bars, requests = [], []
        while cursor <= last:
            query = urllib.parse.urlencode(dict(symbol=symbol, interval=interval,
                startTime=cursor, endTime=last + step - 1, limit=1000))
            url = "https://api.binance.com/api/v3/klines?" + query
            with urllib.request.urlopen(url, timeout=25) as response:
                chunk = json.load(response)
            if not isinstance(chunk, list) or not chunk:
                raise ValueError(f"Incomplete response: {symbol} {interval} {cursor}")
            requests.append(url)
            bars.extend(chunk)
            cursor = int(chunk[-1][0]) + step
        record = dict(symbol=symbol, interval=interval, source="Binance Spot",
            fetched_at=datetime.now(timezone.utc).isoformat(), requests=requests, bars=bars)
        save(path, record)
    opens = [int(b[0]) for b in bars]
    assert opens == list(range(first, last + 1, step)), (symbol, interval, "coverage")
    for b in bars:
        o, h, l, c, v = map(float, b[1:6])
        assert 0 < l <= min(o, c) <= max(o, c) <= h and v >= 0
        assert int(b[6]) == int(b[0]) + step - 1
    return bars


def collect():
    OUT.mkdir(parents=True, exist_ok=True)
    source_path = OUT / "original_records.json"
    if source_path.exists():
        source = json.loads(source_path.read_text(encoding="utf-8"))
    else:
        with sqlite3.connect((ROOT / "data/crypto_trading.db").as_uri() + "?mode=ro", uri=True) as con:
            con.row_factory = sqlite3.Row
            source = {"captured_at": datetime.now(timezone.utc).isoformat(), "plans": []}
            for pid in PLAN_IDS:
                p = dict(con.execute("SELECT * FROM paper_plans WHERE plan_id=?", (pid,)).fetchone())
                assert p["status"] in {"CLOSED", "STOPPED"}
                item = {"plan": p}
                for name, table, sort in [
                    ("events", "paper_events", "event_time,event_id"),
                    ("snapshots", "paper_snapshots", "snapshot_time,snapshot_id"),
                    ("funnel", "paper_shadow_funnel_events", "event_time,event_id"),
                ]:
                    item[name] = [dict(r) for r in con.execute(
                        f"SELECT * FROM {table} WHERE plan_id=? ORDER BY {sort}", (pid,))]
                source["plans"].append(item)
        save(source_path, source)
    summaries = []
    for item in source["plans"]:
        p = item["plan"]
        # Each trade gets full holding-window coverage plus pre-entry history.
        hourly = fetch(p["symbol"], "1h", ms(p["created_at"]), ms(p["closed_at"]))
        fetch(p["symbol"], "4h", ms(p["created_at"]) - 10 * 86_400_000, ms(p["closed_at"]))
        evaluated = {p["entered_at_utc"], p["closed_at"]}
        evaluated.update(e["event_time"] for e in item["funnel"]
            if e["stage"] == "plan_update_evaluated" and e["reason_code"] in {"closed_4h_available", "ticker_update"}
            and dt(p["entered_at_utc"]) <= dt(e["event_time"]) <= dt(p["closed_at"]))
        times = sorted(evaluated, key=dt)
        gaps = []
        for a, b in zip(times, times[1:]):
            if (dt(b) - dt(a)).total_seconds() <= 6 * 3600:
                continue
            # Full bars strictly inside the gap, never using pre-gap extremes.
            subset = [r for r in hourly if int(r[0]) > ms(a) and int(r[6]) < ms(b)]
            prior = [s for s in item["snapshots"] if dt(s["snapshot_time"]) <= dt(a)]
            stop = float(prior[-1]["stop_current"]) if prior else float(p["stop_initial"])
            def first_touch(index, level, below=False):
                hit = next((r for r in subset if (float(r[index]) <= level if below else float(r[index]) >= level)), None)
                return None if hit is None else {"open_utc": iso(hit[0]), "close_utc": iso(hit[6]), "ohlc": hit[1:5]}
            gaps.append(dict(start=a, end=b, hours=round((dt(b)-dt(a)).total_seconds()/3600, 3),
                frozen_stop=stop, tp1=p["tp1"], tp2=p["tp2"],
                whole_hour_bars=len(subset), low=min(float(r[3]) for r in subset) if subset else None,
                high=max(float(r[2]) for r in subset) if subset else None,
                first_stop_touch=first_touch(3,stop,True), first_tp1_touch=first_touch(2,p["tp1"]),
                first_tp2_touch=first_touch(2,p["tp2"])))
        summary = {"plan_id": p["plan_id"], "symbol":p["symbol"], "original_status":p["status"],
            "original_gross_pnl":p["realized_pnl"], "entry":p["entered_at_utc"], "exit":p["closed_at"], "gaps":gaps}
        summaries.append(summary)
        print(json.dumps(summary), flush=True)
    save(OUT / "gap_screen.json", summaries)
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob("*.json") if p.name != "sha256.json"}
    save(OUT / "sha256.json", hashes)


def restore_entered(p):
    values = {name: p[name] for name in PaperTrade.__dataclass_fields__ if name in p}
    values.update(paper_trade_id=p["plan_id"], source_scan_id=p["source_scan_id"],
        created_at_utc=p["created_at"], updated_at_utc=p["entered_at_utc"],
        status="ENTERED", stop_loss=p["stop_initial"], take_profit_1=p["tp1"], take_profit_2=p["tp2"],
        tp1_hit_at_utc=None, closed_at_utc=None, exit_price=None, realized_pnl=0.0,
        unrealized_pnl=0.0, tp1_trailing_ema_stop_active=False)
    return PaperTrade(**values)


def missed_slots(start, end):
    """Five configured 4h slots; the actual resumption minute is not missing."""
    t = dt(start).replace(minute=10, second=0, microsecond=0)
    while t <= dt(start):
        t += timedelta(hours=1)
    boundary = dt(end).replace(second=0, microsecond=0)
    while t < boundary:
        if t.hour in {0, 4, 8, 16, 20}:
            yield t
        t += timedelta(hours=1)


def analyze():
    source = json.loads((OUT / "original_records.json").read_text(encoding="utf-8"))
    screens = {s["plan_id"]:s for s in json.loads((OUT / "gap_screen.json").read_text(encoding="utf-8"))}
    results = []
    for item in source["plans"]:
        p = item["plan"]
        screen = screens[p["plan_id"]]
        hours = fetch(p["symbol"], "1h", ms(p["created_at"]), ms(p["closed_at"]))
        hour_map = {int(b[0]):b for b in hours}
        four = fetch(p["symbol"], "4h", ms(p["created_at"]) - 10*86_400_000, ms(p["closed_at"]))
        evaluated = {e["event_time"] for e in item["funnel"]
            if e["stage"] == "plan_update_evaluated" and e["reason_code"] in {"closed_4h_available", "ticker_update"}}
        snapshots = {s["snapshot_time"]:s for s in item["snapshots"] if s["snapshot_time"] in evaluated
            and dt(p["entered_at_utc"]) < dt(s["snapshot_time"]) <= dt(p["closed_at"])}
        points = [(dt(t), "actual", float(s["current_price"])) for t,s in snapshots.items()]
        missed=[]
        for gap in screen["gaps"]:
            # Daily at 12 UTC is not invented: scan duration/order is unknown.
            missed.extend((t,"missed_4h",None) for t in missed_slots(gap["start"],gap["end"]))
        def replay(mode):
            trade=restore_entered(p)
            events=[]
            path=points if mode=="baseline" else points+missed
            for t,kind,quote in sorted(path):
                stamp=t.isoformat().replace("+00:00","Z")
                # Same request window as production: 25 bars including the live
                # bar, hence the latest 24 closed bars at these decision times.
                history=[float(b[4]) for b in four if int(b[6]) <= int(t.timestamp()*1000)-60_000][-24:]
                assert len(history)==24
                moving=ema(history,20)
                if kind=="missed_4h":
                    h=hour_map[int(t.replace(minute=0,second=0).timestamp()*1000)]
                    effective_stop=max(trade.stop_loss,trade.entry_price,moving) if trade.tp1_trailing_ema_stop_active else trade.stop_loss
                    low,high=float(h[3]),float(h[2])
                    thresholds=[effective_stop,trade.take_profit_2]
                    if trade.status=="ENTERED":thresholds.append(trade.take_profit_1)
                    # The hour is used only to prove decision invariance for
                    # all prices; never use its close as a decision-time quote.
                    if any(low <= level <= high for level in thresholds):
                        minute=fetch(p["symbol"],"1m",int(t.timestamp()*1000),int(t.timestamp()*1000))[0]
                        quote=float(minute[{"open":1,"high":2,"low":3,"close":4}[mode]])
                        quote_basis="minute_"+mode
                    else:
                        quote=(low+high)/2
                        quote_basis="whole_hour_threshold_invariant"
                else:quote_basis="recorded_snapshot"
                emitted=step_trade(trade,high=quote,low=quote,close=quote,event_time_utc=stamp,
                    move_stop_to_breakeven_on_tp1=False,tp1_trailing_ema_stop=moving,tp1_trailing_ema_stop_ready=True)
                for event in emitted:
                    events.append(dict(time=stamp,event=event.event_type,price=event.price,kind=kind,
                        quote=quote,quote_basis=quote_basis,stop=trade.stop_loss))
                if trade.status in {"CLOSED","STOPPED"}:break
            return dict(status=trade.status,closed_at=trade.closed_at_utc,exit_price=trade.exit_price,
                gross_pnl=trade.realized_pnl,events=events)
        baseline=replay("baseline")
        matches=(baseline["status"]==p["status"] and dt(baseline["closed_at"])==dt(p["closed_at"])
            and abs(baseline["gross_pnl"]-p["realized_pnl"])<1e-6)
        result=dict(plan_id=p["plan_id"],symbol=p["symbol"],baseline_reproduces=matches,
            original_gross_pnl=p["realized_pnl"],baseline=baseline,missed_4h_slots=len(missed),
            sensitivities={mode:replay(mode) for mode in ("open","high","low","close")})
        conservative=result["sensitivities"]["high"]
        if (conservative["status"]=="STOPPED" and conservative["exit_price"]==p["stop_initial"]
                and dt(conservative["closed_at"]) < dt(p["closed_at"])):
            proof_time=ms(conservative["closed_at"])
            minute=fetch(p["symbol"],"1m",proof_time,proof_time)[0]
            assert float(minute[2]) < p["stop_initial"]
            result["whole_minute_stop_proof"]={"time":conservative["closed_at"],
                "minute_high":float(minute[2]),"initial_stop":p["stop_initial"],"ohlc":minute[1:5]}
        results.append(result)
        print(json.dumps({"symbol":p["symbol"],"plan":p["plan_id"],"baseline_ok":matches,
            "original":p["realized_pnl"],"paths":{k:{f:v[f] for f in ("status","closed_at","gross_pnl")} for k,v in result["sensitivities"].items()}}),flush=True)
    save(OUT/"replay_audit.json",results)
    assert all(r["baseline_reproduces"] for r in results), "Cannot attribute differences until baseline reproduces"
    save(OUT/"sha256.json",{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob("*.json") if p.name!="sha256.json"})


if __name__ == "__main__":
    if "--analyze" in sys.argv:
        analyze()
    else:
        collect()
