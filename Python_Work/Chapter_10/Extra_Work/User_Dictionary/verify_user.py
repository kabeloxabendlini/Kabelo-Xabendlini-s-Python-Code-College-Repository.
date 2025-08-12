import json

filename = 'username.json'

def get_new_username():
    username = input("What is your username? ")
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    try:
        with open(filename, 'r') as file:
            username = json.load(file)
    except FileNotFoundError:
        username = get_new_username()

    else:
        print(f"Is your username '{username}'? (yes/no)")
        answer = input().lower()
        if answer != 'yes':
            username = get_new_username()

    print(f"Welcome back, {username}!")

if __name__ == "__main__":
    greet_user()
