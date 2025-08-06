# Dictionary of people who already took the poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who should take the poll
people_to_poll = ['jen', 'sarah', 'kabelo', 'alice', 'phil']

# Loop through the list and respond accordingly
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take our favorite programming language poll!")