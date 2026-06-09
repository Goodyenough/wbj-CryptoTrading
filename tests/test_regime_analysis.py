from __future__ import annotations

from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from crypto_trading_system.backtest.regime_analysis import (
    RegimeBucket,
    RegimeComparison,
    RunRegimeBreakdown,
    render_regime_comparison,
    _load_closed_trades,
)


def test_render_regime_comparison_outputs_bucket_metrics() -> None:
    comparison = RegimeComparison(
        baseline=RunRegimeBreakdown(
            run_id="base",
            label="baseline",
            start_utc="2025-01-01T00:00:00+00:00",
            end_utc="2025-09-01T00:00:00+00:00",
            unknown_trades=0,
            buckets={
                "RISK_OFF": RegimeBucket(
                    status="RISK_OFF",
                    closed_trades=2,
                    wins=1,
                    losses=1,
                    stop_trades=1,
                    net_pnl=-10.0,
                    gross_profit=20.0,
                    gross_loss=30.0,
                    avg_r=-0.1,
                )
            },
        ),
        variant=RunRegimeBreakdown(
            run_id="var",
            label="variant",
            start_utc="2025-01-01T00:00:00+00:00",
            end_utc="2025-09-01T00:00:00+00:00",
            unknown_trades=1,
            buckets={
                "RISK_OFF": RegimeBucket(
                    status="RISK_OFF",
                    closed_trades=2,
                    wins=2,
                    losses=0,
                    stop_trades=0,
                    net_pnl=40.0,
                    gross_profit=40.0,
                    gross_loss=0.0,
                    avg_r=0.4,
                )
            },
        ),
        report_paths=[],
    )

    report = render_regime_comparison(comparison, "v1")

    assert "Market Regime Breakdown v1" in report
    assert "| RISK_OFF | 2 | 2 | 0.67 | inf | -10.00 | 40.00 | 50.00% | 100.00% | 50.00% | 0.00% | -0.10 | 0.40 |" in report
    assert "variant UNKNOWN trades: 1" in report


def test_load_closed_trades_ignores_unentered_plans(tmp_path: Path) -> None:
    db_path = tmp_path / "trades.db"
    connection = sqlite3.connect(db_path)
    try:
        connection.execute(
            """
            CREATE TABLE backtest_trades (
                run_id TEXT,
                trade_id TEXT,
                symbol TEXT,
                status TEXT,
                created_at_utc TEXT,
                entered_at_utc TEXT,
                closed_at_utc TEXT,
                net_pnl REAL,
                gross_pnl REAL,
                r_multiple_net REAL
            )
            """
        )
        connection.execute(
            "INSERT INTO backtest_trades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("run", "entered", "BTCUSDT", "STOPPED", "2025-01-01T00:00:00+00:00", "2025-01-01T04:00:00+00:00", "2025-01-02T00:00:00+00:00", -10, -9, -1),
        )
        connection.execute(
            "INSERT INTO backtest_trades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ("run", "expired", "ETHUSDT", "INVALIDATED", "2025-01-01T00:00:00+00:00", None, "2025-01-02T00:00:00+00:00", 0, 0, None),
        )

        trades = _load_closed_trades(connection, "run")
    finally:
        connection.close()

    assert [trade.trade_id for trade in trades] == ["entered"]


if __name__ == "__main__":
    test_render_regime_comparison_outputs_bucket_metrics()
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        test_load_closed_trades_ignores_unentered_plans(Path(tmp))
    print("test_regime_analysis=passed")
