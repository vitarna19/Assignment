from collections import OrderedDict

n = int(input("Enter number of words: "))
word_count = OrderedDict()

for _ in range(n):
    word = input()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(*word_count.values())
