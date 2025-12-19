class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def displayInfo(self):
        print(f"{self.__class__.__name__}: {self.brand} {self.model} {self.year}, Wheels: {Car.wheels}")



car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.displayInfo() 
car2.displayInfo() 

Car.wheels = 6

car1.displayInfo() 
car2.displayInfo()