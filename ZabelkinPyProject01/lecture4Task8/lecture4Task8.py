grades = [70, 70, 70, 70, 70, 70, 70]

status = "Undefined"
countAboveEighty = sum(1 for grade in grades if grade > 80)

if min(grades) < 60:
    status = "Fail"

if min(grades) >= 60 and min(grades) < 70:
    status = "Need improvement"

if min(grades) >= 60 and (countAboveEighty > (len(grades) - countAboveEighty)):
    status = "Average"

if min(grades) > 70 and max(grades) > 90:
    status = "Good"

if min(grades) > 80 and (sum(grades) / len(grades)) > 85:
    status = "Excellent"

print(status)