import yaml
import json
import os

input_folder = "input"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = [f for f in os.listdir(input_folder) if f.endswith(".yaml") or f.endswith(".yml")]
if not files:
    print("No YAML files found in input/")
    exit()

yaml_file = os.path.join(input_folder, files[0])
json_file = os.path.join(output_folder, "output.json")

try:
    with open(yaml_file, "r") as yf:
        data = yaml.safe_load(yf)

    with open(json_file, "w") as out:
        json.dump(data, out, indent=4)

    print("Conversion successful!")
    print(f"Saved → {json_file}")

except yaml.YAMLError as e:
    print("YAML parsing error:", e)
