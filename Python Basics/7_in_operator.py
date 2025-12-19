string = "hello"

if "e" in string:
    print("The letter 'e' is in the string.")

for i in range(1, 10, 2): #Printing all odd numbers
    print(i)

ans = 0
for ch in string:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        ans += 1

print("Ans = ",ans)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

for name, subject in info:
    print(name, subject)