import psutil
import os
from datetime import datetime

report_folder = "reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"{report_folder}/process_report_{timestamp}.txt"

target_process = "chrome.exe"   # you can change this

with open(report_file, "w") as r:
    r.write("===== PROCESS MONITOR REPORT =====\n")
    r.write(f"Generated: {datetime.now()}\n\n")

    chrome_found = False

    for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = proc.info
            r.write(f"PID: {info['pid']}\n")
            r.write(f"Name: {info['name']}\n")
            r.write(f"CPU: {info['cpu_percent']}%\n")
            r.write(f"Memory: {round(info['memory_percent'], 2)}%\n")
            r.write("-" * 30 + "\n")

            if info["name"] and info["name"].lower() == target_process.lower():
                chrome_found = True

        except psutil.NoSuchProcess:
            continue

    if chrome_found:
        r.write(f"\nPROCESS CHECK: {target_process} is RUNNING ✔️\n")
    else:
        r.write(f"\nPROCESS CHECK: {target_process} is NOT running ❌\n")

print(f"Process monitoring complete! Report saved → {report_file}")
