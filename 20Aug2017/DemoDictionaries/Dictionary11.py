stu1 = {
    'name':'Qasim',
    'email':'qasim@gmail.com',
    'languages' : ['C#','Python','JavaScript']
}
stu2 = {'name':'Inzamam','email':'inzamam@gmail.com',
        'languages': ['C#', 'Java', 'JavaScript']
}
stu3 = {'name':'Jaffar','email':'jaffar@gmail.com',
        'languages': ['C#', 'Python', 'PHP']
}

students = [stu1,stu2,stu3]
#print(students)


for stu in students:
    print(stu)
    for key,val in stu.items():
        print("key: ",key," -- Value : ",val)
        if key == 'languages':
            for lang in val:
                print(lang)
    print("")






