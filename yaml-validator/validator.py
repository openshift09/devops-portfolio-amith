import os
import yaml
import json
from datetime import datetime

input_folder = "input"
report_folder = "reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Pick first YAML file from input/
files = [f for f in os.listdir(input_folder) if f.endswith((".yaml", ".yml"))]

if not files:
    print("No YAML files found in input/")
    exit()

yaml_file = os.path.join(input_folder, files[0])
report_file = f"{report_folder}/validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

try:
    # Read YAML
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)

    # Save JSON version for debugging
    json_file = yaml_file.replace("input", "reports").replace(".yaml", ".json").replace(".yml", ".json")
    with open(json_file, "w") as jf:
        json.dump(data, jf, indent=4)

    with open(report_file, "w") as r:
        r.write("==== YAML VALIDATION REPORT ====\n")
        r.write(f"File: {yaml_file}\n")
        r.write(f"Status: VALID\n")
        r.write(f"Generated: {datetime.now()}\n")

    print("YAML is VALID!")
    print(f"Report → {report_file}")
    print(f"JSON Output → {json_file}")

except yaml.YAMLError as e:
    with open(report_file, "w") as r:
        r.write("==== YAML VALIDATION REPORT ====\n")
        r.write(f"File: {yaml_file}\n")
        r.write("Status: INVALID\n")
        r.write(f"Error: {str(e)}\n")
        r.write(f"Generated: {datetime.now()}\n")

    print("YAML is INVALID ❌")
    print("Error details saved in report:")
    print(f"Report → {report_file}")
