import requests
import os
from datetime import datetime

report_folder = "reports"
if not os.path.exists(report_folder):
    os.makedirs(report_folder)

url = input("Enter URL to fetch headers: ")

try:
    response = requests.get(url, timeout=5)
    headers = response.headers
    status = response.status_code

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"{report_folder}/headers_{timestamp}.txt"

    with open(report_file, "w") as r:
        r.write("===== HTTP HEADER REPORT =====\n")
        r.write(f"URL: {url}\n")
        r.write(f"Status Code: {status}\n")
        r.write(f"Generated: {datetime.now()}\n\n")

        for key, value in headers.items():
            r.write(f"{key}: {value}\n")

    print("\nHeaders fetched successfully!")
    print(f"Report saved → {report_file}")

except requests.exceptions.RequestException as e:
    print("\nError fetching URL:")
    print(str(e))
