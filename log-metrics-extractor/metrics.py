import os
from datetime import datetime

log_folder = "logs"
report_folder = "reports"

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Find first .log file
files = [f for f in os.listdir(log_folder) if f.endswith(".log")]
if not files:
    print("No .log files found!")
    exit()

log_file = os.path.join(log_folder, files[0])
report_file = f"{report_folder}/metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Metrics counters
errors = 0
warnings = 0
infos = 0
total = 0

with open(log_file, "r") as f:
    for line in f:
        total += 1
        lower = line.lower()

        if "error" in lower:
            errors += 1
        elif "warning" in lower:
            warnings += 1
        elif "info" in lower:
            infos += 1

# Write metrics report
with open(report_file, "w") as r:
    r.write("===== LOG METRICS REPORT =====\n")
    r.write(f"File: {log_file}\n")
    r.write(f"Generated: {datetime.now()}\n\n")
    r.write(f"Total Lines: {total}\n")
    r.write(f"INFO Count: {infos}\n")
    r.write(f"WARNING Count: {warnings}\n")
    r.write(f"ERROR Count: {errors}\n")

print("Metrics extracted successfully!")
print(f"Report saved → {report_file}")
