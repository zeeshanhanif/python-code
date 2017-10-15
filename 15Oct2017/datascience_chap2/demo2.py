from functools import partial

def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)

print(two_to_the(3))
print(two_to_the(6))
print(two_to_the(9))
