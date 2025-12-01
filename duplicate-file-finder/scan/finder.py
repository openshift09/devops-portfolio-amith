import os
import hashlib
from datetime import datetime

scan_folder = "scan"
report_folder = "reports"
report_file = f"{report_folder}/duplicates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Create report folder if missing
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

def file_hash(path):
    """Return MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

files_seen = {}
duplicates = []

# Walk through folder
for root, _, files in os.walk(scan_folder):
    for f in files:
        path = os.path.join(root, f)
        h = file_hash(path)

        if h in files_seen:
            duplicates.append((files_seen[h], path))
        else:
            files_seen[h] = path

# Save report
with open(report_file, "w") as r:
    r.write("===== DUPLICATE FILE REPORT =====\n")
    r.write(f"Generated: {datetime.now()}\n\n")

    if duplicates:
        for original, dup in duplicates:
            r.write(f"ORIGINAL:  {original}\n")
            r.write(f"DUPLICATE: {dup}\n\n")
    else:
        r.write("No duplicate files found.\n")

print(f"Scan complete! Report saved → {report_file}")
