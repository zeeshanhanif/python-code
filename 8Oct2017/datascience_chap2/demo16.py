import random

a = random.choice(range(10))
print(a)


four_with_replacement = [
    x
    for x in range(4)]

print(four_with_replacement)


four_with_replacement1 = [
    random.choice(range(10))
    for _ in range(4)]

print(four_with_replacement1)