import requests
import json
import os
from datetime import datetime

cache_folder = "cache"
cache_file = f"{cache_folder}/weather_cache.json"

if not os.path.exists(cache_folder):
    os.makedirs(cache_folder)

city = input("Enter city name: ").strip()

# API endpoint (no key needed)
url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url, timeout=5)
    data = response.json()

    # Save to cache
    with open(cache_file, "w") as f:
        json.dump(data, f, indent=4)

    print("\n=== CURRENT WEATHER ===")
    current = data["current_condition"][0]
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Weather: {current['weatherDesc'][0]['value']}")
    print(f"Humidity: {current['humidity']}%")

except:
    print("\nAPI unreachable! Loading cached weather...")
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cached = json.load(f)

        current = cached["current_condition"][0]
        print("\n=== CACHED WEATHER ===")
        print(f"Temperature: {current['temp_C']}°C")
        print(f"Weather: {current['weatherDesc'][0]['value']}")
        print(f"Humidity: {current['humidity']}%")
    else:
        print("No cached data available.")
