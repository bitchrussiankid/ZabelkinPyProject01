import os
from datetime import datetime

if not(os.path.exists("function_log.txt")):
    with open("function_log.txt", "w") as file:
        pass
    
    
def logger(func):
    def wrapper(*arg, **kwarg):
        with open("function_log.txt", "a") as file:
            datetimeNow = str(datetime.now())
            file.write(f"{datetimeNow} - ")
            file.write(f"{func.__name__} - ")
            file.write(f"args: {arg} - ")
            result = func(*arg, **kwarg)
            file.write(f"result: {result}\n")
        return result
    return wrapper


@logger
def exampleFunc(a, b):
    multiply = a * b
    return multiply

print(exampleFunc(5, 5))