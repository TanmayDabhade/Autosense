import random
from datetime import datetime, timedelta

class VehicleSimulator:
    def __init__(self):
        self.speed = 100.0             # km/h
        self.motor_power = 90.0        # kW
        self.battery_soc = 80.0        # %
        self.battery_temp = 38.0       # °C
        self.motor_temp = 45.0         # °C
        self.tire_pressure = 31.0      # PSI

        self.start_time = datetime.now()
        self.time_step = timedelta(seconds=2)
        self.current_time = self.start_time

        # Thermal systems
        self.heat_load = 0
        self.cooling_mode_duration = 0
        self.thermal_warning = False
        self.shutdown_counter = 0

        # Constants for cooling behavior
        self.coolant_efficiency = 0.8
        self.aero_cooling_factor = 0.04
        self.thermal_inertia = 0.2

        # Driving profile
        self.drive_schedule = self.generate_drive_schedule()
        self.current_mode_index = 0
        self.mode_time_remaining = self.drive_schedule[0][0]  # seconds
        self.mode = self.drive_schedule[0][1]

    def generate_drive_schedule(self):
        """
        Generates a driving schedule to make generation of simulated data look realistic. Uses random to generate a random driving schedule for which every driving mode is for a time period between 10-20 seconds and there are 10 time frames in every schedule.
        :return: [list]: random driving schedule
        """
        modes = ['normal', 'aggressive', 'idle']
        return [(random.randint(10, 20), random.choice(modes)) for _ in range(10)]

    def update(self):
        """
        Use real physics relationships and simulates data to calculate the major factors crucial for the functioning of a Electronic Vehicle.
        The function generates the following values.
         - time
         - mode
         - speed
         - motor_power
         - battery_soc
         - battery_temp
         - tire_pressure
         - heat_load
         - cooling_mode_duration
         - thermal_warning
        These values are then used to determine if the vehicle is running well or is nearing a fault point.
        :return: List of values above.
        """
        self.current_time += self.time_step
        ambient_temp = 28.0  # °C

        # Mode timing control
        self.mode_time_remaining -= 2
        if self.mode_time_remaining <= 0:
            self.current_mode_index += 1
            if self.current_mode_index < len(self.drive_schedule):
                duration, self.mode = self.drive_schedule[self.current_mode_index]
                self.mode_time_remaining = duration
            else:
                print("✅ Simulation Complete: Drive cycle finished.")
                exit(0)

        delta = {
            'normal': {'speed': 10, 'motor_power': 5},
            'aggressive': {'speed': 25, 'motor_power': 15},
            'idle': {'speed': -5, 'motor_power': -10}
        }

        # Update speed & motor power
        self.speed = max(0.0, self.speed + random.uniform(-delta[self.mode]['speed'], delta[self.mode]['speed']))
        self.motor_power = max(0.0, self.motor_power + random.uniform(-delta[self.mode]['motor_power'], delta[self.mode]['motor_power']))

        # Accumulate heat load
        if self.mode == 'aggressive':
            self.heat_load += 1
        else:
            self.heat_load = max(0, self.heat_load - 1)

        # Motor temp increase (with thermal inertia)
        raw_heat = self.motor_power * 0.04 + (self.heat_load * 0.5)
        aero_cooling = self.speed * self.aero_cooling_factor
        liquid_cooling = self.coolant_efficiency * 1.5
        net_temp_change = (raw_heat - aero_cooling - liquid_cooling) * self.thermal_inertia
        self.motor_temp = max(ambient_temp, self.motor_temp + net_temp_change)

        # Idle cooldown
        if self.mode == 'idle' and self.speed < 20:
            self.cooling_mode_duration += 1
            fan_cooling = 0.5 + self.cooling_mode_duration * 0.2
            self.motor_temp -= fan_cooling
            self.motor_temp = max(ambient_temp, self.motor_temp)
        else:
            self.cooling_mode_duration = 0

        # Battery temp increase (based on power)
        battery_temp_increase = self.motor_power * 0.02
        self.battery_temp = max(ambient_temp, self.battery_temp + battery_temp_increase - 0.8)

        # Thermal warning status
        self.thermal_warning = self.motor_temp > 85 or self.battery_temp > 60

        # Battery SOC drop
        soc_drop = self.motor_power * 0.01
        self.battery_soc = max(0.0, self.battery_soc - soc_drop)

        # Tire pressure dynamics
        self.tire_pressure -= 0.005
        self.tire_pressure += 0.002 * (self.battery_temp - 30)
        if self.tire_pressure < 28:
            self.tire_pressure += 1.5

        # Delayed thermal shutdown logic
        if self.motor_temp > 100 or self.battery_temp > 70:
            self.shutdown_counter += 1
        else:
            self.shutdown_counter = max(0, self.shutdown_counter - 1)

        if self.shutdown_counter >= 3:
            print("\n🚨 CRITICAL THERMAL SHUTDOWN INITIATED")
            print(f"🔥 Motor Temp: {self.motor_temp:.2f} °C")
            print(f"🧯 Battery Temp: {self.battery_temp:.2f} °C")
            exit(1)

        return {
            "time": self.current_time.isoformat(timespec="seconds"),
            "mode": self.mode,
            "speed": round(self.speed, 2),
            "motor_power": round(self.motor_power, 2),
            "battery_soc": round(self.battery_soc, 2),
            "battery_temp": round(self.battery_temp, 2),
            "motor_temp": round(self.motor_temp, 2),
            "tire_pressure": round(self.tire_pressure, 2),
            "thermal_warning": self.thermal_warning
        }
