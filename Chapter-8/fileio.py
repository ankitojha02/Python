# f = open("file.txt") # By default, the file is opened in read mode
# data = f.read()
# print(data)
# f.close()

st = "Hello, this is a sample text to demonstrate file operations in Python."

f = open("myfile.txt", "w")  # Open the file in write mode
f.write(st)  # Write the string to the file
f.close()  # Close the file

#f.readlines()  # This function reads all the lines of the file and returns them as a list of strings. Each string in the list represents a line in the file, including the newline character at the end of each line.
# r - Open the file in read mode (default mode). You can read the contents of the file using methods like read(), readline(), or readlines().
# w - Open the file in write mode. If the file already exists, its contents will be truncated (deleted) before writing. If the file does not exist, a new file will be created.
# a - Open the file in append mode. If the file already exists, new data will be added to the end of the file. If the file does not exist, a new file will be created.
# x - Open the file in exclusive creation mode. If the file already exists, the operation will fail. If the file does not exist, a new file will be created.

