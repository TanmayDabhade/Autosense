import time
from sensor_simulator import VehicleSimulator        # updated simulator class
from fault_detector import FaultDetector          # upgraded class-based detector
from logger import log_data
from ui import display

def run():
    car = VehicleSimulator()
    detector = FaultDetector()  # class instance to track state over time

    while True:
        data = car.update()
        faults = detector.detect(data)
        display(data, faults)
        log_data(data, faults)
        time.sleep(2)


if __name__ == "__main__":
    run()
