# Создайте два класса для работы с банковскими счетами:
#
# КЛАСС 1: BankAccount (Базовый банковский счет)
# Атрибуты:
#   • account_number (номер счёта) - публичный
#   • _balance (баланс) - защищённый
#   • _owner (владелец) - защищённый
#   • __pin (PIN-код) - приватный

# Методы:
#   • __init__(account_number, owner, initial_balance, pin)
#   • deposit(amount) - пополнить счёт (с проверкой: amount > 0)
#   • withdraw(amount, pin) - снять деньги (проверка PIN и достаточности средств)
#   • check_pin(pin) - проверить PIN-код (приватный метод)
#   • get_balance() - получить баланс
#   • transfer(amount, target_account, pin) - перевести деньги на другой счёт
#   • show_info() - показать информацию о счёте (без баланса)
#
# Property:
#   • balance - только getter (read-only)
#   • owner - getter и setter (при установке проверка: не пустая строка)

# КЛАСС 2: SavingsAccount (Сберегательный счет - наследуется от BankAccount)
# Дополнительные атрибуты:
#   • _interest_rate (процентная ставка) - защищённый
#   • _min_balance (минимальный баланс) - защищённый
#
# Дополнительные методы:
#   • __init__(account_number, owner, initial_balance, pin, interest_rate, min_balance)
#     ↳ ОБЯЗАТЕЛЬНО использовать super().__init__()
#   • withdraw(amount, pin) - ПЕРЕОПРЕДЕЛИТЬ с проверкой минимального баланса
#   • add_interest() - начислить проценты на баланс
#   • get_interest_rate() - получить процентную ставку
#
# Property:
#   • interest_rate - getter и setter (проверка: 0 <= rate <= 20)
#   • min_balance - только getter (read-only)


class BankAccount:
    def __init__(self, account_number: int, owner: str, initial_balance: float, pin: int):
        self.accountNumber = account_number
        self._balance = initial_balance
        self._owner = owner
        self.__pin = pin

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not new_owner:
            raise ValueError("Owner cannot be empty")

        self._owner = new_owner
        print(f'Changed owner to: {new_owner}')

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit cannot be negative or zero")

        self._balance += amount
        print(f'Deposited {amount}, Balance: {self._balance}')

    def withdraw(self, amount: float, pin: int):
        if not self.__check_pin(pin):
            raise ValueError("Invalid pin")

        if self._balance < amount:
            raise ValueError("Not enough balance")

        self._balance -= amount
        print(f'Withdrawed {amount}, Balance: {self._balance}')

    def __check_pin(self, pin):
        return pin == self.__pin

    def get_balance(self):
        return self._balance

    def transfer(self, amount: float, target_account: BankAccount, pin: int):
        self.withdraw(amount, pin)
        target_account.deposit(amount)
        print(f'Transfer {amount} to {target_account.owner}')

    def show_info(self):
        print('-' * 15)
        print(f'Account info: \n'
              f'• Number: {self.accountNumber}\n'
              f'• Owner: {self.owner}')
        print('-' * 15)

class SavingsAccount(BankAccount):
    def __init__(self,
                 accountNumber: int,
                 owner: str,
                 initialBalance: float,
                 pin: int,
                 interestRate: int,
                 minBalance: float
                 ):
        super().__init__(accountNumber, owner, initialBalance, pin)
        self._interestRate = interestRate
        self._minBalance = minBalance

    @property
    def interestRate(self):
        return self._interestRate

    @interestRate.setter
    def interestRate(self, new_interestRate):
        if new_interestRate < 0 or new_interestRate > 20:
            raise ValueError("Interest rate must be between 0 and 20")

        self._interestRate = new_interestRate
        print(f'Changed interest rate to: {new_interestRate}')

    @property
    def minBalance(self):
        return self._minBalance

    def withdraw(self, amount: float, pin: int):
        if self._balance - amount < self._minBalance:
            print(f'Min Balance {self._minBalance} is less than the amount {amount}')
            raise ValueError("Can't withdraw more than minimum balance")

        super().withdraw(amount, pin)

    def add_interest(self):
        self._balance += self._balance * (self.interestRate / 100)
        print(f'Balance with interest {self._balance}')

    def get_interest_rate(self):
        print(f'Interest Rate: {self.interestRate}')

# ПРИМЕР ИСПОЛЬЗОВАНИЯ:
# Обычный счёт
account1 = BankAccount("ACC001", "Иван Петров", 10000, 1234)
print(account1.balance)  # 10000
print(account1.owner)    # Иван Петров

account1.deposit(5000)   # Пополнение: +5000 руб
account1.withdraw(3000, 1234)  # Снятие: -3000 руб
print(account1.balance)  # 12000

# Сберегательный счёт
savings = SavingsAccount("SAV001", "Мария Иванова", 50000, 5678, 5.0, 10000)
print(savings.balance)  # 50000
print(savings.interestRate)  # 5.0

savings.add_interest()  # Начислены проценты: +2500 руб (5% от 50000)
print(savings.balance)  # 52500

# savings.withdraw(40000, 5678)  # Попытка снять 40000
# Ошибка: После снятия баланс будет ниже минимального (10000)

savings.withdraw(30000, 5678)  # Снятие: -30000 руб (баланс = 22500, это > 10000)
print(savings.balance)  # 22500

# Перевод между счетами
account1.transfer(5000, savings, 1234)  # Перевод 5000 от account1 к savings
print(account1.balance)  # 7000
print(savings.balance)   # 27500
