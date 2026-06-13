param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("daily", "paper_4h")]
    [string]$Mode
)

$ErrorActionPreference = "Stop"
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

$env:PYTHONUTF8 = "1"
Set-Location $projectRoot
Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label start ==="

& $python @commandArgs 2>&1 | ForEach-Object {
    Write-LogLine $_.ToString()
}
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label failed exit_code=$exitCode ==="
    exit $exitCode
}

foreach ($step in $successSteps) {
    Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] $step"
}
Write-LogLine "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')] === $label complete ==="
exit 0
