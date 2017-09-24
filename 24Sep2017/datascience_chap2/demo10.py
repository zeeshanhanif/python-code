word_count = {
    "hello":4,
    "world":6,
    "bye":1,
    "working":3
}
x = sorted(word_count.items())
y = sorted(word_count.values())

z = sorted(word_count.items(), key= [lambda a,b:b])
print(x)
print(y)
print(z)
