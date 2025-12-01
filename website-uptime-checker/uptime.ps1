# Website Uptime Checker Script

$website = "https://www.google.com"   # <--- Change to any website you want to monitor
$logFile = "logs\uptime.log"
$intervalSeconds = 15                 # check every 15 seconds

# Create logs folder if missing
if (!(Test-Path -Path "logs")) {
    New-Item -ItemType Directory -Path "logs" | Out-Null
}

Add-Content -Path $logFile -Value "=== Uptime Check Started at $(Get-Date) ==="

while ($true) {
    try {
        $start = Get-Date
        $response = Invoke-WebRequest -Uri $website -TimeoutSec 5
        $end = Get-Date

        $responseTime = ($end - $start).TotalMilliseconds

        Add-Content -Path $logFile -Value "UP: $website responded in ${responseTime}ms at $(Get-Date)"
    }
    catch {
        Add-Content -Path $logFile -Value "DOWN: $website is unreachable at $(Get-Date)"
    }

    Start-Sleep -Seconds $intervalSeconds
}
