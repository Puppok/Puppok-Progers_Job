# Классы
name = 'Puk'
age = 8
isAlive = True

def meow():
    print('meow')

def sleep():
    print('zzz')

def eat():
    print('nom nom nom')

def walk(m):
    print(f'walked {m} meters')

# class Имя:
#   конструктор класса
#   свойства класса (индивидуальные / общие)
#   методы класса

class Cat:
    # общие свойства
    paws = 4
    tail = 1
    ears = 2
    eyes = 2

    # Конструктор класса
    def __init__(self, name, age, isAlive, isHungry):
        # индивидуальные свойства
        self.name = name
        self.age = age
        self.isAlive = isAlive
        self.isHungry = isHungry

    # методы класса
    def meow(self):
        print(f'{self.name} says meow')

    def sleep(self):
        print(f'{self.name} zzz... 😴')

    def walk(self, meters):
        print(f'{self.name} walked {meters} meters')

    def eat(self):
        if self.isHungry:
            print(f'{self.name} nom nom nom')
            self.isHungry = False
        else:
            print(f'{self.name} is not hungry')
    
# kotik = Cat('Kratos', 15, True, False)
# print(kotik.name)
# kotik.sleep()
# kotik.eat()
# print(kotik.paws)
    
# print()

# kotik2 = Cat('Chpok', 3, True, True)
# print(kotik2.name)
# kotik2.sleep()
# kotik2.eat()
# print(kotik2.paws)




# Студент
# Задача 2: Класс "Студент" 🎓
# Условие:

# Создайте класс Student с атрибутами:
# name (имя)
# grades (список оценок, изначально пустой)

# Добавьте методы:
# add_grade(grade) — добавляет оценку в список (от 2 до 5)
# get_average() — возвращает средний балл
# get_status() — возвращает статус:

# "Отличник" если средний балл >= 4.5
# "Хорошист" если >= 3.5
# "Троечник" если >= 3.0
# "Двоечник" если < 3.0

# Пример использования:
# pythonstudent = Student("Иван")
# student.add_grade(5)
# student.add_grade(4)
# student.add_grade(5)
# student.add_grade(4)
# print(student.get_average())  # 4.5
# print(student.get_status())  # Отличник

class Student:
    def __init__(self, name, grades = []):
        self.name = name # имя студента
        self.grades = grades # массив оценок
        
    # добавить оценку в общий список
    def addGrade(self, *grades):
        self.grades.extend(*grades)

    # получить средний балл
    def getAverage(self):
        sum = 0
        for grade in self.grades: # нашли сумму всех оценок
            sum += grade

        self.average = sum / len(self.grades) # нашли средний балл (сумма всех / кол-во)

        print(f'Средний балл {self.name} = {self.average:.2f}')

    # получить статус студента (отличник / троечник и тд)
    def getStatus(self):
        if self.average >= 4.5:
            print('Отличник')
        elif self.average >= 3.5:
            print('Хорошист')
        elif self.average >= 3.0:
            print('Троечник')
        else:
            print('Двоечник')

# bob = Student('Bob', [5, 4, 5, 4])
# tom = Student('Tom', [4, 4, 4, 4])
# zahar = Student('Zahar', [2, 4, 3, 5, 2])

# bob.getAverage()
# bob.getStatus()
# bob.addGrade([2, 2, 3, 2, 2, 2, 2])
# bob.getAverage()
# bob.getStatus()

# print()

# zahar.getAverage()
# zahar.getStatus()
# zahar.addGrade([4, 4, 5, 5, 5])
# zahar.getAverage()
# zahar.getStatus()


# RPG
# Задача 2: RPG Игра ⚔️

class Item:
    def __init__(self, name, itemType, value):
        self.name = name
        self.itemType = itemType
        self.value = value

class Inventory:
    def __init__(self, maxSize, items = []):
        self.items = items
        self.maxSize = maxSize

    def addItem(self, item):
        if len(self.items) >= self.maxSize:
            print('Инвентарь заполнен')
        else:
            self.items.append(item)
            print(f'{item.name} добавлен в инвентарь')

    def removeItem(self, item):
        if item in self.items: # если предмет есть в общем списке
            self.items.remove(item) # удаляем его
            print(f'{item.name} удален')
        else:
            print('такого предмета нет')

    def getItem(self, itemName):
        for item in self.items:
            if item.name == itemName:
                print(f'Ваш предмет: {item.name}, тип: {item.itemType}')
                break

    def showItems(self):
        count = 1
        for item in self.items:
            print(f'{count}. {item.name}, тип: {item.itemType}')
            count += 1

    def isFull(self):
        if len(self.items) >= self.maxSize:
            print('Инвентарь заполнен')
        else:
            print(f'Доступно мест: {self.maxSize - len(self.items)}')

class Character:
    def __init__(self, name, health, maxHealth, attack, defense, inventory):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.attack = attack
        self.defense = defense
        self.inventory = inventory

    def equipWeapon(self, item):
        self.attack += item.value

    def equipArmor(self, item):
        self.defense += item.value

    def usePotion(self, item):
        self.health += item.value
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def attackTarget(self, target):
        if self.attack > target.defense:
            target.health = self.attack - target.defense
            print(f'{self.name} атакует {target.name}, у противника осталось {target.health}хп')
        else:
            target.defense -= self.attack
            print(f'противник очень жирный, у него осталось {target.defense} жира')

    def isAlive(self):
        if self.health > 0:
            print(f'{self.name} еще пока держится')
        else:
            print(f'{self.name} покинул этот бренный мир (сдох)')

    def showStats(self):
        print('-------------------------')
        print(f'Имя: {self.name} \n' \
              f'Здоровье: {self.health} \n' \
              f'Максимальное здоровье: {self.maxHealth} \n' \
              f'Атака: {self.attack} \n' \
              f'Защита: {self.defense}' )
        print('-------------------------')

# Пример использования:
# sword = Item("Железный меч", "weapon", 15)
# shield = Item("Железный щит", "armor", 10)
# potion = Item("Зелье лечения", "potion", 30)

# hero = Character("Hero", 100, 10, 5)
# enemy = Character("Goblin", 50, 8, 2)

# hero.inventory.add_item(sword)
# hero.inventory.add_item(shield)
# hero.inventory.add_item(potion)

# hero.equip_weapon(sword)  # attack: 10 -> 25
# hero.equip_armor(shield)   # defense: 5 -> 15

# hero.attack_target(enemy)  # Goblin получает урон
# hero.use_potion(potion)    # Hero восстанавливает здоровье

# hero.show_stats()



