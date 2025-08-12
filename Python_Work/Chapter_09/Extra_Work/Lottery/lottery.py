import lottery

# List containing 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 unique items
winning_combination = lottery.sample(items, 4)

print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_combination}")
