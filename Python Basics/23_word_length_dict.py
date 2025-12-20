words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}
for word in words:
    dict[word] = len(word)

print(dict.items())