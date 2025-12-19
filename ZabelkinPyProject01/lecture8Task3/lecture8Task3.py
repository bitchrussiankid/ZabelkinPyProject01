import os

if not(os.path.exists("source.txt")):
    with open("source.txt", "w") as file:
        file.write("""first line
second line
third line""")

def copyFile(source, destination):
    copySuccess = False
    try:
        with open(source, "r") as file1:
            with open(destination, "w") as file2:
                for line in file1:
                    file2.write(line)
        print("File copied successfully!")
        copySuccess = True
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission error")
    except Exception as e:
        print("Unavailable error")

    return copySuccess


copyFile("source.txt", "destination.txt")
