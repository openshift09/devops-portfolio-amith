# System Info Gatherer Script

$reportFolder = "reports"
if (!(Test-Path -Path $reportFolder)) {
    New-Item -ItemType Directory -Path $reportFolder | Out-Null
}

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportFile = "$reportFolder\system_info_$timestamp.txt"

# Collect system information
$hostname      = hostname
$osversion     = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion").ProductName
$osbuild       = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion").CurrentBuild
$cpu           = (Get-WmiObject Win32_Processor).Name
$ram           = [Math]::Round((Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)
$user          = $env:USERNAME
$ip            = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -notlike "169.*"}).IPAddress

# Write report
Add-Content $reportFile "===== SYSTEM INFORMATION REPORT ====="
Add-Content $reportFile "Generated: $(Get-Date)"
Add-Content $reportFile ""
Add-Content $reportFile "Hostname:          $hostname"
Add-Content $reportFile "Logged-in User:    $user"
Add-Content $reportFile "Operating System:  $osversion"
Add-Content $reportFile "OS Build Number:   $osbuild"
Add-Content $reportFile "CPU Model:         $cpu"
Add-Content $reportFile "Total RAM:         $ram GB"
Add-Content $reportFile "IP Address:        $ip"

Write-Host "System information gathered → $reportFile"
