users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
 print(f"\nUsername: {username}")
 full_name = f"{user_info['first']} {user_info['last']}"
 location = user_info['location']
 print(f"\tFull name: {full_name.title()}")
 print(f"\tLocation: {location.title()}")

 # Define a dictionary with user information
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Loop through all key-value pairs in the dictionary
for key, value in user_0.items():
    # Print the key
    print(f"\nKey: {key}")
    # Print the value associated with the key
    print(f"Value: {value}")