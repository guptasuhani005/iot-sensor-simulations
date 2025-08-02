import random
import time
from datetime import datetime
import csv

# Define thresholds
LOW_TEMP = 22
HIGH_TEMP = 35

# Create an empty list to store all temperatures
temps = []

# Open the CSV file for writing
with open("temperature_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Status"])

    for i in range(20):  # Take 20 readings
        temp = round(random.uniform(20.0, 40.0), 2)
        temps.append(temp)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if temp < LOW_TEMP:
            status = "Low"
        elif temp > HIGH_TEMP:
            status = "High"
        else:
            status = "Normal"

        print(f"[{timestamp}] Temp: {temp}°C → {status}")
        writer.writerow([timestamp, temp, status])
        time.sleep(1)

    # Calculate average temp AFTER the loop
    average_temp = round(sum(temps) / len(temps), 2)
    print(f"\n🌡️ Average Temperature after 20 readings: {average_temp} °C")
    writer.writerow(["----", "Average Temp", average_temp])
