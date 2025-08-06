# Three dictionaries for different people
person1 = {
    'first_name': 'Kabelo',
    'last_name': 'Xabendlini',
    'age': 25,
    'city': 'Johannesburg'
}

person2 = {
    'first_name': 'Sarah',
    'last_name': 'Mokoena',
    'age': 30,
    'city': 'Cape Town'
}

person3 = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 28,
    'city': 'Durban'
}

# Store the dictionaries in a list
people = [person1, person2, person3]

# Loop through the list and print each person's info
for person in people:
    print(f"\nFull Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")