class Table:
    def __init__(self, tableNumber, capacity, isReserved = False):
        self.tableNumber = tableNumber
        self.capacity = capacity
        self.isReserved = isReserved

    def reserve(self):
        if self.isReserved == False:
            self.isReserved = True
            print(f"The table N.{self.tableNumber} is reserved!")
        else:
            print(f"Table N.{self.tableNumber} is already reserved!")

    def release(self):
        self.isReserved = False

    def getInfo(self):
        return f"Table N.{self.tableNumber}, capacity: {self.capacity}, is reserved: {self.isReserved}"


class Restaurant:
    def __init__(self):
        self.tables = []

    def addTable(self, table):
        self.tables.append(table)

    def findAvailableTable(self, numPeople):
        self.availabilityOfATable = False
        self.numOfList = 0
        print("\nSuitable table:")
        for i in range(len(self.tables)):
            if self.tables[i].capacity >= numPeople and self.tables[i].isReserved == False:
                self.availabilityOfATable = True
                self.numOfList = i
                break
        if self.availabilityOfATable == True:
            print(self.tables[self.numOfList].getInfo())
        else:
            print("No suitable table available!")
            

    def reserveTable(self, tableNumber):
        self.tableNumber = tableNumber
        for i in range(len(self.tables)):
            if self.tableNumber == self.tables[i].tableNumber:
                self.tables[i].reserve()
                break


restaurant = Restaurant()

tables = []
tablesInRestaurant = {}

def createTable(tableNumber, tableCapacity):
    tables.append(Table(tableNumber - 1, tableCapacity))
def storageInfo():
    print("\nTables in the storage:")
    for i in range(len(tables)):
        print(f"id: {i} | Number: {tables[i].tableNumber} | Capacity: {tables[i].capacity} | isReserved: {tables[i].isReserved}")
def restaurantInfo():
    print("\nTables in the restaurant:")
    for key in tablesInRestaurant.keys():
        print(f"id: {key} | Number: {tablesInRestaurant[key].tableNumber} | Capacity: {tablesInRestaurant[key].capacity} | isReserved: {tablesInRestaurant[key].isReserved}")

def checkTableAvailability(tableNumber):
    tableExists = False
    for key in tablesInRestaurant.keys():
        if tableNumber == tablesInRestaurant[key].tableNumber:
            tableExists = True
            break
    return tableExists

def addTable(table):
    try:
        if checkTableAvailability(table.tableNumber) == False:
            tablesInRestaurant[table.tableNumber] = table
            restaurant.addTable(table)
            print(f"The table N.{table.tableNumber} added to restaurant!")
        else:
            print(f"Error: The table N.{table.tableNumber} has already been added to the restaurant!")
    except AttributeError:
        print("Error: Incorrect table data while adding a table!")
    except Exception as e:
        print("Error: Unknown error while adding a table!")
def reserveTable(table):
    try:
        if checkTableAvailability(table.tableNumber) == True:
            restaurant.reserveTable(table.tableNumber)
        else:
            print(f"Error: There is no table N.{table.tableNumber} in the restaurant!")
    except AttributeError:
        print("Error: Incorrect table data while reserving a table!")
    except Exception as e:
        print("Error: Unknown error while reserving a table!")
def releaseTable(table):
    try:
        if table in tables:
            table.release()
            print(f"The table N.{table.tableNumber} was freed!")
        else:
            print(f"The table N.{table.tableNumber} doesn't exist!")
    except AttributeError:
        print("Error: Incorrect table data when clearing a table!")
    except Exception as e:
        print("Error: Unknown error when clearing a table!")


# ALL OPERATIONS ARE PERFORMED BY TABLE ID!

        
# Creating tables (4 tables for 2, 4, 6 people, and 2 tables for 12 people):
counter = 1
while counter <= 4:
    createTable(counter, 2)
    counter += 1

while counter <= 8:
    createTable(counter, 4)
    counter += 1

while counter <= 12:
    createTable(counter, 6)
    counter += 1

while counter <= 14:
    createTable(counter, 12)
    counter += 1

# Tables in storage:
storageInfo()



# Adding tables to a restaurant:
# For 2 people:
addTable(tables[0])
addTable(tables[1])

# For 4 people:
addTable(tables[4])
addTable(tables[5])

# For 6 people:
addTable(tables[8])
addTable(tables[9])

# For 12 people:
addTable(tables[13])

# Tables in restaurant:
restaurantInfo()



# Looking for a free table for 5 people:
restaurant.findAvailableTable(5)

# Reserve a suitable table for 5 people:
reserveTable(tablesInRestaurant[8])

# Looking for a free table for 12 people:
restaurant.findAvailableTable(12)

# Reserve a suitable table for 12 people:
reserveTable(tablesInRestaurant[13])

# Trying to reserve a table again:
reserveTable(tablesInRestaurant[13])

# Looking for a free table for 20 people:
restaurant.findAvailableTable(20)

# Remove a reservation from a table N.13:
releaseTable(tablesInRestaurant[13])