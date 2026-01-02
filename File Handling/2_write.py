f = open("write_sample.txt", "w", encoding="utf-8")  # Open file in write mode
f.write("Hello, World!\n")  # Write a line to the file
f.write("This is a sample text file.\n")  # Write another line
f.close()  # Always close the file after writing

# The write() method writes a string to the file. If the file already exists, it will overwrite the existing content.
# To append to an existing file without overwriting, use "a" mode instead of "w" mode.
# If the file does not exist, it will be created.
# If you want to write multiple lines at once, you can use the writelines() method with a list of strings.