import csv
from datetime import datetime


def log_data(data, faults, filename="data/vehicle_log.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow([
                "Logged_At",
                "Simulated_Time",
                "Mode",
                "Speed_kmh",
                "Motor_Power_kW",
                "Battery_SOC_%",
                "Battery_Temp_°C",
                "Motor_Temp_°C",
                "Tire_Pressure_PSI",
                "Thermal_Warning",
                "Faults"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            data["time"],
            data["mode"],
            data["speed"],
            data["motor_power"],
            data["battery_soc"],
            data["battery_temp"],
            data["motor_temp"],
            data["tire_pressure"],
            "Yes" if data.get("thermal_warning", False) else "No",
            "; ".join(faults) if faults else "None"
        ])
