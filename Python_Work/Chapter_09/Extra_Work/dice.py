import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(result)

# 6-sided die rolled 10 times
six_sided = Die()
print("6-sided die rolls:")
for _ in range(10):
    six_sided.roll_die()

print("\n10-sided die rolls:")
# 10-sided die rolled 10 times
ten_sided = Die(10)
for _ in range(10):
    ten_sided.roll_die()

print("\n20-sided die rolls:")
# 20-sided die rolled 10 times
twenty_sided = Die(20)
for _ in range(10):
    twenty_sided.roll_die()