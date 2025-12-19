import os
import time

if not(os.path.exists("cache.txt")):
    with open("cache.txt", "w") as file:
        pass


def cacheToFile(func):
    def wrapper(*args, **kwargs):
        resultInCache = False
        with open("cache.txt", "a+") as file:
            file.seek(0)
            for line in file:
                if f"{args}_{kwargs}" in line.split(":")[0]:
                    lineForResult = line.split(":")
                    result = int(lineForResult[1])                   
                    resultInCache = True
                    print("result in cache")
                    break
            if resultInCache == False:
                result = func(*args, **kwargs)
                file.write(f"{args}_{kwargs}:{result}\n")
                print("result no cache")

        return result
    return wrapper



@cacheToFile
def expensiveOperation(x, y):
    print("Performing complex calculations...")
    time.sleep(2)
    return x * y + 100

print(expensiveOperation(7, 132))