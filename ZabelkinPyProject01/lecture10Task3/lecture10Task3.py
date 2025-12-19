class Employee:
    def __init__(self, name, employeeId):
        self.name = name
        self.employeeId = employeeId

    def getInfo(self):
        return f"Employee: {self.name}, ID: {self.employeeId}"

class Manager(Employee):
    def __init__(self, name, employeeId, department):
        super().__init__(name, employeeId)
        self.department = department

    def getInfo(self):
        return super().getInfo() + f", department: {self.department}"


emp = Employee("Ivan", "E001")
mng = Manager("Anna", "M005", "Delivery")

print(emp.getInfo())
print(mng.getInfo())