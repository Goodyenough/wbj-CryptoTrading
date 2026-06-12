param(
    [string]$TaskName = "CryptoTrading_4H_PaperUpdate",
    [int]$RequiredStableDays = 5
)

$ErrorActionPreference = "Stop"

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$batchPath = Join-Path $projectRoot "scripts\paper_4h_update.bat"
$pythonPath = "C:\Users\10537\miniconda3\envs\ppt-master\python.exe"

if (-not (Test-Path -LiteralPath $batchPath)) {
    throw "Cannot find 4h paper update batch script: $batchPath"
}

if (-not (Test-Path -LiteralPath $pythonPath)) {
    throw "Cannot find configured Python interpreter: $pythonPath"
}

$currentIdentity = [Security.Principal.WindowsIdentity]::GetCurrent()
$principalCheck = New-Object Security.Principal.WindowsPrincipal($currentIdentity)
$isAdmin = $principalCheck.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    throw "Please run this script from an elevated PowerShell session."
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
    -Execute "$env:SystemRoot\System32\cmd.exe" `
    -Argument "/d /c `"`"$batchPath`"`"" `
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
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
    -MultipleInstances IgnoreNew

$description = "Update existing CryptoTrading paper plans at closed 4h candle intervals; never scans or creates plans."

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
