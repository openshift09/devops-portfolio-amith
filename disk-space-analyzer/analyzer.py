import shutil
import os
from datetime import datetime

# Drives to check
drives = ["C:\\", "D:\\", "E:\\"]

report_folder = "reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"{report_folder}/disk_report_{timestamp}.txt"

LOW_SPACE_THRESHOLD = 20  # percent

def analyze_drive(drive):
    try:
        total, used, free = shutil.disk_usage(drive)

        total_gb = round(total / (1024 ** 3), 2)
        used_gb = round(used / (1024 ** 3), 2)
        free_gb = round(free / (1024 ** 3), 2)
        percent_used = round((used / total) * 100, 2)

        return {
            "drive": drive,
            "total_gb": total_gb,
            "used_gb": used_gb,
            "free_gb": free_gb,
            "percent_used": percent_used
        }
    except:
        return None

with open(report_file, "w") as r:
    r.write("===== DISK SPACE ANALYZER REPORT =====\n")
    r.write(f"Generated: {datetime.now()}\n\n")

    for drive in drives:
        info = analyze_drive(drive)
        if info:
            r.write(f"Drive: {info['drive']}\n")
            r.write(f"Total Space: {info['total_gb']} GB\n")
            r.write(f"Used Space: {info['used_gb']} GB\n")
            r.write(f"Free Space: {info['free_gb']} GB\n")
            r.write(f"Used (%): {info['percent_used']}%\n")

            if info['free_gb'] < LOW_SPACE_THRESHOLD:
                r.write("⚠️  WARNING: LOW DISK SPACE!\n")

            r.write("\n")
        else:
            r.write(f"Drive {drive} not available.\n\n")

print(f"Disk analysis complete! Report saved → {report_file}")
