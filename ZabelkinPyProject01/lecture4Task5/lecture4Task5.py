fruits = [
    "apple",
    "banana",
    "orange",
    "kiwi",
    "banana",
    "pear"
    ]
print(fruits)

fruits.remove("banana")
print(fruits)

del fruits[2]
print(fruits)

fruits.pop()                    # or: del fruits[-1]
print(fruits)