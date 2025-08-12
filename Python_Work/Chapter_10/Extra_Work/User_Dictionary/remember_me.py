import json

filename = 'user_info.json'

def get_user_info():
    user_info = {}
    user_info['username'] = input("Enter your username: ")
    user_info['favorite_color'] = input("Enter your favorite color: ")
    user_info['hobby'] = input("Enter your hobby: ")
    return user_info

def save_user_info(user_info):
    with open(filename, 'w') as file:
        json.dump(user_info, file)

def load_user_info():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def main():
    user_info = load_user_info()

    if user_info:
        print("\nWelcome back! Here's what I remember about you:")
        for key, value in user_info.items():
            print(f"- Your {key.replace('_', ' ')} is {value}.")
    else:
        user_info = get_user_info()
        save_user_info(user_info)
        print("\nThanks! I've saved your information.")

if __name__ == "__main__":
    main()