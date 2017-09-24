import json

stu = 5
name = "hello"
filename = 'numbers4.json'
with open(filename,"w") as file_obj:
    json.dump(stu,file_obj)
    json.dump(name, file_obj)
    json.dump(True, file_obj)
