import os

if not(os.path.exists("notes.txt")):
    with open("notes.txt", "w") as file:
        file.write("""My notes:
1. Buy milk
2. Call mom""")


with open("notes.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    if not("Learn Python" in content):
        file.write("\n3. Learn Python")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)