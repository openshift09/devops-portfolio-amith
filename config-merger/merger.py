import yaml
import json
import os
from datetime import datetime

config_folder = "configs"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read YAML file
yaml_files = [f for f in os.listdir(config_folder) if f.endswith(".yaml") or f.endswith(".yml")]
json_files = [f for f in os.listdir(config_folder) if f.endswith(".json")]

if not yaml_files or not json_files:
    print("Please add both YAML and JSON files to configs/")
    exit()

yaml_file = os.path.join(config_folder, yaml_files[0])
json_file = os.path.join(config_folder, json_files[0])

with open(yaml_file, "r") as yf:
    base_config = yaml.safe_load(yf)

with open(json_file, "r") as jf:
    override_config = json.load(jf)

# Recursive merge
def merge(a, b):
    for key, value in b.items():
        if key in a and isinstance(a[key], dict) and isinstance(value, dict):
            merge(a[key], value)
        else:
            a[key] = value
    return a

merged = merge(base_config, override_config)

# Output file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"{output_folder}/merged_{timestamp}.json"

with open(output_file, "w") as out:
    json.dump(merged, out, indent=4)

print("Config merged successfully!")
print(f"Output → {output_file}")
