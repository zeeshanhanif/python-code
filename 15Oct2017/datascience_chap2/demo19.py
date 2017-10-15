def myfunction(x):
    return x * 3
def doubler(f):
    def g(z):
        return z + f(6)
    return g
myfunc = doubler(myfunction)
print(myfunc)
print(myfunc(2))

