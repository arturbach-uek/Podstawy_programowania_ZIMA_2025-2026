import random
class BankAccount():
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
    
    def deposit(self, amount):
        if amount < 5.0:
            print("You have to deposit at leat 5 PLN!")
            return
        self.balance += amount
        print(f"Deposited: {amount:.2f} PLN")
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("You dont have enaught money!")
            return
        self.balance -= amount
        print(f"Withdrew: {amount:.2f} PLN")
    
    def display(self):
        formatted_number = " ".join(self.account_number[i:i+4] for i in range(0, 26, 4))
        print(f"Bank account number: {formatted_number}")
        print(f"Balance: {self.balance:.2f} PLN")


account = BankAccount("1234555559090111100007722")

account.display()
account.deposit(25.30)
account.display()
account.withdraw(31.70)
account.display()
account.withdraw(14)
account.display()
