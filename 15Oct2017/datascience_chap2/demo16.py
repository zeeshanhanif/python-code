docs = [(1,"a"),(2,"b","rer"),(3,"c"),(4,"d")]

a,b = zip(*docs)

print(a)
print(b)