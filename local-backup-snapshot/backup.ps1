# Local Backup Snapshot Script

$sourceFolder = "source"
$snapshotFolder = "snapshots"

# Create snapshot folder if missing
if (!(Test-Path -Path $snapshotFolder)) {
    New-Item -ItemType Directory -Path $snapshotFolder | Out-Null
}

# Create timestamped ZIP filename
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$zipFile = "$snapshotFolder\backup_$timestamp.zip"

# Create snapshot
Compress-Archive -Path "$sourceFolder\*" -DestinationPath $zipFile -Force

Write-Host "Backup snapshot created: $zipFile"

# Delete snapshots older than 7 days
$limit = (Get-Date).AddDays(-7)

Get-ChildItem $snapshotFolder | Where-Object {
    $_.LastWriteTime -lt $limit
} | Remove-Item

