import configparser
import json
import os
from datetime import datetime

config_folder = "config"
report_folder = "reports"

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Get INI file
files = [f for f in os.listdir(config_folder) if f.endswith(".ini")]
if not files:
    print("No INI files found!")
    exit()

ini_path = os.path.join(config_folder, files[0])
report_file = f"{report_folder}/parsed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Parse INI
config = configparser.ConfigParser()
config.read(ini_path)

parsed_data = {}

for section in config.sections():
    parsed_data[section] = dict(config.items(section))

# Save JSON output
with open(report_file, "w") as out:
    json.dump(parsed_data, out, indent=4)

print("\nINI file parsed successfully!")
print(f"Input:  {ini_path}")
print(f"Output: {report_file}")
