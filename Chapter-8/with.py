# with statement automatically closes the file after the block of code is executed
with open("file.txt", "r") as f:
    print(f.read())