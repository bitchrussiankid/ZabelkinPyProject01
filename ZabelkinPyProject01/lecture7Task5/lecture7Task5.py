import os

try:
    with open("shoppingList.txt", "w") as file:
        file.write("""apple
banana
orange
grape
melon""")
    print("shopping list created successfully!")
except Exception as e:
    print("shopping list was not created!")