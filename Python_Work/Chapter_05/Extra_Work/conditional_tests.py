# Variable for testing
car = 'subaru'
color = 'blue'
age = 25
name = 'Alice'
is_student = True

# Test 1 - should be True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

# Test 2 - should be False
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

# Test 3 - should be True
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')  # True

# Test 4 - should be False
print("\nIs color == 'red'? I predict False.")
print(color == 'red')  # False

# Test 5 - should be True
print("\nIs age > 20? I predict True.")
print(age > 20)  # True

# Test 6 - should be False
print("\nIs age < 20? I predict False.")
print(age < 20)  # False

# Test 7 - should be True
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True

# Test 8 - should be False
print("\nIs name == 'ALICE'? I predict False.")
print(name == 'ALICE')  # False (case-sensitive)

# Test 9 - should be True
print("\nIs is_student == True? I predict True.")
print(is_student == True)  # True

# Test 10 - should be False
print("\nIs is_student == False? I predict False.")
print(is_student == False)  # False