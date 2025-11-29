# ООП 
# 1. Инкапсуляция - приватизация свойств класса от внешней программы
# 2. Наследование - классы наследуют свойства других классов
# 3. Полиморфизм - возможность использовать один и тот же метод в разных классах с разным результатом

class House:
    def __init__(self):
        self.freeItem = 'candies' # доступное свойство
        self._personalItems = 'clothes' # защищенное свойство
        self._age = 18
        self.__secretItems = 'money' # приватное свойство, принцип name mangling (_House__secretItems)

    # Геттер (get - получать) - получение значения из класса
    def getPersonalItems(self):
        return self._personalItems

    # Сеттер (set - задавать) - запись нового значения в переменную класса (обычно присутствует проверка)
    def setAge(self, value):
        if value < 18:
            raise AttributeError('значение не может быть меньше 18') # можно создать ошибку
            # print('значение не может быть меньше 18') - можно вывести через print()
        else:
            self._age = value
            print('Возраст изменен успешно')

    # свойство property
    @property # работает как геттер, но используется как переменная
    def secretItems(self):
        return self.__secretItems
    
    @secretItems.setter # работает как сеттер, но используется как переменная (обязательно наличие @property)
    def secretItems(self, value):
        if value == 'candy':
            raise AttributeError('неверное значение')
        else:
            self.__secretItems = value
            print('значение изменено')

house = House()
print(house.freeItem) # так делать можно
house.freeItem = 'cake'
print(house.freeItem)

print(house._personalItems) # можно, но лучше так не делать
house._personalItems = 'laptop'
print(house._personalItems)

# print(house.__secretItems) - ошибка, нет доступа к переменной
print(house._House__secretItems) # доступ есть, но это полный треш, никогда так не делать!

# вызов геттера, получаем значение
print(house.getPersonalItems())

# вызов сеттера, пытаемся изменить значение
# house.setAge(5) # - ошибка, не пройдет проверку
# house.setAge(35) # все ок, значение изменено

# вызов геттера через property
print(house.secretItems) 

# вызов сеттера через property
# house.secretItems = 'candy' # ошибка, неверное значение
house.secretItems = 'PC' # значение изменено


# Создайте класс User для управления данными пользователя.
# КЛАСС: User

# Атрибуты:
#   • _username (имя пользователя) - защищённый
#   • _email (email) - защищённый
#   • _age (возраст) - защищённый
#   • __password (пароль) - приватный

# Методы:
#   • __init__(username, email, age, password)
#   • show_info() - показать публичную информацию (без пароля)
#   • check_password(password) - проверить пароль (возвращает True/False)

# Property (обязательно использовать @property):
#   1. username - getter и setter
#      Setter должен проверять:
#      • Длина от 3 до 20 символов
#      • Только буквы, цифры и подчёркивание
     
#   2. email - getter и setter
#      Setter должен проверять:
#      • Содержит символ '@'
#      • Содержит точку '.' после @
     
#   3. age - getter и setter
#      Setter должен проверять:
#      • Возраст от 13 до 80
     
#   4. password (только setter, без getter!)
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
    def username(self, newUsername: str):
        if len(newUsername) < 3 or len(newUsername) > 20:
            raise AttributeError(f'Ошибка! Имя пользователя должно быть от 3 до 20 символов (получено: {len(newUsername)})')

        if not newUsername.replace('_', '').isalnum():
            # .replace(check, change) - заменяет символ check на символ change
            # .isalnum() - возвращает True, если строка состоит только из букв и цифр
            raise AttributeError('Ошибка! имя пользователя может содержать только буквы, цифры и подчеркивание')

        self._username = newUsername
        print('Имя пользователя изменено')

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, newEmail: str):
        if not '@' in newEmail:
            raise AttributeError('Некорректный формат почты (нет символа @)')
        
        if len(newEmail.split('@')) != 2:
            raise AttributeError('Некорректный формат почты')
     
        if not '.' in newEmail.split('@')[1]:
            raise AttributeError('Некорректный формат почты')
        
        self._email = newEmail
        print('Email адрес изменен')

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, newAge: int):
        if newAge < 13 or newAge > 80:
            raise AttributeError('Возраст должен быть от 13 до 80 лет')
        
        self._age = newAge
        print('Возраст изменен')
     
    @property
    def password(self):
        raise AttributeError('Нельзя получить информацию о пароле')
    
    @password.setter
    def password(self, newPassword: str):
        if len(newPassword) < 8:
            raise AttributeError('Длина пароля должная быть не меньше 8 символов')
        
        self.__password = newPassword
        print('Пароль изменен')


    def showInfo(self):
        print(f'Username: {self._username} \n' \
              f'Email: {self._email} \n' \
              f'Age: {self._age} \n')

    def checkPassword(self, password: str):
        return True if password == self.__password else False
    
user = User("ivan_petrov", "ivan@example.com", 25, "secret123")

print(user.username)  # ivan_petrov
print(user.email)     # ivan@example.com
print(user.age)       # 25

# print(user.password)  # ❌ Ошибка! Нет getter'а

# Проверка пароля
print(user.checkPassword("wrong"))     # False
print(user.checkPassword("secret123")) # True

# Изменение через property (вызываются setter'ы с проверками)
user.username = "new_user"    # ✅ OK
user.email = "new@mail.com"   # ✅ OK
user.age = 30                 # ✅ OK

# Попытки установить некорректные значения
# user.username = "ab"          # ❌ Слишком короткий (минимум 3)
# user.username = "user@name"   # ❌ Недопустимые символы
# user.email = "invalid"        # ❌ Нет @
# user.email = "test@"          # ❌ Нет точки после @
# user.age = 10                 # ❌ Слишком молодой
# user.age = 150                # ❌ Невозможный возраст

# Смена пароля
# user.password = "newpass"     # ❌ Слишком короткий (минимум 8)
user.password = "newpassword123"  # ✅ OK

# Проверка нового пароля
print(user.checkPassword("secret123"))      # False (старый пароль)
print(user.checkPassword("newpassword123")) # True (новый пароль)

user.showInfo()
# Username: new_user
# Email: new@mail.com
# Age: 30