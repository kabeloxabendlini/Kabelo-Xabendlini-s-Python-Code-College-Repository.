# 7-10. Dream Vacation

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation_spot = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation_spot

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

# Polling is complete, show the results
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")