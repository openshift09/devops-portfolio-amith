# Simple Ping Monitoring Tool

$hostToPing = "8.8.8.8"        # <-- Change to any IP or domain
$logFile = "logs\ping.log"
$intervalSeconds = 10          # Ping every 10 seconds

# Create logs folder if missing
if (!(Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

Add-Content -Path $logFile -Value "=== Ping Monitoring Started at $(Get-Date) ==="

while ($true) {
    $ping = Test-Connection -ComputerName $hostToPing -Count 1 -ErrorAction SilentlyContinue

    if ($ping) {
        $time = $ping.ResponseTime
        Add-Content -Path $logFile -Value "UP: $hostToPing responded in ${time}ms at $(Get-Date)"
    }
    else {
        Add-Content -Path $logFile -Value "DOWN: $hostToPing unreachable at $(Get-Date)"
    }

    Start-Sleep -Seconds $intervalSeconds
}
