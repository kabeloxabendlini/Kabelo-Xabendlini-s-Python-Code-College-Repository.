# 7-5. Movie Tickets

print("Enter 'quit' to stop the program.")

while True:
    age_input = input("How old are you? ")

    if age_input.lower() == 'quit':
        print("Thanks for checking the ticket prices!")
        break

    age = int(age_input)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")