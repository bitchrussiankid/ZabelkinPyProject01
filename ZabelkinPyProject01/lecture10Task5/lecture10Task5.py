class Engine:
    def __init__(self, power):
        self.power = power

    def getPowerInfo(self):
        return f"Power: {self.power}h.p."


class Radio:
    def __init__(self, hasRadio: bool):
        self.hasRadio = hasRadio

    def playMusic(self):
        if self.hasRadio:
            return "Music plays"
        else: 
            return "No radio"

class Car(Engine, Radio):
    def __init__(self, power, hasRadio, brand, model):
        Engine.__init__(self, power)
        Radio.__init__(self, hasRadio)
        self.brand = brand
        self.model = model

    def getPowerInfo(self):
        return Engine.getPowerInfo(self) + f" for {self.brand} {self.model}"


car = Car(brand = "Bugatti", model = "Chiron", power = 1500, hasRadio = True)
print(car.playMusic())
print(car.getPowerInfo())