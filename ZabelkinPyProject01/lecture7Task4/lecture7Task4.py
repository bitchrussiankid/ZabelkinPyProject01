import os

if not(os.path.exists("fruits.txt")):
    with open("fruits.txt", "w") as file:
        file.write("""apple
banana
orange
grape
melon""")

        
lineNumber = 0
with open("fruits.txt", "r") as file:
    for line in file:
        lineNumber += 1
        print(f"Fruit {lineNumber}: {line.strip()}")

print(f"Total fruits: {lineNumber}")