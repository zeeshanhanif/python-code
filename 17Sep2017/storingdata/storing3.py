import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers3.json'
with open(filename, 'w') as f_obj:
    f_obj.write(str(numbers))