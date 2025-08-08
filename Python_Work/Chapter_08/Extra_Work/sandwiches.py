def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print()  # Blank line for readability

# Call the function with different numbers of items
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato")
make_sandwich("peanut butter", "jelly", "banana", "honey")