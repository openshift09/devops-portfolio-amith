# Folder Cleanup Script

$targetFolder = "C:\Users\Amit\Desktop\tmp"      # <--- Change this to any folder you want to clean
$logFile = "logs\cleanup.log"
$retentionDays = 7

# Create logs folder if missing
if (!(Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

# Write log start
Add-Content -Path $logFile -Value "=== Cleanup Started at $(Get-Date) ==="

# Cleanup files older than X days
$limit = (Get-Date).AddDays(-$retentionDays)

Get-ChildItem -Path $targetFolder -File | Where-Object {
    $_.LastWriteTime -lt $limit
} | ForEach-Object {
    Add-Content -Path $logFile -Value "Deleting: $($_.FullName)"
    Remove-Item $_.FullName -Force
}

# Cleanup empty folders
Get-ChildItem -Path $targetFolder -Directory | Where-Object {
    (Get-ChildItem -Path $_.FullName).Count -eq 0
} | ForEach-Object {
    Add-Content -Path $logFile -Value "Removing empty folder: $($_.FullName)"
    Remove-Item $_.FullName -Force
}

Add-Content -Path $logFile -Value "=== Cleanup Completed at $(Get-Date) ==="
Write-Host "Cleanup complete."
