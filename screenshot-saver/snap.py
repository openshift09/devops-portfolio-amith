from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

url = input("Enter URL to capture: ")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

shots_folder = "shots"
if not os.path.exists(shots_folder):
    os.makedirs(shots_folder)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = f"{shots_folder}/screenshot_{timestamp}.png"

driver.get(url)
driver.save_screenshot(file_path)
driver.quit()

print(f"Screenshot saved → {file_path}")
