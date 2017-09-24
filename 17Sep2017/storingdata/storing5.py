import json

data = []
filename = 'numbers.json'
with open(filename) as f_obj:
    data = json.load(f_obj)

print(data);
print(data[1]);