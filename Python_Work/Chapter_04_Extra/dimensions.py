# Create a tuple named 'dimensions'
dimensions = (200, 50)

# Access and print the first element of the tuple
print("Access and print the first element of the tuple")
print(dimensions[0])  # Output: 200

# Access and print the second element of the tuple
print("\nAccess and print the second element of the tuple")
print(dimensions[1])  # Output: 50


# Loop through the original dimensions and print each value
print("\nLoop through the original dimensions and print each value;")
for dimension in dimensions:
    print(dimension)

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

# Reassign the tuple to new values
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


# Try to change the first element (this will cause an error!)
dimensions[0] = 250  # ERROR: tuples do not support item assignment