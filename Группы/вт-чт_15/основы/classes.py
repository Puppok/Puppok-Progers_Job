# Классы

# стандартный способ описать собачку
name = 'good dog'
age = 5

def bark():
    print('woof')

print('================')

# шаблон собачки через класс
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('woof')

dog1 = Dog('bad dog', 155) # создаем собачку по шаблону класса
dog1.bark() 
print(dog1.name)


# Создание класса
class Cat:
    paws = 4 # общая переменная для всех объектов класса

    # инициализация объекта класса с уникальными значениями для каждого
    def __init__(self, name, breed, isHungy): 
        self.name = name
        self.breed = breed
        self.isHungy = isHungy

    # метод класса
    def meow(self):
        print('meow')

    def feedCat(self):
        if self.isHungy == True:
            print(f'{self.name} ест')
            self.isHungy = False
        else:
            print(f'{self.name} не голоден')

britishCat = Cat('Чпокучечка', 'Британка', False)
print(f'Имя котика: {britishCat.name}, порода: {britishCat.breed}')
britishCat.meow()
britishCat.feedCat()

streetCat = Cat('хз как', 'штрих', True)
print(f'Имя котика: {streetCat.name}, порода: {streetCat.breed}')
streetCat.meow()
streetCat.feedCat()

print('лапки британки:', britishCat.paws)
print('лапки хз кого:', streetCat.paws)

