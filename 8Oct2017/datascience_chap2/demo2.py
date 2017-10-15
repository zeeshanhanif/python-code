from collections import defaultdict
document = "That the quick brown fox jumps over the lazy dog"

word_counts = defaultdict(int)
for word in document.split():
    word_counts[word] += 1

print(word_counts)