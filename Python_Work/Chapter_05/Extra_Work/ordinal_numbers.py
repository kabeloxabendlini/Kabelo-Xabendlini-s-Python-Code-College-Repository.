numbers = list(range(1, 10))  # Numbers 1 through 9

for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{number}{suffix}")