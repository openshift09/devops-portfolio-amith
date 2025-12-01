import os
from collections import Counter
from datetime import datetime

input_folder = "input"
report_folder = "reports"
report_file = f"{report_folder}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Create reports folder if missing
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

# Get the file to analyze
files = os.listdir(input_folder)
if len(files) == 0:
    print("No files found in input/ folder.")
    exit()

file_path = os.path.join(input_folder, files[0])  # analyze first file

# Read file content
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

# Count word frequency
word_count = Counter(words)
top_words = word_count.most_common(5)

# Write report
with open(report_file, "w") as report:
    report.write("===== TEXT ANALYZER REPORT =====\n")
    report.write(f"Analyzed file: {files[0]}\n")
    report.write(f"Generated: {datetime.now()}\n\n")

    report.write(f"Total Lines: {len(lines)}\n")
    report.write(f"Total Words: {len(words)}\n")
    report.write(f"Total Characters: {characters}\n\n")
    
    report.write("Top 5 Most Frequent Words:\n")
    for word, count in top_words:
        report.write(f"  {word}: {count}\n")

print(f"Analysis complete! Report saved as: {report_file}")
