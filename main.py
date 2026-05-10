from file_handler import load_vehicles, save_vehicles, load_history
from rental import rent_vehicle, return_vehicle
from car import Vehicle, BOLD, CYAN, YELLOW, GREEN, RESET

DIVIDER = "  " + "─" * 46

def print_header():
    print("\n" + "  " + "═" * 46)
    print(f"  {BOLD}{CYAN}   🚗  VEHICLE RENTAL MANAGEMENT SYSTEM  🚗{RESET}")
    print("  " + "═" * 46)

def show_menu():
    print_header()
    print(f"\n  {YELLOW}1.{RESET} View all vehicles")
    print(f"  {YELLOW}2.{RESET} Rent a vehicle")
    print(f"  {YELLOW}3.{RESET} Return a vehicle")
    print(f"  {YELLOW}4.{RESET} Add a new vehicle")
    print(f"  {YELLOW}5.{RESET} View rental history")
    print(f"  {YELLOW}6.{RESET} Exit")
    print(DIVIDER)

def main():
    vehicles = load_vehicles()

    while True:
        show_menu()
        choice = input(f"  {BOLD}Choose an option (1-6): {RESET}").strip()

        if choice == "1":
            print(f"\n{DIVIDER}")
            print(f"  {BOLD}All Vehicles:{RESET}")
            print(DIVIDER)
            for v in vehicles:
                print(v)
            print(DIVIDER)

        elif choice == "2":
            print(f"\n  {BOLD}Available vehicles:{RESET}")
            available = [v for v in vehicles if v.is_available]
            if not available:
                print("  No vehicles available right now.")
            else:
                for v in available:
                    print(v)
            try:
                vid  = int(input("\n  Enter vehicle ID: "))
                name = input("  Your name: ").strip()
                days = int(input("  How many days? "))
                rent_vehicle(vehicles, vid, name, days)
                save_vehicles(vehicles)
            except ValueError:
                print("  ❌ Invalid input.")

        elif choice == "3":
            print(f"\n  {BOLD}Rented vehicles:{RESET}")
            rented = [v for v in vehicles if not v.is_available]
            if not rented:
                print("  No vehicles are currently rented.")
            else:
                for v in rented:
                    print(v)
            try:
                vid  = int(input("\n  Enter vehicle ID to return: "))
                name = input("  Your name: ").strip()
                return_vehicle(vehicles, vid, name)
                save_vehicles(vehicles)
            except ValueError:
                print("  ❌ Invalid input.")

        elif choice == "4":
            try:
                vid   = max(v.vehicle_id for v in vehicles) + 1
                brand = input("\n  Brand: ").strip()
                model = input("  Model: ").strip()
                year  = int(input("  Year: "))
                price = float(input("  Price per day ($): "))
                vehicles.append(Vehicle(vid, brand, model, year, price))
                save_vehicles(vehicles)
                print(f"\n  {GREEN}✅ Vehicle added successfully! ID: {vid}{RESET}")
            except ValueError:
                print("  ❌ Invalid input.")

        elif choice == "5":
            history = load_history()
            print(f"\n{DIVIDER}")
            print(f"  {BOLD}Rental History:{RESET}")
            print(DIVIDER)
            if not history:
                print("  No history yet.")
            else:
                for entry in history:
                    action = entry.get("action", "?")
                    icon   = "🔑" if action == "RENT" else "🔄"
                    print(f"  {icon} [{entry['date']}] {action} — {entry['vehicle']} — {entry['renter']}", end="")
                    if action == "RENT":
                        print(f" — {entry['days']} day(s) — ${entry['total_cost']}")
                    else:
                        print()
            print(DIVIDER)

        elif choice == "6":
            print(f"\n  {GREEN}👋 Thank you for using Vehicle Rental Management System. Goodbye!{RESET}\n")
            break

        else:
            print("  ⚠️  Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
