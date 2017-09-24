import json

stu = {
    "name":"Qasim",
    "age": 21
}

filename = 'numbers2.json'
with open(filename, 'w') as f_obj:
    json.dump(stu, f_obj)