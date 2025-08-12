class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Welcome!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        """Increase the number of customers served."""
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")

# Create an instance
restaurant = Restaurant("Mama's Kitchen", "Italian")

# Print initial number served
print(f"Number of customers served: {restaurant.number_served}")

# Change the value directly
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

# Use set_number_served()
restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

# Use increment_number_served()
restaurant.increment_number_served(25)
print(f"Number of customers served: {restaurant.number_served}")