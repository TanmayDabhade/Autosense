from datetime import datetime
import os

def log_data(data, faults, filename="data/vehicle_log.txt"):
    """
    Logs data to a text file in CSV-like format without using the csv module.
    :param data: Dictionary containing vehicle parameters
    :param faults: List of detected faults
    :param filename: File path to log the data
    """
    log_entry = [
        datetime.now().isoformat(timespec="seconds"),
        data["time"],
        data["mode"],
        f'{data["speed"]:.2f}',
        f'{data["motor_power"]:.2f}',
        f'{data["battery_soc"]:.2f}',
        f'{data["battery_temp"]:.2f}',
        f'{data["motor_temp"]:.2f}',
        f'{data["tire_pressure"]:.2f}',
        "Yes" if data.get("thermal_warning", False) else "No",
        "; ".join(faults) if faults else "None"
    ]

    # Create header if file does not exist or is empty
    file_exists = os.path.isfile(filename)
    is_empty = not file_exists or os.stat(filename).st_size == 0

    with open(filename, "a") as file:
        if is_empty:
            file.write(",".join([
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
            ]) + "\n")

        file.write(",".join(str(val) for val in log_entry) + "\n")


