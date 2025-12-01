import os
import time
from datetime import datetime, timedelta

target_folder = "target"
log_folder = "logs"

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file = f"{log_folder}/cleanup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

days_old = 3  # delete files older than 3 days
limit = datetime.now() - timedelta(days=days_old)

with open(log_file, "w") as log:
    log.write("===== DISK CLEANUP REPORT =====\n")
    log.write(f"Deleting files older than {days_old} days\n\n")

    for f in os.listdir(target_folder):
        path = os.path.join(target_folder, f)
        if os.path.isfile(path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(path))
            if modified_time < limit:
                os.remove(path)
                log.write(f"Deleted: {path}\n")

print("Disk cleanup complete!")
print(f"Report saved → {log_file}")
