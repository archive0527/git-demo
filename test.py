import random

numbers = []

while True:
        x = random.randint(1, 49)
        if x  not in numbers:
            numbers.append(x) 
            if len(numbers) == 10:
                break

print(numbers)