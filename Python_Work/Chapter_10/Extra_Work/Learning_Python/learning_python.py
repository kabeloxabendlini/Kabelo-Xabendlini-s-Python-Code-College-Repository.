# Open and read the entire file at once
with open('learning_python.txt', 'r') as file:
    contents = file.read()

print("Reading entire file at once:")
print(contents)

print("\nReading the file line by line:")

# Open again, read lines into a list, then print line by line
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line, end='')  # end='' to avoid double newlines