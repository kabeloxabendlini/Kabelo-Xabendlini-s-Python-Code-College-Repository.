# List of magician names
magicians = ['alice', 'david', 'carolina']

# Loop through each name in the list
for magician in magicians:
    # Print the magician's name
    print(magician)

    # Print a personalized message for each magician
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")  # \n adds a blank line for readability

# Print a final thank-you message after the loop ends
print("Thank you, everyone. That was a great magic show!")
