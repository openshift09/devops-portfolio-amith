import json
import os
from datetime import datetime

input_folder = "input"
output_folder = "output"
log_folder = "logs"

# Create missing folders
for folder in [output_folder, log_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

log_file = f"{log_folder}/formatter.log"

def log(msg):
    with open(log_file, "a") as f:
        f.write(msg + "\n")

# Get first JSON file from input/
files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

if not files:
    print("No JSON files found in input folder.")
    log("No JSON files found.")
    exit()

file_path = os.path.join(input_folder, files[0])
output_file = os.path.join(output_folder, "formatted_" + files[0])

try:
    with open(file_path, "r") as f:
        data = json.load(f)   # VALIDATES JSON automatically

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)   # Beautify JSON

    print(f"JSON formatted successfully → {output_file}")
    log(f"SUCCESS: {files[0]} formatted at {datetime.now()}")

except json.JSONDecodeError as e:
    print(f"JSON is invalid: {e}")
    log(f"ERROR: Invalid JSON in {files[0]} at {datetime.now()} - {e}")
