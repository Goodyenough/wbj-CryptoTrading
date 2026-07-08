param(
    [string]$Account = "demo",
    [string]$StartDate = "2026-07-03",
    [string]$EndDate = "2026-07-16",
    [string]$PythonPath = "python",
    [switch]$NoObsidian,
    [switch]$CheckpointOnly
)

$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom

$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

function Invoke-PythonStep {
    param(
        [string]$Label,
        [string[]]$Arguments,
        [int[]]$AllowedExitCodes = @(0)
    )

    Write-Host ""
    Write-Host "==> $Label"
    Push-Location $projectRoot
    try {
        & $PythonPath @Arguments
        $script:LastStepExitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }
    if ($AllowedExitCodes -notcontains $script:LastStepExitCode) {
        throw "$Label failed with exit code $script:LastStepExitCode"
    }
}

Write-Host "Project: $projectRoot"
Write-Host "Window: $StartDate -> $EndDate"
Write-Host "Account: $Account"

$settingsDiff = & git -C $projectRoot diff -- config/settings.toml
if ($LASTEXITCODE -ne 0) {
    throw "git diff -- config/settings.toml failed with exit code $LASTEXITCODE"
}
if (-not [string]::IsNullOrWhiteSpace(($settingsDiff -join "`n"))) {
    Write-Host "config/settings.toml has uncommitted differences:"
    $settingsDiff | ForEach-Object { Write-Host $_ }
    throw "Refusing to run checkpoint review while settings.toml differs."
}

$commonArgs = @("--account", $Account, "--start-date", $StartDate, "--end-date", $EndDate)
$obsidianArgs = @()
if ($NoObsidian) {
    $obsidianArgs += "--no-obsidian"
}

$checkpointArgs = @("main.py", "paper", "checkpoint") + $commonArgs + $obsidianArgs + @("--fail-on-not-ready")
Invoke-PythonStep -Label "paper checkpoint" -Arguments $checkpointArgs -AllowedExitCodes @(0, 2)
$checkpointExit = $script:LastStepExitCode
if ($checkpointExit -eq 2) {
    Write-Host ""
    Write-Host "Checkpoint verdict is not formal_audit_ready. Stop here; do not run formal audit or A/B."
    exit 2
}

if ($CheckpointOnly) {
    Write-Host ""
    Write-Host "Checkpoint passed. CheckpointOnly was set, so formal audit and shadow replay were not run."
    exit 0
}

$auditArgs = @("main.py", "paper", "audit") + $commonArgs + $obsidianArgs
Invoke-PythonStep -Label "paper audit" -Arguments $auditArgs | Out-Null

$entryReplayArgs = @("main.py", "paper", "shadow-replay") + $commonArgs + @("--variant", "entry_reclaim_confirm_1bar") + $obsidianArgs
Invoke-PythonStep -Label "shadow replay entry_reclaim_confirm_1bar" -Arguments $entryReplayArgs | Out-Null

$relativeReplayArgs = @("main.py", "paper", "shadow-replay") + $commonArgs + @("--variant", "relative_strength_gate") + $obsidianArgs
Invoke-PythonStep -Label "shadow replay relative_strength_gate" -Arguments $relativeReplayArgs | Out-Null

Write-Host ""
Write-Host "Paper checkpoint review completed. Review the generated reports before making any strategy decision."
