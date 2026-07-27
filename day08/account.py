class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
        self.observers = []
        self.history = []

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
        else:
            self.__balance += amount

        print(f"Undid {action} of {amount} birr")

    def total_transactions(self):
        return self.count(self.history)

    def count(self, history):
        if not history:
            return 0
        return 1 + self.count(history[1:])

    def statement(self):
        print(f"{self.owner}: {self.balance} birr")


class SavingsAccount(Account):
    def __init__(self, owner, number, balance, rate):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)


class CurrentAccount(Account):
    def __init__(self, owner, number, balance, overdraft):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft


class SMSAlert:
    def update(self, message):
        print("SMS:", message)


class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance):
        if kind == "savings":
            return SavingsAccount(owner, number, balance, 0.05)
        elif kind == "current":
            return CurrentAccount(owner, number, balance, 500)


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.account_number] = account

    def find(self, number):
        return self.accounts.get(number)

    def list_all(self):
        for number in sorted(self.accounts):
            self.accounts[number].statement()

    def top_by_balance(self, n):
        return sorted(
            self.accounts.values(),
            key=lambda x: x.balance,
            reverse=True
        )[:n]

    def binary_search(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == target:
                return self.accounts[numbers[mid]]
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def find_by_number(self, number):
        return self.binary_search(sorted(self.accounts), number)


# Create accounts
account1 = AccountFactory.create("savings", "Rahwi", "1001", 1000)
account2 = AccountFactory.create("current", "Abel", "1002", 500)
account3 = AccountFactory.create("savings", "Hana", "1003", 2000)

sms = SMSAlert()
registry = AccountRegistry()

for account in [account1, account2, account3]:
    account.subscribe(sms)
    registry.add(account)

# Sample transactions
account1.deposit(200)
account1.withdraw(100)
account2.deposit(300)
account3.deposit(500)

print("\nTop 2 Accounts by Balance:")
for account in registry.top_by_balance(2):
    account.statement()

print("\nBinary Search:")
found = registry.find_by_number("1002")
if found:
    found.statement()

print("\nTotal Transactions:")
for account in [account1, account2, account3]:
    print(account.owner, ":", account.total_transactions())