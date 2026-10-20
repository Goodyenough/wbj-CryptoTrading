param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("prewake", "run", "sleep")]
    [string]$Operation,

    [ValidateSet("daily", "paper_4h")]
    [string]$Mode,

    [ValidateRange(1, 3600)]
    [int]$DurationSeconds = 240,

    [ValidateRange(0, 3600)]
    [int]$SleepAfterSuccessSeconds = 180,

    [ValidateRange(0, 3600)]
    [int]$MinimumIdleSeconds = 120,

    [string]$TaskRunnerPath,

    [switch]$SkipSuspend
)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$powerShellPath = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$powerLogPath = Join-Path $projectRoot "logs\paper_task_power.log"
$thisScriptPath = $MyInvocation.MyCommand.Path

if ([string]::IsNullOrWhiteSpace($TaskRunnerPath)) {
    $TaskRunnerPath = Join-Path $projectRoot "scripts\run_logged_paper_task.ps1"
}

New-Item -ItemType Directory -Force -Path (Split-Path $powerLogPath -Parent) | Out-Null

function Write-PowerLog([string]$Message) {
    Add-Content -LiteralPath $powerLogPath -Value "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] $Message" -Encoding UTF8
}

if (-not ("CryptoTrading.NativePower" -as [type])) {
    Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

namespace CryptoTrading
{
    public static class NativePower
    {
        [StructLayout(LayoutKind.Sequential)]
        public struct LASTINPUTINFO
        {
            public uint cbSize;
            public uint dwTime;
        }

        [DllImport("kernel32.dll", SetLastError = true)]
        public static extern uint SetThreadExecutionState(uint esFlags);

        [DllImport("kernel32.dll")]
        public static extern ulong GetTickCount64();

        [DllImport("user32.dll")]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool GetLastInputInfo(ref LASTINPUTINFO info);

        [DllImport("PowrProf.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        public static extern bool SetSuspendState(bool hibernate, bool forceCritical, bool disableWakeEvent);
    }
}
"@
}

function Set-SystemAwake {
    $result = [CryptoTrading.NativePower]::SetThreadExecutionState([uint32]2147483649)
    if ($result -eq 0) {
        throw "SetThreadExecutionState failed error=$([Runtime.InteropServices.Marshal]::GetLastWin32Error())"
    }
}

function Clear-SystemAwake {
    [void][CryptoTrading.NativePower]::SetThreadExecutionState([uint32]2147483648)
}

function Get-IdleSeconds {
    $info = New-Object CryptoTrading.NativePower+LASTINPUTINFO
    $info.cbSize = [Runtime.InteropServices.Marshal]::SizeOf($info)
    if (-not [CryptoTrading.NativePower]::GetLastInputInfo([ref]$info)) {
        throw "GetLastInputInfo failed error=$([Runtime.InteropServices.Marshal]::GetLastWin32Error())"
    }
    $tick32 = [CryptoTrading.NativePower]::GetTickCount64() % 4294967296
    if ($tick32 -ge $info.dwTime) {
        return [math]::Floor(($tick32 - $info.dwTime) / 1000)
    }
    return [math]::Floor((4294967296 + $tick32 - $info.dwTime) / 1000)
}

if ($Operation -eq "prewake") {
    Set-SystemAwake
    try {
        Write-PowerLog "prewake hold started duration_seconds=$DurationSeconds"
        Start-Sleep -Seconds $DurationSeconds
        Write-PowerLog "prewake hold completed"
    }
    finally {
        Clear-SystemAwake
    }
    exit 0
}

if ($Operation -eq "sleep") {
    Write-PowerLog "post-success sleep timer started delay_seconds=$SleepAfterSuccessSeconds"
    if ($SleepAfterSuccessSeconds -gt 0) {
        Start-Sleep -Seconds $SleepAfterSuccessSeconds
    }
    $idleSeconds = Get-IdleSeconds
    if ($idleSeconds -lt $MinimumIdleSeconds) {
        Write-PowerLog "post-success sleep skipped user_active idle_seconds=$idleSeconds minimum_idle_seconds=$MinimumIdleSeconds"
        exit 0
    }
    if ($SkipSuspend) {
        Write-PowerLog "post-success sleep skipped test_mode idle_seconds=$idleSeconds"
        exit 0
    }
    Write-PowerLog "post-success sleep requested idle_seconds=$idleSeconds"
    $suspended = [CryptoTrading.NativePower]::SetSuspendState($false, $false, $false)
    if (-not $suspended) {
        Write-PowerLog "post-success sleep failed error=$([Runtime.InteropServices.Marshal]::GetLastWin32Error())"
        exit 1
    }
    exit 0
}

if ([string]::IsNullOrWhiteSpace($Mode)) {
    throw "Mode is required for the run operation."
}
if (-not (Test-Path -LiteralPath $TaskRunnerPath)) {
    throw "Paper task runner not found: $TaskRunnerPath"
}

$taskExitCode = 1
Set-SystemAwake
try {
    Write-PowerLog "paper task started mode=$Mode runner=$TaskRunnerPath"
    & $powerShellPath -NoProfile -ExecutionPolicy Bypass -File $TaskRunnerPath -Mode $Mode
    $taskExitCode = $LASTEXITCODE
    Write-PowerLog "paper task completed mode=$Mode exit_code=$taskExitCode"
}
catch {
    Write-PowerLog "paper task failed mode=$Mode exception=$($_.Exception.Message)"
    $taskExitCode = 1
}
finally {
    Clear-SystemAwake
}

if ($taskExitCode -eq 0) {
    $sleepArguments = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", "`"$thisScriptPath`"",
        "-Operation", "sleep",
        "-SleepAfterSuccessSeconds", $SleepAfterSuccessSeconds,
        "-MinimumIdleSeconds", $MinimumIdleSeconds
    )
    if ($SkipSuspend) {
        $sleepArguments += "-SkipSuspend"
    }
    try {
        Start-Process -FilePath $powerShellPath -ArgumentList $sleepArguments -WindowStyle Hidden | Out-Null
        Write-PowerLog "post-success sleep scheduled mode=$Mode delay_seconds=$SleepAfterSuccessSeconds minimum_idle_seconds=$MinimumIdleSeconds"
    }
    catch {
        Write-PowerLog "post-success sleep scheduling failed mode=$Mode exception=$($_.Exception.Message)"
    }
}

exit $taskExitCode
