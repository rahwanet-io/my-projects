class AlertService:
    # Separate alert responsibility (SRP)
    def send(self, message):
        print("Alert:", message)


class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []
        self.history = []   # Stack for transaction history

    @property
    def balance(self):
        return self.__balance

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.history.append(("deposit", amount))
            self.notify(f"{amount} birr deposited")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.__balance -= amount
            self.history.append(("withdraw", amount))
            self.notify(f"{amount} birr withdrawn")
        else:
            print("Invalid withdrawal.")

    def undo_last(self):
        if not self.history:
            print("No transaction to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self.__balance -= amount

        elif action == "withdraw":
            self.__balance += amount

        print(f"Undid {action} of {amount} birr")

    def statement(self):
        print(f"{self.owner}: {self.balance} birr")


class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance, rate):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)


class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance, overdraft):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft


class SMSAlert:
    # Observer
    def update(self, message):
        print("SMS:", message)


class AccountFactory:
    # Factory Pattern
    @staticmethod
    def create(kind, owner, number, balance):
        if kind == "savings":
            return SavingsAccount(owner, number, balance, 0.05)

        elif kind == "current":
            return CurrentAccount(owner, number, balance, 500)

        else:
            print("Unknown account type")


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.account_number] = account

    def find(self, account_number):
        return self.accounts.get(account_number)

    def list_all(self):
        for number in sorted(self.accounts):
            self.accounts[number].statement()


# Create accounts using factory
account1 = AccountFactory.create(
    "savings",
    "Rahwi",
    "1001",
    1000
)

account2 = AccountFactory.create(
    "current",
    "Abel",
    "1002",
    500
)

# Add SMS alert observer
sms = SMSAlert()

account1.subscribe(sms)
account2.subscribe(sms)

# Create registry and add accounts
registry = AccountRegistry()

registry.add(account1)
registry.add(account2)

# Transactions
account1.deposit(200)
account2.deposit(300)
account1.withdraw(100)

# Statements
print("\nStatements:")
registry.list_all()

# Find an account
print("\nFind Account 1001:")
found = registry.find("1001")
if found:
    found.statement()

# Undo last transaction
print("\nUndo Last Transaction:")
account1.undo_last()
account1.statement()