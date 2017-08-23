def fayyaz(noOfCups, sugar=2,elichi=''):
    print("Make Tea")
    print("Preparing "+str(noOfCups)+" cups of Tea")
    print("Adding sugar "+str(sugar)+" spoon")
    if(elichi=='yes'):
        print("Adding Elichi")
    print("Add 1 Tea bag")
    print("Fill cup")
    return {"Cups":noOfCups,"sugar":sugar,"elichi":elichi}


collectTea = fayyaz(4,elichi="yes")
print(collectTea)

