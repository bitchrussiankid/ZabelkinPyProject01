class Calculator:
    def __init__(self):
        self.result = 0
        

    def add(self, x):
        self.result = x + self.result
        
    def subtract(self, x):
        self.result = self.result - x

    def multiply(self, x):
        self.result = self.result * x

    def getResult(self):
        return self.result

calc = Calculator()

calc.add(5)
calc.multiply(3)
calc.subtract(2)
print(calc.getResult())