import yaml
import os

# Folder to scan
folder = "examples/output"

print("Validating generated YAML...\n")

for file in os.listdir(folder):
    if file.endswith(".yaml"):
        path = f"{folder}/{file}"
        try:
            with open(path, "r") as f:
                yaml.safe_load(f)
            print(f"[OK] {path}")
        except Exception as e:
            print(f"[ERROR] {path} → {e}")
