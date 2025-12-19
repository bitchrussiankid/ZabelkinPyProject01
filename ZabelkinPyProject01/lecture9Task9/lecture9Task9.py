class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough funds")

    def transfer(self, otherAccount, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            otherAccount.deposit(amount)
        else: 
            print("Not enough funds")

    def getBalance(self):
        return(self.balance)

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.withdraw(300)
account2.deposit(200)

account1.transfer(account2, 150)

print(f"Alice balance: {account1.getBalance()}")
print(f"Bob balance: {account2.getBalance()}")