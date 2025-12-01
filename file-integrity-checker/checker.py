import hashlib
import os
from datetime import datetime

files_folder = "files"
report_folder = "reports"

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Hash function
def sha256_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Pick first file to check
files = os.listdir(files_folder)
if not files:
    print("No files found in 'files/' folder!")
    exit()

file_path = os.path.join(files_folder, files[0])

# Create report file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"{report_folder}/integrity_report_{timestamp}.txt"

# Compute hash
current_hash = sha256_hash(file_path)

# Save hash
with open(report_file, "w") as r:
    r.write("===== FILE INTEGRITY REPORT =====\n")
    r.write(f"File: {file_path}\n")
    r.write(f"Generated: {datetime.now()}\n\n")
    r.write(f"SHA256 Hash:\n{current_hash}\n")

print("\nIntegrity check complete!")
print(f"Hash generated: {current_hash}")
print(f"Report saved → {report_file}")
