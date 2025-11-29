# ООП - Объектно-ориентированное программирование
# 1. Инкапсуляция - скрытие данных
# 2. Наследование - наследование данных от одного класса другому
# 3. Полиморфизм - использование одного и того же метода в разных классах с разным результатом

# Инкапсуляция
class House:
    def __init__(self):
        self.free = 'candies' # доступное свойство
        self._protect = 'clothes' # защищенное свойство
        self.__private = 'money' # приватное свойство, name mangling (_House__private)

    # Геттер (get - получать)
    def getPrivate(self):
        return self.__private

    # Сеттер (set - задавать)
    def setProtect(self, value):
        if value == 'chpok':
            raise AttributeError('Неверное значение, выйдите в окно')
        else:
            self._protect = value

    # Конструкция property
    @property # геттер через property
    def private(self):
        return self.__private
    
    @private.setter # сеттер через property (не может существовать, если нет @property)
    def private(self, value):
        if value == 'pep':
            raise AttributeError('Неверное значение')
        else:
            self.__private = value


house = House()
print(house.free) # так делать можно
house.free = 'chocolate'
print(house.free)

print(house._protect) # не запрещено, но и не стоит делать (тебе втащат)
house._protect = 'laptop'
print(house._protect)

# print(house.__private) - Ошибка!
# print(house._House__private) # так делать запрещено

# вызов геттера
print(house.getPrivate()) 

# вызов сеттера
# house.setProtect('chpok') - ошибка, не прошло проверку
house.setProtect('piska')

# property
print('через property: ', house.private) # вызов геттера через property
house.private = 'shmak' # вызов сеттера через property

