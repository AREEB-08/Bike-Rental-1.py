import datetime

class BikeRental:
    def __init__(self):
        """Initialize bike rental system with different bikes and scooters."""
        self.vehicle_stock = {
            "Bullet": {"stock": 10, "symbol": "🏍️", "type": "bike"},
            "Ninja H2R": {"stock": 5, "symbol": "🏎️", "type": "bike"},
            "Splendor": {"stock": 15, "symbol": "🚲", "type": "bike"},
            "Pulsar": {"stock": 12, "symbol": "🏍️", "type": "bike"},
            "FZ": {"stock": 8, "symbol": "🏍️", "type": "bike"},
            "Activa": {"stock": 20, "symbol": "🛵", "type": "scooter"},
            "Jupiter": {"stock": 18, "symbol": "🛵", "type": "scooter"},
            "Fascino": {"stock": 12, "symbol": "🛵", "type": "scooter"},
        }
        self.rental_records = {}  # Stores customer rentals
        print("\n🚴 Welcome to the Bike & Scooter Rental Store! 🚴")

    def show_stock(self):
        """Displays the available stock of each vehicle."""
        print("\n✅ Available Bikes & Scooters for Rent:")
        for vehicle, details in self.vehicle_stock.items():
            print(f"{details['symbol']} {vehicle}: {details['stock']} available")

    def rent_vehicle(self, customer_name, vehicle, count, rental_type, rental_for):
        """Allows users to rent a specific bike or scooter."""
        if vehicle not in self.vehicle_stock:
            print("❌ Invalid vehicle selection. Please choose from the available options.")
            return

        if count <= 0:
            print("❌ Invalid input. Please enter a number greater than 0.")
            return

        if count > self.vehicle_stock[vehicle]["stock"]:
            print(f"⚠️ Sorry, we only have {self.vehicle_stock[vehicle]['stock']} {vehicle}(s) available.")
            return

        rental_time = datetime.datetime.now()
        self.vehicle_stock[vehicle]["stock"] -= count  # Reduce stock

        # Store rental details
        self.rental_records[customer_name] = {
            "vehicle": vehicle,
            "bikes": count,
            "rental_type": rental_type,
            "rental_time": rental_time,
            "rental_for": rental_for
        }

        print(f"\n✅ {customer_name}, you have rented {count} {vehicle}(s) {self.vehicle_stock[vehicle]['symbol']}.")
        print(f"📅 Rental Time: {rental_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📉 Remaining {vehicle}(s) in stock: {self.vehicle_stock[vehicle]['stock']}")
        print("ℹ️ Return the vehicle on time to avoid extra charges.")

    def return_vehicle(self, customer_name):
        """Allows users to return a vehicle and calculates rental cost."""
        if customer_name not in self.rental_records:
            print("❌ No rental record found. Please enter a valid name.")
            return

        rental_info = self.rental_records.pop(customer_name)
        vehicle = rental_info["vehicle"]
        count = rental_info["bikes"]
        rental_time = rental_info["rental_time"]
        rental_type = rental_info["rental_type"]
        rental_for = rental_info["rental_for"]
        
        vehicle_type = self.vehicle_stock[vehicle]["type"]

        return_time = datetime.datetime.now()
        duration = (return_time - rental_time).total_seconds() / 3600  # Convert seconds to hours

        # Pricing Structure
        if rental_for == "company":
            hourly_rate, daily_rate, weekly_rate = 40, 250, 1800
        else:
            if vehicle_type == "bike":
                hourly_rate, daily_rate, weekly_rate = 100, 500, 2500
            else:
                hourly_rate, daily_rate, weekly_rate = 50, 300, 2000

        if rental_type == "hourly":
            cost = count * hourly_rate * max(1, round(duration))
        elif rental_type == "daily":
            cost = count * daily_rate * max(1, round(duration / 24))
        elif rental_type == "weekly":
            cost = count * weekly_rate * max(1, round(duration / 168))
        else:
            print("❌ Invalid rental type.")
            return

        self.vehicle_stock[vehicle]["stock"] += count  # Update stock

        print(f"\n✅ {customer_name}, you have returned {count} {vehicle}(s) {self.vehicle_stock[vehicle]['symbol']}.")
        print(f"📅 Rental Duration: {round(duration, 2)} hours")
        print(f"💰 Total Cost: ₹{cost}")
        print(f"📈 Updated {vehicle} Stock: {self.vehicle_stock[vehicle]['stock']}")
        print("🙏 Thank you for using our service!")

# Main program
if __name__ == "__main__":
    rental_store = BikeRental()

    while True:
        print("\n🚴 Bike & Scooter Rental Options 🚴")
        print("1️⃣ Rent a bike/scooter")
        print("2️⃣ Return a bike/scooter")
        print("3️⃣ Check vehicle stock")
        print("4️⃣ Exit")
        
        try:
            choice = int(input("👉 Enter your choice (1-4): "))
            if choice == 1:
                rental_store.show_stock()
                name = input("👤 Enter your name: ")
                vehicle = input("🏍️ Enter the bike/scooter name: ").strip().title()
                bikes_to_rent = int(input("🔢 How many do you want to rent? "))
                print("⏳ Choose rental type: (hourly/daily/weekly)")
                rental_type = input("👉 Enter rental type: ").strip().lower()
                rental_for = input("🏢 Is this for personal use or company? (personal/company): ").strip().lower()

                if rental_type in ["hourly", "daily", "weekly"] and rental_for in ["personal", "company"]:
                    rental_store.rent_vehicle(name, vehicle, bikes_to_rent, rental_type, rental_for)
                else:
                    print("❌ Invalid rental type or user category.")

            elif choice == 2:
                name = input("👤 Enter your name: ")
                rental_store.return_vehicle(name)

            elif choice == 3:
                rental_store.show_stock()

            elif choice == 4:
                print("🙏 Thank you for using our service. Have a great day! 🚴")
                break

            else:
                print("❌ Invalid option. Please select a valid choice (1-4).")

        except ValueError:
            print("❌ Please enter a valid number.")
