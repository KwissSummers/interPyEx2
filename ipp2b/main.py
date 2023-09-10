from BankAccount import BankAccount

bankAccount1 = BankAccount("Kwiss Sumwas", 3000.00)
print("My inital amount is $3000.00")
bankAccount1.deposit(4200.69)
print("I have deposited $4200.69")
bankAccount1.withdraw(5)
print("I have withdrawn $5")
print(bankAccount1.getBalance())