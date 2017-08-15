value = int(input("Enter value? "))
check = True
num = 2
while num<=value/2:
    if(value % num ==0):
        check = False
        break
    num +=1
if check:
    print("This is Prime Number.")
else:

    print("This isn't Prime Number.")