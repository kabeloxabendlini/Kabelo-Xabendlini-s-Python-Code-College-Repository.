# Create a dictionary representing an alien with color and points attributes
alien_0 = {'color': 'green', 'points': 5}

# Print the value associated with the 'color' key
print(alien_0['color'])

# Print the value associated with the 'points' key
print(alien_0['points'])

# Store the value of the 'points' key in a variable called new_points
new_points = alien_0['points']

# Print a message showing how many points were earned
print(f"You just earned {new_points} points!")

# Print the current state of the alien_0 dictionary
print(alien_0)

# Add a new key-value pair for the alien's x-coordinate position
alien_0['x_position'] = 0

# Add a new key-value pair for the alien's y-coordinate position
alien_0['y_position'] = 25

# Print the updated dictionary to show the newly added position information
print(alien_0)

# Create an empty dictionary to store information about an alien
alien_0 = {}

# Add a key-value pair for the alien's color
alien_0['color'] = 'green'

# Add a key-value pair for the alien's points
alien_0['points'] = 5


# Print the dictionary to show its current contents
print("Alien Dictionary:\n")
print(alien_0)

# Create a dictionary with the alien's initial color
alien_0 = {'color': 'green'}

# Print the current color of the alien
print(f"The alien is {alien_0['color']}.")

# Change the value associated with the 'color' key
alien_0['color'] = 'yellow'

# Print the updated color of the alien
print(f"The alien is now {alien_0['color']}.\n")

# Create a dictionary to store the alien's position and speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}

# Print the original horizontal position of the alien
print(f"Original position: {alien_0['x_position']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

# Print the new position of the alien
print(f"New position: {alien_0['x_position']}\n")

# Create a dictionary representing an alien with color and points
alien_0 = {'color': 'green', 'points': 5}

# Print the original dictionary
print(alien_0)

# Delete the 'points' key-value pair from the dictionary
del alien_0['points']

# Print the updated dictionary after deletion
print(alien_0)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)
 # Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)

# ... (20 lines left)

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  # ❌ This will cause a KeyError

# Try to get the value for 'points'; if it doesn't exist, return a default message
point_value = alien_0.get('points', 'No point value assigned.')

# Print the result
print(point_value)