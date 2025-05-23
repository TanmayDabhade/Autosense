import csv
from datetime import datetime

def log_data(data, faults, filename="data/vehicle_log.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Time", "Speed", "Temp", "Torque", "Battery", "Tire_Pressure", "Faults"])
        writer.writerow([
            datetime.now().isoformat(),
            data["speed"], data["temp"], data["torque"],
            data["battery"], data["tire_pressure"],
            "; ".join(faults) if faults else "None"
        ])