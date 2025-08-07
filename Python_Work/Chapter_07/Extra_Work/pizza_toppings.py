# 7-4. Pizza Toppings

print("Enter 'quit' when you are finished adding toppings.")

while True:
    topping = input("Enter a pizza topping: ")

    if topping.lower() == 'quit':
        print("Thank you! We're preparing your pizza.")
        break
    else:
        print(f"I'll add {topping} to your pizza.")