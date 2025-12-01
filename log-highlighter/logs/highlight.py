import os
from datetime import datetime

log_folder = "logs"
output_folder = "output"
output_file = f"{output_folder}/highlights_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Create output folder if missing
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get log file (first one in logs folder)
files = [f for f in os.listdir(log_folder) if f.endswith(".log")]
if not files:
    print("No log files found.")
    exit()
log_file = os.path.join(log_folder, files[0])

# Read and filter logs
keywords = ["error", "warning", "critical"]

with open(log_file, "r") as f:
    lines = f.readlines()

highlights = [line for line in lines if any(k in line.lower() for k in keywords)]

# Write results
with open(output_file, "w") as out:
    out.write("=== LOG HIGHLIGHTS ===\n")
    out.write(f"Generated at: {datetime.now()}\n\n")
    for h in highlights:
        out.write(h)

print(f"Highlights extracted → {output_file}")
