# Folder to watch
$watchPath = "watch"

# Log folder
$logFile = "logs\file_changes.log"

# Create log directory if missing
if (!(Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

# Create log file if missing
if (!(Test-Path -Path $logFile)) {
    New-Item -ItemType File -Path $logFile | Out-Null
}

Write-Host "Monitoring folder: $watchPath"
Add-Content -Path $logFile -Value "==== Monitoring Started at $(Get-Date) ===="

# Create FileSystemWatcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchPath
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

# Define Actions
$onCreated = Register-ObjectEvent $watcher Created -Action {
    Add-Content -Path "logs\file_changes.log" -Value "CREATED: $($Event.SourceEventArgs.FullPath) at $(Get-Date)"
}

$onChanged = Register-ObjectEvent $watcher Changed -Action {
    Add-Content -Path "logs\file_changes.log" -Value "MODIFIED: $($Event.SourceEventArgs.FullPath) at $(Get-Date)"
}

$onDeleted = Register-ObjectEvent $watcher Deleted -Action {
    Add-Content -Path "logs\file_changes.log" -Value "DELETED: $($Event.SourceEventArgs.FullPath) at $(Get-Date)"
}

# Run indefinitely
while ($true) {
    Start-Sleep -Seconds 1
}
