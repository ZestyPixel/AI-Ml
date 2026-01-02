f = open("sample.txt", "r", encoding = "utf-8") # File object. We use encoding utf-8 to read special characters.
a = f.read()
print(a)
f.close() #Always close file after using it.

#read() method reads the whole file and returns it as a single string.
#readline() method reads a single line from the file.
#readlines() method reads all the lines of a file and returns them as a list of strings.