def rotate_and_mask(s: str, n: int) -> str:
    if len(s) != 0:
        shift = n % len(s)
        if shift > 0:
            newS = s[-shift : ] + s[: -shift]
        elif shift < 0:
            newS = s[shift : ] + s[ : shift]
        else:
            newS = s

        vowelsSet = ("a", "e", "i", "o", "u")
        numbersSet = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    
        i = 0
        while i < len(newS):
            for j in range(len(vowelsSet)):
                if newS[i].lower() == vowelsSet[j]:
                    newS = newS[ : i] + "*" + newS[i + 1: ]
                else:
                    for l in range(len(numbersSet)):
                        if newS[i] == numbersSet[l]:
                            newS = newS[ : i] + "#" + newS[i + 1: ]
            i = i + 1

        return newS
    else:
        return "Error: Your line is empty"


myString = ""
print(rotate_and_mask(myString, 54))