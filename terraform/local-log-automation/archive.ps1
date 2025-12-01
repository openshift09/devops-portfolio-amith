# Archive Script: Compress logs into a backup file with timestamp

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$source = "logs"
$destination = "backups"
$zipFile = "$destination\backup_$timestamp.zip"

# Create backup folder if missing
if (!(Test-Path -Path $destination)) {
    New-Item -ItemType Directory -Path $destination | Out-Null
}

# Compress logs
Compress-Archive -Path "$source\*" -DestinationPath $zipFile -Force

# Remove logs older than 7 days
$limit = (Get-Date).AddDays(-7)
Get-ChildItem $destination -Filter *.zip | Where-Object { $_.LastWriteTime -lt $limit } | Remove-Item

Write-Host "Backup created: $zipFile"
