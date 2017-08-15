current_number = int(input("Enter number "))
num = 0

while num < current_number:
    num += 1
    if num == 3:
        continue
    print(num)


print("Final",num)
