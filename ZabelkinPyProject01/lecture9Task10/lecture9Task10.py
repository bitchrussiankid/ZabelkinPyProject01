class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.grades = []

    def addGrade(self, grade: int):
        self.grades.append(grade)

    def getAverage(self):
        if not(self.grades):
            return 0.0
        else:
            return round((sum(self.grades) / len(self.grades)), 2)

class Teacher:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject

    def addGradeToStudent(self, student, grade):
        student.addGrade(grade)


student1 = Student("Alice", 15)
student2 = Student("Bob", 16)

teacher = Teacher("Mr. Smith", "Math")

teacher.addGradeToStudent(student1, 5)
teacher.addGradeToStudent(student1, 4)
teacher.addGradeToStudent(student1, 5)

teacher.addGradeToStudent(student2, 3)
teacher.addGradeToStudent(student2, 4)

print(f"Alice average grade: {student1.getAverage()}")
print(f"Bob average grade: {student2.getAverage()}")