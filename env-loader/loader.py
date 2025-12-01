import os
import json
from datetime import datetime

env_folder = "env"
report_folder = "reports"

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Pick first env file
files = [f for f in os.listdir(env_folder) if f.endswith(".env")]
if not files:
    print("No .env files found!")
    exit()

env_file = os.path.join(env_folder, files[0])
report_file = f"{report_folder}/env_loaded_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

env_vars = {}

# Load .env file
with open(env_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            env_vars[key] = value
            os.environ[key] = value  # Load into system environment

# Save to JSON report
with open(report_file, "w") as out:
    json.dump(env_vars, out, indent=4)

print("Environment variables loaded successfully!")
print(f"Loaded {len(env_vars)} variables.")
print(f"Saved report → {report_file}")

# Display loaded variables
print("\nLoaded Variables:")
for k, v in env_vars.items():
    print(f"{k}={v}")
