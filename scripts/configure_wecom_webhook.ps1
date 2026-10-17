param(
    [switch]$SkipTest
)

$ErrorActionPreference = "Stop"
$secureWebhook = Read-Host "Paste the Enterprise WeChat robot webhook URL (input is hidden)" -AsSecureString
$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureWebhook)
try {
    $webhookUrl = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr).Trim()
}
finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
}

$uri = $null
if (-not [Uri]::TryCreate($webhookUrl, [UriKind]::Absolute, [ref]$uri)) {
    throw "The webhook is not a valid absolute URL."
}
if (
    $uri.Scheme -ne "https" -or
    $uri.Host -ne "qyapi.weixin.qq.com" -or
    $uri.AbsolutePath -ne "/cgi-bin/webhook/send" -or
    [string]::IsNullOrWhiteSpace($uri.Query) -or
    $uri.Query -notmatch "(^|[?&])key=[^&]+"
) {
    throw "The webhook must be an https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=... URL."
}

if (-not $SkipTest) {
    $body = @{
        msgtype = "markdown"
        markdown = @{
            content = (
                "## CryptoTrading scheduler restored`n" +
                "- time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')`n" +
                "- host: $env:COMPUTERNAME`n" +
                "- status: webhook connectivity test"
            )
        }
    } | ConvertTo-Json -Depth 4
    Invoke-RestMethod `
        -Uri $webhookUrl `
        -Method Post `
        -ContentType "application/json; charset=utf-8" `
        -Body $body `
        -TimeoutSec 15 | Out-Null
    Write-Host "Enterprise WeChat test notification sent."
}

[Environment]::SetEnvironmentVariable(
    "CRYPTO_TRADING_WECOM_WEBHOOK_URL",
    $webhookUrl,
    "User"
)
$env:CRYPTO_TRADING_WECOM_WEBHOOK_URL = $webhookUrl
Write-Host "Saved CRYPTO_TRADING_WECOM_WEBHOOK_URL in the current user's environment."
