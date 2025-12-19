import os

if not(os.path.exists("example.txt")):
    with open("example.txt", "w") as file:
        file.write("""first line
second line
third line
fourth line
fifth line""")

def countLine(fileName):
    try:
        counter = 0
        with open(fileName, "r") as file:
            for line in file:
                counter += 1               
    except FileNotFoundError:
        print(f"File {fileName} are not found!")
        counter = -1
    except Exception as e:
        print("Unavailable error")
        counter = -1

    return counter


countLines = countLine("example.txt")
if countLines != -1:
    print(f"File 'example.txt' has {countLines} lines")