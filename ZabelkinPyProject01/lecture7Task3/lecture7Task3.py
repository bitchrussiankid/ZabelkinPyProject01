import os

if not(os.path.exists("poem.txt")):
    with open("poem.txt", "w") as file:
        file.write("""Roses are red,
Violets are blue,
Python is fun,
And so are you!""")

lineCount = 0
with open("poem.txt", "r") as file:
    content = file.read()
    print(content)

    file.seek(0)

    for line in file:
        lineCount += 1
        print((f"Line {lineCount}: {line}").strip())

    print(f"The file contains {lineCount} lines")