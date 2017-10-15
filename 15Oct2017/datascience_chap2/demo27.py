def f2(x, y):
    return x + y

def f3(x, y,z):
    return x + y +z

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
#print(g(1, 2,3)) # 6
print(g(1, 2)) # 6
print("=======")

g1 = doubler_correct(f3)
print(g1(1, 2,3)) # 6