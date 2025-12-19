import time

def timer(func):
    def wrapper(*arg):
        startTime = time.time()
        result = func(*arg)
        endTime = time.time()
        executionTime = endTime - startTime
        print(f"Function '{func.__name__}' executed in {executionTime:.10f} seconds")
        return result
    return wrapper

@timer
def exampleFunc(n):
    total = 0
    for i in range(n):
        total += 1
    return total

exampleFunc(10)