# Dictionary of people and their favorite places
favorite_places = {
    'kabelo': ['Cape Town', 'Durban', 'Kruger National Park'],
    'sarah': ['Paris', 'Rome'],
    'john': ['New York']
}

# Loop through the dictionary and print each person's favorite places
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")