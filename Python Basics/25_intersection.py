list1 = input("Enter elements of first list (space-separated): ").split()
list2 = input("Enter elements of second list (space-separated): ").split()

set1 = set(list1)
set2 = set(list2)


if set1.intersection(set2):
    print("The lists have common elements:")
else:
    print("The lists share no common elements.")
