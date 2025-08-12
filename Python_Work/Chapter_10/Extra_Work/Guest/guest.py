# Prompt the user for their name
name = input("Please enter your name: ")

# Open the file in write mode and write the name
with open('guest.txt', 'w') as file:
    file.write(name + '\n')

print(f"Thanks, {name}! Your name has been saved.")