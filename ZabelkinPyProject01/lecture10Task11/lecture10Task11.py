class Engine:
    def __init__(self, horsePower):
        self.horsePower = horsePower

    def getInfo(self):
        return f"Engine power: {self.horsePower}"


class Transmission:
    def __init__(self, transmissionType):
        self.transmissionType = transmissionType

    def getInfo(self):
        return f"Transmission type: {self.transmissionType}"


class WholeCar(Engine, Transmission):
    def __init__(self, brand, model, horsePower, transmissionType):
        Engine.__init__(self, horsePower)
        Transmission.__init__(self, transmissionType)
        self.brand = brand
        self.model = model

    def getInfo(self):
        return f"{self.brand} {self.model}, {self.horsePower}h.p., transmission: {self.transmissionType}"


class CarAssembly:
    def __init__(self, brand, model, engine, transmission):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.transmission = transmission

    def getInfo(self):
        return f"{self.brand} {self.model}, {self.engine.horsePower}h.p., transmission: {self.transmission.transmissionType}"


car1 = WholeCar(brand = "Nissan", model = "Teana", horsePower = 249, transmissionType = "variator")
print(car1.getInfo())


engine1 = Engine(249)
engine2 = Engine(420)

transmission1 = Transmission("variator")
transmission2 = Transmission("manual")

standartCar2 = CarAssembly("Nissan", "Fuga", engine1, transmission1)
print(standartCar2.getInfo())

swapCar2 = CarAssembly("Nissan", "Fuga Nismo", engine2, transmission2)
print(swapCar2.getInfo())