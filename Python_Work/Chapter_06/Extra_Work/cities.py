# Dictionary of cities, each containing info about country, population, and a fact
cities = {
    'cape town': {
        'country': 'South Africa',
        'population': '4.6 million',
        'fact': 'It is known for the iconic Table Mountain.'
    },
    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'It is called the "City of Light".'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'It is the largest metropolitan area in the world.'
    }
}

# Loop through the dictionary and print info about each city
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")