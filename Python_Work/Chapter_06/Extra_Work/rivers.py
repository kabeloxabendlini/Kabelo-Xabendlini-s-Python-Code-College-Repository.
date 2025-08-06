# Dictionary of rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'danube': 'germany'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
# Print the name of each river
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries included in the dictionary:")
# Print the name of each country
for country in rivers.values():
    print(f"- {country.title()}")