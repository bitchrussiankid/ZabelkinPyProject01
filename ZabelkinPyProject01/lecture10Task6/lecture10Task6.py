class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, i am {self.age} y.o."


class Student(Person):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId

    def introduce(self):
        return f"My name is {self.name}, my ID: {self.studentId}"


person = Person("Andrey", 27)
student = Student("Andrey", 27, 123456)

print(student.introduce())
print(person.introduce())