score = 100
print(f"Initial score: {score}")
bonus = input("Enter bonus points: ")
score = score + int(bonus)
print(f"The new score: {score}")

if score > 150:
    a = True
else:
    a = False

print(f"The score has more than 150? {a}")