# Collection of unique elements
# Only immutable types can be added to a set but the set itself is mutable.

s = {1, 2, 3, 3, 4} #Even though 3 is repeated, it will only appear once in the set.
s2 = {5, 6, 7, 8, 9, 10}
print(s)

s3=set() #To make an empty set

s.add(5)
s.remove(2)
print(s)
print(s.pop())

print(s.union(s2))
print(s.intersection(s2))
s.clear()


