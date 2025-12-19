def fillingTheInventory(goods: dict):
    inventory = {}
    goodsToInventory = list(goods.values())
    countsAndGoods = []
    validItems = ["apples", "bananas", "oranges", "grapes"]

    i = 1
    while i in range(len(goods) + 1):
        if any(goods[i].lower().endswith(item) for item in validItems):
            countsAndGoods.append(goods[i].lower().split(" "))
        else: print("Fruits not found")
        i += 1

    for i in range(len(countsAndGoods)):
        try:
            if countsAndGoods[i][1] in inventory.keys():
                inventory[countsAndGoods[i][1]] += int(countsAndGoods[i][0])
            else:
                inventory[countsAndGoods[i][1]] = int(countsAndGoods[i][0])
        except IndexError:
            if countsAndGoods[i][0] in inventory.keys():
                inventory[countsAndGoods[i][0]] += 1
            else:
                inventory[countsAndGoods[i][0]] = 1
            print(f"The number of {countsAndGoods[i][0]} is not specified! One {countsAndGoods[i][0]} added.")
        except Exception as e:
            print(f"An unknown error occured while filling inventory with item {i}.")
    return inventory


goods = {
    1: "10 APPLES",
    2: "5 bananas",
    3: "8 oranges",
    4: "23 grapes",
    5: "grapes",
    6: "eggs"
    }

try:
    inventory = fillingTheInventory(goods)
    print(inventory)
except Exception as e:
    print("An unknown error occured while placint goods into inventory!")

print(inventory)