# Open the file and read line by line
with open('learning_python.txt', 'r') as file:
    for line in file:
        # Replace 'Python' with 'C'
        modified_line = line.replace('Python', 'C')
        print(modified_line, end='')  # end='' to avoid extra newlines