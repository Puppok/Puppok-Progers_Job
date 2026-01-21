# Создать класс **User** для управления данными пользователя
#
# **Атрибуты:**
#   • `_username` (имя пользователя) - защищенный
#   • `_email` (email) - защищенный
#   • `_age` (возраст) - защищенный
#   •` __password` (пароль) - приватный
#
# **Методы:**
#   • `show_info()` - показать публичную информацию (без пароля)
#   • `check_password(password)` - проверить пароль (возвращает True/False)
#

# **Property:**
#   1. username - getter и setter
#      Setter должен проверять:
#      • Длина от 3 до 20 символов
#      • Только буквы, цифры и подчёркивание
#
# email - getter и setter
#      Setter должен проверять:
#      • Содержит символ '@'
#      • Содержит точку '.' после @

# age - getter и setter
#      Setter должен проверять:
#      • Возраст от 13 до 120
#
# password (только setter, без getter!)
#      Setter должен проверять:
#      • Длина минимум 8 символов

class User:
    def __init__(self, username: str, email: str, age: int, password: str):
        self._username = username
        self._email = email
        self._age = age
        self.__password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username: str):
        if not len(new_username) >= 3 and len(new_username) <= 20:
            raise ValueError('Username must be between 3 and 20 characters long')

        if not new_username.replace('_', '').isalnum():
            raise ValueError('Username must contain only alphanumeric characters and underscore')

        self._username = new_username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str):
        if not '@' in new_email or not '.' in new_email.split('@')[1]:
            raise ValueError('Email must contain @ and . after it')

        self._email = new_email

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        if not 0 <= new_age <= 100:
            raise ValueError('Age must be between 0 and 100')

        self._age = new_age

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, new_password: str):
        if not len(new_password) >= 8:
            raise ValueError('Password must be above 8 characters long')

        self.__password = new_password

    def check_password(self, password: str):
        return password == self.__password

    def show_info(self):
        print(f'Username: {self._username}\n'
              f'Email: {self._email}\n'
              f'Age: {self._age}')
