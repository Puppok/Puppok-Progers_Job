# ООП
# 1. Инкапсуляция - скрытие свойств класса от внешней программы
# 2. Наследование - наследование свойств от одного класса к другому
# 3. Полиморфизм - использование одного и того же метода в разных классах по разному 

# Инкапсуляция
class House:
    def __init__(self):
        self.freeItems = 'candies' # доступный уровень
        self._personalItems = 'underpants' # защищенный уровень
        self.__secretItems = 'money' # приватный уровень, name mangling (_House__secretItems)

    # Геттер (get)
    def getPersonal(self):
        return self._personalItems

    # Сеттер (set)
    def setPersonal(self, value):
        if value == 'chpok':
            print('Ты кусок идиота')
        else:
            self._personalItems = value
            print('Такое подойдет')
    
    # Геттер и сеттер через @property
    @property # работает как геттер, только через название переменной
    def secretItems(self):
        return 'Нельзя получить значение'
    
    # Не сработает, если нет @property
    @secretItems.setter # сеттер через property, работает через запись значения в переменную
    def secretItems(self, value):
        if value == '1525':
            print('Не подходит')
        else:
            self.__secretItems = value
            print('все ок')

# house = House()
# print(house.freeItems) # так делать можно
# print(house._personalItems) # можно, но лучше так не делать
# print(house._House__secretItems) # дичь полная, не делайте так никогда!

# house.setPersonal('tshirt') # используем сеттер
# print(house.getPersonal()) # используем геттер

# print(house.secretItems) # вызывается геттер через property
# house.secretItems = '125' # вызывается сеттер через property
# print(house.secretItems)



#^ Задача

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
#~      • Только буквы, цифры и подчёркивание
     
#   2. email - getter и setter
#      Setter должен проверять:
#      • Содержит символ '@'
#      • Содержит точку '.' после @
     
#   3. age - getter и setter
#      Setter должен проверять:
#      • Возраст от 13 до 100
     
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
            raise AttributeError('Имя пользователя должно быть от 3 до 20 символов')
        
        # .isalnum() - вернет True, если строка состоит только из букв и цифр
        # .replace(find, change) - заменяет искомый символ find на символ change
        if not newUsername.replace('_', '').isalnum():
            raise AttributeError('Имя пользователя может состоять только из букв, цифр и подчеркивания')
        
        self._username = newUsername
        print('имя изменено')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, newEmail: str):
        # .split(separator) - разбивает строку на элементы массива, используя separator как разделитель
        if not '@' in newEmail:
            raise AttributeError('Почта должна содержать символ @')
        
        if not '.' in newEmail.split('@')[1]:
            raise AttributeError('Некорректная запись почты')   
                
        self._email = newEmail
        print('email изменено')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newAge):
        if newAge < 13 or newAge > 100:
            raise AttributeError('Возраст должен быть от 13 до 100')
        
        self._age = newAge
        print('возраст изменено')

    @property
    def password(self):
        raise AttributeError('Значение пароля недоступно')

    @password.setter
    def password(self, newPassword):
        if len(newPassword) < 8:
            raise AttributeError('Длина пароля должна быть не менее 8 символов')
        
        self.__password = newPassword
        print('пароль изменено')


    def showInfo(self):
        '''показать публичную информацию (без пароля)'''
        print(f'Имя пользователя: {self._username} \n' \
              f'Email: {self._email} \n' \
              f'Возраст: {self._age}')

    def checkPassword(self, password: str):
        '''проверка пароля'''
        if self.__password == password:
            return True
        else:
            return False


user = User("ivan_petrov", "ivan@example.com", 25, "secret123")

# Чтение через property (вызываются getter'ы)
print(user.username)  # ivan_petrov
print(user.email)     # ivan@example.com
print(user.age)       # 25

# Попытка прочитать пароль
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

# Информация о пользователе
user.showInfo()
# Username: new_user
# Email: new@mail.com
# Age: 30