def display(data, faults):
    print("\n📊 Vehicle Telemetry Dashboard")
    print("=" * 80)

    # Section: Timestamp and Driving Mode
    print(f"⏱️  Time: {data['time']:<20}       Mode: {data['mode'].capitalize()}")

    # Section: Motion and Power
    print(f"🚗 Speed:          {data['speed']:>6} km/h")
    print(f"⚡ Motor Power:     {data['motor_power']:>6} kW")

    # Section: Battery Health
    print(f"🔋 Battery SOC:     {data['battery_soc']:>6}%")
    print(f"🌡️  Battery Temp:   {data['battery_temp']:>6} °C")

    # Section: Motor System
    print(f"🔥 Motor Temp:      {data['motor_temp']:>6} °C")
    print(f"🛞 Tire Pressure:   {data['tire_pressure']:>6} PSI")

    # Section: Fault Display
    print("-" * 80)
    if faults:
        print("🚨 FAULTS DETECTED:")
        for fault in faults:
            print(f"   ➤ {fault}")
    else:
        print("✅ All systems operating within safe parameters.")

    # Thermal Warning
    if data.get("thermal_warning", False):
        print("⚠️  THERMAL WARNING: Vehicle is nearing overheat thresholds!")

    print("=" * 80)
