prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#################################### Line 1 - 11 ###############################

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#################################### Line 15 - 16 ###############################
