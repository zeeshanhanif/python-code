def myFunction(count):
    print("count",count)
    for x in range(count):
        yield x

myval = myFunction(10)
print(myval)
print(next(myval))
print(next(myval))
print(next(myval))

#for z in myval:
#    print(z)