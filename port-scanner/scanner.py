import socket
from datetime import datetime
import os

report_folder = "reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Ask user for target
target = input("Enter IP or domain to scan: ")
ports_to_scan = [22, 80, 443, 3306, 8080]  # Common ports

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"{report_folder}/scan_report_{timestamp}.txt"

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    try:
        s.connect((target, port))
        return True
    except:
        return False
    finally:
        s.close()

with open(report_file, "w") as r:
        r.write(f"=== PORT SCAN REPORT ===\n")
        r.write(f"Target: {target}\n")
        r.write(f"Date: {datetime.now()}\n\n")

        for port in ports_to_scan:
            status = "OPEN" if scan_port(port) else "CLOSED"
            line = f"Port {port}: {status}\n"
            print(line.strip())
            r.write(line)

print(f"\nScan complete! Report saved → {report_file}")
