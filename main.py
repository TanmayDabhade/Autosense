import time
from sensor_simulator import VehicleSimulator
from fault_detector import detect_faults
from logger import log_data
from ui import display

def run():
    car = VehicleSimulator()

    while True:
        data = car.update()
        faults = detect_faults(data)
        display(data, faults)
        log_data(data, faults)
        time.sleep(2)


if __name__ == "__main__":
    run()