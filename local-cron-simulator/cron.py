import time
import os
from datetime import datetime

task_folder = "tasks"
log_folder = "logs"

# Create logs folder if missing
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_file = f"{log_folder}/cron_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Choose task
files = [f for f in os.listdir(task_folder) if f.endswith(".txt")]
if not files:
    print("No task file found in tasks/ folder.")
    exit()

task_file = os.path.join(task_folder, files[0])

interval = 10  # Run every 10 seconds

print(f"Running cron simulation every {interval} seconds...")
print(f"Task file: {task_file}")

while True:
    timestamp = datetime.now()
    
    with open(task_file, "r") as t:
        task_output = t.read().strip()

    with open(log_file, "a") as log:
        log.write(f"[{timestamp}] Task executed.\n")
        log.write(f"Output: {task_output}\n\n")

    print(f"[{timestamp}] Task executed.")
    time.sleep(interval)
