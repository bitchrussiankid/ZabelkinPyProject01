def orderCost(prPrice, prAmount, shipCost):
    totalAmount = prPrice * prAmount + shipCost
    return totalAmount

prPrice = float(input("Enter the price of the product: "))
prAmount = int(input("Enter the quantity of the product: "))
shipCost = float(input("Enter shipping cost: "))
totalAmount = orderCost(prPrice, prAmount, shipCost)
print("Total amount is:", totalAmount, "RUB")