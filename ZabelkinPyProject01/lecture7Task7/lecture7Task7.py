import os

def createAndWrite(fileName, content, rewrite):
    if rewrite == False:
        if not(os.path.exists(fileName)):
            with open(fileName, "w") as file:
                file.write(content)
    else:
         with open(fileName, "w") as file:
                file.write(content)

createAndWrite("emails.txt","""john@gmail.com
alice@yahoo.com
bob@gmail.com
carol@hotmail.com
dave@gmail.com
eve@yahoo.com""", False)

gmailCount = 0
with open("emails.txt", "r") as file1:
    with open("gmailAddresses.txt", "w") as file2:
        for line in file1:
            if "@gmail.com" in line:
                gmailCount += 1
                file2.write(line)

print("Gmail addresses saved to file\n")

print(f"{gmailCount} gmail addresses found:")
with open("gmailAddresses.txt", "r") as file:
    for line in file:
        print(line.strip())