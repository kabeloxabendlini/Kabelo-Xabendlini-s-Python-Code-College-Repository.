filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    
    except FileNotFoundError:
        pass  # Fail silently, do nothing if file not found