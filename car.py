# Vehicle class represents a single vehicle in the rental system
# Each vehicle has an ID, brand, model, year, price and availability status
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, price_per_day, is_available=True):
        self.vehicle_id    = vehicle_id
        self.brand         = brand
        self.model         = model
        self.year          = year
        self.price_per_day = price_per_day
        self.is_available  = is_available

    def __str__(self):
        if self.is_available:
            status = f"{GREEN}✅ Available{RESET}"
        else:
            status = f"{RED}❌ Rented{RESET}"
        return (f"  {CYAN}[{self.vehicle_id}]{RESET} {BOLD}{self.brand} {self.model}{RESET} "
                f"({self.year})  💰 ${self.price_per_day}/day  {status}")
