import json

data = 0

filename = 'numbers4.json'
with open(filename) as file_obj:
    data = json.load(file_obj)

print(data)
