import random

numbers = []
for _ in range(6):
    n = random.randint(1, 60)
    numbers.append(n)

numbers.sort()

for num in numbers:
    print(num, end=" ")

