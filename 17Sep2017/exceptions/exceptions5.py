print("First")
a = 5
b = 0
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
else:
    print(c)

print("last")

