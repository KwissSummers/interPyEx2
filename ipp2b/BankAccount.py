class BankAccount:
    def __init__(self, accountName, balance):
        self.accountName = accountName
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return f"{self.accountName} has a balance of ${self.balance}"