class Counter:
    def __init__(self):
        self.value = 0

    def incrementBy1(self):
        self.value += 1
        print("value increased by 1")

    def increment(self, userValue):
        self.value += userValue

    def decrementBy1(self):
        self.value -= 1
        print("value decreased by 1")

    def decrement(self, userValue):
        self.value -= userValue

    def getValue(self):
        print("value returned")
        return(self.value)


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()

for i in range(3):
    counter1.incrementBy1()
for i in range(2):
    counter2.decrementBy1()
counter3.decrement(15)
counter4.increment(15)

print(f"counter1: {counter1.getValue()}")
print(f"counter2: {counter2.getValue()}")
print(f"counter3: {counter3.getValue()}")
print(f"counter4: {counter4.getValue()}")