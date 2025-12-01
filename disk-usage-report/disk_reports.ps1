# Disk Usage Report Script

$reportFolder = "reports"

# Create folder if missing
if (!(Test-Path -Path $reportFolder)) {
    New-Item -ItemType Directory -Path $reportFolder | Out-Null
}

# Create timestamped report file
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportFile = "$reportFolder\disk_report_$timestamp.txt"

# Get all logical disks
$disks = Get-WmiObject win32_logicaldisk -Filter "DriveType=3"

# Write report header
Add-Content $reportFile "===== DISK USAGE REPORT ====="
Add-Content $reportFile "Generated: $(Get-Date)"
Add-Content $reportFile ""

# Loop through disks
foreach ($disk in $disks) {
    $total = [math]::Round($disk.Size / 1GB, 2)
    $free  = [math]::Round($disk.FreeSpace / 1GB, 2)
    $used  = [math]::Round($total - $free, 2)

    $percent = [math]::Round(($used / $total) * 100, 2)

    Add-Content $reportFile "Drive: $($disk.DeviceID)"
    Add-Content $reportFile "  Total Space: ${total}GB"
    Add-Content $reportFile "  Used Space:  ${used}GB"
    Add-Content $reportFile "  Free Space:  ${free}GB"
    Add-Content $reportFile "  Usage:       ${percent}%"
    Add-Content $reportFile ""
}

Write-Host "Disk usage report created: $reportFile"
