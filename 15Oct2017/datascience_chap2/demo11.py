from functools import partial

def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0
    #return True

xs = [1, 2, 3, 4]

x_evens = filter(is_even, xs) # same as above
print(list(x_evens))
#list_evener = partial(filter, is_even) # *function* that filters a list
#x_evens = list_evener(xs)