class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def displayInfo(self):
        return f"{self.brand}, {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def displayInfo(self):
        return f"{self.brand}, {self.year}, {self.doors}"


vehicle = Vehicle("Generic", 2020)
car = Car("Toyota", 2022, 4)

print(vehicle.displayInfo())
print(car.displayInfo())