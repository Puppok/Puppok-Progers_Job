import re

class Bank:
    def __init__(self, name: str, bik: str):
        self.name = name
        self.bik = bik
        self._accounts: list[BankAccount] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not re.match(r'^[A-Za-zА-Яа-я\s-]{3,50}$', new_name):
            raise ValueError("Invalid name")

        self._name = new_name

    @property
    def bik(self):
        return self._bik

    @bik.setter
    def bik(self, new_bik: str):
        if not re.match(r'^\d{9}$', new_bik):
            raise ValueError("Invalid bik")

        self._bik = new_bik

    @property
    def accounts(self):
        return tuple(self._accounts)

    def add_account(self, account: 'BankAccount'):
        if self.find_account(account.account_number):
            raise ValueError("Account already exists")
        self._accounts.append(account)

    def remove_account(self, account_number: str):
        acc = self.find_account(account_number)
        if not acc:
            raise ValueError("Account not found")

        self._accounts.remove(acc)

    def find_account(self, account_number: str):
        for account in self._accounts:
            if account.account_number == account_number:
                return account

        return None

    def get_total_balance(self):
        return sum(account.balance for account in self._accounts)

    def show_info(self):
        print(f'Bank: {self.name}\n'
              f'Bank bik: {self.bik}')

class BankAccount:
    def __init__(self,
                 account_number: str,
                 owner: str,
                 balance: int | float,
                 currency: str,
                 pin: str,
                 overdraft_limit: int | float = 0,):

        self.owner = owner
        self.currency = currency
        self.overdraft_limit = overdraft_limit
        self.pin = pin

        if not re.match(r'^\d{20}$', account_number):
            raise ValueError("Invalid account number")
        self._account_number = account_number

        if not isinstance(balance, (int, float)) or balance < -self._overdraft_limit:
            raise ValueError("Invalid balance")
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner: str):
        if not re.match(r'^[A-Za-zА-Яа-я\s]{2,100}$', new_owner):
            raise ValueError("Invalid owner")

        self._owner = new_owner

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, new_currency: str):
        if not re.match(r'^(USD|EUR|RUB|GBP)$', new_currency):
            raise ValueError("Invalid currency")

        self._currency = new_currency

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, new_overdraft_limit: int | float):
        if new_overdraft_limit < 0:
            raise ValueError("Invalid overdraft limit")

        self._overdraft_limit = new_overdraft_limit

    @property
    def pin(self):
        raise AttributeError('PIN is not accessible')

    @pin.setter
    def pin(self, new_pin: str):
        if not re.match(r'^\d{4}$', new_pin):
            raise ValueError("Invalid PIN")

        self.__pin = new_pin

    def deposit(self, amount: int | float):
        if amount <= 0:
            raise ValueError("Must be positive number")

        self._balance += amount

    def withdraw(self, amount: int | float):
        if amount <= 0:
            raise ValueError("Must be positive number")

        if not self._balance + self._overdraft_limit >= amount:
            raise ValueError("Cannot withdraw more")

        self._balance -= amount

    def transfer(self, other_account: 'BankAccount', amount: int | float):
        self.withdraw(amount)
        other_account.deposit(amount)

    def check_pin(self, pin: str):
        return self.__pin == pin

    def show_info(self):
        print(f'Account Number: {self._account_number}\n'
              f'Owner: {self._owner}\n'
              f'Balance: {self._balance}\n'
              f'Currency: {self._currency}\n'
              f'Overdraft Limit: {self._overdraft_limit}\n')


