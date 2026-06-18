param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("daily", "paper_4h")]
    [string]$Mode
)

$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$python = "C:\Users\10537\miniconda3\envs\ppt-master\python.exe"
$logDir = Join-Path $projectRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

if ($Mode -eq "daily") {
    $logPath = Join-Path $logDir "daily_paper_update.log"
    $label = "daily paper update"
    $commandArgs = @("main.py", "daily", "--account", "demo")
    $successSteps = @("scan done", "add-from-scan done", "paper update done", "paper report done", "observation-dashboard done")
} else {
    $logPath = Join-Path $logDir "paper_4h_update.log"
    $label = "paper 4h update"
    $commandArgs = @("main.py", "paper", "cycle", "--run-type", "paper_4h_update", "--account", "demo")
    $successSteps = @("paper update done", "paper report done", "observation-dashboard done")
}

if (Test-Path -LiteralPath $logPath) {
    $bytes = [System.IO.File]::ReadAllBytes($logPath)
    $isUtf16 = $bytes.Length -ge 2 -and (
        ($bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) -or
        ($bytes[0] -eq 0xFE -and $bytes[1] -eq 0xFF)
    )
    if ($isUtf16) {
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $archivePath = Join-Path $logDir "$([System.IO.Path]::GetFileNameWithoutExtension($logPath)).legacy_utf16_$timestamp.log"
        Move-Item -LiteralPath $logPath -Destination $archivePath
    }
}

function Write-LogLine([string]$Message) {
    Add-Content -LiteralPath $logPath -Value $Message -Encoding UTF8
}

function Get-NotifyWebhookUrl {
    $candidateNames = @(
        "CRYPTO_TRADING_WECOM_WEBHOOK_URL",
        "WECHAT_WORK_WEBHOOK_URL",
        "WECOM_WEBHOOK_URL",
        "QYWX_WEBHOOK_URL"
    )
    foreach ($name in $candidateNames) {
        $value = [Environment]::GetEnvironmentVariable($name, "Process")
        if ([string]::IsNullOrWhiteSpace($value)) {
            $value = [Environment]::GetEnvironmentVariable($name, "User")
        }
        if ([string]::IsNullOrWhiteSpace($value)) {
            $value = [Environment]::GetEnvironmentVariable($name, "Machine")
        }
        if (-not [string]::IsNullOrWhiteSpace($value)) {
            return $value.Trim()
        }
    }
    return $null
}

function Send-TaskNotification([string]$Status, [int]$ExitCode, [string]$ExtraLine) {
    $webhookUrl = Get-NotifyWebhookUrl
    if ([string]::IsNullOrWhiteSpace($webhookUrl)) {
        Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] notification skipped: no WeCom webhook env var"
        return
    }

    $statusText = if ($Status -eq "success") { "completed" } else { "failed" }
    $title = "CryptoTrading $label $statusText"
    $lines = @(
        "## $title",
        "- mode: $Mode",
        "- time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        "- exit_code: $ExitCode",
        "- host: $env:COMPUTERNAME",
        "- project: $projectRoot"
    )
    if (-not [string]::IsNullOrWhiteSpace($ExtraLine)) {
        $lines += "- detail: $ExtraLine"
    }
    $body = @{
        msgtype = "markdown"
        markdown = @{
            content = ($lines -join "`n")
        }
    } | ConvertTo-Json -Depth 4

    try {
        Invoke-RestMethod -Uri $webhookUrl -Method Post -ContentType "application/json; charset=utf-8" -Body $body -TimeoutSec 15 | Out-Null
        Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] notification sent status=$Status"
    }
    catch {
        Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] notification failed: $($_.Exception.Message)"
    }
}

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
Set-Location $projectRoot
Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label start ==="

& $python @commandArgs 2>&1 | ForEach-Object {
    Write-LogLine $_.ToString()
}
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label failed exit_code=$exitCode ==="
    Send-TaskNotification "failed" $exitCode "See $logPath"
    exit $exitCode
}

foreach ($step in $successSteps) {
    Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] $step"
}
Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label complete ==="
Send-TaskNotification "success" 0 "See $logPath"
exit 0
