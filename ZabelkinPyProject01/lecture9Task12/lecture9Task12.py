class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def updateQuantity(self, amount):
        self.quantity += amount


    def displayInfo(self):
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"



class Shop:
    def __init__(self, name):
        self.name = name
        self.products = {}


    def addProduct(self, product):
        self.products[product.name] = product


    def sellProduct(self, productName, quantity):
        self.productName = productName
        self.quantity = quantity

        if self.productName in self.products.keys():
            if self.quantity <= self.products[self.productName].quantity:
                self.products[self.productName].updateQuantity(-self.quantity)

                return self.products[self.productName].price * self.quantity
            else: 
                print(f"\nError: not enough {self.productName} in stock\n")
                return -1
        else:
            print(f"\nError: Product {self.productName} not found\n")
            return -1


        


    def restockProduct(self, productName, quantity):
        self.productName = productName
        self.quantity = quantity

        if self.productName in self.products.keys():
            self.products[self.productName].updateQuantity(self.quantity)
            return self.products[self.productName].quantity
        else:
            print(f"""\nError: the product '{self.productName}' hasn't been added to the store
Firstly, add the product specifying its name, price and quantity\n""")
            return -1


    def displayInventory(self):
        print(f"{self.name} inventory:\n")
        self.productNum = 1
        if self.products != {}:
            for key, value in self.products.items():
                print(f"{self.productNum}. {key} | price: {value.price}$, quantity: {value.quantity}")
                self.productNum += 1
        else:
            print("Shop is empty")


# create products:
product1 = Product("iPhone 13", 600, 10)
product2 = Product("Samsung Z Fold", 1500, 5)
product3 = Product("Honor V3", 1300, 20)

# create the shop:
shop1 = Shop("TechStore")

# add product to the shop:
shop1.addProduct(product1)
shop1.addProduct(product2)
shop1.addProduct(product3)

# shop products in the stock:
shop1.displayInventory()

# sell products:
def checkSale(productName, productQuantity):
    salesResult = shop1.sellProduct(productName, productQuantity)
    if salesResult != -1:
        print(f"\nThe sold product: {productName}. Quantity: {productQuantity}. Total price: {salesResult}\n")

checkSale(product1.name, 10)
checkSale(product1.name, 2)

# restock products:
def checkRestock(productName, productQuantity):
    restockResult = shop1.restockProduct(productName, productQuantity)
    if restockResult != -1:
        print(f"\nRestock {productName}. New quantity: {restockResult}\n")

checkRestock(product1.name, 100)


# show products in the stock:
shop1.displayInventory()