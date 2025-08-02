# List of usernames (initially filled, then emptied to test the condition)
usernames = ['Samkelo', 'Bantu', 'Kabelo', 'Werner', 'Zuko', 'Thozie']
# To test the empty list condition, uncomment the line below:
# usernames = []

# Check if the list is not empty
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")