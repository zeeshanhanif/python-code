document = "That the quick brown fox jumps over the lazy dog"

word_counts = {}
for word in document.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)