class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} from the balance.")

# Usage
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print("Final balance:", account.balance)