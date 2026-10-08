"""Fixed-window, read-only ATR 0.35 evidence review; no new strategy backtest.

Run from the repo root: python scripts/review_atr_shadow_evidence.py
Snapshot pairing, independent decision-time kline checks, and prior gap-audit
outcomes are kept separate. No production DB writers are imported.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from crypto_trading_system.indicators import atr

OUT = ROOT / "reports/2026-10-09/atr_shadow_evidence"
PREVIOUS = ROOT / "reports/2026-10-09/closed_trade_gap_evidence"
START, END = "2026-08-15T16:00:00Z", "2026-09-24T16:00:00Z"
LINES = {"reference_baseline", "atr_reclaim_0_35_shadow", "research_incumbent"}
STEP = 14_400_000


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def epoch(value):
    return int(datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()*1000)


def pair_rows(rows):
    groups = defaultdict(dict)
    for r in rows:
        key = (r["plan_id"], r["kline_time"])
        if r["line_name"] in groups[key]:
            raise ValueError(f"Duplicate decision line: {key}")
        groups[key][r["line_name"]] = r
    for key, lines in groups.items():
        if set(lines) != LINES:
            raise ValueError(f"Incomplete lines: {key}")
        ref = lines["reference_baseline"]
        for r in lines.values():
            for field in ("decision_time", "current_price", "last_4h_close", "entry_high", "atr_4h", "capacity_state"):
                if r[field] != ref[field]:
                    raise ValueError(f"Unpaired context: {key} {field}")
            if r["controls_paper"]:
                raise ValueError("Shadow must not control paper")
        a = ref["atr_4h"]
        original = ref["last_4h_close"] >= ref["entry_high"]
        filtered = bool(a and a > 0 and ref["last_4h_close"] >= ref["entry_high"]+0.35*a)
        if bool(ref["accepted"]) != original:
            raise ValueError("Original rule does not reproduce")
        if any(bool(lines[k]["accepted"]) != filtered for k in LINES-{"reference_baseline"}):
            raise ValueError("ATR rule does not reproduce")
        if epoch(ref["kline_time"]) >= epoch(ref["decision_time"]):
            raise ValueError("Decision uses a future bar")
    return groups


def bars_for(row):
    last_open = epoch(row["kline_time"]) // STEP * STEP
    first_open = last_open - 23*STEP
    target = OUT / f"{row['symbol']}_{last_open}_4h.json"
    if target.exists():
        evidence = json.loads(target.read_text(encoding="utf-8"))
    else:
        found = {}
        sources = []
        for path in PREVIOUS.glob(row["symbol"]+"_4h_*.json"):
            raw = json.loads(path.read_text(encoding="utf-8"))
            for b in raw["bars"]:
                if first_open <= b[0] <= last_open:
                    if b[0] in found and found[b[0]] != b:
                        raise ValueError("Conflicting historical evidence")
                    found[b[0]] = b
            sources.append({"file":str(path.relative_to(ROOT)),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
        if len(found)==24:
            bars=[found[k] for k in sorted(found)]
            evidence={"source":"prior Binance audit evidence", "sources":sources,"bars":bars}
        else:
            url="https://api.binance.com/api/v3/klines?"+urllib.parse.urlencode(dict(
                symbol=row["symbol"],interval="4h",startTime=first_open,endTime=last_open+STEP-1,limit=1000))
            with urllib.request.urlopen(url,timeout=25) as response:
                bars=json.load(response)
            evidence={"source":"Binance Spot", "url":url,"fetched_at":datetime.now(timezone.utc).isoformat(),"bars":bars}
        save(target,evidence)
    bars=evidence["bars"]
    assert [b[0] for b in bars]==list(range(first_open,last_open+1,STEP))
    for b in bars:
        o,h,l,c,v=map(float,b[1:6])
        assert 0 < l <= min(o,c) <= max(o,c) <= h and v>=0
        assert int(b[6])==b[0]+STEP-1
    assert bars[-1][6] < epoch(row["decision_time"])
    assert math.isclose(float(bars[-1][4]),row["last_4h_close"],rel_tol=1e-10)
    assert math.isclose(atr(bars),row["atr_4h"],rel_tol=1e-10)
    return str(target.relative_to(ROOT))


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    snapshot=OUT/"original_shadow_records.json"
    if snapshot.exists():
        original=json.loads(snapshot.read_text(encoding="utf-8"))
    else:
        with sqlite3.connect((ROOT/"data/crypto_trading.db").as_uri()+"?mode=ro",uri=True) as c:
            c.row_factory=sqlite3.Row
            rows=[dict(r) for r in c.execute("SELECT * FROM paper_shadow_decisions WHERE plan_id IS NOT NULL AND decision_time>=? AND decision_time<? ORDER BY decision_time,plan_id,line_name",(START,END))]
            ids=sorted({r["plan_id"] for r in rows if r["line_name"]=="reference_baseline" and r["accepted"]})
            plans={}
            for pid in ids:
                p=dict(c.execute("SELECT * FROM paper_plans WHERE plan_id=?",(pid,)).fetchone())
                asof=c.execute("SELECT * FROM paper_snapshots WHERE plan_id=? AND snapshot_time<? ORDER BY snapshot_time DESC LIMIT 1",(pid,END)).fetchone()
                obs=c.execute("SELECT * FROM paper_shadow_candidate_observations WHERE scan_id=? AND symbol=? AND account_name=?",(p["source_scan_id"],p["symbol"],p["account_name"])).fetchone()
                candidates=[dict(r) for r in c.execute("SELECT * FROM paper_shadow_counterfactual_outcomes WHERE observation_id=?",(obs["observation_id"],))]
                after=c.execute("SELECT COUNT(*) FROM paper_shadow_decisions WHERE plan_id=? AND decision_time>?",(pid,p["entered_at_utc"])).fetchone()[0]
                plans[pid]={"current_plan":p,"snapshot_at_cutoff":dict(asof),"candidate_observation":dict(obs),"candidate_outcomes_current":candidates,"rows_after_baseline_entry_at_capture":after}
            original={"captured_at":datetime.now(timezone.utc).isoformat(),"start_inclusive":START,"end_exclusive":END,"rows":rows,"accepted_plans":plans}
        save(snapshot,original)
    pairs=pair_rows(original["rows"])
    audited={r["plan_id"]:r for r in json.loads((PREVIOUS/"replay_audit.json").read_text(encoding="utf-8"))}
    review=[]
    for key,lines in pairs.items():
        r=lines["reference_baseline"]
        if not r["accepted"]:
            continue
        pid=r["plan_id"]
        p=original["accepted_plans"][pid]
        assert r["decision_time"]==p["current_plan"]["entered_at_utc"]
        margin=(r["last_4h_close"]-r["entry_high"])/r["atr_4h"]
        assert math.isclose(margin,r["reclaim_margin_atr"],abs_tol=1e-12)
        exclusions=[]
        if p["rows_after_baseline_entry_at_capture"]==0:
            exclusions.append("no_independent_plan_decisions_after_baseline_entry")
        if pid in audited:
            exclusions.append("baseline_has_collection_gaps_only_partial_reconstruction")
        if p["snapshot_at_cutoff"]["status"] not in {"CLOSED","STOPPED"}:
            exclusions.append("baseline_not_closed_at_fixed_cutoff")
        if p["candidate_observation"]["data_quality_state"]!="CLEAN":
            exclusions.append("not_a_clean_provider_sample")
        result={"plan_id":pid,"symbol":r["symbol"],"decision_time":r["decision_time"],"margin_atr":margin,
            "extra_close_needed":r["entry_high"]+0.35*r["atr_4h"]-r["last_4h_close"],
            "baseline_accept":True,"atr_accept":bool(lines["atr_reclaim_0_35_shadow"]["accepted"]),
            "capacity":r["capacity_state"],"data_quality":p["candidate_observation"]["data_quality_state"],
            "status_at_cutoff":p["snapshot_at_cutoff"]["status"],"independent_bar_check":bars_for(r),
            "performance_exclusions":exclusions,
            "clean_paired_terminal_performance_eligible":not exclusions}
        if pid in audited:
            a=audited[pid]
            result["baseline_outcome_class"]="gap_affected_fixed_entry_reconstruction"
            result["baseline_conditional_gross_pnl"]=a["sensitivities"]["high"]["gross_pnl"]
            result["verified_missed_stop"]="whole_minute_stop_proof" in a
        else:
            result["baseline_outcome_class"]="right_censored_at_cutoff_unreviewed"
        review.append(result)
        print(json.dumps(result,ensure_ascii=False),flush=True)
    summary={"decision_rows":len(original["rows"]),"paired_moments":len(pairs),
        "unique_plan_count":len({k[0] for k in pairs}),"baseline_accept_moments":len(review),
        "atr_accept_moments":sum(bool(x["atr_reclaim_0_35_shadow"]["accepted"]) for x in pairs.values()),
        "joint_reject_moments":sum(not x["reference_baseline"]["accepted"] for x in pairs.values()),
        "margin_min":min(r["margin_atr"] for r in review),"margin_max":max(r["margin_atr"] for r in review),
        "accepted_data_quality":dict(Counter(r["data_quality"] for r in review)),
        "accepted_capacity":dict(Counter(r["capacity"] for r in review)),
        "clean_paired_terminal_performance_count":sum(x["clean_paired_terminal_performance_eligible"] for x in review),
        "accepted_reviews":review}
    save(OUT/"review.json",summary)
    save(OUT/"sha256.json",{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob("*.json") if p.name!="sha256.json"})
    print(json.dumps({k:v for k,v in summary.items() if k!="accepted_reviews"}),flush=True)


if __name__=="__main__":
    main()
