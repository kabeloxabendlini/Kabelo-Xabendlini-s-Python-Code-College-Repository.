# Create a list of favorite foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# Make a copy of the list using slicing
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


# Now, assign the list directly (no copy, just a reference)
my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't create a new list, friend_foods points to the same list as my_foods
friend_foods = my_foods

# Add new items to both lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
