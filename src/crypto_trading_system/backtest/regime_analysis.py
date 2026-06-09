from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import sqlite3
from pathlib import Path

from ..config import Settings
from ..market_regime import classify_market_regime
from ..report_versions import next_report_version, versioned_markdown_filename
from ..storage import init_db


@dataclass(frozen=True)
class RegimeTrade:
    run_id: str
    trade_id: str
    symbol: str
    status: str
    created_at_utc: str
    closed_at_utc: str | None
    net_pnl: float
    gross_pnl: float
    r_multiple_net: float | None


@dataclass(frozen=True)
class RegimeBucket:
    status: str
    closed_trades: int
    wins: int
    losses: int
    stop_trades: int
    net_pnl: float
    gross_profit: float
    gross_loss: float
    avg_r: float | None


@dataclass(frozen=True)
class RunRegimeBreakdown:
    run_id: str
    label: str
    start_utc: str
    end_utc: str
    buckets: dict[str, RegimeBucket]
    unknown_trades: int


@dataclass(frozen=True)
class RegimeComparison:
    baseline: RunRegimeBreakdown
    variant: RunRegimeBreakdown
    report_paths: list[Path]


def _parse_utc(value: str) -> datetime:
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _ms(value: str) -> int:
    return int(_parse_utc(value).timestamp() * 1000)


def _normalise_kline(row: sqlite3.Row) -> list:
    return [
        int(row["open_time"]),
        str(row["open"]),
        str(row["high"]),
        str(row["low"]),
        str(row["close"]),
        str(row["volume"]),
        int(row["close_time"]),
        str(row["quote_volume"]),
        int(row["trades"]),
        str(row["taker_buy_base_volume"]),
        str(row["taker_buy_quote_volume"]),
        "0",
    ]


def _load_1d_before(connection: sqlite3.Connection, symbol: str, decision_ms: int, limit: int = 120) -> list[list]:
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """
        SELECT *
        FROM kline_cache
        WHERE source = 'Binance'
          AND symbol = ?
          AND interval = '1d'
          AND close_time < ?
          AND is_closed = 1
        ORDER BY open_time DESC
        LIMIT ?
        """,
        (symbol, decision_ms, limit),
    ).fetchall()
    return [_normalise_kline(row) for row in reversed(rows)]


def _load_run(connection: sqlite3.Connection, run_id: str) -> tuple[str, str]:
    row = connection.execute(
        "SELECT start_utc, end_utc FROM backtest_runs WHERE run_id = ?",
        (run_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"Unknown backtest run_id: {run_id}")
    return str(row[0]), str(row[1])


def _load_closed_trades(connection: sqlite3.Connection, run_id: str) -> list[RegimeTrade]:
    rows = connection.execute(
        """
        SELECT run_id, trade_id, symbol, status, created_at_utc, closed_at_utc,
               net_pnl, gross_pnl, r_multiple_net
        FROM backtest_trades
        WHERE run_id = ?
          AND entered_at_utc IS NOT NULL
          AND closed_at_utc IS NOT NULL
        ORDER BY created_at_utc, symbol
        """,
        (run_id,),
    ).fetchall()
    return [
        RegimeTrade(
            run_id=str(row[0]),
            trade_id=str(row[1]),
            symbol=str(row[2]),
            status=str(row[3]),
            created_at_utc=str(row[4]),
            closed_at_utc=None if row[5] is None else str(row[5]),
            net_pnl=float(row[6] or 0),
            gross_pnl=float(row[7] or 0),
            r_multiple_net=None if row[8] is None else float(row[8]),
        )
        for row in rows
    ]


def _trade_regime(connection: sqlite3.Connection, trade: RegimeTrade) -> str:
    decision_ms = _ms(trade.created_at_utc)
    btc_1d = _load_1d_before(connection, "BTCUSDT", decision_ms)
    eth_1d = _load_1d_before(connection, "ETHUSDT", decision_ms)
    return classify_market_regime(btc_1d, eth_1d).status


def _bucket(status: str, trades: list[RegimeTrade]) -> RegimeBucket:
    wins = [trade for trade in trades if trade.net_pnl > 0]
    losses = [trade for trade in trades if trade.net_pnl < 0]
    gross_profit = sum(trade.net_pnl for trade in wins)
    gross_loss = abs(sum(trade.net_pnl for trade in losses))
    r_values = [trade.r_multiple_net for trade in trades if trade.r_multiple_net is not None]
    return RegimeBucket(
        status=status,
        closed_trades=len(trades),
        wins=len(wins),
        losses=len(losses),
        stop_trades=sum(1 for trade in trades if trade.status == "STOPPED"),
        net_pnl=sum(trade.net_pnl for trade in trades),
        gross_profit=gross_profit,
        gross_loss=gross_loss,
        avg_r=(sum(r_values) / len(r_values)) if r_values else None,
    )


def _analyse_run(connection: sqlite3.Connection, run_id: str, label: str) -> RunRegimeBreakdown:
    start_utc, end_utc = _load_run(connection, run_id)
    grouped: dict[str, list[RegimeTrade]] = {}
    unknown_trades = 0
    for trade in _load_closed_trades(connection, run_id):
        status = _trade_regime(connection, trade)
        if status == "UNKNOWN":
            unknown_trades += 1
        grouped.setdefault(status, []).append(trade)
    buckets = {status: _bucket(status, trades) for status, trades in grouped.items()}
    return RunRegimeBreakdown(
        run_id=run_id,
        label=label,
        start_utc=start_utc,
        end_utc=end_utc,
        buckets=buckets,
        unknown_trades=unknown_trades,
    )


def _pct(numerator: int | float, denominator: int | float) -> float | None:
    if denominator == 0:
        return None
    return float(numerator) / float(denominator) * 100


def _profit_factor(bucket: RegimeBucket) -> float | None:
    if bucket.gross_loss == 0:
        return None if bucket.gross_profit == 0 else float("inf")
    return bucket.gross_profit / bucket.gross_loss


def _fmt(value: float | None, suffix: str = "", digits: int = 2) -> str:
    if value is None:
        return "n/a"
    if value == float("inf"):
        return "inf"
    return f"{value:.{digits}f}{suffix}"


def render_regime_comparison(comparison: RegimeComparison, version: str) -> str:
    statuses = sorted(set(comparison.baseline.buckets) | set(comparison.variant.buckets))
    lines = [
        "---",
        f"created: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "tags:",
        "  - crypto",
        "  - trading-system",
        "  - regime-analysis",
        f"baseline_run_id: {comparison.baseline.run_id}",
        f"variant_run_id: {comparison.variant.run_id}",
        f"report_version: {version}",
        "---",
        "",
        f"# Market Regime Breakdown {version}",
        "",
        f"- baseline: `{comparison.baseline.label}` / `{comparison.baseline.run_id}`",
        f"- variant: `{comparison.variant.label}` / `{comparison.variant.run_id}`",
        f"- period: `{comparison.baseline.start_utc}` -> `{comparison.baseline.end_utc}`",
        "- grouping: trade `created_at_utc` classified by BTC/ETH daily regime.",
        "",
        "## Regime Metrics",
        "",
        "| Regime | baseline closed | variant closed | baseline PF | variant PF | baseline net PnL | variant net PnL | baseline win | variant win | baseline stop | variant stop | baseline avg R | variant avg R |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for status in statuses:
        base = comparison.baseline.buckets.get(status, _bucket(status, []))
        variant = comparison.variant.buckets.get(status, _bucket(status, []))
        lines.append(
            "| "
            + " | ".join(
                [
                    status,
                    str(base.closed_trades),
                    str(variant.closed_trades),
                    _fmt(_profit_factor(base)),
                    _fmt(_profit_factor(variant)),
                    _fmt(base.net_pnl),
                    _fmt(variant.net_pnl),
                    _fmt(_pct(base.wins, base.closed_trades), "%"),
                    _fmt(_pct(variant.wins, variant.closed_trades), "%"),
                    _fmt(_pct(base.stop_trades, base.closed_trades), "%"),
                    _fmt(_pct(variant.stop_trades, variant.closed_trades), "%"),
                    _fmt(base.avg_r),
                    _fmt(variant.avg_r),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            f"- baseline UNKNOWN trades: {comparison.baseline.unknown_trades}",
            f"- variant UNKNOWN trades: {comparison.variant.unknown_trades}",
            "- Profit factor uses closed trade net PnL within each regime bucket.",
            "- Drawdown is not attributed by regime in this report; use it as a trade-quality stratification view.",
            "",
            "## Raw Buckets",
            "",
            "```json",
            json.dumps(
                {
                    "baseline": {
                        status: comparison.baseline.buckets[status].__dict__
                        for status in sorted(comparison.baseline.buckets)
                    },
                    "variant": {
                        status: comparison.variant.buckets[status].__dict__
                        for status in sorted(comparison.variant.buckets)
                    },
                },
                ensure_ascii=False,
                indent=2,
            ),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def write_regime_comparison_report(settings: Settings, comparison: RegimeComparison, report_date: str | None = None) -> RegimeComparison:
    date_part = report_date or datetime.now().strftime("%Y-%m-%d")
    reports_dir = settings.output.reports_dir / date_part
    obsidian_dir = settings.output.obsidian_dir / "Reports" / date_part if settings.output.obsidian_dir else None
    prefix = f"backtest_regime_breakdown_{comparison.baseline.run_id}_{comparison.variant.run_id}"
    version_number = next_report_version([reports_dir, obsidian_dir], prefix)
    version = f"v{version_number}"
    filename = versioned_markdown_filename(prefix, version_number)
    markdown = render_regime_comparison(comparison, version)
    report_paths: list[Path] = []
    for directory in [reports_dir, obsidian_dir]:
        if directory is None:
            continue
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / filename
        path.write_text(markdown, encoding="utf-8")
        report_paths.append(path)
    return RegimeComparison(comparison.baseline, comparison.variant, report_paths)


def build_regime_comparison(settings: Settings, baseline_run_id: str, variant_run_id: str) -> RegimeComparison:
    init_db(settings.output.database_path)
    with sqlite3.connect(settings.output.database_path) as connection:
        comparison = RegimeComparison(
            baseline=_analyse_run(connection, baseline_run_id, "baseline"),
            variant=_analyse_run(connection, variant_run_id, "variant"),
            report_paths=[],
        )
    return comparison
