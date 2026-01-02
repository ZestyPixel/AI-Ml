try:
    with open("File Handling/data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
