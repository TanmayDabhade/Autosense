def display(data, faults):
    print(f"Speed: {data['speed']} km/h | Temp: {data['temp']} °C | "
          f"Torque: {data['torque']} Nm | Battery: {data['battery']} V | "
          f"Tire Pressure: {data['tire_pressure']} PSI | Time: {data['time']}")
    if faults:
        print("⚠️ FAULTS DETECTED:", ", ".join(faults))
    else:
        print("✅ Status: Normal")
    print("-" * 80)