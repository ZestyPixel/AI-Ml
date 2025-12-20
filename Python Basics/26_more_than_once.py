lst = input("Enter elements: ").split()

for i in set(lst):
    if lst.count(i) > 1:
        print(i)