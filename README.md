# Autosense

---

#  Automated Fault Detection using Simulated Sensor Data
This project is a **real-time vehicle telemetry simulator** built in pure Python.
It is supposed to help us model, simulate and understand how EVs manage motor load, 
battery health, thermal regulation, and other factors in real-world scenarios.

This script can be used in **testing newer systems** by manipulating the calculations for certain 
values crucial for functioning of the machine.

It models **dynamic driving behavior, power output, heat buildup, and fault detection** 
calculated using physics-based relationships and equations that use these interdependent factors.
The model uses:

-  Motor power, speed, tire pressure, battery SOC & temps
-  Fault detection (thresholds, rates of change, multi-sensor conditions)
-  Cooling system logic (fan, aerodynamic & liquid cooling simulation)
-  Thermal shutdown and throttle behavior
-  Modular architecture: sensor simulation, logger, fault engine, UI

---

##  Features

###  Mode-Based Driving Schedule
**Why a mode based driving schedule and not a random number to choose between the 3 modes>**

Using random to choose modes made it look unrealistic, ask yourself, would you be switching from 
```
aggressive->idle->normal->aggressive
```
every 2 seconds? No right, hence the driving mode schedule to
keep the simulated data realistic.

For this Driving Schedule we use:
- Predefined list of 10 `(duration_in_seconds, driving_mode)` tuples  
- Modes: `aggressive`, `normal`, `idle`
- Each mode executes for realistic durations before transitioning  
  → e.g., `[(15, 'aggressive'), (20, 'idle'), (18, 'normal')]`

###  Physics-Inspired Thermal System
- Heat generated from:
  - Motor power × time
  - Accumulated stress (via `heat_load`)
- Cooling via:
  - Airflow from vehicle speed
  - Coolant loop efficiency
  - Fan-assisted idle cooling
- Thermal inertia buffers short-term spikes

###  Fault Detection Engine
- Critical and warning-level fault analysis
- Monitors:
  - Motor Overheating
  - Battery SOC Depletion
  - Tire Pressure Drop
  - High temp + power combinations
- Tracks rate-of-change + persistence

###  Dashboard UI (Terminal)
- Live telemetry printout
- Real-time fault display

###  Logging
- Logs every update to `vehicle_log.csv`
- Includes sensor values and triggered faults

---

##  Sample Output

```

#  Tesla Vehicle Telemetry Dashboard

️ Time: 2025-05-23T16:44:26        Mode: Aggressive
 Speed:          104.33 km/h
 Motor Power:      91.27 kW
 Battery SOC:      68.42%
 Battery Temp:    52.1 °C
 Motor Temp:       89.7 °C
 Tire Pressure:    31.3 PSI
-----------------------------

 FAULTS DETECTED:
➤  Motor Overheating \[Critical]
➤  Battery Hot & Low SOC \[Critical]
THERMAL WARNING: Vehicle is nearing overheat thresholds!
============================================================
```


---

##  Why This Project Matters

This is not just any other python script, it simulates **how real EV systems work**:
- Demonstrates understanding of **thermal management, systems design, and fault tolerance**
- No external libraries (except `random`, `datetime`, `csv`)
- Built with **embedded engineering principles** in mind

---

##  Run It

```bash
python3 main.py
```

You can modify the drive schedule length or thresholds directly in `VehicleSimulator`.

---

## Directory Structure

```
autosense/
│
├── main.py                # Simulation runner
├── vehicle_simulator.py     # Core simulation logic
├── fault_detector.py      # Fault detection engine
├── logger.py              # CSV logger
├── ui.py                  # Terminal dashboard
└── data/vehicle_log.csv   # Logged output
```

---

## Ideas to Extend

* Add Streamlit-based web dashboard
* Simulate regenerative braking
* Visualize log data in a graph
* Train ML model to predict faults
* Simulate limp mode (power-limited state before shutdown)

---
## Built By
**Tanmay Dabhade**\
[LinkedIn](https://www.linkedin.com/in/tanmay-dabhade)
---
