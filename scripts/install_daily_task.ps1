param(
    [string]$TaskName = "CryptoTrading_DailyPaperUpdate",
    [string]$At = "20:05"
)

$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$taskScriptPath = Join-Path $projectRoot "scripts\run_power_managed_paper_task.ps1"
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"
$preWakeTaskName = "${TaskName}_PreWake"

if (-not (Test-Path -LiteralPath $taskScriptPath)) {
    throw "Cannot find unified paper task script: $taskScriptPath"
}
if (-not (Test-Path -LiteralPath $pythonPath)) {
    throw "Cannot find project Python interpreter: $pythonPath. Create .venv and install the project dependencies first."
}

$scriptTime = [datetime]::ParseExact($At, "HH:mm", [Globalization.CultureInfo]::InvariantCulture)
$preWakeAt = $scriptTime.AddMinutes(-3).ToString("HH:mm")
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$preWakeTrigger = New-ScheduledTaskTrigger -Daily -At $preWakeAt
$action = New-ScheduledTaskAction `
    -Execute "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$taskScriptPath`" -Operation run -Mode daily -SleepAfterSuccessSeconds 180 -MinimumIdleSeconds 120" `
    -WorkingDirectory $projectRoot
$preWakeAction = New-ScheduledTaskAction `
    -Execute "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$taskScriptPath`" -Operation prewake -DurationSeconds 240" `
    -WorkingDirectory $projectRoot
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
$preWakePrincipal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -WakeToRun `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
    -MultipleInstances IgnoreNew

$description = "Wake the PC and run the unified CryptoTrading paper task script with the project .venv in daily mode every day at $At."
$preWakeDescription = "Wake the PC three minutes before $TaskName and keep it awake until the main task starts."

Register-ScheduledTask `
    -TaskName $preWakeTaskName `
    -Action $preWakeAction `
    -Trigger $preWakeTrigger `
    -Principal $preWakePrincipal `
    -Settings (New-ScheduledTaskSettingsSet -WakeToRun -ExecutionTimeLimit (New-TimeSpan -Minutes 10) -MultipleInstances IgnoreNew) `
    -Description $preWakeDescription `
    -Force | Out-Null

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description $description `
    -Force | Out-Null

Write-Host "Scheduled task updated: $TaskName"
Write-Host "Pre-wake task updated: $preWakeTaskName at $preWakeAt"
Get-ScheduledTask -TaskName $TaskName |
Select-Object -ExpandProperty Triggers |
Select-Object Enabled, StartBoundary, DaysInterval

Get-ScheduledTaskInfo -TaskName $TaskName |
Select-Object LastRunTime, LastTaskResult, NextRunTime, NumberOfMissedRuns
