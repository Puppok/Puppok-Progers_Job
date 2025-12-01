# Инкапсуляция
class House:
    def __init__(self):
        self.freeItems = 'candies'  # общедоступное свойства
        self._personalItems = 'clothes'  # защищенное свойство
        self.__secretItems = 'money'  # приватное свойство, name mangling (_House__secretItems)

    # Getter (get - получать)
    def getPersonalItems(self):
        return self._personalItems

    # Setter (set - задавать)
    def setSecretItems(self, value):
        if value == 'chpok':  # проверка значения
            raise AttributeError('Неверное значение')  # выводим ошибку, если значение не подошло
        else:
            self.__secretItems = value  # если подошло, записываем в переменную
            print('Значение изменено')


    @property # геттер через свойство @property
    def secretItems(self):
        return self.__secretItems

    @secretItems.setter # сеттер через property (обязательно наличие @property)
    def secretItems(self, value):
        # isinstance(value, type) - вернет True если значение value будет содержать тип данных type
        if isinstance(value, int):
            raise AttributeError('Можно использовать только буквенные значения')
        else:
            self.__secretItems = value
            print('Значение изменено')

myHouse = House()
print(myHouse.freeItems) # так делать можно
print(myHouse._personalItems) # не запрещено, но не стоит так делать
# print(myHouse.__secretItems) # ошибка, нет доступа к свойству
print(myHouse._House__secretItems) # дичь полнейшая, так делать вообще нельзя

# Получение значения через геттер (read-only, можем только прочитать значение)
print(myHouse.getPersonalItems())

# Изменение значения через сеттер
# print(myHouse.setSecretItems('chpok')) - ошибка, не прошло проверку
myHouse.setSecretItems('Pep') # успешно

print('Через property: ', myHouse.secretItems) # вызов геттера через property
# myHouse.secretItems = 23745 - ошибка, не прошло проверку типа
myHouse.secretItems = 'sosok' # успешно


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