# Modified dictionary: each person has a list of favorite numbers
favorite_numbers = {
    'alice': [7, 13],
    'brian': [42],
    'cynthia': [11, 8, 27],
    'david': [23, 5],
    'ella': [5, 17]
}

# Loop through and print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")