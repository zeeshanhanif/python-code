print("First")
a = 5
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
else:
    print(c)

print("last")

