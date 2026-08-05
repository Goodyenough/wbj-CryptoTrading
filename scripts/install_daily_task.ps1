param(
    [string]$TaskName = "CryptoTrading_DailyPaperUpdate",
    [string]$At = "20:05"
)

$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$taskScriptPath = Join-Path $projectRoot "scripts\run_logged_paper_task.ps1"

if (-not (Test-Path -LiteralPath $taskScriptPath)) {
    throw "Cannot find unified paper task script: $taskScriptPath"
}

$currentIdentity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principalCheck = New-Object Security.Principal.WindowsPrincipal($currentIdentity)
$isAdmin = $principalCheck.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    throw "Please run this script from an elevated PowerShell session so the existing scheduled task can be replaced."
}

$trigger = New-ScheduledTaskTrigger -Daily -At $At
$action = New-ScheduledTaskAction `
    -Execute "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$taskScriptPath`" -Mode daily" `
    -WorkingDirectory $projectRoot
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -WakeToRun `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
    -MultipleInstances IgnoreNew

$description = "Wake the PC and run the unified CryptoTrading paper task script in daily mode every day at $At."

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description $description `
    -Force | Out-Null

Write-Host "Scheduled task updated: $TaskName"
Get-ScheduledTask -TaskName $TaskName |
Select-Object -ExpandProperty Triggers |
Select-Object Enabled, StartBoundary, DaysInterval

Get-ScheduledTaskInfo -TaskName $TaskName |
Select-Object LastRunTime, LastTaskResult, NextRunTime, NumberOfMissedRuns
