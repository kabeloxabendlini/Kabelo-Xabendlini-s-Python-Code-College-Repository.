# List of player names
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print slices of the list with descriptive formatting
print(f"List: {players[0:3]}")  # ['charles', 'martina', 'michael']
print(f"List: {players[1:4]}")  # ['martina', 'michael', 'florence']
print(f"List: {players[:4]}")   # ['charles', 'martina', 'michael', 'florence']
print(f"List: {players[2:]}")   # ['michael', 'florence', 'eli']

# Print a message and then the first three players with names capitalized
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
