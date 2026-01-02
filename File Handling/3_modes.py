# Different modes to open a file in Python
# "r" - Read mode (default): Opens a file for reading. The file pointer is placed at the beginning of the file.
# "w" - Write mode: Opens a file for writing. If the file already exists, it will overwrite the existing content. If the file does not exist, it will be created.
# "a" - Append mode: Opens a file for appending. The file pointer is at the end of the file if it exists. If the file does not exist, it will be created.
# "b" - Binary mode: Used to handle non-text files (like images or executable files). It can be combined with other modes (e.g., "rb" for reading a binary file, "wb" for writing a binary file).
# "x" - Exclusive creation mode: Creates a new file and opens it for writing. If the file already exists, the operation fails. This is for explicitly creating a new file.
# "t" - Text mode (default): Used to handle text files. It can be combined with other modes (e.g., "rt" for reading a text file, "wt" for writing a text file).
# + - Update mode: Opens a file for both reading and writing. It can be combined with other modes (e.g., "r+" for reading and writing, "w+" for writing and reading).
# We use r+ if we want to read and write to a file without truncating it. For example, to read the existing content and then append new content.
#The file must exist when using "r+" mode; otherwise, it will raise an error. Pointer is at the beginning of the file.

#We use w+ if we want to write and read to a file. It will truncate the file to zero length if it exists or create a new file if it does not exist. Pointer is at the beginning of the file.