# Variable name for if statement (age):
age = 12 

# If statement for the age variable along wity it's conditions:
if age < 4:
    price = 0
# Else If statement's for the age variable along wity it's conditions:
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

# Print out prpmpt for an F - String in the terminal.
print(f"Your admission cost is ${price}.")