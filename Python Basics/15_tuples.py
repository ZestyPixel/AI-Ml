#Tuples are immutable
tup = (1, 2, 3, 4, 5, 5, 5)
print(tup[2])

#To create a single value tuple, you need to include a comma after the value since otherwise it is considered as a regular parentheses.

for val in tup:
    print(val)

print(tup.index(5))
print(tup.count(5))