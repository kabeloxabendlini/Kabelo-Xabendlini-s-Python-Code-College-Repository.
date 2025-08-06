# Individual pet dictionaries
pet1 = {
    'animal': 'dog',
    'name': 'Max',
    'owner': 'Kabelo'
}

pet2 = {
    'animal': 'cat',
    'name': 'Whiskers',
    'owner': 'Sarah'
}

pet3 = {
    'animal': 'parrot',
    'name': 'Polly',
    'owner': 'John'
}

pet4 = {
    'animal': 'rabbit',
    'name': 'Thumper',
    'owner': 'Ella'
}

# Store the pet dictionaries in a list
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print pet details
for pet in pets:
    print(f"\n{pet['name']} is a {pet['animal']}.")
    print(f"Owner: {pet['owner']}")