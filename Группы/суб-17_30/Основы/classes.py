# Классы

# Привычный способ
name = 'Pipka'
age = 4
isHunger = True
isAlive = True

def meow():
    print(f'{name} says meow!')

def sleep():
    print(f'{name} 😴...')

def feed():
    if isHunger:
        print(f'{name} is eating food!')
    else:
        print(f'{name} is not hungry!')


# class Имя:
#   общедоступные свойства
#   конструктор класса
#   индивидуальные свойства
#   методы класса

class Cat:
    # общедоступные свойства
    paws = 4
    tail = 1
    ears = 2
    eyes = 2

    # конструктор класса
    def __init__(self, name, age, isHungry, isAlive):
        # индивидуальные свойства
        self.name = name
        self.age = age
        self.isHungry = isHungry
        self.isAlive = isAlive

    # методы класса
    def meow(self):
        print(f'{self.name} says meow!')

    def sleep(self):
        print(f'{self.name} 😴...')

    def feed(self, food):
        if self.isHungry:
            print(f'{self.name} is eating {food}')
        else:
            print(f'{self.name} is not hungry')
    

pipka = Cat('Pipka', 4, True, True)
pipka.meow()
pipka.feed('chicken')
print(f'My name is {pipka.name}')
print(f'I have {pipka.paws} paws')

print()

chpek = Cat('Chpek', 10, False, True)
chpek.meow()
chpek.feed('tuna')
print(f'My name is {chpek.name}')
print(f'I have {chpek.paws} paws')


# Задача 2: Класс "Студент" 🎓
class Student:
    checkGrades = '2345'

    def __init__(self, name, grades = []):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        # проверка, если число адекватное (2-5)
        if str(grade) in self.checkGrades:
            # добавляем в массив оценок grades новую оценку grade
            self.grades.append(grade) 
            print(f'Оценка {grade} добавлена!')
        else:
            print(f'Неверная оценка')

    def add_grades(self, grades):
        print(f'Проверяем список оценок {grades}')
        # перебираем список добавляемых оценок
        for grade in grades:

            # проверка, если число адекватное (2-5)
            if str(grade) in self.checkGrades:
                # добавляем в список оценок студента
                self.grades.append(grade) 
            else:
                # если нет, удаляем ее из списка
                print(f'Оценка {grade} неверная')
                grades.remove(grade)

        # вывод списка добавленных оценок
        print(f'Список оценок {grades} добавлены!')

    def get_average(self):
        print(f'Средний балл студента {self.name}: {(sum(self.grades) / len(self.grades)):.2f}')

    def get_status(self):
        average = sum(self.grades) / len(self.grades)

        if average >= 4.5:
            print(f'{self.name} - Отличник')
        elif average >= 3.5:
            print(f'{self.name} - Хорошист')
        elif average >= 3:
            print(f'{self.name} - Троечник')
        else:
            print(f'{self.name} - Двоечник')

# tom = Student('Tom')
# tom.add_grade(3)
# tom.add_grades([4, 5, 2, 4, 7, 5, 5, 10])
# tom.get_average()
# tom.get_status()





# Задача 2: RPG Игра ⚔️
# Условие:
# Создайте три класса: Item, Inventory, и Character

# Класс Item:
# Атрибуты: name, item_type ("weapon", "armor", "potion"), value (урон/защита/лечение)

class Item:
    def __init__(self, name: str, itemType: str, value: int):
        self.name = name
        self.itemType = itemType
        self.value = value

    
# Класс Inventory:
# Атрибуты: items (список предметов), max_size (максимальный размер)

# Методы:
# add_item(item) — добавляет предмет (с проверкой места)
# remove_item(item_name) — удаляет предмет по имени
# get_item(item_name) — возвращает предмет по имени
# show_items() — показывает все предметы
# is_full() — проверяет, заполнен ли инвентарь

class Inventory:
    def __init__(self, maxSize: int):
        self.items: list[Item] = []
        self.maxSize = maxSize

    def addItem(self, item: Item):
        if self.isFull():
            print('Инвентарь заполнен')
        else:
            self.items.append(item)
            print(f'{item.name} добавлен в инвентарь')

    def removeItem(self, itemName: str):
        for item in self.items: # перебираем все предметы
            if item.name == itemName: # если название предмета совпадает с искомым
                self.items.remove(item) # удаляем предмет из массива
                break # останавливаем цикл, чтобы не работал дальше

    def getItem(self, itemName: str):
        for item in self.items:
            if item.name == itemName:
                print(f'{item.name}, тип: {item.itemType}, значение: {item.value}')
                break

    def showItems(self):
        # enumerate(массив) - нумерует каждый элемент массива (с нуля)
        for index, item in enumerate(self.items):
            print(f'{index + 1}. {item.name}, тип: {item.itemType}')

    def isFull(self):
        if len(self.items) >= self.maxSize:
            return True
        else:
            return False
        
        # тоже самое, сокращенная запись
        # return True if len(self.items) >= self.maxSize else False


# Класс Character:
# Атрибуты: name, health, max_health, attack, defense, inventory (объект Inventory)

# Методы:
# equip_weapon(item) — экипирует оружие (увеличивает attack)
# equip_armor(item) — экипирует броню (увеличивает defense)
# use_potion(item) — использует зелье (восстанавливает здоровье)
# attack_target(target) — атакует другого персонажа (урон = attack - defense цели)
# is_alive() — проверяет, жив ли персонаж
# show_stats() — показывает характеристики

class Character:
    def __init__(self, name: str, health: int, maxHealth: int, attack: int, defense: int, inventory: Inventory):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
    
    def equipWeapon(self, item: Item):
        if item.itemType == 'weapon':
            self.attack += item.value
        else:
            print('Неверный тип предмета')

    def equipArmor(self, item: Item):
        if item.itemType == 'armor':
            self.defense += item.value
        else:
            print('Неверный тип предмета')

    def usePotion(self, item: Item):
        if item.itemType == 'potion':
            self.health += item.value

            if self.health > self.maxHealth: # если здоровье больше максимального
                self.health = self.maxHealth # снижаем здоровье до максимального
        else:
            print('Неверный тип предмета')

    def attackTarget(self, target: Character):
        if self.attack >= target.defense: # если наша атака больше чем защита цели
            target.health -= self.attack - target.defense #  бьем противника 
        else: # если наша атака меньше защиты цели
            target.defense -= self.attack # снижаем защиту цели

    def isAlive(self):
        if self.health <= 0:
            print('Персонаж умер')
        else:
            print('Персонаж еще жив')

    def showStats(self):
        print(f'Имя: {self.name} \n' \
              f'Здоровье: {self.health}/{self.maxHealth} \n' \
              f'Атака: {self.attack} \n' \
              f'Защита: {self.defense}')


sword = Item('Меч', 'weapon', 10)
shield = Item('Щит', 'armor', 5)
heal = Item('Зелье', 'potion', 20)

hero = Character('Герой', 100, 100, 10, 5, Inventory(5))
enemy = Character('Ящерка Илья', 100, 100, 10, 5, Inventory(5))

hero.inventory.addItem(sword)
hero.equipWeapon(sword)

hero.inventory.addItem(shield)
hero.equipArmor(shield)

hero.inventory.addItem(heal)

hero.attackTarget(enemy)

hero.showStats()
print('------------------')
enemy.showStats()