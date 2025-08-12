class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # New attribute

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Create a user instance
user = User("Alice", "Johnson", 28, "alice@example.com", "New York")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print current login attempts
print(f"Login attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")