with open('learning_python.txt') as file:
    contents = file.read()

for line in contents.splitlines():
    print(line)