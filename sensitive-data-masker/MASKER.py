import os
import re
from datetime import datetime

log_folder = "logs"
report_folder = "reports"

if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Masking Patterns
patterns = {
    r"(password\s*=\s*)(\S+)": r"\1********",
    r"(password:?\s*)(\S+)": r"\1********",
    r"(token[:=]\s*)(\S+)": r"\1********",
    r"(api[_\-]?key[:=]\s*)(\S+)": r"\1********",
    r"(secret[:=]\s*)(\S+)": r"\1********",
    r"(auth[_\-]?key[:=]\s*)(\S+)": r"\1********",
    r"(db[_\-]?password[:=]\s*)(\S+)": r"\1********"
}

# Get first log file
files = [f for f in os.listdir(log_folder) if f.endswith(".log")]
if not files:
    print("No log files found in logs/")
    exit()

log_file = os.path.join(log_folder, files[0])
output_file = f"{report_folder}/sanitized_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

with open(log_file, "r") as f:
    content = f.read()

# Apply masking
for pattern, replacement in patterns.items():
    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

# Save sanitized log
with open(output_file, "w") as out:
    out.write(content)

print("Sensitive data masked successfully!")
print(f"Sanitized output → {output_file}")
