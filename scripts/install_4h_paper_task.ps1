param(
    [string]$TaskName = "CryptoTrading_4H_PaperUpdate",
    [int]$RequiredStableDays = 5
)

$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$taskScriptPath = Join-Path $projectRoot "scripts\run_logged_paper_task.ps1"
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $taskScriptPath)) {
    throw "Cannot find unified paper task script: $taskScriptPath"
}

if (-not (Test-Path -LiteralPath $pythonPath)) {
    throw "Cannot find project Python interpreter: $pythonPath. Create .venv and install the project dependencies first."
}

Push-Location $projectRoot
try {
    & $pythonPath main.py db stability --days $RequiredStableDays
    if ($LASTEXITCODE -ne 0) {
        throw "SQLite daily_full stability gate has not passed. The 4h task was not installed."
    }
}
finally {
    Pop-Location
}

$action = New-ScheduledTaskAction `
    -Execute "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$taskScriptPath`" -Mode paper_4h" `
    -WorkingDirectory $projectRoot
$triggers = @(
    New-ScheduledTaskTrigger -Daily -At "00:10"
    New-ScheduledTaskTrigger -Daily -At "04:10"
    New-ScheduledTaskTrigger -Daily -At "08:10"
    New-ScheduledTaskTrigger -Daily -At "12:10"
    New-ScheduledTaskTrigger -Daily -At "16:10"
)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -WakeToRun `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
    -MultipleInstances IgnoreNew

$description = "Wake the PC and run the unified CryptoTrading paper task script with the project .venv in paper_4h mode at closed 4h candle intervals; never scans or creates plans."

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $triggers `
    -Principal $principal `
    -Settings $settings `
    -Description $description `
    -Force | Out-Null

Write-Host "Scheduled task installed: $TaskName"
Get-ScheduledTask -TaskName $TaskName |
    Select-Object -ExpandProperty Triggers |
    Select-Object Enabled, StartBoundary, DaysInterval

Get-ScheduledTaskInfo -TaskName $TaskName |
    Select-Object LastRunTime, LastTaskResult, NextRunTime, NumberOfMissedRuns
