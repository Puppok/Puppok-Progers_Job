# Наследование
class Animal: # родительский класс (superclass)
    # значения, доступные всем дочерним классам
    def __init__(self, type, lifecycle):
        self.type = type
        self.lifecycle = lifecycle

    # методы, доступные всем дочерним классам
    def sleep(self):
        print(f'{self.type} спит')

    def eat(self, food):
        print(f'{self.type} кушает {food}')

class Cat(Animal): # дочерний класс (subclass), наследуется от класса Animal
    def meow(self):
        print(f'{self.type} говорит мяу')

class Dog(Animal): # дочерний класс (subclass), наследуется от класса Animal
    def bark(self):
        print(f'{self.type} говорит гав гав')

# cat = Cat('кошка', 20)
# cat.meow()
# cat.sleep()
# cat.eat('рыбку')
# print(cat.lifecycle, 'лет')
# print(cat.type)
#
# print()
#
# dog = Dog('собака', 25)
# dog.bark()
# dog.sleep()
# dog.eat('мяско')
# print(dog.lifecycle, 'лет')
# print(dog.type)

# правило is a
# Cat is an Animal - логично 
# isinstance(value, type) - проверить, является ли value значением типа type
# print(isinstance(2, int))
# print(isinstance(dog, Dog))
# print(isinstance(dog, Cat))

# issubclass(subclass, superclass) - проверяет, является ли subclass дочерним для superclass
# print(issubclass(Cat, Animal))
# print(issubclass(Cat, Dog))

class Auto:
    def __init__(self, engine: str, mark: str, model: str, hPower: int = 100):
        self.engine = engine
        self.mark = mark
        self.model = model
        self.hPower = hPower

    def getHPower(self):
        return self.hPower

    def showInfo(self):
        return f'{self.engine}, {self.mark}, {self.model}, {self.hPower}'

    def startEngine(self):
        print('врум врум')

    def stopEngine(self):
        print('стоп')

class Honda(Auto):
    # Конструктор дочернего класса
    def __init__(self, engine: str, mark: str, model: str, climat: str, media: str):
        # Инициализация конструктора родителя
        super().__init__(engine, mark, model)
        self.climat = climat
        self.media = media

    # Перезапись родительского метода
    def startEngine(self):
        print('Двигатель запущен')

    # Дозапись родительского метода
    def stopEngine(self):
        super().stopEngine() # вызов метода родителя
        print('Двигатель остановлен')

    def tuning(self):
        basePower = super().getHPower()
        tuningPower = basePower + 50
        print(f'После тюнинга: {tuningPower}')

    def info(self):
        baseInfo = super().showInfo()
        print(baseInfo + f', {self.climat}, {self.media}')

honda = Honda('2NZ', 'Honda', 'Accord', 'Выключен', 'Pioneer')
honda.startEngine()
honda.stopEngine()
honda.tuning()
honda.info()
