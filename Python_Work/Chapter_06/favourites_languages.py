favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

# Loop through only the keys (names) in the dictionary
for name in favorite_languages.keys():
    # Print each name with the first letter capitalized
    print(name.title())
# Loop through each key-value pair in the dictionary
for name, language in favorite_languages.items():
    # Print a nicely formatted message
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Access Sarah's favorite language, capitalize the first letter
language = favorite_languages['sarah'].title()

# Print a formatted message showing Sarah's favorite language
print(f"Sarah's favorite language is {language}.")

# List of friends
friends = ['phil', 'sarah']

# Loop through all names in the dictionary
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    # If the person is in the friends list, print a personalized message
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Check if 'erin' is not one of the keys (names) in the dictionary
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Loop through all the names (keys) in the dictionary, sorted alphabetically
for name in sorted(favorite_languages.keys()):
    # Print a thank-you message for each person
    print(f"{name.title()}, thank you for taking the poll.")
# Print a message before listing the languages
print("The following languages have been mentioned:\n")

# # Loop through all the values (languages) in the dictionary
for language in favorite_languages.values():
    # Print each language with the first letter capitalized
    print(language.title())
# # Loop through the set of unique favorite languages
for language in set(favorite_languages.values()):
    # Print each language with the first letter capitalized
    print(language.title())

# Create a dictionary storing people's favorite programming languages
favorite_languages = {
 'jen': ['python', 'rust'],
 'sarah': ['c'],
 'edward': ['rust', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
 print(f"\n{name.title()}'s favorite languages are:")
 for language in languages:
    print(f"\t{language.title()}")
