student = {
    "name": "Andrey",
    "age": 27,
    "course": "Computer science",
    "gpa": 4.8,
    "isGraduated": False,
    "subjects": ["Math", "Programming", "Physics"]   
    }


listStudent = list(student.items())
print(listStudent, "\n")
for i in range(len(student)):
    print(f"{listStudent[i][0]}: {listStudent[i][1]}, dataType: {type(listStudent[i][1])} \n")