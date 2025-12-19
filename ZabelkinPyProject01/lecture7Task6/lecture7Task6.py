import os

def createAndWrite(file, content, rewrite: bool):
    if rewrite == False:
        if not(os.path.exists(file)):
            with open(file, "w") as file:
                file.write(content)
    else:
        with open(file, "w") as file:
                file.write(content)

def printFile(file):
    with open(file, "r") as file:
        for line in file:
            print(line.strip())



createAndWrite("source.txt", """First line
Second line
Third line""", False)

sourceContent = ""
with open("source.txt", "r") as file:
    sourceContent = file.read()
    print("File copied successfully!")

createAndWrite("destination.txt", sourceContent, True)

printFile("source.txt")
printFile("destination.txt")