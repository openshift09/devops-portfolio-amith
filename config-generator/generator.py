import json
import yaml
import os
from datetime import datetime

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Ask user for config details
app_name = input("Enter application name: ")
environment = input("Enter environment (dev/stage/prod): ")
version = input("Enter version: ")

db_host = input("Enter DB host: ")
db_user = input("Enter DB username: ")
db_pass = input("Enter DB password: ")

config = {
    "app": {
        "name": app_name,
        "environment": environment,
        "version": version
    },
    "database": {
        "host": db_host,
        "username": db_user,
        "password": db_pass
    },
    "generated_at": str(datetime.now())
}

# Save JSON file
json_file = f"{output_folder}/config_{environment}.json"
with open(json_file, "w") as jf:
    json.dump(config, jf, indent=4)

# Save YAML file
yaml_file = f"{output_folder}/config_{environment}.yaml"
with open(yaml_file, "w") as yf:
    yaml.dump(config, yf, default_flow_style=False)

print("\nConfig files generated:")
print(f"  JSON → {json_file}")
print(f"  YAML → {yaml_file}")
