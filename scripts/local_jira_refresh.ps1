# local_jira_refresh.ps1 — Daily JIRA cache refresh + git push
# Schedule via Windows Task Scheduler to run daily.
#
# Prerequisites:
#   - .env file with JIRA_PAT and JIRA_BASE_URL
#   - Git configured with SSH or credential manager
#   - Python 3.x with requests, python-dotenv, urllib3 installed
#
# Task Scheduler setup:
#   Action: powershell.exe -ExecutionPolicy Bypass -File "C:\Users\sajivfra\Documents\IAO-JPNotebookPython\scripts\local_jira_refresh.ps1"
#   Trigger: Daily at 06:00 (or preferred time)
#   Conditions: Start only if network connection available

$ErrorActionPreference = "Stop"
$workspace = Split-Path -Parent $PSScriptRoot  # go up from scripts/ to repo root
Set-Location $workspace

$logFile = Join-Path $workspace "data\jira\refresh.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

function Log($msg) {
    $entry = "[$timestamp] $msg"
    Write-Host $entry
    Add-Content -Path $logFile -Value $entry
}

Log "Starting JIRA data refresh..."

# Fetch latest from remote
try {
    git pull --rebase origin main 2>&1 | Out-Null
    Log "Git pull complete"
} catch {
    Log "WARNING: git pull failed — continuing with local state"
}

# Run the JIRA fetch script
try {
    $output = python scripts/fetch_jira_data.py 2>&1
    Log "JIRA fetch complete: $($output | Select-Object -Last 3 | Out-String)"
} catch {
    Log "ERROR: JIRA fetch failed — $($_.Exception.Message)"
    exit 1
}

# Check if jira_cache.json changed
$status = git status --porcelain "data/jira/jira_cache.json"
if (-not $status) {
    Log "No changes in JIRA cache — skipping commit"
    exit 0
}

# Commit and push
try {
    git add "data/jira/jira_cache.json"
    git commit -m "data: JIRA cache refresh $timestamp"
    git push origin main
    Log "Committed and pushed JIRA cache update"
} catch {
    Log "ERROR: git push failed — $($_.Exception.Message)"
    exit 1
}

Log "JIRA refresh complete"
