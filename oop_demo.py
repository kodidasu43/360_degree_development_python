class BankAccount:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds")

  def get_balance(self):
    return self.balance

account1 = BankAccount("John Doe", 1000) #opening of account in a bank
account2 = BankAccount("Jane Doe", 500)

account1.deposit(500)
account2.withdraw(600)

print(account1.get_balance())  
print(account2.get_balance())  