import os
import subprocess
from datetime import datetime

commands_folder = "commands"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Pick first command file
files = [f for f in os.listdir(commands_folder) if f.endswith(".txt")]
if not files:
    print("No command files found!")
    exit()

cmd_file = os.path.join(commands_folder, files[0])
output_file = f"{output_folder}/ssh_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(cmd_file, "r") as f:
    commands = f.readlines()

results = []

for cmd in commands:
    cmd = cmd.strip()
    if not cmd:
        continue

    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
        results.append(f"COMMAND: {cmd}\nRESULT:\n{result}\n")
    except subprocess.CalledProcessError as e:
        results.append(f"COMMAND: {cmd}\nERROR:\n{e}\n")

# Save output
with open(output_file, "w") as out:
    out.write("===== SSH SIMULATION OUTPUT =====\n")
    out.write(f"Generated: {datetime.now()}\n\n")
    for block in results:
        out.write(block + "\n")

print("Commands executed successfully!")
print(f"Output saved → {output_file}")
