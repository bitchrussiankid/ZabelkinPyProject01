import os
import time
from datetime import datetime

if not(os.path.exists("function_log.txt")):
    with open("function_log.txt", "w") as file:
        pass


def logger(func):
    def wrapper(*args, **kwargs):
        with open("function_log.txt", "a") as file:
            datetimeNow = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            file.write(f"{datetimeNow} - ")
            file.write(f"{func.__name__} - ")
            file.write(f"args: {args} {kwargs} - ")
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        executionTime = (endTime - startTime)
        with open("function_log.txt", "a") as file:
            file.write(f"result: {result} - ")
            file.write(f"time: {executionTime:.6f}s\n")
        return result
    return wrapper


@logger
def basicCalc(a, b, operator, verbose):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b

    if verbose:
        print(f"Operation: {a} {operator} {b} = {result}")
    return result

access = False
try:
    num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
    access = True
except ValueError:
    print("Value error!")
except Exception as e:
    print("Unavailable error!")

if access == True:
    
    basicOperators = ["+", "-", "*", "/"]
    print(f"Basic operators: {basicOperators}")
    operator = input("Enter operator: ")

    showDetails = input("Show detailed calculation? (yes/no): ").lower() == "yes"
    if showDetails == True:
        basicCalc(num1, num2, operator, verbose = True)
    else: 
        print(f"result: {basicCalc(num1, num2, operator, verbose = False)}")