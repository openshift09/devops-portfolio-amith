# Log Rotation Script

$logFolder = "logs"
$archiveFolder = "archive"
$retentionDays = 7   # delete archives older than 7 days

# Create archive folder if missing
if (!(Test-Path -Path $archiveFolder)) {
    New-Item -ItemType Directory -Path $archiveFolder | Out-Null
}

# Get all log files
$logFiles = Get-ChildItem -Path $logFolder -Filter *.log

foreach ($file in $logFiles) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $zipName = "$archiveFolder\$($file.BaseName)_$timestamp.zip"

    # Compress log file
    Compress-Archive -Path $file.FullName -DestinationPath $zipName -Force

    # Clear original log content
    Clear-Content $file.FullName

    Write-Host "Rotated log: $($file.Name) → $zipName"
}

# Delete old archive files
$limit = (Get-Date).AddDays(-$retentionDays)
$oldArchives = Get-ChildItem -Path $archiveFolder | Where-Object {
    $_.LastWriteTime -lt $limit
}

foreach ($old in $oldArchives) {
    Remove-Item $old.FullName -Force
    Write-Host "Deleted old archive: $($old.Name)"
}

Write-Host "Log rotation complete."
