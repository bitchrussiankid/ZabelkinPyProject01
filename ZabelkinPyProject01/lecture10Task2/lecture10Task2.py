class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makeSound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def makeSound(self):
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def makeSound(self):
        return "Meow! Meow!"

    def play(self):
        return f"{self.name} plays with its tail!"


dog = Dog("Sharik", "Canine", "Beagle")
cat = Cat("Lada", "Feline", "Grey")

print(cat.makeSound())
print(cat.play())
print(f"Cat color: {cat.color}")

print(dog.makeSound())
print(dog.fetch())
print(f"Dog breed: {dog.breed}")