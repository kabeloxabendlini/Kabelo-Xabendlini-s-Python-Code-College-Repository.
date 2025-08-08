def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and it will have the message: '{message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Any size with a different message
make_shirt(size="Small", message="Code Every Day!")