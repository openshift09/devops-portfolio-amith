import os
import zipfile
from datetime import datetime
import shutil

data_folder = "data"
backup_folder = "backups"
max_backups = 5   # keep last 5 backups

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Create backup name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
zip_name = f"backup_{timestamp}.zip"
zip_path = os.path.join(backup_folder, zip_name)

# Create ZIP backup
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(data_folder):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, data_folder)
            zipf.write(full_path, arcname)

print(f"Backup created: {zip_path}")

# Cleanup old backups (keep last N)
existing_backups = sorted(os.listdir(backup_folder))

if len(existing_backups) > max_backups:
    to_delete = existing_backups[:-max_backups]
    for old in to_delete:
        old_path = os.path.join(backup_folder, old)
        os.remove(old_path)
        print(f"Deleted old backup: {old_path}")
