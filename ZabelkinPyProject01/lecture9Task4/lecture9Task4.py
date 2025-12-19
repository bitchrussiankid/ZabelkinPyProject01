# create class:
class Student:
    # class constructor:
    def __init__(self, name:str, age:int, course:int):
        self.name = name
        self.age = age
        self.course = course

    def studentData(self):
        return f"Name - {self.name}, Age - {self.age}, Course - {self.course}"


student1 = Student("Alice", 20, 3)
student2 = Student("Bob", 22, 4)
student3 = Student("Charlie", 19, 2)

print(f"student1: {student1.studentData()}")
print(f"student2: {student2.studentData()}")
print(f"student3: {student3.studentData()}")