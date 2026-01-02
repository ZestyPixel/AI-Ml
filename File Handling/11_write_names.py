with open("File Handling/names.txt", "w") as file:
    for i in range(5):
        name = input("Enter a name: ")
        file.write(name + "\n")

with open("File Handling/names.txt", "r") as file:
    print("\nNames in file:")
    for line in file:
        print(line.strip())

