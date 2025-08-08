def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

# Original list of messages
text_messages = [
    "Hey, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy Birthday!",
    "See you later!"
]

sent_messages = []

# Pass a copy of text_messages using list slicing [:]
send_messages(text_messages[:], sent_messages)

print("\nOriginal messages:", text_messages)
print("Sent messages:", sent_messages)