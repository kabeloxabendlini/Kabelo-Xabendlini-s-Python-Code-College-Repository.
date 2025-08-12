import lottery_analysis

# The pool to draw from: 10 numbers + 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Your ticket: pick 4 unique items (fixed for this simulation)
my_ticket = lottery_analysis.sample(items, 4)
print(f"My ticket: {my_ticket}")

draws = 0
while True:
    draws += 1
    draw = lottery_analysis.sample(items, 4)
    if sorted(draw) == sorted(my_ticket):
        print(f"Winning combination {draw} found after {draws} draws!")
        break