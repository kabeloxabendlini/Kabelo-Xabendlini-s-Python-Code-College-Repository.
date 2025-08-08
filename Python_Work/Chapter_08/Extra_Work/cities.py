def describe_city(city, country="South Africa"):
    print(f"{city} is in {country}.")

# Calls with default country
describe_city("Cape Town")
describe_city("Johannesburg")

# Call with a different country
describe_city("Tokyo", "Japan")