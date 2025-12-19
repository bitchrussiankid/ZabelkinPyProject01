import os


if not(os.path.exists("example.txt")):
    with open("example.txt", "w") as file:
        file.write("""Hello, World!
This is a test file.
Python is awesome.
Working with files is fun.""")


with open("example.txt", "r") as file:
    content = file.read()
    print(content)