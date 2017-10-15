document = "That the quick brown fox jumps quick over fox the lazy dog fox Jumps"

word_counts = {}
for word in document.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
print(word_counts.items())

wc = sorted(word_counts.items(),key=lambda i: i[1],reverse=True)
print(wc)