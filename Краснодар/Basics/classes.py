# # Классы

# # Привычный способ работы со значениями
# name = 'Bobik'
# age = 5
# isHungry = False

# def bark():
#     print('woof woof')

# def feed(name, hungryStatus):
#     if hungryStatus == True:
#         print(f'{name} is eating')
#     else:
#         print(f'{name} is not hungry')

    
# # Способ через класс
# # class Имя:
# #   общедоступные свойства (переменные)
# #   конструктор класса (обязательная спец. функция)
# #   индивидуальные свойства (переменные)
# #   методы класса (функции)

# class Dog:
#     # общедоступные свойства
#     paws = 4
#     tail = 1

#     # конструктор класса
#     def __init__(self, name, age, isHungry):
#         # индивидуальные свойства
#         self.name = name
#         self.age = age
#         self.isHungry = isHungry

#     # методы класса
#     def bark(self):
#         print(f'{self.name} says woof woof')

#     def feed(self):
#         if self.isHungry == True:
#             print(f'{self.name} is eating')
#         else:
#             print(f'{self.name} is not hungry')

#     def showInfo(self):
#         print(f'Кличка: {self.name} \n' \
#               f'Возраст: {self.age} \n' \
#               f'Хочет кушать: {'Да' if self.isHungry == True else 'Нет'}')


# # # создаем первый объект класса 
# # bobik = Dog('Bobik', 10, False)
# # bobik.bark()
# # bobik.feed()
# # print(bobik.name)
# # print(bobik.paws)

# # print()

# # # создаем второй объект класса 
# # pushok = Dog('Pushok', 2, True)
# # pushok.bark()
# # pushok.feed()
# # print(pushok.name)
# # print(pushok.paws)



# # Задача 3: Класс "Калькулятор" 🧮
# # Условие:
# # Создайте класс Calculator с атрибутом:

# # result (результат, изначально 0)

# # Добавьте методы:

# # add(number) — прибавляет число к результату
# # subtract(number) — вычитает число из результата
# # multiply(number) — умножает результат на число
# # divide(number) — делит результат на число (с проверкой на 0)
# # reset() — сбрасывает результат на 0
# # show() — выводит текущий результат

# class Calculator:
#     def __init__(self, result = 0):
#         self.result = result

#     def add(self, num1, num2):
#         self.result = num1 + num2 # запоминаем результат
#         print(f'Результат суммы: {num1} + {num2} = {self.result}')

#     def subtract(self, num1, num2):
#         self.result = num1 - num2
#         print(f'Результат разности: {num1} - {num2} = {self.result}')

#     def multiply(self, num1, num2):
#         self.result = num1 * num2 
#         print(f'Результат умножения: {num1} * {num2} = {self.result}')

#     def divide(self, num1, num2):
#         self.result = num1 / num2 
#         print(f'Результат деления: {num1} / {num2} = {self.result}')

#     def reset(self):
#         self.result = 0
#         print('Результаты сброшены')

#     def show(self):
#         print(f'Последний результат: {self.result}')


# calc = Calculator()

# calc.show()

# calc.add(12, 57)
# calc.show()

# calc.multiply(45, 18)
# calc.show()

# calc.reset()
# calc.show()


# Задача 2: RPG Игра ⚔️
# Условие:
# Создайте три класса: Item, Inventory, и Character

# Класс Item:
# Атрибуты: name, item_type ("weapon", "armor", "potion"), value (урон/защита/лечение)

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

class Item:
    def __init__(self, name: str, item_type: str, value: int):
        self.name = name
        self.item_type = item_type
        self.value = value

class Inventory:
    def __init__(self, max_size: int, items: list[Item] = []):
        self.max_size = max_size
        self.items = items

    def add_item(self, item: Item):
        if len(self.items) >= self.max_size:
            print('В инвентаре нет места')
        else:
            self.items.append(item)
            print(f'{item.name} добавлен в инвентарь')

    def remove_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f'Предмет: {item.name} удален')
                break

    def get_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                print(f'{item.name}, {item.item_type}')
                break

    def show_items(self):
        for i, item in enumerate(self.items):
            print(f'{i + 1}. {item.name}, тип: {item.item_type}, значение: {item.value}')

    def is_full(self):
        if len(self.items) >= self.max_size:
            print('Инвентарь заполнен')
        else:
            print(f'Доступно мест: {self.max_size - len(self.items)}')

class Character:
    def __init__(self, name: str, health: int, max_health: int, attack: int, defense: int, inventory: Inventory):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory

    def equip_weapon(self, item: Item):
        self.attack += item.value
        print(f'Надето оружие: {item.name}, значение атаки: {self.attack}')

    def equip_armor(self, item: Item):
        self.defense += item.value
        print(f'Надето: {item.name}, значение защиты: {self.defense}')

    def use_potion(self, item: Item):
        self.health += item.value

        if self.health > self.max_health:
            self.health = self.max_health

        print(f'Подлечились, теперь здоровье равно {self.health}')

    def attack_target(self, target: Character):
        if self.attack >= target.defense:
            target.health -= self.attack - target.defense
            print(f'Нанесено {self.attack - target.defense} урона, здоровье противнка: {target.health}')
        else:
            target.defense -= self.attack
            print(f'Урон не прошел, показатель брони противника: {target.defense}')

    def is_alive(self):
        if self.health > 0:
            print(f'Персонаж жив, здоровье: {self.health}')
        else:
            print('Персонаж мертв')

    def show_stats(self):
        print(f'Имя: {self.name} \n' \
              f'Здоровье: {self.health} \n' \
              f'Макс. здоровье: {self.max_health} \n' \
              f'Атака: {self.attack} \n' \
              f'Защита: {self.defense} \n')

sword = Item('Хороший меч', 'оружие', 30)
shield = Item('Деревянный щит', 'броня', 5)
chest = Item('Железный нагрудник', 'броня', 15)
healPotion = Item('Зелье лечения', 'зелье', 15)

hero = Character('Игрок', 100, 100, 5, 1, Inventory(5))
enemy = Character('Гоблин', 100, 100, 10, 5, Inventory(5))

hero.inventory.add_item(sword)
hero.inventory.add_item(shield)
hero.inventory.add_item(chest)
hero.inventory.add_item(healPotion)

print('----------')

hero.equip_weapon(sword)
hero.equip_armor(shield)
hero.equip_armor(chest)

print('----------')

hero.show_stats()
print('----------')
enemy.show_stats()

print('----------')

hero.attack_target(enemy)
enemy.attack_target(hero)

hero.inventory.get_item('Хороший меч')
hero.use_potion(healPotion)
hero.show_stats()