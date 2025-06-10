with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("This is the first line.\n")

with open('file.txt', 'a', encoding='utf-8') as f:
    f.write("This is an appended line.\n")

with open('file.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)


with open('file.txt', 'w+', encoding='utf-8') as f:
    f.write("This is the first line.\n")
    
    # Move pointer to the end of the file
    f.seek(0, 2)  # 0 offset, 2 means from the end
    
    # Write (append) new content
    f.write("This is an appended line using seek.\n")
    
    # Go back to the start to read everything
    f.seek(0)
    content = f.read()
    print(content)
