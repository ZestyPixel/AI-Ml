#List comprehsension: A concise way to create lists.
#Syntax: [expression for item in iterable if condition]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [item for item in list if item%2==0]

print(list2)

list3 = [item*item for item in range(0,11)]

print(list3)

list4 = ["even" if val%2==0 else "odd" for val in range(0,11)]
print(list4)

words = ["Hello", "World"]
words = [val.upper() for val in words]
print(words)