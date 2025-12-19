class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getInfo(self):
        return "I perform general tasks"


class Developer(Employee):
    def __init__(self, name, salary, programmingLanguage):
        super().__init__(name, salary)
        self.programmingLanguage = programmingLanguage

    def getInfo(self):
        return "I write code in Python"


class SeniorDeveloper(Developer):
    def __init__(self, name, salary, programmingLanguage, teamSize):
        super().__init__(name, salary, programmingLanguage)
        self.teamSize = teamSize

    def getInfo(self):
        return f"I manage a team of {self.teamSize} people and write code"


class FullstackDeveloper(Developer):
    def __init__(self, name, salary, programmingLanguage, programmingLanguage1, programmingLanguage2):
        super().__init__(name, salary, programmingLanguage)
        self.programmingLanguage1 = programmingLanguage1
        self.programmingLanguage2 = programmingLanguage2

    def getInfo(self):
        if self.programmingLanguage2 != None:
            self.fullStack = self.programmingLanguage + ", " + self.programmingLanguage1 + ", " + self.programmingLanguage2
        else:
            self.fullStack = self.programmingLanguage + ", " + self.programmingLanguage1
        return f"I write code in the following languages: {self.fullStack}"


employee = Employee("Nikita", 2000)
print(employee.getInfo())

developer = Developer("Maria", 3500, "Java")
print(developer.getInfo())

seniorDeveloper = SeniorDeveloper("Andrey", 5000, "Python", 20)
print(seniorDeveloper.getInfo())

fullstackDeveloper = FullstackDeveloper(name = "Nikolai", salary = 7000, programmingLanguage = "Java", programmingLanguage1 = "JavaScript", programmingLanguage2 = "Python")
print(fullstackDeveloper.getInfo())