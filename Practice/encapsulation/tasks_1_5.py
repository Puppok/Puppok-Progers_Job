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
from statistics import mean


class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise AttributeError('Can\'t be lower than -273.15')

        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 1.8

# temp = Temperature(50)
# print(temp.celsius)
# print(temp.fahrenheit)
# # temp.celsius = -273.19
# temp.celsius = 128
# print(temp.celsius)
# temp.farenheit = 3_275
# print(temp.farenheit)

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
class Student:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        self._grades: list[int] = []

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise AttributeError('Can\'t be lower than 6')

        if value > 18:
            raise AttributeError('Can\'t be higher than 18')

        self._age = value

    @property
    def average_grade(self):
        return mean(self._grades)
        return sum(self._grades) / len(self._grades)

    def add_grade(self, grade: int):
        if grade < 2 or grade > 5:
            raise AttributeError('Can\'t be lower than 2 or higher than 5')

        self._grades.append(grade)

# tom = Student('tom', 18)
# tom.add_grade(5)
# tom.add_grade(4)
# tom.add_grade(3)
# tom.add_grade(4)
# # tom.add_grade(1)
# tom.add_grade(2)
# print(tom.average_grade)
# print(tom.age)
# print(tom.name)
# tom.age = 15
# print(tom.age)


"""
ЗАДАЧА 3: Класс "Прямоугольник"
Создайте класс Rectangle с приватными атрибутами _width и _height.
Реализуйте:
- property width и height с getter и setter (только положительные значения)
- property area - площадь (только для чтения)
- property perimeter - периметр (только для чтения)
- метод is_square() - проверка, является ли квадратом
"""

class Rect:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        if value <= 0:
            raise AttributeError('Не может быть отрицательным')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        if value <= 0:
            raise AttributeError('Не может быть отрицательным')
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def is_square(self):
        return self._width == self._height


"""
ЗАДАЧА 4: Класс "Пользователь"
Создайте класс User с приватными атрибутами _login и _password.
Реализуйте:
- property login (только для чтения)
- метод set_password(old_pass, new_pass) - смена пароля
- метод check_password(password) - проверка пароля
- property password_length - длина пароля (только для чтения)
"""

class User:
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @property
    def password_length(self):
        return len(self._password)

    def check_password(self, password: str):
        return password == self._password

    def set_password(self, old_pass: str, new_pass: str):
        if not self.check_password(old_pass):
            raise AttributeError('Wrong old password')

        self._password = new_pass

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

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError('Only positive numbers are allowed')

        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError('Can\'t be lower than 0')

        self._quantity = value

    @property
    def total_cost(self):
        return self._quantity * self._price

    def sell(self, amount: int):
        self.quantity -= amount