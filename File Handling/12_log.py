with open("File Handling/log.txt", "a") as file:
    file.write("Program run successfully\n")

with open("File Handling/log.txt", "r") as file:
    print("\nlog entries:")
    for line in file:
        print(line.strip())
