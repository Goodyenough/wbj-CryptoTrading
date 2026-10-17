param(
    [string]$DailyTaskName = "CryptoTrading_DailyPaperUpdate",
    [string]$FourHourTaskName = "CryptoTrading_4H_PaperUpdate"
)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$runnerPath = Join-Path $projectRoot "scripts\run_logged_paper_task.ps1"
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"
$failures = New-Object System.Collections.Generic.List[string]

function Test-ConfiguredTask([string]$TaskName, [string]$Mode, [int]$ExpectedTriggerCount) {
    $task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
    if ($null -eq $task) {
        $failures.Add("scheduled task is missing: $TaskName")
        return
    }
    if ($task.State -eq "Disabled") {
        $failures.Add("scheduled task is disabled: $TaskName")
    }

    $matchingAction = @($task.Actions | Where-Object {
        $_.Execute -match "(?i)powershell(\.exe)?$" -and
        $_.Arguments -like "*$runnerPath*" -and
        $_.Arguments -match "(?i)-Mode\s+$([regex]::Escape($Mode))(\s|$)"
    })
    if ($matchingAction.Count -ne 1) {
        $failures.Add("scheduled task action is invalid: $TaskName mode=$Mode")
    }

    $enabledTriggers = @($task.Triggers | Where-Object { $_.Enabled })
    if ($enabledTriggers.Count -ne $ExpectedTriggerCount) {
        $failures.Add(
            "scheduled task trigger count is invalid: $TaskName expected=$ExpectedTriggerCount actual=$($enabledTriggers.Count)"
        )
    }

    $info = Get-ScheduledTaskInfo -TaskName $TaskName
    Write-Host (
        "PASS task=$TaskName state=$($task.State) next_run=$($info.NextRunTime.ToString('s')) " +
        "last_result=$($info.LastTaskResult)"
    )
}

if (-not (Test-Path -LiteralPath $runnerPath)) {
    $failures.Add("paper task runner is missing: $runnerPath")
}
if (-not (Test-Path -LiteralPath $pythonPath)) {
    $failures.Add("project Python is missing: $pythonPath")
} else {
    $version = & $pythonPath --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("project Python cannot start: $pythonPath")
    } else {
        Write-Host "PASS python=$pythonPath version=$version"
    }
}

$webhookNames = @(
    "CRYPTO_TRADING_WECOM_WEBHOOK_URL",
    "WECHAT_WORK_WEBHOOK_URL",
    "WECOM_WEBHOOK_URL",
    "QYWX_WEBHOOK_URL"
)
$configuredWebhook = $null
foreach ($scope in @("Process", "User", "Machine")) {
    foreach ($name in $webhookNames) {
        $value = [Environment]::GetEnvironmentVariable($name, $scope)
        if (-not [string]::IsNullOrWhiteSpace($value)) {
            $configuredWebhook = "$scope/$name"
            break
        }
    }
    if ($null -ne $configuredWebhook) {
        break
    }
}
if ($null -eq $configuredWebhook) {
    $failures.Add("WeCom webhook environment variable is missing")
} else {
    Write-Host "PASS wecom_webhook=$configuredWebhook"
}

Test-ConfiguredTask $DailyTaskName "daily" 1
Test-ConfiguredTask $FourHourTaskName "paper_4h" 5

if ($failures.Count -gt 0) {
    foreach ($failure in $failures) {
        [Console]::Error.WriteLine("FAIL $failure")
    }
    exit 1
}

Write-Host "PASS paper task setup is healthy"
exit 0
