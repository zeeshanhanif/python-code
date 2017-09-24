print("First")
a = 5
b = 1
d = []
try:
    c = a/b
    e = d[5]
except Exception as e:
    print("Handle Error == " +str(e))
else:
    print(c)

print("last")

