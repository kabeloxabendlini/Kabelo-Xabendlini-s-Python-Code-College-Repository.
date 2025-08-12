class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

# Create several users
user1 = User("Alice", "Johnson", 28, "alice@example.com", "New York")
user2 = User("Bob", "Smith", 35, "bobsmith@example.com", "London")
user3 = User("Charlie", "Brown", 22, "charlieb@example.com", "Sydney")

# Call methods for each user
for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()