import re

LOG_FILE = "logs/sample.log"

def read_log(file_path):
    """Reads log file line by line."""
    with open(file_path, 'r') as file:
        return file.readlines()

def count_log_levels(lines):
    """Counts INFO, WARNING, ERROR entries."""
    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        if "INFO" in line:
            summary["INFO"] += 1
        if "WARNING" in line:
            summary["WARNING"] += 1
        if "ERROR" in line:
            summary["ERROR"] += 1

    return summary

def extract_errors(lines):
    """Extracts all ERROR messages with timestamp."""
    error_list = []
    for line in lines:
        if "ERROR" in line:
            error_list.append(line.strip())
    return error_list

def filter_by_keyword(lines, keyword):
    """Filter logs that contain a keyword."""
    return [line.strip() for line in lines if keyword.lower() in line.lower()]

def save_report(summary, errors):
    """Save analysis report to a file."""
    with open("report.txt", "w") as file:
        file.write("LOG ANALYSIS REPORT\n")
        file.write("------------------\n")
        file.write(f"INFO Count: {summary['INFO']}\n")
        file.write(f"WARNING Count: {summary['WARNING']}\n")
        file.write(f"ERROR Count: {summary['ERROR']}\n\n")

        file.write("ERROR DETAILS:\n")
        for err in errors:
            file.write(err + "\n")

def main():
    print("Reading log file...")
    lines = read_log(LOG_FILE)

    print("Counting log levels...")
    summary = count_log_levels(lines)
    print(summary)

    print("Extracting errors...")
    errors = extract_errors(lines)
    print(errors)

    print("Filtering logs containing 'CPU'...")
    cpu_logs = filter_by_keyword(lines, "CPU")
    print(cpu_logs)

    print("Saving report...")
    save_report(summary, errors)

    print("Analysis complete. Report saved as report.txt")

if __name__ == "__main__":
    main()
