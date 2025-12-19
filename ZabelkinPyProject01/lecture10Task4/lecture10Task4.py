class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def startEngine(self):
        return "The engine is running"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def startEngine(self):
        return "Car engine started"

class ElectricCar(Car):
    def __init__(self, brand, year, doors, batteryCapacity):
        super().__init__(brand, year, doors)
        self.batteryCapacity = batteryCapacity

    def startEngine(self):
        return "The electric motor started silently"


vehicle = Vehicle("Generic", 2020)
car = Car("Toyota", 2022, 4)
electricCar = ElectricCar("Tesla", 2023, 4, 100)

print(vehicle.startEngine())
print(car.startEngine())
print(electricCar.startEngine())