# --- Original variables ---
car = 'subaru'
color = 'blue'
age = 25
name = 'Alice'
is_student = True

# --- New variables ---
language = 'Python'
number = 10
hobbies = ['reading', 'gaming', 'cycling']

print("\n--- Tests for equality and inequality with strings ---")
print("Is language == 'Python'? I predict True.")
print(language == 'Python')  # True

print("Is language != 'Java'? I predict True.")
print(language != 'Java')  # True

print("Is language == 'python'? I predict False.")
print(language == 'python')  # False (case-sensitive)

print("Is language != 'Python'? I predict False.")
print(language != 'Python')  # False

print("\n--- Tests using the lower() method ---")
print("Is language.lower() == 'python'? I predict True.")
print(language.lower() == 'python')  # True

print("Is name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True

print("Is name.lower() == 'bob'? I predict False.")
print(name.lower() == 'bob')  # False

print("\n--- Numerical comparisons ---")
print("Is number == 10? I predict True.")
print(number == 10)  # True

print("Is number != 5? I predict True.")
print(number != 5)  # True

print("Is age > 30? I predict False.")
print(age > 30)  # False

print("Is age < 30? I predict True.")
print(age < 30)  # True

print("Is age >= 25? I predict True.")
print(age >= 25)  # True

print("Is number <= 5? I predict False.")
print(number <= 5)  # False

print("\n--- Tests with 'and' and 'or' ---")
print("Is age > 20 and is_student == True? I predict True.")
print(age > 20 and is_student == True)  # True

print("Is age < 20 or is_student == True? I predict True.")
print(age < 20 or is_student == True)  # True

print("Is age < 20 and is_student == False? I predict False.")
print(age < 20 and is_student == False)  # False

print("Is color == 'red' or car == 'bmw'? I predict False.")
print(color == 'red' or car == 'bmw')  # False

print("\n--- Test whether an item is in a list ---")
print("Is 'gaming' in hobbies? I predict True.")
print('gaming' in hobbies)  # True

print("Is 'swimming' in hobbies? I predict False.")
print('swimming' in hobbies)  # False

print("\n--- Test whether an item is not in a list ---")
print("Is 'running' not in hobbies? I predict True.")
print('running' not in hobbies)  # True

print("Is 'reading' not in hobbies? I predict False.")
print('reading' not in hobbies)  # False