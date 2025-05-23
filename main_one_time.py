import time
from sensor_simulator import VehicleSimulator
from fault_detector import detect_faults
from logger import log_data
from ui import display

def run():
    car = VehicleSimulator()
    i=0
    fault_count = 0
    while i<1000:
        data = car.update()
        faults = detect_faults(data)
        if faults:
            fault_count += 1
            print(f"Speed: {data['speed']} km/h | Temp: {data['temp']} °C | "
                  f"Torque: {data['torque']} Nm | Battery: {data['battery']} V | "
                  f"Tire Pressure: {data['tire_pressure']} PSI | Time: {data['time']}")
            print("⚠️ FAULTS DETECTED:", ", ".join(faults))
        i += 1
    print(fault_count)

if __name__ == "__main__":
    run()