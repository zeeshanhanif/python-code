from functools import reduce
def multiply(x, y):
    return x * y
xs = [1, 2, 3, 4]
x_product = reduce(multiply, xs)

print(x_product)