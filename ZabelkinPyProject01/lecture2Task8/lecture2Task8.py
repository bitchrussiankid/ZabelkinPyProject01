def pluralForm(fruit: str, count: int) -> str:
    if count == 1:
        return fruit
    else:
        return fruit + "s"

fruit = "apple"
count = 5

print("i have " + str(count) + " " + pluralForm(fruit, count))