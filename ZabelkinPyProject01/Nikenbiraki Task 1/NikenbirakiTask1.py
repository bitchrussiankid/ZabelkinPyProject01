import random

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def randomizer(z):
    x = random.randint(0, z)
    return x

z = len(myList) - 1
for _ in range(len(myList)):
    y = randomizer(z)
    print(myList[y])
    myList[y] = myList[-1]
    del(myList[-1])
    z = z - 1