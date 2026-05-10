from datetime import datetime
from decorators import log_action
from file_handler import save_history

@log_action
def rent_vehicle(vehicles, vehicle_id, renter_name, days):
    for v in vehicles:
        if v.vehicle_id == vehicle_id:
            if v.is_available:
                v.is_available = False
                total = v.price_per_day * days
                save_history({
                    "action":     "RENT",
                    "renter":     renter_name,
                    "vehicle":    f"{v.brand} {v.model}",
                    "days":       days,
                    "total_cost": total,
                    "date":       datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                print(f"\n  ✅ {renter_name} rented {v.brand} {v.model} for {days} day(s).")
                print(f"  💵 Total cost: ${total}")
            else:
                print("\n  ❌ Sorry, this vehicle is already rented.")
            return
    print("\n  ❌ Vehicle not found.")

@log_action
def return_vehicle(vehicles, vehicle_id, renter_name):
    for v in vehicles:
        if v.vehicle_id == vehicle_id:
            if not v.is_available:
                v.is_available = True
                save_history({
                    "action":  "RETURN",
                    "renter":  renter_name,
                    "vehicle": f"{v.brand} {v.model}",
                    "date":    datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                print(f"\n  ✅ {v.brand} {v.model} returned successfully. Thank you, {renter_name}!")
            else:
                print("\n  ⚠️  This vehicle was not rented.")
            return
    print("\n  ❌ Vehicle not found.")
