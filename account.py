class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} birr.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} birr.")


# Create two accounts
account1 = Account("Rahwi", "1001")
account2 = Account("Abel", "1002", 500)

# Transactions
account1.deposit(1000)
account1.withdraw(300)
account1.withdraw(800)

print()

account2.deposit(-100)
account2.withdraw(600)
account2.deposit(200)

print()

# Show balances
print(f"{account1.owner}'s balance: {account1.balance} birr")
print(f"{account2.owner}'s balance: {account2.balance} birr")