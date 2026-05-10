import json
from car import Vehicle

VEHICLES_FILE = "vehicles.json"
HISTORY_FILE  = "history.json"

def save_vehicles(vehicles):
    with open(VEHICLES_FILE, "w") as f:
        json.dump([v.__dict__ for v in vehicles], f, indent=4)

def load_vehicles():
    try:
        with open(VEHICLES_FILE, "r") as f:
            data = json.load(f)
        return [Vehicle(**item) for item in data]
    except FileNotFoundError:
        return _default_vehicles()

def _default_vehicles():
    return [
        Vehicle(1, "Toyota",  "Camry",   2020, 45),
        Vehicle(2, "BMW",     "X5",      2022, 120),
        Vehicle(3, "Hyundai", "Sonata",  2021, 55),
        Vehicle(4, "Tesla",   "Model 3", 2023, 95),
        Vehicle(5, "Kia",     "Sportage",2022, 60),
    ]

def save_history(entry):
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
