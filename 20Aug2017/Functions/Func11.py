def fayyaz(itemList):
    itemList[0] = "Pulaoo"
    for i in itemList:
        print("Buying "+i)

myItems = ["Briyani","Anday wala burger","Nihari","Lassi"]
print(myItems)
fayyaz(myItems[:])
print(myItems)