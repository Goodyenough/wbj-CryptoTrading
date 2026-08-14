from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import http.client
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any

from .config import Settings
from .models import DataQualityIssue, DataSourceCheck, TradeCandidate


class ProviderError(Exception):
    def __init__(
        self,
        message: str,
        status: str = "DATA_WARNING",
        code: str = "EXTERNAL_PROVIDER_UNAVAILABLE",
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _pct_diff(left: float | None, right: float | None) -> float | None:
    if left is None or right is None:
        return None
    return abs(left - right)


def _price_diff_pct(provider_price: float | None, binance_price: float) -> float | None:
    if provider_price is None or binance_price <= 0:
        return None
    return abs(provider_price - binance_price) / binance_price * 100


def _get_json(
    base_url: str,
    path: str,
    params: dict[str, Any] | None,
    headers: dict[str, str] | None,
    timeout_seconds: int,
    retries: int = 2,
    pause_seconds: float = 0.08,
) -> Any:
    query = ""
    if params:
        query = "?" + urllib.parse.urlencode(params)
    url = f"{base_url.rstrip('/')}{path}{query}"
    request_headers = {"User-Agent": "CryptoTradingSystem/0.1"}
    if headers:
        request_headers.update(headers)

    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=request_headers)
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                payload = response.read().decode("utf-8")
            if pause_seconds:
                time.sleep(pause_seconds)
            return json.loads(payload)
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code in {408, 418, 429, 500, 502, 503, 504}:
                time.sleep(2**attempt + 1)
                continue
            raise ProviderError(
                f"HTTP {exc.code} for {url}",
                status="DATA_ERROR",
                code="EXTERNAL_PROVIDER_ERROR",
            ) from exc
        except (urllib.error.URLError, http.client.IncompleteRead, json.JSONDecodeError) as exc:
            last_error = exc
            time.sleep(2**attempt + 1)

    if last_error:
        if isinstance(last_error, urllib.error.HTTPError) and last_error.code in {418, 429}:
            raise ProviderError(
                f"Provider rate limited request for {url}: HTTP {last_error.code}",
                code="EXTERNAL_PROVIDER_RATE_LIMITED",
            ) from last_error
        raise ProviderError(
            f"Failed to fetch {url}: {last_error}",
            code="EXTERNAL_PROVIDER_UNAVAILABLE",
        ) from last_error
    raise ProviderError(f"Failed to fetch {url}", code="EXTERNAL_PROVIDER_UNAVAILABLE")


def _issue_status(issues: list[DataQualityIssue]) -> str:
    if any(issue.severity == "ERROR" for issue in issues):
        return "DATA_ERROR"
    if issues:
        return "DATA_WARNING"
    return "DATA_OK"


def _issue_message(issues: list[DataQualityIssue], default: str) -> str:
    if not issues:
        return default
    return "; ".join(f"[{issue.code}] {issue.message}" for issue in issues)


def _diff_issues(
    price_diff_pct: float | None,
    pct_24h_diff: float | None,
    settings: Settings,
    provider: str,
    mapping_warning: str | None = None,
) -> list[DataQualityIssue]:
    issues: list[DataQualityIssue] = []
    if price_diff_pct is not None and price_diff_pct > settings.data_validation.price_error_pct:
        issues.append(
            DataQualityIssue(
                provider=provider,
                code="EXTERNAL_PRICE_DIFF_ERROR",
                severity="ERROR",
                blocking=True,
                message=f"price diff {price_diff_pct:.2f}% exceeds error threshold",
                context={"price_diff_pct": price_diff_pct},
            )
        )
    elif price_diff_pct is not None and price_diff_pct > settings.data_validation.price_warning_pct:
        issues.append(
            DataQualityIssue(
                provider=provider,
                code="EXTERNAL_PRICE_DIFF_WARNING",
                severity="WARNING",
                blocking=True,
                message=f"price diff {price_diff_pct:.2f}% exceeds warning threshold",
                context={"price_diff_pct": price_diff_pct},
            )
        )

    if pct_24h_diff is not None and pct_24h_diff > settings.data_validation.pct_24h_warning_points:
        issues.append(
            DataQualityIssue(
                provider=provider,
                code="EXTERNAL_24H_DIFF_WARNING",
                severity="WARNING",
                blocking=True,
                message=f"24h change diff {pct_24h_diff:.2f} points exceeds warning threshold",
                context={"pct_24h_diff": pct_24h_diff},
            )
        )

    if mapping_warning:
        issues.append(
            DataQualityIssue(
                provider=provider,
                code="EXTERNAL_IDENTITY_AMBIGUOUS",
                severity="WARNING",
                blocking=False,
                message=mapping_warning,
            )
        )
    return issues


def _status_from_diffs(
    price_diff_pct: float | None,
    pct_24h_diff: float | None,
    settings: Settings,
    provider: str = "External",
    mapping_warning: str | None = None,
) -> tuple[str, str]:
    issues = _diff_issues(price_diff_pct, pct_24h_diff, settings, provider, mapping_warning)
    return _issue_status(issues), _issue_message(
        issues,
        "External source agrees with Binance within thresholds.",
    )


def _binance_check(
    candidate: TradeCandidate,
    fetched_at_utc: str,
    issues: list[DataQualityIssue] | None = None,
) -> DataSourceCheck:
    primary_issues = list(issues or [])
    return DataSourceCheck(
        provider="Binance",
        status=_issue_status(primary_issues),
        provider_asset_id=candidate.symbol,
        provider_symbol=candidate.symbol,
        price_usd=candidate.price,
        pct_24h=candidate.pct_24h,
        volume_24h=candidate.quote_volume_24h,
        last_updated=None,
        fetched_at_utc=fetched_at_utc,
        price_diff_pct=0.0,
        pct_24h_diff=0.0,
        volume_note="Binance USDT spot 24h quoteVolume.",
        message=_issue_message(primary_issues, "Primary market data source passed health checks."),
        blocking=any(issue.blocking for issue in primary_issues),
        identity_status="CONFIRMED",
        issues=primary_issues,
    )


class CoinGeckoClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_url = settings.data_validation.coingecko_base_url

    def _resolve_coin_id(self, base_asset: str) -> tuple[str, str | None]:
        override = self.settings.data_validation.coin_id_overrides.get(base_asset)
        if override:
            return override, None

        payload = _get_json(
            self.base_url,
            "/search",
            {"query": base_asset},
            headers=None,
            timeout_seconds=self.settings.data_validation.request_timeout_seconds,
            pause_seconds=self.settings.data_validation.request_pause_seconds,
        )
        coins = payload.get("coins", []) if isinstance(payload, dict) else []
        exact = [coin for coin in coins if str(coin.get("symbol", "")).upper() == base_asset]
        if not exact:
            raise ProviderError(
                f"CoinGecko could not map symbol {base_asset} to a unique coin id",
                status="DATA_ERROR",
                code="EXTERNAL_IDENTITY_NOT_FOUND",
            )

        exact.sort(key=lambda coin: coin.get("market_cap_rank") or 10**9)
        warning = None
        if len(exact) > 1:
            warning = f"CoinGecko symbol mapping has {len(exact)} exact matches; selected highest market-cap rank"
        return str(exact[0]["id"]), warning

    def market_check(self, candidate: TradeCandidate, fetched_at_utc: str) -> DataSourceCheck:
        coin_id, mapping_warning = self._resolve_coin_id(candidate.base_asset)
        payload = _get_json(
            self.base_url,
            "/coins/markets",
            {
                "vs_currency": "usd",
                "ids": coin_id,
                "price_change_percentage": "24h",
                "per_page": 1,
                "page": 1,
            },
            headers=None,
            timeout_seconds=self.settings.data_validation.request_timeout_seconds,
            pause_seconds=self.settings.data_validation.request_pause_seconds,
        )
        if not isinstance(payload, list) or not payload:
            raise ProviderError(
                f"CoinGecko market data not found for id={coin_id}",
                status="DATA_ERROR",
                code="EXTERNAL_MARKET_DATA_MISSING",
            )

        item = payload[0]
        price = None if item.get("current_price") is None else float(item["current_price"])
        pct_24h = None
        if item.get("price_change_percentage_24h") is not None:
            pct_24h = float(item["price_change_percentage_24h"])
        volume = None if item.get("total_volume") is None else float(item["total_volume"])
        price_diff = _price_diff_pct(price, candidate.price)
        pct_diff = _pct_diff(pct_24h, candidate.pct_24h)
        issues = _diff_issues(price_diff, pct_diff, self.settings, "CoinGecko", mapping_warning)
        status = _issue_status(issues)
        message = _issue_message(issues, "External source agrees with Binance within thresholds.")

        return DataSourceCheck(
            provider="CoinGecko",
            status=status,
            provider_asset_id=coin_id,
            provider_symbol=str(item.get("symbol", "")).upper() or candidate.base_asset,
            price_usd=price,
            pct_24h=pct_24h,
            volume_24h=volume,
            last_updated=item.get("last_updated"),
            fetched_at_utc=fetched_at_utc,
            price_diff_pct=price_diff,
            pct_24h_diff=pct_diff,
            volume_note="CoinGecko total market volume; not the same venue scope as Binance quoteVolume.",
            message=message,
            blocking=any(issue.blocking for issue in issues),
            identity_status="UNCONFIRMED" if mapping_warning else "CONFIRMED",
            issues=issues,
        )


class CoinMarketCapClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.base_url = settings.data_validation.coinmarketcap_base_url
        self.api_key = settings.data_validation.coinmarketcap_api_key

    def market_check(self, candidate: TradeCandidate, fetched_at_utc: str) -> DataSourceCheck:
        if not self.api_key:
            issue = DataQualityIssue(
                provider="CoinMarketCap",
                code="EXTERNAL_PROVIDER_SKIPPED",
                severity="WARNING",
                blocking=False,
                message="Skipped because CMC_API_KEY or COINMARKETCAP_API_KEY is not configured.",
            )
            return DataSourceCheck(
                provider="CoinMarketCap",
                status="DATA_SKIPPED",
                provider_asset_id=None,
                provider_symbol=candidate.base_asset,
                price_usd=None,
                pct_24h=None,
                volume_24h=None,
                last_updated=None,
                fetched_at_utc=fetched_at_utc,
                price_diff_pct=None,
                pct_24h_diff=None,
                volume_note="CoinMarketCap requires an API key.",
                message=issue.message,
                blocking=False,
                identity_status="NOT_CHECKED",
                issues=[issue],
            )

        params: dict[str, Any]
        cmc_id = self.settings.data_validation.cmc_id_overrides.get(candidate.base_asset)
        if cmc_id is not None:
            params = {"id": cmc_id, "convert": "USD"}
        else:
            params = {"symbol": candidate.base_asset, "convert": "USD"}

        payload = _get_json(
            self.base_url,
            "/v2/cryptocurrency/quotes/latest",
            params,
            headers={"X-CMC_PRO_API_KEY": self.api_key},
            timeout_seconds=self.settings.data_validation.request_timeout_seconds,
            pause_seconds=self.settings.data_validation.request_pause_seconds,
        )
        data = payload.get("data", {}) if isinstance(payload, dict) else {}
        if cmc_id is not None:
            rows = [data.get(str(cmc_id))]
        else:
            rows = data.get(candidate.base_asset, [])
        if isinstance(rows, dict):
            rows = [rows]
        rows = [row for row in rows if row]
        if not rows:
            raise ProviderError(
                f"CoinMarketCap market data not found for {candidate.base_asset}",
                status="DATA_ERROR",
                code="EXTERNAL_IDENTITY_NOT_FOUND",
            )

        rows.sort(key=lambda row: row.get("cmc_rank") or 10**9)
        item = rows[0]
        quote = item.get("quote", {}).get("USD", {})
        price = None if quote.get("price") is None else float(quote["price"])
        pct_24h = None if quote.get("percent_change_24h") is None else float(quote["percent_change_24h"])
        volume = None if quote.get("volume_24h") is None else float(quote["volume_24h"])
        price_diff = _price_diff_pct(price, candidate.price)
        pct_diff = _pct_diff(pct_24h, candidate.pct_24h)
        mapping_warning = None
        if cmc_id is None and len(rows) > 1:
            mapping_warning = f"CoinMarketCap symbol mapping has {len(rows)} matches; selected lowest cmc_rank"
        issues = _diff_issues(price_diff, pct_diff, self.settings, "CoinMarketCap", mapping_warning)
        status = _issue_status(issues)
        message = _issue_message(issues, "External source agrees with Binance within thresholds.")

        return DataSourceCheck(
            provider="CoinMarketCap",
            status=status,
            provider_asset_id=str(item.get("id")) if item.get("id") is not None else None,
            provider_symbol=str(item.get("symbol", "")).upper() or candidate.base_asset,
            price_usd=price,
            pct_24h=pct_24h,
            volume_24h=volume,
            last_updated=quote.get("last_updated"),
            fetched_at_utc=fetched_at_utc,
            price_diff_pct=price_diff,
            pct_24h_diff=pct_diff,
            volume_note="CoinMarketCap total market volume; not the same venue scope as Binance quoteVolume.",
            message=message,
            blocking=any(issue.blocking for issue in issues),
            identity_status="CONFIRMED" if cmc_id is not None else ("UNCONFIRMED" if mapping_warning else "CONFIRMED"),
            issues=issues,
        )


def _provider_failure(
    provider: str,
    candidate: TradeCandidate,
    fetched_at_utc: str,
    message: str,
    status: str = "DATA_WARNING",
    code: str = "EXTERNAL_PROVIDER_UNAVAILABLE",
) -> DataSourceCheck:
    if status == "DATA_SKIPPED":
        issue = DataQualityIssue(
            provider=provider,
            code="EXTERNAL_PROVIDER_SKIPPED",
            severity="WARNING",
            blocking=False,
            message=message,
        )
        identity_status = "NOT_CHECKED"
    else:
        issue = DataQualityIssue(
            provider=provider,
            code=code,
            severity="ERROR" if status == "DATA_ERROR" else "WARNING",
            blocking=status == "DATA_ERROR",
            message=message,
        )
        identity_status = "UNCONFIRMED"
    return DataSourceCheck(
        provider=provider,
        status=status,
        provider_asset_id=None,
        provider_symbol=candidate.base_asset,
        price_usd=None,
        pct_24h=None,
        volume_24h=None,
        last_updated=None,
        fetched_at_utc=fetched_at_utc,
        price_diff_pct=None,
        pct_24h_diff=None,
        volume_note="External provider data unavailable.",
        message=message,
        blocking=issue.blocking,
        identity_status=identity_status,
        issues=[issue],
    )


def _overall_status(checks: list[DataSourceCheck]) -> tuple[str, str]:
    all_issues = [issue for check in checks for issue in check.issues]
    external = [check for check in checks if check.provider != "Binance"]
    if any(issue.severity == "ERROR" for issue in all_issues):
        return "DATA_ERROR", _issue_message(all_issues, "At least one data quality error was detected.")
    if all_issues:
        return "DATA_WARNING", _issue_message(all_issues, "At least one data quality warning was detected.")
    if any(check.status == "DATA_ERROR" for check in external):
        return "DATA_ERROR", "At least one external provider returned a data error."
    if any(check.status == "DATA_WARNING" for check in external):
        return "DATA_WARNING", "At least one external provider needs manual review."
    if any(check.status == "DATA_OK" for check in external):
        return "DATA_OK", "External provider checks agree with Binance within configured thresholds."
    return "DATA_WARNING", "No external provider completed validation; use Binance data only with manual review."


def _with_data_checks(candidate: TradeCandidate, checks: list[DataSourceCheck]) -> TradeCandidate:
    status, message = _overall_status(checks)
    issues = [issue for check in checks for issue in check.issues]
    if any(issue.blocking for issue in issues):
        state = "BLOCKED"
    elif issues or not any(check.provider != "Binance" and check.status == "DATA_OK" for check in checks):
        state = "DEGRADED"
    else:
        state = "CLEAN"

    external_checks = [check for check in checks if check.provider != "Binance"]
    if not external_checks:
        identity_status = "NOT_CHECKED"
    elif any(check.identity_status == "UNCONFIRMED" for check in external_checks) or any(
        check.status == "DATA_SKIPPED" for check in external_checks
    ):
        identity_status = "UNCONFIRMED"
    elif any(check.identity_status == "CONFIRMED" for check in external_checks):
        identity_status = "CONFIRMED"
    else:
        identity_status = "UNCONFIRMED"

    risks = list(candidate.risks)
    verdict = candidate.verdict
    if state == "BLOCKED":
        verdict = "只观察"
        risk = "Blocking data-quality issue detected; paper plan creation is not allowed."
    elif state == "DEGRADED":
        risk = "External validation is degraded; this candidate is not a clean data sample."
    else:
        risk = ""
    if risk and risk not in risks:
        risks.append(risk)

    return replace(
        candidate,
        verdict=verdict,
        risks=risks,
        data_quality_status=status,
        data_quality_message=f"{state}: {message}",
        data_checks=checks,
        data_quality_state=state,
        data_quality_issues=issues,
        external_identity_status=identity_status,
    )


def cross_validate_candidates(
    settings: Settings,
    candidates: list[TradeCandidate],
    progress: Callable[[str], None] | None = None,
    primary_issues_by_symbol: Mapping[str, list[DataQualityIssue]] | None = None,
) -> tuple[list[TradeCandidate], list[str]]:
    if not candidates:
        return candidates, []

    fetched_at = _utc_now()
    if not settings.data_validation.enabled:
        checked = []
        for candidate in candidates:
            if primary_issues_by_symbol is None or candidate.symbol not in primary_issues_by_symbol:
                primary_issues = [
                    DataQualityIssue(
                        provider="Binance",
                        code="BINANCE_PRIMARY_CHECK_MISSING",
                        severity="ERROR",
                        blocking=True,
                        message="Binance primary health check was not supplied by scanner.",
                    )
                ]
            else:
                primary_issues = primary_issues_by_symbol[candidate.symbol]
            checks = [
                _binance_check(candidate, fetched_at, primary_issues),
                _provider_failure(
                    "CrossValidation",
                    candidate,
                    fetched_at,
                    "Data cross-check disabled by settings.",
                    status="DATA_SKIPPED",
                ),
            ]
            checked.append(_with_data_checks(candidate, checks))
        return checked, ["Data cross-validation is disabled by settings."]

    coingecko = CoinGeckoClient(settings)
    coinmarketcap = CoinMarketCapClient(settings)
    checked_candidates: list[TradeCandidate] = []
    notes: list[str] = [
        "Data cross-validation enabled: Binance primary source plus CoinGecko; CoinMarketCap is checked when an API key is configured."
    ]
    if not settings.data_validation.coinmarketcap_api_key:
        notes.append("CoinMarketCap cross-check skipped: no CMC_API_KEY or COINMARKETCAP_API_KEY configured.")

    total = len(candidates)
    for index, candidate in enumerate(candidates, start=1):
        if progress is not None:
            progress(f"cross-checking {index}/{total} {candidate.symbol} with external providers")
        if primary_issues_by_symbol is None or candidate.symbol not in primary_issues_by_symbol:
            primary_issues = [
                DataQualityIssue(
                    provider="Binance",
                    code="BINANCE_PRIMARY_CHECK_MISSING",
                    severity="ERROR",
                    blocking=True,
                    message="Binance primary health check was not supplied by scanner.",
                )
            ]
        else:
            primary_issues = primary_issues_by_symbol[candidate.symbol]
        checks = [_binance_check(candidate, fetched_at, primary_issues)]

        try:
            if progress is not None:
                progress(f"checking CoinGecko for {candidate.symbol}")
            checks.append(coingecko.market_check(candidate, fetched_at))
        except ProviderError as exc:
            checks.append(
                _provider_failure(
                    "CoinGecko", candidate, fetched_at, str(exc), status=exc.status, code=exc.code
                )
            )

        try:
            if progress is not None:
                if settings.data_validation.coinmarketcap_api_key:
                    progress(f"checking CoinMarketCap for {candidate.symbol}")
                else:
                    progress("skipping CoinMarketCap: API key not configured")
            checks.append(coinmarketcap.market_check(candidate, fetched_at))
        except ProviderError as exc:
            checks.append(
                _provider_failure(
                    "CoinMarketCap", candidate, fetched_at, str(exc), status=exc.status, code=exc.code
                )
            )

        checked = _with_data_checks(candidate, checks)
        if checked.data_quality_state != "CLEAN":
            notes.append(
                f"{checked.symbol} validation state {checked.data_quality_state}: {checked.data_quality_message}"
            )
        checked_candidates.append(checked)

    return checked_candidates, notes
