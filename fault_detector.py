def detect_faults(data):
    faults = []

    if data["temp"] > 120:
        faults.append("🔥 Engine Overheating")
    if data["battery"] < 12.0:
        faults.append("🔋 Low Battery")
    if data["tire_pressure"] < 30:
        faults.append("⚠️ Tire Pressure Low")
    if data["speed"] > 120:
        faults.append("🚗 Overspeeding")

    return faults