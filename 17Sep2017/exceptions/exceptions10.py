print("First")
a = 5
b = 2
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handel ZeroDivisionError")
except Exception as e:
    print("Handle Error == " +str(e))
else:
    print(c)

print("last")

