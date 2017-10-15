from functools import partial
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
list_doubler = partial(map, double)

print(list(list_doubler(xs)))




