import random
from datetime import datetime, timedelta

class VehicleSimulator:
    def __init__(self):
        self.speed = 100.0       # km/h
        self.temp = 90.0        # °C
        self.torque = 250.5      # Nm
        self.battery = 12.5      # V
        self.tire_pressure = 31.0  # PSI
        self.start_time = datetime.now()
        self.time_step = timedelta(seconds=2)
        self.current_time = self.start_time

        self.overheat_duration = 0
        self.aggressive_count = 0
        self.cooldown_counter = 0

    def update(self):
        self.current_time += self.time_step

        # Simulated environment variable
        ambient_temp = 30  # °C constant for simplicity

        # Driving mode
        mode = random.choices(
            ['normal', 'aggressive', 'idle'],
            weights=[0.5, 0.3, 0.2],
            k=1
        )[0]

        delta = {
            'normal': {'speed': 10, 'temp': 0.5, 'torque': 5},
            'aggressive': {'speed': 5, 'temp': 1.2, 'torque': 10},
            'idle': {'speed': -5, 'temp': -0.5, 'torque': -15}
        }

        # Mode effects
        self.speed = max(0.0, self.speed + random.uniform(-delta[mode]['speed'], delta[mode]['speed']))
        self.torque = max(50.0, self.torque + random.uniform(-delta[mode]['torque'], delta[mode]['torque']))

        # Gradual heating effect
        temp_change = random.uniform(-0.3, 0.3)
        if mode == 'aggressive':
            self.aggressive_count += 1
            temp_change += 0.6
        else:
            self.aggressive_count = max(0, self.aggressive_count - 1)
            temp_change -= 0.2

        if self.aggressive_count > 3:
            temp_change += 1.5  # heat buildup after sustained aggression

        self.temp = max(ambient_temp, self.temp + temp_change)

        # Cooldown (simulated fan effect)
        if self.temp > 120:
            self.cooldown_counter = 5  # fault lingers
        elif self.cooldown_counter > 0:
            self.cooldown_counter -= 1
        elif self.temp > 90:
            self.temp -= 0.4  # fan cools down

        # Battery & tire pressure
        self.battery = round(random.gauss(12.4, 0.1), 2)
        self.tire_pressure -= 0.01
        if self.tire_pressure < 28:
            self.tire_pressure += 1.5

        return {
            "time": self.current_time.isoformat(timespec="seconds"),
            "speed": round(self.speed, 2),
            "temp": round(self.temp, 2),
            "torque": round(self.torque, 2),
            "battery": round(self.battery, 2),
            "tire_pressure": round(self.tire_pressure, 2),
            "mode": mode,
            "overheat": self.temp > 120 or self.cooldown_counter > 0
        }
