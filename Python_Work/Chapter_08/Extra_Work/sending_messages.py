def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)  # Remove from messages
        print(current_message)
        sent_messages.append(current_message)  # Add to sent_messages

# List of short text messages
text_messages = [
    "Hey, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "See you later!"
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nMessages still in inbox:", text_messages)
print("Messages sent:", sent_messages)