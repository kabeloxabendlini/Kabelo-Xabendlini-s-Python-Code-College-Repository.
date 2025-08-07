# 7-9. No Pastrami

# Initial sandwich orders (with 'pastrami' appearing at least 3 times)
sandwich_orders = [
    'tuna', 'pastrami', 'chicken mayo', 'pastrami',
    'beef', 'veggie', 'pastrami', 'egg'
]
finished_sandwiches = []

# Inform the customer that there's no pastrami
print("Sorry, the deli has run out of pastrami.\n")

# Remove all occurrences of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Final list of finished sandwiches
print("\nAll the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")