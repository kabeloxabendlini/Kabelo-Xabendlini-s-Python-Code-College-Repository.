class Battery:
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 50:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 215
        else:
            range_miles = 0
        print(f"This car can go approximately {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


# Create an electric car with default battery
my_tesla = ElectricCar("Tesla", "Model S", 2020)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Get range before upgrade
my_tesla.battery.get_range()

# Upgrade battery
my_tesla.battery.upgrade_battery()

# Get range after upgrade
my_tesla.battery.get_range()