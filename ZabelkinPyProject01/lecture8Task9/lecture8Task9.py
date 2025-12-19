def createDataFile(fileName, dataList):
    totalCounter = 0
    numsCounter = 0
    stringCounter = 0
    otherTypeCounter = 0

    with open(fileName, "w") as file:
    
        for item in dataList:
            file.write(f"{item}\n")
            totalCounter += 1
            if isinstance(item, (int, float)):
                numsCounter += 1
            elif type(item) == str:
                stringCounter += 1
            else:
                otherTypeCounter += 1

    print(f"File '{fileName}' created successfully!")
    print(f"Total items: {totalCounter}")
    print(f"Strings: {stringCounter}")
    print(f"Numbers: {numsCounter}")
    
    countsDatasTuple = (totalCounter, numsCounter, stringCounter, otherTypeCounter)
    return countsDatasTuple


dataList = [1, 2, "three", "4", 3.14]
createDataFile("output.txt", dataList)