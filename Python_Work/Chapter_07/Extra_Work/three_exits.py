# Version 1: Conditional test in while loop
age_input = input("Enter your age (or 'quit' to stop): ")

while age_input.lower() != 'quit':
    age = int(age_input)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    age_input = input("Enter your age (or 'quit' to stop): ")

print("Goodbye!")
