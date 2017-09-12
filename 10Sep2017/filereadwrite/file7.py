
with open('demo1.txt','r+') as fileObj:
    fileObj.write("I love programming!\n")

    fileObj.seek(0)
    content = fileObj.readlines()
    print(content)

