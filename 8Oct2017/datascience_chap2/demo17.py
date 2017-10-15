import re

myVal = "Hello World!"
a = re.search("[a-z]", myVal)
print(a.group())
