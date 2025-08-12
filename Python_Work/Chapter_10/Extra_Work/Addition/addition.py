try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Try converting inputs to integers
    number1 = int(num1)
    number2 = int(num2)

    total = number1 + number2
    print(f"The sum of {number1} and {number2} is {total}.")

except ValueError:
    print("Oops! One or both inputs were not valid numbers. Please enter numbers only.")