import os

if not(os.path.exists("text.txt")):
    with open("text.txt", "w") as file:
        file.write("""Hello world
Python is great
Hello again
World of python""")


def findWordInFile(fileName, word):
    with open("text.txt", "r") as file:
        listLinesNumsWithWords = []
        lineNumber = 0
        listOfLinesWithWords = {}
        for line in file:
            lineNumber += 1
            lowerLine = line.lower()
            if word.lower() in lowerLine:
                listLinesNumsWithWords.append(lineNumber)
                listOfLinesWithWords[lineNumber] = line.replace("\n", "")
                
        print(f"Line numbers with a word '{word}': {listLinesNumsWithWords}")
        print(f"Words '{word}' found in text: {len(listLinesNumsWithWords)}\n")
        for i in listOfLinesWithWords:
            print(f"line {i}: {listOfLinesWithWords[i]}")
        

   
findWordInFile("text.txt", "python")