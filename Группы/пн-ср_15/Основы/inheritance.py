# Наследование
class Auto:
    def __init__(self, name, color, wheels, doors, engine):
        self.name = name
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.engine = engine

    def startEngine(self):
        print(f'{self.name} вжуух')

    def openDoor(self):
        print(f'{self.name} звук скрипа двери')

class Honda(Auto): # указание класса родителя, при создании дочернего класса
    def stopEngine(self):
        print('бррр')

class Kia(Auto): # указание класса родителя, при создании дочернего класса
    def refuel(self):
        print('бензинчик, еее')


honda = Honda('Honda', 'синий', 4, 4, 1)
honda.stopEngine()
honda.startEngine()
honda.openDoor()
print(honda.name)
print(honda.wheels)
print(honda.color)

print()

kia = Kia('Kia', 'красный', 4, 4, 1)
kia.refuel()
kia.startEngine()
kia.openDoor()
print(kia.name)
print(kia.wheels)
print(kia.color)


class Animal:
    def __init__(self, type, lifecycle):
        self.type = type
        self.lifecycle = lifecycle

    def walk(self):
        print(f'{self.type} гуляет')    

    def sleep(self):
        print(f'{self.type} спит')

    def eat(self, food):
        print(f'{self.type} ест {food}')

class Cat(Animal):
    def __init__(self, type, lifecycle, hasUsiki, hasTail):
        super().__init__(type, lifecycle) # инициализация конструктора родителя
        self.hasUsiki = hasUsiki
        self.hasTail = hasTail

    def meow(self):
        print(f'{self.type} говорит мяу')

    def sleep(self): # переопределение метода sleep() с другим принципом работы
        print('Кошка спит обосраться как долго')

cat = Cat('кошка', 20, True, True)
cat.meow()
cat.eat('рыбку')
print(cat.hasTail)
print(cat.lifecycle, 'лет')
cat.sleep()

# Полезные проверки
print(isinstance(cat, Auto)) # проверка типа данных 
print(issubclass(Cat, Kia)) # проверка, является ли класс дочерним к другому классу

# is a - проверка принадлежности дочернего класса к родителю
# Cat is a Animal
# Kia is a Auto
