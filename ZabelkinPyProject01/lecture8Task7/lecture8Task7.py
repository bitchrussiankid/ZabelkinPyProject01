import os
from datetime import date

if not(os.path.exists("call_counter.txt")):
    with open("call_counter.txt", "w") as file:
        pass

def limitCalls(maxCalls):
    def innerDecorator(func):
        def wrapper(*arg, **kwarg):
            with open("call_counter.txt", "a+") as file:

                file.seek(0)
                dateToday = str(date.today())
                lineCallsToday = f"{dateToday}:0\n"
                for line in file:
                    if dateToday in line:
                        lineCallsToday = line
            
                callsToday = int(lineCallsToday.split(":")[1])

                if callsToday < maxCalls:
                    result = func(*arg, **kwarg)
                    file.write(f"{dateToday}:{callsToday + 1}\n")
                    return result
                else:
                    print(f"Limit ({maxCalls} attempts) exceeded")
        
        return wrapper
    return innerDecorator

@limitCalls(maxCalls = 3)
def testFunc(a, b):
    result = a + b
    return result

testFunc(1, 2)