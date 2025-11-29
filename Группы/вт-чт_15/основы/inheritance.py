# Наследование
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(f'{self.name} is eating {food}')

    def sleep(self):
        print(f'{self.name} is zzzz')

class Dog(Animal):
    def bark(self):
        print(f'{self.name} saying woof woof')

class Cat(Animal):
    def meow(self):
        print(f'{self.name} saying meow')


dog = Dog('Pep', 4)
dog.bark()
dog.sleep()
dog.eat('meat')
print(dog.age)
print(dog.name)

cat = Cat('sas', 15)
cat.sleep()
cat.meow()
print(cat.name)

class Auto:
    def __init__(self, mark, model, engine, year, type):
        self.mark = mark
        self.model = model
        self.engine = engine
        self.year = year
        self.type = type

    def startEngine(self):
        print('Тр тр тр')

    def stopEngine(self):
        print('пфффшшш')

class Toyota(Auto):
    def __init__(self, mark, model, engine, year, type, climate, hasElectricBreak):
        super().__init__(mark, model, engine, year, type) # инициализация конструктора родителя
        self.climate = climate
        self.hasElectricBreak = hasElectricBreak

    def enableClimate(self):
        self.climate = 'enabled'

    def startEngine(self):
        print('Вжууух')

car = Toyota('Toyota', 'Camry', '2NZ', 2015, 'sedan', 'disabled', True)
car.startEngine()
car.stopEngine()
print(car.climate)
print(car.mark)

# Проверка типа танных у объекта
print(isinstance(car, Toyota)) # true
print(isinstance(car, Animal)) # false

# Проверка наследования класса
print(issubclass(Toyota, Auto)) # true
print(issubclass(Toyota, Dog)) # false
 