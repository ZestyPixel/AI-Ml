list1 = list(map(int, input("Enter list elements seperated with spaces: ").split()))
print(list1)

list2 = list(map(int, input("Enter list elements seperated with spaces: ").split()))
print(list2)

merge = list1 + list2

merge.sort()

print(merge)