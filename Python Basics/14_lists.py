list = [1, 2, 3, 4, 5, 110.2]
print(len(list))
print(type(list))
print(list[0::1])

list.append(5)
list.sort()
print(list)
list.insert(0, "abc")   
list.reverse()
print(list)