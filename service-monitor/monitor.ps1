# Windows Service Monitor Script
# Monitors a service and restarts it if it stops

$serviceName = "Spooler"   # <--- change to any service name (Print Spooler, W32Time, etc.)
$logFile = "logs\service_monitor.log"

# Create logs folder if missing
if (!(Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

Add-Content -Path $logFile -Value "=== Monitoring Started at $(Get-Date) ==="

while ($true) {
    $service = Get-Service -Name $serviceName

    if ($service.Status -ne "Running") {
        Add-Content -Path $logFile -Value "$serviceName stopped at $(Get-Date). Attempting restart..."
        Restart-Service -Name $serviceName
        Add-Content -Path $logFile -Value "$serviceName restarted at $(Get-Date)"
    }

    Start-Sleep -Seconds 5
}
