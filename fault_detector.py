class FaultDetector:
    def __init__(self):
        self.overheat_duration = 0
        self.low_soc_duration = 0
        self.pressure_drop_duration = 0
        self.last_values = {}

    def detect(self, data):
        faults = []

        # Store trends
        current = data
        prev = self.last_values or current
        self.last_values = current

        # === Persistent Fault Conditions ===

        # 🚨 Motor Overheat (time-based)
        if current["motor_temp"] > 85:
            self.overheat_duration += 1
        else:
            self.overheat_duration = max(0, self.overheat_duration - 1)

        if self.overheat_duration >= 3:
            faults.append("🔥 Motor Overheating [Critical]")

        # ⚠️ Battery Low SOC
        if current["battery_soc"] < 15:
            self.low_soc_duration += 1
        else:
            self.low_soc_duration = max(0, self.low_soc_duration - 1)

        if self.low_soc_duration >= 3:
            faults.append("🔋 Critically Low Battery [Warning]")

        # ⚠️ Tire Pressure Drop
        if current["tire_pressure"] < 29.0:
            self.pressure_drop_duration += 1
        else:
            self.pressure_drop_duration = max(0, self.pressure_drop_duration - 1)

        if self.pressure_drop_duration >= 5:
            faults.append("⚠️ Tire Pressure Critically Low")

        # === Context-Aware Conditions ===

        # ⚠️ Overpower while hot
        if current["motor_power"] > 100 and current["motor_temp"] > 75:
            faults.append("⚡ Motor Overload in High Temp [Warning]")

        # ⚠️ Hot Battery + Low SOC
        if current["battery_temp"] > 55 and current["battery_soc"] < 20:
            faults.append("🧯 Battery Hot & Low SOC [Critical]")

        # ⚠️ High speed + low tire pressure
        if current["speed"] > 120 and current["tire_pressure"] < 30:
            faults.append("🚗⚠️ Overspeeding with Low Tire Pressure [Risky]")

        # === Rate-of-Change Checks ===

        def delta(field):
            return abs(current[field] - prev[field])

        if delta("motor_temp") > 10:
            faults.append("🔥 Rapid Motor Temp Rise")

        if delta("battery_temp") > 6:
            faults.append("🧯 Battery Thermal Spike")

        if delta("tire_pressure") > 1.5:
            faults.append("💥 Sudden Tire Pressure Change")

        # === Hard Faults ===

        if current["battery_soc"] < 5:
            faults.append("🚨 Battery Shutdown Imminent")

        if current["motor_temp"] > 95:
            faults.append("🔥🔥 Motor System Critical Shutdown Required")

        return faults
