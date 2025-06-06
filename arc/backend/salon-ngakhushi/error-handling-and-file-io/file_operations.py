def read_file():
    try:
        file= open("fileoperations.txt", "r")
        content = file.read()
        print("\nReading file content:")
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not found: Read an existing file.")

def write_file():
    with open("fileoperations.txt", "w") as file:
        file.write("This is a writing file operation test.\n")
        file.write("This content has been writen in the file through write operation.\n")
    print("File written successfully.")

def append_file():
    with open("fileoperations.txt", "a") as file:
        file.write("This line was appended using the append operation.\n")
    print("Example of append.")


# write_file()
read_file()
# append_file()
# read_file()
