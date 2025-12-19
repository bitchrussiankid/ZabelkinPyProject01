def sumNumbersChecker(numbers):
    try:
        if len(numbers) >= 2:
            listMidpointIndex = len(numbers) // 2

            evenNumbers = numbers[0 : listMidpointIndex : 2]
            print(evenNumbers)

            if listMidpointIndex % 2 == 1:
                oddNumbers = numbers[listMidpointIndex : : 2]
                print(oddNumbers)
            else: 
                oddNumbers = numbers[listMidpointIndex + 1 : : 2]
                print(oddNumbers)

            allNumbers = evenNumbers + oddNumbers

        else:
            allNumbers = [25, 25]
            print("Error: list is too short!")

        if sum(allNumbers) > 50:
            print("Large sum")
        else: 
            print("Small sum")
        
    except TypeError:
        print("Error: the value is not a list or number")
    except Exception as e:
        print("Unknown error")


numbers = [15, 231]
sumNumbersChecker(numbers)