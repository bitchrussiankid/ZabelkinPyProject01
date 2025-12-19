import os

def createAndWrite(fileName, content, rewrite: bool):
    if rewrite == False:
        if not(os.path.exists(fileName)):
            with open(fileName, "w") as file:
                file.write(content)
    else:
        with open(fileName, "w") as file:
                file.write(content)

createAndWrite("file1.txt", """Hello from file 1
This is line 2
End of file 1""", False)

createAndWrite("file2.txt", """Hello from file 2
This is line B
End of file 2""", False)

with open("merged.txt", "w") as fileMerged:
    with open("file1.txt", "r") as file1:
        for line in file1:
            fileMerged.write(line)
        fileMerged.write("\n--- Merged ---\n")
    with open("file2.txt", "r") as file2:
        for line in file2:
            fileMerged.write(line)
    print("Files merged successfully!")

with open("merged.txt", "r") as file:
    for line in file:
        print(line.strip())