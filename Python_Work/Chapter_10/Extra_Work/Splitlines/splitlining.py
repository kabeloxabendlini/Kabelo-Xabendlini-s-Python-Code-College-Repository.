with open('learning_python.txt', 'r') as file:
    contents = file.read()

for line in contents.splitlines():
    print(line.replace('Python', 'C'))