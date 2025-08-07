# 7-8. Deli

# List of sandwich orders
sandwich_orders = ['tuna', 'chicken mayo', 'beef', 'veggie', 'egg']
finished_sandwiches = []

# Process each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Final list of finished sandwiches
print("\nAll the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")