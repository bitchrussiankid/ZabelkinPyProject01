import os
from datetime import datetime
import traceback

if not(os.path.exists("backup_results.txt")):
    with open("backup_results.txt", "w"):
        pass

def backupResults(func):
    def wrapper(*args, **kwargs):
        with open("backup_results.txt", "a") as file:

            datetimeNow = datetime.now().replace(microsecond = 0)

            try:
                result = func(*args, **kwargs)
                file.write(f"{datetimeNow} | {func.__name__} | {args}, {kwargs} | {result}\n")
            except Exception as e:
                file.write(f"{datetimeNow} | {func.__name__} | {args}, {kwargs} | {traceback.format_exc()}\n")
                result = f"Error: {type(e).__name__}"

        return result
    return wrapper

@backupResults
def calculateExpression(expression):
    return eval(expression)

print(calculateExpression("7 * 7"))