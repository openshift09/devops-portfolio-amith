# Create reports folder if not present
if (!(Test-Path -Path "reports")) {
    New-Item -ItemType Directory -Path "reports" | Out-Null
}

# Timestamp for report file
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportFile = "reports\health_report_$timestamp.txt"

# CPU Usage
$cpu = Get-Counter '\Processor(_Total)\% Processor Time'
$cpuUsage = [Math]::Round($cpu.CounterSamples.CookedValue, 2)

# Memory Usage
$mem = Get-WmiObject win32_operatingsystem
$totalMem = [Math]::Round($mem.TotalVisibleMemorySize / 1MB , 2)
$freeMem  = [Math]::Round($mem.FreePhysicalMemory / 1MB , 2)
$usedMem  = [Math]::Round($totalMem - $freeMem , 2)

# Disk Usage
$disk = Get-WmiObject win32_logicaldisk -Filter "DriveType=3"
$diskInfo = $disk | ForEach-Object {
    "Drive: $($_.DeviceID)  Total: $([Math]::Round($_.Size/1GB,2))GB  Free: $([Math]::Round($_.FreeSpace/1GB,2))GB"
}

# Network Info
$network = Get-NetIPAddress | Select-Object -ExpandProperty IPAddress

# Running Processes (Top 5 by CPU)
$processes = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5

# Write Report
@"
================= SYSTEM HEALTH REPORT =================
Generated: $(Get-Date)

CPU Usage: $cpuUsage %

Memory Usage:
  Total: $totalMem GB
  Used:  $usedMem GB
  Free:  $freeMem GB

Disk Usage:
$diskInfo

Network Addresses:
$($network -join ", ")

Top 5 CPU Processes:
$($processes | Format-Table -AutoSize | Out-String)

=======================================================
"@ | Out-File $reportFile

Write-Host "Health report generated: $reportFile"
