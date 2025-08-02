# Current users already registered
current_users = ['John', 'Alice', 'Kabelo', 'Emma', 'Samantha']

# New users trying to register (some names already used)
new_users = ['emMa', 'Michael', 'john', 'Liam', 'sarah']

# Create a lowercase version of current_users for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Check each new username
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different one.")
    else:
        print(f"Great! The username '{new_user}' is available.")