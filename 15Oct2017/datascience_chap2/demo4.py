from functools import partial

def exp(base, power):
    return base ** power

two_to_the = partial(exp,power=3)

print(two_to_the(5))
