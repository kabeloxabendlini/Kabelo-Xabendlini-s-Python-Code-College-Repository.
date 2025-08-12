print("Welcome to the addition calculator!")
print("Enter 'quit' at any time to exit.")

while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'quit':
        break

    num2 = input("Enter the second number: ")
    if num2.lower() == 'quit':
        break

    try:
        number1 = int(num1)
        number2 = int(num2)
    except ValueError:
        print("Oops! Please enter valid numbers only.")
        continue  # Skip to next iteration to retry

    total = number1 + number2
    print(f"The sum of {number1} and {number2} is {total}.\n")

print("Thanks for using the calculator. Goodbye!")