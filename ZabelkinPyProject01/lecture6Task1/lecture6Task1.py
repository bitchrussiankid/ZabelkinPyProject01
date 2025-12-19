students = [
    "Alice", 
    "Bob", 
    "Charlie", 
    "Diana", 
    "Eve"
    ]

grades = {
    "Alice": [85, 92, 78],
    "Bob": [65, 70, 80],
    "Charlie": [90, 85, 95],
    "Diana": [75, 80, 70],
    "Eve": [80, 92, 96]    
    }

def GPAFormula(keyName: str) -> float:
    GPA = sum(grades[keyName]) / len(grades[keyName])
    return round(GPA, 1)

# Filling out the dictionary "averageGrades":
averageGrades = {}
for i in range(len(students)):
    try:
        averageGrades[students[i]] = GPAFormula(students[i])
    except KeyError:
        print(f"The student {students[i]} has no grades")

print(averageGrades)

# Search for students with an GPA above 85:
countMore85Students = 0
print("Excellent students:\n")
for i in range(len(averageGrades)):
    if averageGrades[students[i]] > 85:
        print(students[i])
        countMore85Students += 1
print(f"\nThe scool has {countMore85Students} excellent students!")

# Search for students with low GPA:

for i in range(len(averageGrades)):
    if averageGrades[students[i]] < 75:
        print(f"\nAttention! {students[i]} has a low GPA: {averageGrades[students[i]]}")