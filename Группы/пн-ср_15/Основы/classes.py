# Классы
name = 'Pankratos'
age = 6.7
isAlive = True

def meow():
    print('Meow')

def eat(food):
    print('I am eating ' + food)

# class Название_класса:
#     конструктор класса
#     свойства класса
#     методы класса

# имя_объекта = Название_класса(параметры_конструктора)

class Cat: # создание класса
    # общие свойства
    paws = 4
    tail = 1

    def __init__(self, name, age, isAlive): # конструктор
        # свойства класса
        self.name = name
        self.age = age
        self.isAlive = isAlive

    # методы класса
    def meow(self): 
        print('Meow')

    def eat(self, food):
        print(self.name + ' is eating ' + food)

    def sleep(self):
        print(self.name + ' 😴zzz...')

# создание объектов (экземпляров класса)
kotik = Cat('Pankratos', 6.7, True)
kotik2 = Cat('Pepchik', 3, True)
kotik3 = Cat('Olduha', 20, False)
kotik4 = Cat('Mishka', 8, True)

# print(kotik2.name)
# kotik2.eat('Tuna')

# kotik4.eat('Fish')

# kotik.sleep()

print(kotik.name)
print(kotik.paws)

print(kotik4.name)
print(kotik4.paws)


# Книга
# RGP игра

# Задача 1: Класс "Книга" 📚
# Условие:
# Создайте класс Book с атрибутами:

# title (название)
# author (автор)
# pages (количество страниц)
# current_page (текущая страница, изначально 0)

# Добавьте методы:

# read(pages_count) — читает указанное количество страниц (увеличивает current_page)
# info() — выводит информацию о книге
# is_finished() — возвращает True, если книга дочитана

# book = Book("Война и мир", "Толстой", 1300)
# book.info()  # Книга: "Война и мир" by Толстой, 1300 страниц
# book.read(50)  # Прочитано 50 страниц
# book.read(30)  # Прочитано 30 страниц
# print(book.current_page)  # 80
# print(book.is_finished())  # False

class Book:
    # конструктор (название книги, автор, общее кол-во стр, текущая страница)
    def __init__(self, title, author, pages, currentPage = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.currentPage = currentPage

    # прочитать количество страниц
    def read(self, pagesCount):
        self.currentPage += pagesCount # к текущим стр прибавляем кол-во прочитанных
        print(f'Прочитано {pagesCount} страниц')

    # вывод информации о книге
    def info(self):
        print(f'Книга {self.title}, автор {self.author}, всего {self.pages} страниц')

    # проверка на дочитанность
    def is_finished(self):
        # если число текущих стр больше или равно общему кол-ву в книге
        if self.currentPage >= self.pages: 
            print('Книга дочитана')
        else:
            print('Книга не дочитана')


book = Book("Война и мир", "Толстой", 1300)
book.info()  
book.read(50) 
book.read(30)  
print(book.currentPage)  
book.is_finished()  

book.read(1250)
print(book.currentPage)  
book.is_finished()  


# Задача 2: RPG Игра ⚔️
# Условие:
# Создайте три класса: Item, Inventory, и Character

# Класс Item:
# Атрибуты: name, item_type ("weapon", "armor", "potion"), value (урон/защита/лечение)
# Методы:
# use(character) — использует предмет на персонаже (лечение для зелья)

# Класс Inventory:
# Атрибуты: items (список предметов), max_size (максимальный размер)

# Методы:
# add_item(item) — добавляет предмет (с проверкой места)
# remove_item(item_name) — удаляет предмет по имени
# get_item(item_name) — возвращает предмет по имени
# show_items() — показывает все предметы
# is_full() — проверяет, заполнен ли инвентарь

# Класс Character:
# Атрибуты: name, health, max_health, attack, defense, inventory (объект Inventory)

# Методы:
# equip_weapon(item) — экипирует оружие (увеличивает attack)
# equip_armor(item) — экипирует броню (увеличивает defense)
# use_potion(item) — использует зелье (восстанавливает здоровье)
# attack_target(target) — атакует другого персонажа (урон = attack - defense цели)
# is_alive() — проверяет, жив ли персонаж
# show_stats() — показывает характеристики

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

class Item:
    def __init__(self, name, item_type, value):
        self.name = name
        self.item_type = item_type
        self.value = value

class Inventory:
    def __init__(self, max_size, items = []):
        self.items = items # массив всех предметов в инвентаре
        self.max_size = max_size

    def addItem(self, item):
        # Если кол-во всех предметов больше либо равно максимально допустимому
        if len(self.items) >= self.max_size:
            print("Инвентарь переполнен")
        else:
            self.items.append(item)
            print(f"Предмет {item.name} добавлен в инвентарь")

    def removeItem(self, item_name):
        # перебираем все предметы
        for item in self.items:
            # если имя предмета совпадает с введенным
            if item.name == item_name:
                self.items.remove(item) # удаляем предмет
                print(f"Предмет {item.name} удален из инвентаря")
                break # завершаем цикл, чтобы не искал дальше
                
    def get_item(self, item_name):
        if item_name in self.items:
            print(f'Предмет есть в инвентаре')
        else:
            print(f'Предмет не найден')

    def show_items(self):
        for item in self.items:
            print(item.name)

    def is_full(self):
        if len(self.items) >= self.max_size:
            print('Инвентарь переполнен')
        else:
            print(f'Доступно еще {self.max_size - len(self.items)} мест')

class Character:
    def __init__(self, name, health, max_health, attack, defense, inventory):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory

    def equip_weapon(self, weapon):
        # прибавляем к атаке персонажа значение атаки оружия
        self.attack += weapon.value

    def equip_armor(self, armor):
        # прибавляем к защите персонажа значение защиты брони
        self.defense += armor.value

    def use_potion(self, potion):
        # прибавляем к здоровью персонажа значение зелья 
        # (здоровье не может быть больше максимального)
        self.health += potion.value

        # не даем здоровью стать больше максимального
        if self.health > self.max_health:
            self.health = self.max_health
    
    def attack_target(self, target):
        if self.attack - target.defense <= 0:
            print(f'{target.name} получил {0} урона')
            target.defense -= self.attack
        else:
            print(f'{target.name} получил {self.attack - target.defense} урона')
        
    def is_alive(self):
        if self.health > 0:
            print(f'Персонаж еще жив, здоровье: {self.health}')
        else:
            print('Персонаж умер')

    def show_stats(self):
        print(f'Имя: {self.name} \n' \
              f'Здоровье: {self.health} \n' \
              f'Атака: {self.attack} \n' \
              f'Защита: {self.defense} \n'
              f'Инвентарь, доступно мест: {self.inventory.max_size - len(self.inventory.items)}')
        
# Создаем предметы
sword = Item("Железный меч", "weapon", 15)
shield = Item("Железный щит", "armor", 10)
chestArmor = Item('Алмазный нагрудник', 'armor', 20)
potion = Item("Зелье лечения", "potion", 30)


# Создаем персонажей
hero = Character('Шклгеыл', 50, 100, 5, 3, Inventory(5))
goblin = Character('Кусок очка', 80, 150, 10, 5, Inventory(5))

# Основная программа
hero.inventory.addItem(sword)
hero.inventory.addItem(shield)
hero.inventory.addItem(chestArmor)
hero.inventory.addItem(potion)
print('-------------------------')
hero.equip_weapon(sword)
hero.equip_armor(shield)
hero.equip_armor(chestArmor)

hero.show_stats()
print('-------------------------')
goblin.show_stats()

print('-------------------------')
hero.attack_target(goblin)
goblin.attack_target(hero)

print('-------------------------')
hero.show_stats()

hero.use_potion(potion)
print('-------------------------')
hero.show_stats()
