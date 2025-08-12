import json

with open('favorite_number.json', 'r') as file:
    number = json.load(file)

print(f"I know your favorite number! It’s {number}.")