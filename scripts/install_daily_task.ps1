param(
    [string]$TaskName = "CryptoTrading_DailyPaperUpdate",
    [string]$At = "20:05"
)

$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$batchPath = Join-Path $projectRoot "scripts\daily_paper_update.bat"

if (-not (Test-Path -LiteralPath $batchPath)) {
    throw "Cannot find daily batch script: $batchPath"
}

$currentIdentity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principalCheck = New-Object Security.Principal.WindowsPrincipal($currentIdentity)
$isAdmin = $principalCheck.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    throw "Please run this script from an elevated PowerShell session so the existing scheduled task can be replaced."
}

$trigger = New-ScheduledTaskTrigger -Daily -At $At
$action = New-ScheduledTaskAction -Execute $batchPath -WorkingDirectory $projectRoot
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel LeastPrivilege
$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
    -AllowStartIfOnBatteries:$false `
    -DisallowStartIfOnBatteries

$description = "Run CryptoTrading daily scan, paper update, and paper report every day at $At."

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
