# f = open("file.txt") # By default, the file is opened in read mode
# data = f.read()
# print(data)
# f.close()

st = "Hello, this is a sample text to demonstrate file operations in Python."

f = open("myfile.txt", "w")  # Open the file in write mode
f.write(st)  # Write the string to the file
f.close()  # Close the file

#f.readlines()  # This function reads all the lines of the file and returns them as a list of strings. Each string in the list represents a line in the file, including the newline character at the end of each line.
