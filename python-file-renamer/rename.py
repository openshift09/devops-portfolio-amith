import os
from datetime import datetime

folder = "sample_files"
log_folder = "logs"
log_file = f"{log_folder}/rename.log"

# Create log folder if missing
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Log function
def write_log(message):
    with open(log_file, "a") as f:
        f.write(message + "\n")

write_log(f"=== Rename Script Started at {datetime.now()} ===")

# Process files
for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        # create new filename
        new_name = filename.lower().replace(" ", "_")
        new_path = os.path.join(folder, new_name)

        # rename file
        os.rename(old_path, new_path)

        write_log(f"Renamed: '{filename}' -> '{new_name}' at {datetime.now()}")

write_log(f"=== Rename Script Completed at {datetime.now()} ===")
print("File renaming completed successfully.")
