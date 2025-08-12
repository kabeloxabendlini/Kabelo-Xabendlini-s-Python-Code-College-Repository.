guest_names = []

print("Enter guest names. Type 'quit' to finish.")

while True:
    name = input("Enter a guest name: ")
    if name.lower() == 'quit':
        break
    guest_names.append(name)

# Write all guest names to the file, each on a new line
with open('guest_book.txt', 'w') as file:
    for guest in guest_names:
        file.write(guest + '\n')

print("Guest names saved to guest_book.txt.")