def sum_and_product(x, y):
    return (x + y),(x * y), (x*y)

sp = sum_and_product(2, 3) # equals (5, 6)
s, p,t = sum_and_product(5, 10) # s is 15, p is 50

print(sp)
print(s)
print(p)
print(t)