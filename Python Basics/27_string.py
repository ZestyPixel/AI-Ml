sentence = input("Enter a string: ")
list = []
for char in sentence:
    if char not in list:
        list.append(char)

print(list)