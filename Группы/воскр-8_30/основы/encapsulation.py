# Инкапсуляция
# Скрытие свойств и методов класса от внешнего использования

class House:
    def __init__(self):
        self.free = 'candies' # доступное свойства
        self._personal = 'clothes' # защищенное свойство
        self.__secret = 'money' # приватное свойство, name mangling (_House__secret)

    # Getter (get - получать)
    def getPersonal(self):
        return self._personal

    def getSecret(self):
        return self.__secret

    # Setter (set - задать)
    def setPersonal(self, value):
        # isinstance(value, type) - вернет True если value имеет тип данных type
        # raise AttributeError(message) - создать ошибку с сообщением message
        if not isinstance(value, str):
            raise AttributeError('Значение должно быть строковым')

        self._personal = value
        print('Значение изменено')


    # Свойство property (работает как геттер)
    @property
    def secret(self):
        return self.__secret

    # сеттер через property (обязательно наличие @property)
    @secret.setter
    def secret(self, value: str):
        # .isalnum() - вернет True, если строка состоит только из букв и цифр
        if not isinstance(value, str):
            raise AttributeError('Value must be a string')

        if not value.isalnum():
            raise AttributeError('Value must contain only alphanumeric')

        self.__secret = value
        print('Значение изменено')


house = House()

# Работа с общедоступными свойствами (так делать можно)
print(house.free)
house.free = 'berries'
print(house.free)

# Работа с защищенными свойствами (не запрещено, но не стоит так делать)
print(house._personal)
house._personal = 'laptop'
print(house._personal)

# Работа с приватными свойствами
# print(house.__secret) - ошибка
print(house._House__secret) # дичь полнейшая, вообще так не делать никогда

# Вызов геттера, получаем read-only значение
print('Защищенное через геттер:', house.getPersonal())
print('Приватное через геттер:', house.getSecret())

# Вызов сеттера
# house.setPersonal(327523) - ошибка, значение не является строкой
# house.setPersonal(True) - ошибка, значение не является строкой
house.setPersonal('шмотки') # успешно

# Вызов геттера через property
print('Вызов property:', house.secret)

# Вызов сеттера через property
# house.secret = 1254 - ошибка, значение не строка
# house.secret = 'chpok12!' - ошибка, значение не содержит только буквы и цифры
house.secret = 'chpok12' # успешно

"""
ЗАДАЧА 1: Класс "Температура"

Создайте класс Temperature с приватным атрибутом _celsius.
Реализуйте:
- property celsius для получения температуры в Цельсиях
- setter для celsius (не ниже -273.15°C - абсолютный ноль)
- property fahrenheit для получения температуры в Фаренгейтах
- setter для fahrenheit (с автоматическим пересчетом в Цельсии)

Формулы: 
F = C * 9/5 + 32, 
C = (F - 32) * 5/9
"""


"""
ЗАДАЧА 2: Класс "Ученик"

Создайте класс Student с приватными атрибутами _name и _age.
Реализуйте:
- property name (только для чтения)
- property age с getter и setter (возраст от 6 до 18 лет)
- приватный список _grades (оценки)
- метод add_grade(grade) - добавление оценки (от 2 до 5)
- property average_grade - средний балл (только для чтения)
"""

"""
ЗАДАЧА 3: Класс "Прямоугольник"
Создайте класс Rectangle с приватными атрибутами _width и _height.
Реализуйте:
- property width и height с getter и setter (только положительные значения)
- property area - площадь (только для чтения)
- property perimeter - периметр (только для чтения)
- метод is_square() - проверка, является ли квадратом
"""

"""
ЗАДАЧА 4: Класс "Пользователь"
Создайте класс User с приватными атрибутами _login и _password.
Реализуйте:
- property login (только для чтения)
- метод set_password(old_pass, new_pass) - смена пароля
- метод check_password(password) - проверка пароля
- property password_length - длина пароля (только для чтения)
"""

"""
ЗАДАЧА 5: Класс "Товар"
Создайте класс Product с приватными атрибутами _name, _price, _quantity.
Реализуйте:
- property name (только для чтения)
- property price с getter и setter (только положительная цена)
- property quantity с getter и setter (только неотрицательное количество)
- property total_cost - общая стоимость товара (только для чтения)
- метод sell(amount) - продажа товара (уменьшение количества)
"""

