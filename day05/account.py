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
            print(f"Deposited {amount} birr")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} birr")

    def statement(self):
        print(f"Account: {self.owner}, Balance: {self.balance} birr")


# SavingsAccount inherits Account
class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance, rate):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print(f"Savings Account - {self.owner}: {self.balance} birr")


# CurrentAccount inherits Account
class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance, overdraft):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            print(f"Withdrew {amount} birr")
        else:
            print("Overdraft limit exceeded")

    def statement(self):
        print(f"Current Account - {self.owner}: {self.balance} birr")


# Create accounts
account1 = Account("Rahwi", "1001", 1000)

savings = SavingsAccount("Abel", "1002", 2000, 0.05)

current = CurrentAccount("Sara", "1003", 500, 300)


# Add interest to savings
savings.add_interest()


# Polymorphic loop
accounts = [account1, savings, current]

for account in accounts:
    account.statement()