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
            self.notify(f"{amount} birr deposited")


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


# Transactions
account1.deposit(200)
account2.deposit(300)


# Statements
account1.statement()
account2.statement()