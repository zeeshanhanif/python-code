squares = []

for value in range(1,11):
    squares.append(value**2)


print(squares)

minVal = min(squares)
maxVal = max(squares)
sumVal = sum(squares)
countVal = len(squares)

print("Min",minVal)
print("Max",maxVal)
print("Sum",sumVal)
print("Count",countVal)
print("Average",sumVal/countVal)


