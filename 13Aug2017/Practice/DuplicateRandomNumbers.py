from random import randint
max = int(input("Enter max number"))
count = max+1
mylist = []

while len(mylist) != count:
    num = randint(0, max)
    if( num not in mylist):
        mylist.append(num)

print (mylist)