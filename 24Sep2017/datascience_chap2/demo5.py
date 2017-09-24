from collections import Counter
c = Counter([0, 1, 2, 0])
print(c)
mostCommon = c.most_common(1)
print(mostCommon)

a,b = mostCommon[0]
print(a)
print(b)
