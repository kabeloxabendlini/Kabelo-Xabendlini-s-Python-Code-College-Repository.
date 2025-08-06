cities = {
    'cape town': {
        'country': 'South Africa',
        'population': '4.6 million',
        'fact': 'Known for the iconic Table Mountain.',
        'area': '400 km²',
        'famous_for': ['Table Mountain', 'Robben Island', 'Cape Winelands']
    },
    'paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Called the "City of Light".',
        'area': '105 km²',
        'famous_for': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral']
    },
    'tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Largest metropolitan area in the world.',
        'area': '2,194 km²',
        'famous_for': ['Shibuya Crossing', 'Tokyo Tower', 'Sensō-ji Temple']
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Area: {info['area']}")
    print(f"Fact: {info['fact']}")
    print("Famous for:")
    for landmark in info['famous_for']:
        print(f"  - {landmark}")