import json

stu = {}
filename = 'numbers2.json'
with open(filename) as f_obj:
    stu = json.load(f_obj)

print(stu);
print(stu["name"]);