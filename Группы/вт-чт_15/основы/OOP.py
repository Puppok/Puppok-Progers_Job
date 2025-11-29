# Концепции ООП
# 1. Инкапсуляция - скрытие свойств класса
# 2. Наследование - наследование свойств и методов
# 3. Полиморфизм - возможность использовать один и тот же метод в разных классах

# 1. Инкапсуляция
class House:
    def __init__(self):
        self.freeStaff = 5 # публичное свойство
        self._staff = 10 # минимальная защита
        self.__secretStaff = 15 # максимальная защита (name mangling - _House__secretStaff)
        self._name = 'Pep'
        self._age = 10

    # Геттеры
    def getStaff(self):
        return self._staff # отдаем значение, сама переменная при этом не затронута

    # Сеттеры
    def setStaff(self, value):
        if value > 50:
            print('Ошибка, ты кривая жопа')
        else:
            self._staff = value
            print('Изменено успешно')

    @property # геттер через property, обращаемся как к обычной переменной
    def name(self):
        return f'Имя: {self._name}'
    
    @name.setter # сеттер через property, значение вносим как в переменную
    def name(self, value):
        if value == 'Ochko':
            print('Ты дурак что ли?')
        else:
            self._name = value
            print('Намана, подходит')


house = House()
# print(house.freeStaff) # имеем свободный доступ
# print(house._staff) # можем обратиться но лучше не стоит
# print(house.__secretStaff) # ошибка, нет доступа

# print(house.getStaff())
# house.setStaff(15)
# print(house.getStaff())

# print(house.name) # вызов геттера через property
# house.name = 'Tom' # вызов сеттера через property
# print(house.name)


# КЛАСС: User
# Атрибуты:
#   _username (имя пользователя) - защищённый
#   _email (email) - защищённый
#   _age (возраст) - защищённый
#   __password (пароль) - приватный

# Методы:
#   __init__(username, email, age, password)
#   show_info() - показать публичную информацию (без пароля)
#   check_password(password) - проверить пароль (возвращает True/False)

class User:
    def __init__(self, username: str, email: str, age: int, password: str):
        self._username = username
        self._email = email
        self._age = age
        self.__password = password

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, newUsername: str):
        pass


    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self):
        pass


    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self):
        pass


    @property
    def password(self) -> str:
        return '❌ Нет доступа к паролю'

    @password.setter
    def password():
        pass


    def showInfo():
        pass

    def checkPassword():
        pass


print('sdjgskGDSGSGgs'.isalnum())
print('skjg.tlhkfj'.replace('_', '').isalnum())

# .isalnum() - вернет True если строка состоит только из букв и цифр
# .replace(check, change) - заменяет символ check на символ change
# if 10 > 3:
#     raise AttributeError('Ты тупой, учи математику')
# else:
#     print('ok')


def add(self, number):
    self.result = self.result + number


string = 'SKJGHS@348.7632'
if '@' in string:
    if '.' in string.split('@')[1]:
        print('ok')
    else:
        print('no')

