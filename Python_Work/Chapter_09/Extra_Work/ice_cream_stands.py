class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Welcome!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")


# Subclass for Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # List of ice cream flavors

    def display_flavors(self):
        if self.flavors:
            print(f"{self.restaurant_name} offers the following flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print(f"{self.restaurant_name} has no flavors listed yet.")


# Create an instance
ice_cream_stand = IceCreamStand("Sweet Treats")

# Add some flavors
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

# Show restaurant description
ice_cream_stand.describe_restaurant()

# Display flavors
ice_cream_stand.display_flavors()